# loon-config

A lightweight Loon cloud configuration template.

## Important

- Do **not** commit proxy subscription URLs, node passwords, cookies, MITM certificates, or private keys.
- Loon cloud import needs URLs that the app can fetch directly.
- A GitHub **private** repository's `raw.githubusercontent.com` URLs usually require authentication, so they may not work directly in Loon.
- Recommended setup: keep this repo public with no secrets, or keep source private and publish generated files to a public/unlisted hosting endpoint.

## Files

- `loon.conf`: main cloud config
- `plugins/ad-lite.plugin`: tiny no-MITM/no-script ad starter
- `rules/*.list`: lightweight remote rules
- `sources.md`: upstream/source tracking

## Public raw import URL, if repository is public

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/loon.conf
```
