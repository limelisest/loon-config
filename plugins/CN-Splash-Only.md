# 国内常用 App · 仅开屏

安装地址：<https://limelisest.github.io/loon-config/plugins/CN-Splash-Only.plugin>

2026-10-21 更新，收录下表 34 个 App 的已知开屏接口或专用素材。这里的“覆盖”表示规则已收录，不表示每个版本、每次启动都有效；尚未完成 iPhone / Loon 设备实测。

需要 **Loon Build 729 或以上**（京东、小红书、酷安使用原生 `response-body-json-jq`），开启 MITM 并信任证书。云配置启用本插件、WeatherKit、Kelee YouTube，以及独立的 [Biliverse B站官方插件](https://github.com/Biliverse/ADBlock/releases/latest/download/BiliBili.ADBlock.plugin)，共四项。B站已从本合并插件中移出，由官方插件按其默认参数处理；该官方插件包含完整去广告功能，范围不限于开屏。单独安装过旧插件的设备需手动停用旧项，尤其是旧 Kelee B站插件和本站 B站仅开屏插件，避免重复处理。

| App | 收录范围 |
| --- | --- |
| 京东 | `functionId=start` 的 images / showTimesDaily；home_launchConfig |
| 小红书 | `system_service/splash_config` 的 data.ads_groups |
| 酷安 | `v6/main/init` 的 data 数组中仅移除数值 entityId=945 的开屏项 |
| 拼多多 | `api/cappuccino/splash`，含 yangkeduo 域名 |
| 闲鱼 | idlecommerce.splash.ads / splash.async.ads，含旧 taobao 网关 |
| 淘宝 | 带 tao_splash 的 noah.query；home.splash.awesome.get |
| 知乎 | commercial_api/launch_v2、real_time_launch_v2 |
| 豆瓣 | v2/app_ads/splash |
| 高德地图 | alimama/splash_screen |
| 腾讯地图 | mwaSplash 专用素材目录 |
| 美团外卖 | startpicture、openscreen；不处理 loadInfo |
| 麦当劳 | home/splash |
| 库迪咖啡 | position/list 仅 code=cotti-launch-window |
| 叮咚买菜 | advert/startUpScreen |
| 去哪儿 | qrt=p_splashAd、front/splash/ad |
| 马蜂窝 | get_launch_ad_list/v2 |
| 途牛 | operation/splash |
| 途家 | getStartPictureAdvertising |
| 希尔顿 | graphql 仅 type=splashAd |
| 穷游 | qyer/startpage |
| 腾讯新闻 | getSplash |
| 人民日报 | launchPage |
| 百度贴吧 | splashSchedule |
| 米游社 | getAppSplash |
| QQ音乐 | t_splash_info 专用素材目录；不处理其他音乐广告 |
| 酷狗音乐 | 两个 splashimg 专用素材域名；不处理其他音乐广告 |
| 雪球 | snowpard/launch_strategy/query.json |
| 中国联通 | uniAdmsInterface/getWelcomeAd |
| 天翼云盘 | include/splash 专用素材目录 |
| 有道词典 | recommend/dict/startup |
| 起点读书 | client/getsplashscreen |
| 向日葵 | materials/SLCC_IOS_STARTUP |
| 脉脉 | sdk/global/splash_ad、maimai/launch_ad |
| 微博 | sdkapp 请求仅 sub_ad_type=splash |

插件不注册首页信息流、评论、视频详情、搜索、订单、支付、登录处理，不拦整个共享广告 SDK / CDN 域名。京东、小红书、酷安会保留正常响应结构；字段缺失或类型不符合预期时保持原值。酷安仅处理启动配置中的 945 项，保留热搜、首页 Tab、其他模块和原有顺序；不引入全局穿山甲拦截。此标识来自上游脚本，尚未用当前设备响应验证；其他 SDK 下发或缓存开屏不保证覆盖。其他收录接口采用拒绝响应；可能触发 App 的本地缓存或回退逻辑，不能承诺每次冷启动无广告。

12306、滴滴、菜鸟、网易云音乐及爱奇艺等暂不纳入：本次审阅到的方案涉及共享广告位、混合启动配置或加密响应，尚不能确认可在该范围内单独处理开屏。后续仅在找到可明确区分的开屏接口后补入。

插件没有禁用 HTTPDNS，也没有强制全域 QUIC 回落；HTTP/3、直连 IP、证书校验、已有素材缓存或接口升级可能影响命中。先更新云配置和插件，彻底退出目标 App 后重新打开；若无效，在 Loon 请求记录核对 URL、协议和匹配项，不建议为清理缓存删除 App 数据。

**现有云配置仍保留 AdvertisingLite / Hijacking 通用规则订阅。** 仅开屏是本插件的范围，整个云配置仍有其他广告拦截；遇到正常页面异常时，应同时检查设备上的其他插件与通用规则。

来源、许可和维护：见 [sources.md](../sources.md)。大部分规则从 blackmatrix7/ios_rule_script 筛选并缩小范围，本插件按 [GPL-2.0](../licenses/GPL-2.0.txt) 发布。B站官方插件通过主配置独立订阅，不属于本文件的收录范围。不自动同步上游整套去广告规则。接口事实亦交叉核对 Thelongdarkorg/loon-plugins；未复制其完整插件或 jq 表达式。

静态回归检查：`python3 scripts/check_splash_plugin.py`。此检查验证 URL 范围、MITM 覆盖、配置启用项和 jq 字段保留，不模拟 Loon 原生解析器、真实 App 响应或设备网络。
