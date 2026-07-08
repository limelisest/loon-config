# Sources

## Current copied base

- Repcz/Tool Loon config: https://github.com/Repcz/Tool/blob/X/Loon/Loon.conf
  - Raw URL copied into `limelisest-loon-config.lcf`: https://raw.githubusercontent.com/Repcz/Tool/X/Loon/Loon.conf
  - Upstream header reports last update: `2026-6-29 19:50`.
  - Upstream says it is based on iKeLee's Loon simple sample configuration.
  - License checked from upstream `LICENSE`: MIT License, Copyright (c) 2024 Repcz.
  - The upstream author/TG/update header is preserved in the copied config.

## Upstream resources referenced by the copied config

- Primary remote rules: blackmatrix7/ios_rule_script Loon rules under `https://cdn.jsdelivr.net/gh/blackmatrix7/ios_rule_script@master/rule/Loon/...`.
  - Repository: https://github.com/blackmatrix7/ios_rule_script
  - Used because it provides native Loon rule paths and maintained category rules.
  - AI is split into `OpenAI`, `Anthropic`, and `Gemini`, all using policy `AI`.
  - Pixiv / BOOTH / FANBOX uses upstream `Pixiv/Pixiv.list`, which contains `booth.pm`, `fanbox.cc`, `pixiv.*`, and `pximg.net`, all using policy `Pixiv/booth/fanbox`.
  - Pixiv policy icon: https://raw.githubusercontent.com/lige47/QuanX-icon-rule/main/icon/04ProxySoft/pixiv.png
  - Apple rules use policy `DIRECT`.
  - Tencent/QQ handling: local DIRECT overrides force `appcfg.v.qq.com`, `*.qq.com`, `*.gtimg.com`, `*.qpic.cn`, `*.tencent.com`, `*.tencent-cloud.net`, `*.myqcloud.com`, and `*.wechat.com` to direct. Upstream `TencentVideo` and `WeChat` rules are also referenced as DIRECT before the general `Proxy` rule.
  - `China`, `LAN`, Tencent/QQ direct rules are kept before the general `Proxy` rule to avoid domestic domains falling into proxy fallback.
  - Ad blocking uses `AdvertisingLite` and `Hijacking`.
- Base config source remains Repcz/Tool; plugin URLs inherited from the copied base remain unchanged except user-requested edits.
- Loyalsoldier GeoIP / ASN databases:
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-without-asn.mmdb`
  - `https://raw.githubusercontent.com/Loyalsoldier/geoip/release/GeoLite2-ASN.mmdb`
- Icons from Koolson/Qure, Orz-3/mini, and lige47/QuanX-icon-rule.
- Plugins from VirgilClyne/GetSomeFries, chavyleung/scripts, sub-store-org/Sub-Store, Script-Hub-Org/Script-Hub, kelee.one, DualSubs, and NSRingo.
- Added user-requested plugin references:
  - BiliBili ad removal: https://kelee.one/Tool/Loon/Lpx/Bilibili_remove_ads.lpx
  - iRingo WeatherKit v2.0.1: https://github.com/NSRingo/WeatherKit/releases/download/v2.0.1/iRingo.WeatherKit.plugin

## Previous design references

These were used by the old lightweight template and may still be useful when customizing:

- Loon official/example config format: https://github.com/Loon0x00/LoonExampleConfig
- blackmatrix7/ios_rule_script: https://github.com/blackmatrix7/ios_rule_script
- luestr/ShuntRules: https://github.com/luestr/ShuntRules

## Import notes

- Loon's unified import link uses `sub=encode(url)`, so README import links percent-encode the config URL.
- `limelisest-loon-config.lcf` is the only recommended import target.

## Maintenance notes

- Keep subscription URLs, node passwords, cookies, MITM certificates, and private keys out of this public repository.
- If plugin behavior causes breakage, disable the relevant `[Plugin]` line first, then test again.
- If this config is republished publicly, preserve upstream attribution and license notices.
