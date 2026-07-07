# limelisest-loon-config

A Loon cloud configuration based on a mature upstream template.

## Current base

- Base config: `Repcz/Tool` → `Tool/X/Loon/Loon.conf`.
- Remote rules primarily use `blackmatrix7/ios_rule_script` Loon rule lists via jsDelivr (`cdn.jsdelivr.net/gh/...`).
- Upstream author header is preserved in `limelisest-loon-config.lcf`.
- Loon requirement noted by upstream: `Loon Version ≥ 3.2.3`.

## Import

Recommended import URL, served by GitHub Pages:

```text
https://limelisest.github.io/loon-config/limelisest-loon-config.lcf
```

Loon unified import link:

```text
https://www.nsloon.com/openloon/import?sub=https%3A%2F%2Flimelisest.github.io%2Floon-config%2Flimelisest-loon-config.lcf
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/limelisest-loon-config.lcf
```

## What to change first

1. Add your proxy subscription/nodes locally in Loon or under `[Remote Proxy]` if you publish privately.
2. Check `[Remote Filter]` node matching: `HK`, `US`, `SG`, `JP`, `TW`.
3. Tune `[Proxy Group]`: `兜底后备` is the only base manual selector, and its default first option is `自动选择`.
4. Category groups such as `AI`, `Streaming`, `Telegram`, and `二次元` point to their preferred default first, then fallback choices.
5. `二次元` covers Pixiv / BOOTH / FANBOX via the upstream `Pixiv` rule and defaults to `Japan`.
6. Apple rules default to `DIRECT`.
7. Keep secrets out of this public repo: subscription URLs, node passwords, cookies, MITM certificates, private keys.

## Files

- `limelisest-loon-config.lcf`: main cloud config, recommended for import
- `sources.md`: upstream/source tracking
- `LICENSE`: repository license
