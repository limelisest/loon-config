#!/usr/bin/env python3
"""Check references, paired subscriptions and domain routing; not a Loon runtime test."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sections = {}
for raw in (ROOT / 'limelisest-loon-config.lcf').read_text().splitlines():
    line = raw.strip()
    if line.startswith('['):
        section = line
        sections[section] = []
    elif line and not line.startswith(('#', ';', '//')):
        sections[section].append(line)
groups = dict(x.split('=', 1) for x in sections['[Proxy Group]'])
groups = {k.strip(): v.strip() for k, v in groups.items()}
filters = {x.split('=', 1)[0].strip() for x in sections['[Remote Filter]']}
known = set(groups) | filters | {'DIRECT', 'REJECT'}

def visit(name, path=()):
    assert name not in path, ('Group cycle', path, name)
    for item in groups[name].split(',')[1:]:
        item = item.strip()
        if '=' in item:
            continue
        assert item in known, ('Unknown group option', name, item)
        if item in groups:
            visit(item, path + (name,))

for name in groups:
    visit(name)
subscriptions = []
for line in sections['[Remote Rule]']:
    url, *options = line.split(',')
    options = dict(x.strip().split('=', 1) for x in options)
    assert options['policy'] in known, options
    if options.get('enabled') != 'false':
        subscriptions.append((url, options['policy']))

for name in ['Global', 'ChinaMax', 'Apple', 'AdvertisingLite']:
    pair = [(u, p) for u, p in subscriptions if f'/{name}/{name}' in u]
    assert len(pair) == 2 and len({p for _, p in pair}) == 1, ('Missing pair', name)
    assert any(u.endswith(f'{name}_Domain.list') for u, _ in pair), name

def download(item):
    url, policy = item
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as response:
                body = response.read().decode('utf-8-sig')
            break
        except (OSError, TimeoutError) as error:
            if attempt == 2:
                raise RuntimeError(f'Cannot download {url}: {error}') from error
    assert '<html' not in body.lower(), ('HTML instead of rules', url)
    lines = [x.strip() for x in body.splitlines() if x.strip() and not x.startswith(('#', ';', '//'))]
    assert lines, ('Empty rules', url)
    return url, policy, lines

with ThreadPoolExecutor(max_workers=8) as pool:
    resources = list(pool.map(download, subscriptions))

rules = []
def add(line, policy=None):
    parts = line.split(',')
    if parts[0] in {'DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD'}:
        rules.append((parts[0], parts[1], policy or parts[2]))
    elif ',' not in line and policy:
        assert re.fullmatch(r'\.?[\w.-]+', line), ('Invalid domain-set entry', line)
        rules.append(('DOMAIN-SUFFIX' if line.startswith('.') else 'DOMAIN', line.lstrip('.'), policy))

for line in sections['[Rule]']:
    assert line.split(',')[-1] in known, line
    add(line)
for url, policy, lines in resources:
    for line in lines:
        add(line, policy)
    if '_Domain.list' in url:
        print(f'{url.split("/")[-1]}: {len(lines)} domain entries')

def route(domain):
    for kind, value, policy in rules:
        if ((kind == 'DOMAIN' and domain == value)
            or (kind == 'DOMAIN-SUFFIX' and (domain == value or domain.endswith('.' + value)))
            or (kind == 'DOMAIN-KEYWORD' and value in domain)):
            return policy
    return 'DIRECT'

cases = {
    'Nintendo': ['accounts.nintendo.com', 'api-lp1.znc.srv.nintendo.net', 'api-lp1.av5ja.srv.nintendo.net'],
    'Discord': ['discord.com', 'gateway.discord.gg', 'cdn.discordapp.com', 'discord.media'],
    'Social': ['www.instagram.com', 'web.whatsapp.com', 'line.me', 'www.reddit.com'],
    'Streaming': ['www.twitch.tv', 'www.netflix.com'],
    '兜底后备': ['www.notion.so', 'www.dropbox.com', 'en.wikipedia.org', 'signal.org', 'www.perplexity.ai'],
    'Game': ['store.steampowered.com'],
    'Google': ['www.youtube.com'],
    'AI': ['chatgpt.com'],
    'DIRECT': ['appcfg.v.qq.com', 'www.bilibili.com', 'www.taobao.com', 'www.apple.com', 'example.org'],
}
failures = []
for expected, domains in cases.items():
    for domain in domains:
        actual = route(domain)
        print(f'{domain} -> {actual}')
        if actual != expected:
            failures.append((domain, expected, actual))
assert not failures, failures
print(f'PASS: {len(resources)} subscriptions, {sum(map(len, cases.values()))} domain cases, policy references and cycles')
print('Static domain checks only; device import, plugins, IP routing and connectivity require Loon.')
