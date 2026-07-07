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
https://limelisest.github.io/loon-config/limelisest-loon-config.conf
```

Loon unified import link. The Loon manual requires `sub=encode(url)`, so the config URL is percent-encoded here:

```text
https://www.nsloon.com/openloon/import?sub=https%3A%2F%2Flimelisest.github.io%2Floon-config%2Flimelisest-loon-config.conf
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/limelisest-loon-config.conf
```

Raw GitHub fallback import link:

```text
https://www.nsloon.com/openloon/import?sub=https%3A%2F%2Fraw.githubusercontent.com%2Flimelisest%2Floon-config%2Fmain%2Flimelisest-loon-config.conf
```

## What to change first

1. Add your proxy subscription/nodes locally in Loon or under `[Remote Proxy]` if you publish privately.
2. Check `[Remote Filter]` node matching: `HK`, `US`, `SG`, `JP`, `TW`.
3. Tune `[Proxy Group]` defaults, especially `Manual`, `Global`, `AI`, `Streaming`, `Telegram`, and `Final`.
4. Review `[Remote Rule]`: rules are sourced from `blackmatrix7/ios_rule_script`; AI is split into `OpenAI` / `Anthropic` / `Gemini`, and ad blocking uses `AdvertisingLite` + `Hijacking`.
5. Review `[Plugin]`: this base enables many plugin/ad-removal entries by default, including `whatshub.top` YouTube and `iRingo WeatherKit v2.0.1`. Disable entries you do not need if an app breaks.
6. Keep secrets out of this public repo: subscription URLs, node passwords, cookies, MITM certificates, private keys.

Note: `[Proxy]` and `[Remote Proxy]` are intentionally empty in this public config. After importing the profile, add your own node subscription in Loon or in a private copy of `[Remote Proxy]`; otherwise the node/proxy list will appear empty.

## Files

- `limelisest-loon-config.conf`: main cloud config, recommended for import
- `limelisest-loon-config.lcf`: compatibility copy with the same content
- `sources.md`: upstream/source tracking
- `LICENSE`: repository license
