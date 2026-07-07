# Sources

## Current copied base

- Repcz/Tool Loon config: https://github.com/Repcz/Tool/blob/X/Loon/Loon.conf
  - Raw URL copied into `limelisest-loon-config.conf` and `limelisest-loon-config.lcf`: https://raw.githubusercontent.com/Repcz/Tool/X/Loon/Loon.conf
  - Upstream header reports last update: `2026-6-29 19:50`.
  - Upstream says it is based on iKeLee's Loon simple sample configuration.
  - License checked from upstream `LICENSE`: MIT License, Copyright (c) 2024 Repcz.
  - The upstream author/TG/update header is preserved in the copied config.

## Upstream resources referenced by the copied config

- Primary remote rules: blackmatrix7/ios_rule_script Loon rules under `https://cdn.jsdelivr.net/gh/blackmatrix7/ios_rule_script@master/rule/Loon/...` (jsDelivr mirror of the GitHub repository, used to reduce first-import failures in Loon).
  - Repository: https://github.com/blackmatrix7/ios_rule_script
  - Verified current commit feed during this update: `master` feed updated at `2026-07-05T19:14:21Z`.
  - Replaced the original Repcz remote-rule links so rule categories can stay aligned with the larger maintained Loon rule tree.
  - AI is split into `OpenAI`, `Anthropic`, and `Gemini`; ad blocking uses `AdvertisingLite` and `Hijacking`; CN/LAN uses `China` and `Lan`.
- Base config source remains Repcz/Tool; plugin URLs inherited from the copied base remain unchanged.
- Loyalsoldier GeoIP / ASN databases:
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-without-asn.mmdb`
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/GeoLite2-ASN.mmdb`
- Icons from Koolson/Qure, Orz-3/mini, and lige47/QuanX-icon-rule.
- Plugins from VirgilClyne/GetSomeFries, chavyleung/scripts, sub-store-org/Sub-Store, Script-Hub-Org/Script-Hub, kelee.one, DualSubs, NSRingo, and whatshub.top.
- Previous Repcz remote-rule URLs were replaced by blackmatrix7 equivalents where available; no Repcz rule-list URL remains in `[Remote Rule]`.
- Added user-requested plugin references:
  - YouTube plugin: https://whatshub.top/plugin/youtube.plugin
  - iRingo WeatherKit v2.0.1: https://github.com/NSRingo/WeatherKit/releases/download/v2.0.1/iRingo.WeatherKit.plugin

## Previous design references

These were used by the old lightweight template and may still be useful when customizing:

- Loon official/example config format: https://github.com/Loon0x00/LoonExampleConfig
- blackmatrix7/ios_rule_script: https://github.com/blackmatrix7/ios_rule_script
- luestr/ShuntRules: https://github.com/luestr/ShuntRules

## Import notes

- Loon's official scheme/unified-link manual says remote config import uses `loon://import?sub=encode(url)` / `https://www.nsloon.com/openloon/import?sub=encode(url)`, so README import links percent-encode the config URL.
- `limelisest-loon-config.conf` is the recommended import target; `limelisest-loon-config.lcf` is kept as a compatibility copy.

## Maintenance notes

- Keep subscription URLs, node passwords, cookies, MITM certificates, and private keys out of this public repository.
- If plugin behavior causes breakage, disable the relevant `[Plugin]` line first, then test again.
- If this config is republished publicly, preserve upstream attribution and license notices.
