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

## Important

- Do **not** commit proxy subscription URLs, node passwords, cookies, MITM certificates, or private keys.
- Loon cloud import needs URLs that the app can fetch directly.
- This repo is public so Loon can fetch the raw files directly.
- Keep nodes/subscriptions local in Loon unless you are using a private publishing pipeline.

## Files

- `loon.lcf`: main cloud config for current Loon versions
- `loon.conf`: compatibility copy for older naming habits
- `plugins/ad-lite.lpx`: tiny no-MITM/no-script ad starter
- `plugins/ad-lite.plugin`: compatibility copy
- `rules/*.lsr`: lightweight remote rules for current Loon naming
- `rules/*.list`: compatibility copies
- `sources.md`: upstream/source tracking
