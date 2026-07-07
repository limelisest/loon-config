# Sources

## Current copied base

- Repcz/Tool Loon config: https://github.com/Repcz/Tool/blob/X/Loon/Loon.conf
  - Raw URL copied into `loon.lcf` and `loon.conf`: https://raw.githubusercontent.com/Repcz/Tool/X/Loon/Loon.conf
  - Upstream header reports last update: `2026-6-29 19:50`.
  - Upstream says it is based on iKeLee's Loon simple sample configuration.
  - License checked from upstream `LICENSE`: MIT License, Copyright (c) 2024 Repcz.
  - The upstream author/TG/update header is preserved in the copied config.

## Upstream resources referenced by the copied config

- Repcz rule lists under `https://github.com/Repcz/Tool/raw/X/Loon/Rules/...`
- Repcz Surge proxy list: `https://github.com/Repcz/Tool/raw/X/Surge/Rules/Proxy.list`
- Loyalsoldier GeoIP / ASN databases:
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-without-asn.mmdb`
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/GeoLite2-ASN.mmdb`
- Icons from Koolson/Qure, Orz-3/mini, and lige47/QuanX-icon-rule.
- Plugins from VirgilClyne/GetSomeFries, chavyleung/scripts, sub-store-org/Sub-Store, Script-Hub-Org/Script-Hub, kelee.one, DualSubs, and NSRingo.

## Previous design references

These were used by the old lightweight template and may still be useful when customizing:

- Loon official/example config format: https://github.com/Loon0x00/LoonExampleConfig
- blackmatrix7/ios_rule_script: https://github.com/blackmatrix7/ios_rule_script
- luestr/ShuntRules: https://github.com/luestr/ShuntRules

## Maintenance notes

- Keep subscription URLs, node passwords, cookies, MITM certificates, and private keys out of this public repository.
- If plugin behavior causes breakage, disable the relevant `[Plugin]` line first, then test again.
- If this config is republished publicly, preserve upstream attribution and license notices.
