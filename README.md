# loon-config

A lightweight Loon cloud configuration template.

## Import

Recommended import URL, served by GitHub Pages:

```text
https://limelisest.github.io/loon-config/loon.lcf
```

Loon URL scheme import link:

```text
https://www.nsloon.com/openloon/import?sub=https://limelisest.github.io/loon-config/loon.lcf
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/loon.lcf
```

## Routing design

This config references popular upstream rules directly instead of copying them:

- `blackmatrix7/ios_rule_script` via jsDelivr CDN for Apple, Microsoft, GitHub, Google, Telegram, AI, streaming, China, Direct, and ProxyLite rules.
- Local `rules/*.lsr` files are only small personal overrides.
- `AdvertisingLite` and the local ad plugin are included but disabled by default to avoid app startup slowdowns while testing.

## Node automation

Node names are auto-classified by `[Remote Filter]` into:

- `HK`, `JP`, `US`, `SG`, `TW`, `KR`
- `Auto`, `Manual`, `Fallback`
- `AI` and `Gemini` default to `JP`, then `US` / `SG` / `HK` / `PROXY`

After importing, add your proxy subscription/nodes in Loon, then check whether each region group has matched nodes.

## Important

- Do **not** commit proxy subscription URLs, node passwords, cookies, MITM certificates, or private keys.
- Loon cloud import needs URLs that the app can fetch directly.
- This repo is public so Loon can fetch the config and local override files directly.
- Keep nodes/subscriptions local in Loon unless you are using a private publishing pipeline.

## Files

- `loon.lcf`: main cloud config for current Loon versions
- `loon.conf`: compatibility copy for older naming habits
- `plugins/ad-lite.lpx`: tiny no-MITM/no-script ad starter, disabled by default
- `plugins/ad-lite.plugin`: compatibility copy
- `rules/*.lsr`: lightweight local override rules for current Loon naming
- `rules/*.list`: compatibility copies
- `sources.md`: upstream/source tracking
