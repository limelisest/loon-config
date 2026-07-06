# loon-config

A lightweight Loon cloud configuration template.

## Import

Recommended current Loon config file:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/loon.lcf
```

Loon URL scheme import link:

```text
https://www.nsloon.com/openloon/import?sub=https://raw.githubusercontent.com/limelisest/loon-config/main/loon.lcf
```

## Routing design

This starter config references popular upstream rules directly instead of copying them:

- `blackmatrix7/ios_rule_script` for Apple, Microsoft, GitHub, Telegram, AI, streaming, China, Direct, and ProxyLite rules.
- Local `rules/*.lsr` files are only small personal overrides.
- `AdvertisingLite` is included but disabled by default to avoid app startup slowdowns while testing.

Policy groups:

- `PROXY`: default proxy selector
- `Manual` / `Auto`: node selection helpers
- `AI`, `GitHub`, `Telegram`, `Streaming`: service-specific selectors
- `Apple`, `Microsoft`: default to `DIRECT`, can switch to proxy if needed
- `AdBlock`: `REJECT` or `DIRECT`
- `Final`: fallback group

## Important

- Do **not** commit proxy subscription URLs, node passwords, cookies, MITM certificates, or private keys.
- Loon cloud import needs URLs that the app can fetch directly.
- This repo is public so Loon can fetch the raw files directly.
- Keep nodes/subscriptions local in Loon unless you are using a private publishing pipeline.
- After importing the cloud config, add your proxy subscription/nodes in Loon, then select policies in the groups above.

## Files

- `loon.lcf`: main cloud config for current Loon versions
- `loon.conf`: compatibility copy for older naming habits
- `plugins/ad-lite.lpx`: tiny no-MITM/no-script ad starter, disabled by default
- `plugins/ad-lite.plugin`: compatibility copy
- `rules/*.lsr`: lightweight local override rules for current Loon naming
- `rules/*.list`: compatibility copies
- `sources.md`: upstream/source tracking
