# limelisest-loon-config

A Loon cloud configuration based on a mature upstream template.

## Current base

- Base config: `Repcz/Tool` → `Tool/X/Loon/Loon.conf`.
- Remote rules primarily use `blackmatrix7/ios_rule_script` Loon rule lists via GitHub raw direct links (`raw.githubusercontent.com/...`).
- Upstream author header is preserved in `limelisest-loon-config.lcf`.
- Loon requirement noted by upstream: `Loon Version ≥ 3.2.3`.

## Import

Recommended import URL, served by GitHub Pages:

```text
https://limelisest.github.io/loon-config/limelisest-loon-config.lcf
```

Loon unified import link:

```text
https://www.nsloon.com/openloon/import?sub=https%3A%2F%2Flimelisest.github.io%2Floon-config%2Flimelisest-loon-config.lcf
```

Raw GitHub fallback:

```text
https://raw.githubusercontent.com/limelisest/loon-config/main/limelisest-loon-config.lcf
```

## What to change first

1. Add your proxy subscription/nodes locally in Loon or under `[Remote Proxy]` if you publish privately.
2. Check `[Remote Filter]` node matching: `HK`, `US`, `SG`, `JP`, `TW`.
3. `[Proxy Group]` is organized into three sections: `节点选择策略`, `分流策略`, and `国家策略`.
4. Tune `节点选择策略`: `兜底后备` is the base manual selector; its first/default option is `自动选择`, followed by `本地节点`. `本地节点` uses the `本地节点筛选` NodeSelect filter, intended to include only nodes added locally in Loon.
5. Category groups such as `iOS推送`, `AI`, `Streaming`, `Telegram`, `Game`, and `Pixiv/booth/fanbox` are under `分流策略` and point to their preferred default first, then fallback choices.
6. `Pixiv/booth/fanbox` covers Pixiv / BOOTH / FANBOX via the upstream `Pixiv` rule and defaults to `Japan`.
7. `游戏服务` uses the upstream aggregate `Game` rule with policy `Game`, covering Steam, Epic, Xbox, Nintendo/Switch, PlayStation, EA, Blizzard, Ubisoft and other platforms. Nintendo/Switch now has a dedicated `Nintendo` group and rule before `Game`, defaulting to `Game`; select a concrete node via `All` when diagnosing connections. Separate Steam/Epic rules are retained but disabled to avoid duplicate matching.
8. Default route is `DIRECT` (`FINAL,DIRECT`). Foreign access relies on upstream `Global`/GFW-style rules to enter `兜底后备`; the redundant `Proxy` rule is retained but disabled because Global already includes it.
9. Apple rules default to `DIRECT`; ChinaMax is enabled for broad CN direct matching, while the old China rule is kept disabled. Tencent/QQ overrides are maintained in the cloud rule `rules/limelisest-direct.lsr` and referenced before upstream proxy rules.
10. BiliBili ad removal uses the original Kelee `Bilibili_remove_ads.lpx`, enabled by default.
11. `iOS推送` directly references QuixoticHeart's Loon `apns.list`, defaults to `DIRECT`, and can be switched to `兜底后备`. The rule covers APNs domains plus selected IPv4/IPv6 prefixes; APNs domains remain excluded from MITM.
12. Keep secrets out of this public repo: subscription URLs, node passwords, cookies, MITM certificates, private keys.

## Files

- `limelisest-loon-config.lcf`: main cloud config, recommended for import
- `rules/limelisest-direct.lsr`: self-maintained DIRECT cloud rule for Tencent/QQ/domestic overrides
- `sources.md`: upstream/source tracking
- `LICENSE`: repository license

## Discord / Nintendo Switch App 连接排查（2026-09-26）

- 新增 `Discord` 专用策略及完整远程规则；核心域名另有本地规则，优先于插件/订阅。原配置遗漏 `Global_Domain.list`（其中包含 Discord），配合 `FINAL,DIRECT` 会漏走代理。
- 新增 `Nintendo` 策略，默认延续 `Game`，可独立切换具体节点或 `DIRECT`。原 `Game` 已覆盖任天堂域名；新增入口用于隔离排查，不代表已确认 App 连接恢复。
- 在 `Discord` / `Nintendo` 中选择 `All` 下的一个具体节点，确认节点支持并开启 UDP，先分别测试两个 App 的启动、登录和页面加载，再测试语音。地区组仍使用自动测速，不等于固定节点。
- 保留 `udp-fallback-mode = REJECT`：不支持 UDP 的节点会拒绝 UDP。改成 `DIRECT` 只会绕开代理，不会让节点获得 UDP 能力。HTTP 测速不能验证 UDP/NAT。
- Discord 语音协商会返回服务器 IP/端口，单靠域名规则不能保证所有语音 UDP 都命中；若仍卡 RTC，请在 Loon 请求记录确认该 UDP 的实际规则、策略和节点。未命中的裸 IP 仍可能落入 `FINAL,DIRECT`。
- 测速地址统一改为 Loon 官方示例 `http://cp.cloudflare.com/generate_204`；本机检查返回 204，原 `http://1.1.1.1/generate_204` 请求失败。此结果不代替你的节点实测。
- 更新云配置后还需刷新远程规则，确认出现 `Discord`、`Nintendo` 策略，再重新连接应用。

### 整体检查的其他发现

- 第一轮检查的 38 个远程规则 URL（含禁用项及新增两项）均返回 HTTP 200；7 个非 Kelee 插件 URL 也返回 200，仅证明下载可达。
- 20 个 `kelee.one` 插件 URL 从本机请求均返回 403；可能是客户端限制，不能据此断言 Loon 下载失败。保留原地址，请检查 Loon 内插件更新结果。未能检查其内容或脚本冲突。
- `Script-Hub` 有官方插件和 Kelee 插件两个入口；YouTube/Spotify 也同时有多个处理插件。若相关应用异常，逐个关闭对应插件做对照，不要同时叠加排查。
- Nintendo 上游包含 `35.192.0.0/12` 大网段，原 Game 列表也包含它；该 IP 规则并非只代表任天堂。未扩大网段，未添加通用 UDP 全代理规则。
- `FINAL,DIRECT` 仍保留：其他未列入规则的海外服务可能直连；节点订阅为空是公共模板设计，需要 Loon 本地已有节点。
- 此仓库只能做静态检查与资源可达性验证；最终需要 Loon 导入、真实节点及 Nintendo Switch App/Discord 实机验证。

## 完整规则覆盖修复

原配置漏引了上游拆分的域名集。现在 `Global`、`ChinaMax`、`Apple`、`AdvertisingLite` 都同时加载普通规则与 `_Domain.list`；只加载普通文件，即使 HTTP 200、头部统计有数万条，实际也不代表域名规则已加载。

2026-09-26 下载快照中，补入 Global 34,901 条、ChinaMax 111,521 条、Apple 1,560 条、AdvertisingLite 37,692 条域名记录；数量会随上游更新变化。保留 `FINAL,DIRECT`，国内规则在 Global 前，恢复完整的国内直连/海外代理/广告拦截覆盖。

| 服务 | 策略 |
| --- | --- |
| Nintendo Switch App 登录/API（如 accounts.nintendo.com、api-lp1.znc.srv.nintendo.net、api-lp1.av5ja.srv.nintendo.net） | Nintendo |
| Discord 登录、网关、附件 | Discord |
| Instagram、WhatsApp、LINE、Reddit，以及已有 Twitter/Facebook/TikTok | Social |
| Twitch，以及已有 Netflix/Disney/PrimeVideo/HBO/Bahamut | Streaming |
| Notion、Dropbox、Wikimedia | 兜底后备 |
| Signal、Perplexity 等其他 Global 域名集收录服务 | 兜底后备 |

Nintendo App 原域名已被 Game 覆盖，不能把所有连接故障都归因于漏规则。更新后若仍无法登录，固定一个节点对照，并查看失败请求的目标域名、命中策略和错误信息；目前未取得设备日志。规则命中只证明选路，不证明节点可用或账号地区符合服务要求。

规则资源与域名覆盖可用 `python3 scripts/check_rules.py` 检查（会联网下载规则）。这是静态域名匹配检查，不模拟插件、DNS、IP 规则、节点转发或 Loon 原生解析器。
