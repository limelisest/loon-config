# Sources

## Current copied base

- Repcz/Tool Loon config: https://github.com/Repcz/Tool/blob/X/Loon/Loon.conf
  - Raw URL copied into `limelisest-loon-config.lcf`: https://raw.githubusercontent.com/Repcz/Tool/X/Loon/Loon.conf
  - Upstream header reports last update: `2026-6-29 19:50`.
  - Upstream says it is based on iKeLee's Loon simple sample configuration.
  - License checked from upstream `LICENSE`: MIT License, Copyright (c) 2024 Repcz.
  - The upstream author/TG/update header is preserved in the copied config.

## Upstream resources referenced by the copied config

- Primary remote rules: blackmatrix7/ios_rule_script Loon rules under `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/...`.
  - Repository: https://github.com/blackmatrix7/ios_rule_script
  - Used because it provides native Loon rule paths and maintained category rules.
  - `[Proxy Group]` is organized into three sections: `节点选择策略`, `分流策略`, and `国家策略`.
  - `节点选择策略` includes `本地节点`, a manual select group referencing the `本地节点筛选` NodeSelect filter. `兜底后备` defaults to `自动选择`, with `本地节点` as the next manual option.
  - Apple push routing directly references QuixoticHeart's Loon APNs rule with policy `iOS推送`: https://raw.githubusercontent.com/QuixoticHeart/rule-set/refs/heads/ruleset/loon/apns.list
  - Upstream repository: https://github.com/QuixoticHeart/rule-set (GPL-3.0). The rule covers APNs-related domains and selected Apple IPv4/IPv6 prefixes without routing all Apple services.
  - Apple APNs network requirements: https://support.apple.com/102266 — device connections use TCP 5223 with TCP 443 fallback; Apple states a proxy must pass port 443 traffic without decrypting it.
  - `[Mitm]` explicitly excludes APNs-related `push.apple.com`, `identity.apple.com`, `akadns.net`, and `apple.com.edgekey.net` hostnames using negative entries.
  - AI is split into `OpenAI`, `Anthropic`, and `Gemini`, all using policy `AI`.
  - Pixiv / BOOTH / FANBOX uses upstream `Pixiv/Pixiv.list`, which contains `booth.pm`, `fanbox.cc`, `pixiv.*`, and `pximg.net`, all using policy `Pixiv/booth/fanbox`.
  - Game platforms use upstream aggregate `Game/Game.list` with policy `Game`. Its upstream README states it includes Steam, Epic, Xbox, Nintendo, PlayStation, EA, Blizzard, UBI/Ubisoft, Rockstar and other game services. Separate Steam/Epic entries remain disabled to avoid duplicates.
  - Pixiv policy icon: https://raw.githubusercontent.com/lige47/QuanX-icon-rule/main/icon/04ProxySoft/pixiv.png
  - Apple rules use policy `DIRECT`.
  - Tencent/QQ handling: self-maintained cloud rule `rules/limelisest-direct.lsr` forces `appcfg.v.qq.com`, `*.qq.com`, `*.gtimg.com`, `*.qpic.cn`, `*.tencent.com`, `*.tencent-cloud.net`, `*.myqcloud.com`, and `*.wechat.com` to direct. Upstream `TencentVideo` and `WeChat` rules are also referenced as DIRECT.
  - Default route is `DIRECT`. Upstream `Global/Global.list` is used as the GFW-style proxy rule into `兜底后备`; `Proxy/Proxy.list` is retained but disabled because Global includes Proxy.
  - `limelisest-direct`, `ChinaMax`, `LAN`, Tencent/QQ direct rules are kept before the Global/Proxy fallback rules. The original `China` rule is retained but disabled for easy rollback.
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

## 2026-09-26 connectivity review

- Discord rules: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Discord/Discord.list
- Nintendo rules: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Nintendo/Nintendo.list
- Both use dedicated policies before aggregate rules; core domains also have local overrides.
- Loon rule priority (local > plugin > remote, FINAL only after no match): https://nsloon.app/docs/Rule/
- Loon UDP fallback, LAN access and official test endpoint: https://nsloon.app/en/docs/General/
- Discord voice uses separately negotiated UDP IP/port: https://docs.discord.com/developers/topics/voice-connections
- No device/node connection success is claimed by this source review.

## Complete split-rule coverage

- The upstream explicitly requires paired files: https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Loon/Global/README.md
- Added matching `_Domain.list` subscriptions for Global, ChinaMax, Apple and AdvertisingLite with the same policy as their normal list.
- Global already includes Proxy; the disabled Proxy entry remains disabled to avoid redundant coverage.
- Added native Loon lists for Instagram, Whatsapp, Line, Reddit, Twitch, Notion, Dropbox and Wikimedia, all from the same blackmatrix7 upstream.
- Correction to the initial diagnosis: Discord exists in Global_Domain.list; the old config omitted that file. HTTP 200 alone did not establish complete rule coverage.
