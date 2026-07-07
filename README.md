# limelisest-loon-config

A Loon cloud configuration based on a mature upstream template.

## Current base

- Base config: `Repcz/Tool` → `Tool/X/Loon/Loon.conf`.
- Remote rules now primarily use `blackmatrix7/ios_rule_script` Loon rule lists, because that project has native Loon rule paths and is actively maintained.
- Rule URLs use the jsDelivr GitHub mirror (`cdn.jsdelivr.net/gh/...`) to reduce import/update failures compared with direct raw GitHub access.
- Upstream author header is preserved in `limelisest-loon-config.lcf`.
- Loon requirement noted by upstream: `Loon Version ≥ 3.2.3`.

## Import

Recommended import URL, served by GitHub Pages:

```text
https://limelisest.github.io/loon-config/limelisest-loon-config.lcf
```

Loon URL scheme import link:

```text
https://www.nsloon.com/openloon/import?sub=https://limelisest.github.io/loon-config/limelisest-loon-config.lcf
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/limelisest-loon-config.lcf
```

## What to change first

1. Add your proxy subscription/nodes locally in Loon or under `[Remote Proxy]` if you publish privately.
2. Check `[Remote Filter]` node matching: `HK`, `US`, `SG`, `JP`, `TW`.
3. Tune `[Proxy Group]` defaults, especially `Manual`, `Global`, `AI`, `Streaming`, `Telegram`, and `Final`.
4. Review `[Remote Rule]`: rules are sourced from `blackmatrix7/ios_rule_script`; AI is split into `OpenAI` / `Anthropic` / `Gemini`, and ad blocking uses `AdvertisingLite` + `Hijacking`.
5. Review `[Plugin]`: this base enables many plugin/ad-removal entries by default, including `whatshub.top` YouTube and `iRingo WeatherKit v2.0.1`. Disable entries you do not need if an app breaks.
6. Keep secrets out of this public repo: subscription URLs, node passwords, cookies, MITM certificates, private keys.

## Files

- `limelisest-loon-config.lcf`: main cloud config for current Loon versions
- `sources.md`: upstream/source tracking
- `LICENSE`: repository license
