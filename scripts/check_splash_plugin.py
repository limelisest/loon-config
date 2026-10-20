#!/usr/bin/env python3
"""Offline scope and preservation checks; does not emulate Loon or an iPhone."""

import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/CN-Splash-Only.plugin"


def sections(text):
    result = {}
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].lower()
            result[current] = []
        elif line and not line.startswith("#") and current:
            result[current].append(line)
    return result


def main():
    content = sections(PLUGIN.read_text())
    assert set(content) == {"rewrite", "script", "mitm"}, "Unexpected processing section"
    handlers = []
    jq_filters = []
    for line in content["rewrite"]:
        pattern, action = line.split(" ", 1)
        assert action in {"reject", "reject-dict"} or action.startswith("response-body-json-jq ")
        handlers.append(re.compile(pattern))
        if action.startswith("response-body-json-jq "):
            expression = action.split(" ", 1)[1]
            assert expression.startswith("'") and expression.endswith("'")
            jq_filters.append(expression[1:-1])
    assert len(content["script"]) == 1
    script = content["script"][0]
    assert "releases/download/v0.7.5/response.bundle.js" in script
    assert "requires-body=1" in script
    handlers.append(re.compile(script.split()[1]))
    hosts = {s.strip() for s in content["mitm"][0].split("=", 1)[1].split(",")}
    assert all(not any(c in host for c in "*?") for host in hosts), "Use exact MITM hosts"

    # Concrete endpoint examples, not fetched responses. Cover every registered handler.
    positive = [
        "https://api.m.jd.com/client.action?functionId=start&client=apple",
        "https://api.m.jd.com/client.action?client=apple&functionId=start",
        "https://api.m.jd.com/client.action?functionId=home_launchConfig",
        "https://edith.xiaohongshu.com/api/sns/v1/system_service/splash_config?device=ios",
        "https://www.xiaohongshu.com/api/sns/v2/system_service/splash_config",
        "https://api.coolapk.com/v6/main/init",
        "https://api.coolapk.com/v6/main/init?app=ios",
        "https://api.pinduoduo.com/api/cappuccino/splash?app_version=1",
        "https://api.yangkeduo.com/api/cappuccino/splash",
        "https://acs.m.goofish.com/gw/mtop.taobao.idlecommerce.splash.ads/1.0/?data=x",
        "https://acs.m.goofish.com/gw/mtop.taobao.idlecommerce.splash.async.ads/1.0/",
        "https://acs.m.taobao.com/gw/mtop.taobao.idlecommerce.splash.ads/1.0/",
        "https://acs.m.taobao.com/gw/mtop.etao.noah.query/1.0/?data=%7B%22scene%22%3A%22tao_splash%22%7D",
        "https://guide-acs.m.taobao.com/gw/mtop.taobao.wireless.home.splash.awesome.get/1.0/",
        "https://api.zhihu.com/commercial_api/launch_v2?app=ios",
        "https://api.zhihu.com/commercial_api/real_time_launch_v2?app=ios",
        "https://api.douban.com/v2/app_ads/splash",
        "https://amap-aos-info-nogw.amap.com/ws/aos/alimama/splash_screen?x=1",
        "https://m5.amap.com/ws/valueadded/alimama/splash_screen/?x=1",
        "https://4gimg.map.qq.com/mwaSplash/ad.png",
        "https://wmapi.meituan.com/api/v7/startpicture?x=1",
        "https://wmapi.meituan.com/api/v7/openscreen?ad=1",
        "https://api.mcd.cn/bff/portal/home/splash?x=1",
        "https://gateway.abite.com/cotti-capi/customer/position/list?city=1&code=cotti-launch-window",
        "https://maicai.api.ddxq.mobi/advert/startUpScreen",
        "https://client.qunar.com/pitcher-proxy?client=ios&qrt=p_splashAd&x=1",
        "https://homefront.qunar.com/front/splash/ad",
        "https://mapi.mafengwo.cn/ad/get_launch_ad_list/v2",
        "https://m.tuniu.com/api/operation/splash/v1",
        "https://client.tujia.com/bnbapp-node/app/portal/getStartPictureAdvertising",
        "https://wcprd.hilton.com.cn/app-middleware/graphql?client=ios&type=splashAd",
        "https://open.qyer.com/qyer/startpage/v1",
        "https://r.inews.qq.com/getSplash?x=1",
        "https://pdapis.pdnews.cn/api/rmrb-bff-display-zh/display/zh/c/launchPage?x=1",
        "https://c.tieba.baidu.com/c/s/splashSchedule",
        "https://bbs-api.miyoushe.com/apihub/api/getAppSplash",
        "https://y.gtimg.cn/music/common/upload/t_splash_info/ad.jpg",
        "https://splashimgbssdl.yun.kugou.com/ad.jpg",
        "https://splashimgretrybssdl.cloud.kugou.com/ad.jpg",
        "https://api.xueqiu.com/snowpard/launch_strategy/query.json?x=1",
        "https://m.client.10010.com/uniAdmsInterface/getWelcomeAd?x=1",
        "https://cloud.189.cn/include/splash/ad.png",
        "https://cdke.youdao.com/course3/recommend/dict/startup",
        "https://mage.if.qidian.com/argus/api/v1/client/getsplashscreen",
        "https://client-api.oray.com/materials/SLCC_IOS_STARTUP?lang=zh-Hans-CN",
        "https://client-api-v2.oray.com/materials/SLCC_IOS_STARTUP?lang=zh-Hans-CN",
        "https://api.taou.com/sdk/global/splash_ad",
        "https://open.taou.com/maimai/launch_ad",
        "https://sdkapp.uve.weibo.com/interface/sdk/sdkad.php?x=1&sub_ad_type=splash&y=1",
    ]
    for host in ["app.bilibili.com", "app.biliapi.net"]:
        for route in ["list", "show", "brand/list", "event/list2"]:
            positive.append(f"https://{host}/x/v2/splash/{route}?build=1")

    covered = set()
    for url in positive:
        matches = {i for i, pattern in enumerate(handlers) if pattern.search(url)}
        assert matches, f"Missed splash URL: {url}"
        assert urlsplit(url).hostname in hosts, f"Missing MITM host: {url}"
        covered |= matches
    assert covered == set(range(len(handlers))), "A handler has no positive fixture"

    # Normal and shared interfaces must never match, even when a query mentions splash.
    negative = [
        "https://api.coolapk.com/v6/feed/detail?feedid=1",
        "https://api.coolapk.com/v6/feed/replyList?feedid=1",
        "https://api.coolapk.com/v6/main/dataList?x=1",
        "https://api.coolapk.com/v6/main/indexV8?x=1",
        "https://api.coolapk.com/v6/page/dataList?x=1",
        "https://api.coolapk.com/v6/search?type=hotSearch",
        "https://api.coolapk.com/v6/account/loadConfig?key=my_page_card_config",
        "https://api.coolapk.com/v6/main/initOther?x=1",
        "https://api.coolapk.com/v60/main/init?x=1",
        "https://api-access.pangolin-sdk-toutiao.com/api/ad/union/sdk",
        "https://ads.pangle.cn/api/ad/union/sdk",
        "https://app.bilibili.com/x/v2/feed/index?screen=splash",
        "https://app.bilibili.com/x/v2/view?aid=1",
        "https://app.bilibili.com/x/v2/reply?aid=1",
        "https://api.bilibili.com/x/v2/reply?aid=1",
        "https://api.bilibili.com/x/web-interface/view?bvid=1",
        "https://api.m.jd.com/client.action?functionId=welcomeHome",
        "https://api.m.jd.com/client.action?functionId=cart",
        "https://api.m.jd.com/client.action?functionId=deliverLayer",
        "https://api.m.jd.com/client.action?functionId=queryMaterialAdverts",
        "https://api.m.jd.com/client.action?functionId=startOther",
        "https://api.m.jd.com/client.action?functionId=home_launchConfigExtra",
        "https://api.m.jd.com/client.action?xfunctionId=start",
        "https://api.m.jd.com/client.action?x=functionId=start",
        "https://m.360buyimg.com/mobilecms/s1125x2436_jfs/product.jpg",
        "https://edith.xiaohongshu.com/api/sns/v1/system_service/config?x=1",
        "https://edith.xiaohongshu.com/api/sns/v1/homefeed?x=1",
        "https://edith.xiaohongshu.com/api/sns/v1/note/comment/list?x=1",
        "https://edith.xiaohongshu.com/api/sns/v1/note/widgets?x=1",
        "https://acs.m.taobao.com/gw/mtop.etao.noah.query/1.0/?scene=home_banner",
        "https://acs.m.taobao.com/gw/mtop.taobao.idle.home.welcome/1.0/",
        "https://api.zhihu.com/commercial_api/feed?x=1",
        "https://api.zhihu.com/api/v4/answers/123",
        "https://wmapi.meituan.com/api/v7/loadInfo?x=1",
        "https://api.mcd.cn/bff/portal/richpop?x=1",
        "https://client.qunar.com/pitcher-proxy?qrt=p_splashAdExtra",
        "https://gateway.abite.com/cotti-capi/customer/position/list?code=cotti-home-window",
        "https://wcprd.hilton.com.cn/app-middleware/graphql?type=booking",
        "https://wcprd.hilton.com.cn/app-middleware/graphql?type=splashAdExtra",
        "https://m.client.10010.com/uniAdmsInterface/getHomePageAd",
        "https://y.gtimg.cn/music/common/upload/album/cover.jpg",
        "https://client-api.oray.com/materials/SLCC_IOS_DEVICE?lang=zh-Hans-CN",
        "https://sdkapp.uve.weibo.com/interface/sdk/sdkad.php?sub_ad_type=feed",
        "https://sdkapp.uve.weibo.com/interface/sdk/sdkad.php?sub_ad_type=splashExtra",
        "https://sdkapp.uve.weibo.com/interface/sdk/sdkad.php?xsub_ad_type=splash",
    ]
    # Detect unanchored hosts and page-wide matching on every intercepted host.
    splash_material_hosts = {"splashimgbssdl.yun.kugou.com", "splashimgretrybssdl.cloud.kugou.com"}
    for url in positive:
        parts = urlsplit(url)
        negative.append(url.replace(parts.netloc, parts.netloc + ".example.invalid", 1))
        if parts.netloc not in splash_material_hosts:
            for route in ["/", "/home", "/search", "/comment/list", "/video/detail", "/login", "/order/detail", "/pay"]:
                negative.append(f"https://{parts.netloc}{route}?scene=splash")
        # Complete endpoint names must not consume suffixes (directory selectors excepted).
        if not parts.path.endswith("/"):
            if not any(token in parts.path for token in ["/mwaSplash/", "/splash/v1", "/startpage/", "/t_splash_info/", "/include/splash/"]) and not any(host in parts.netloc for host in ["kugou.com", "sdkapp.uve.weibo.com"]):
                negative.append(f"{parts.scheme}://{parts.netloc}{parts.path}Extra?{parts.query}")
    for url in negative:
        assert not any(pattern.search(url) for pattern in handlers), f"Overbroad match: {url}"

    assert len(jq_filters) == 3
    assert shutil.which("jq"), "Install jq to check JSON preservation"

    def jq(expression, value):
        result = subprocess.run(["jq", "-c", expression], input=json.dumps(value), text=True, capture_output=True, check=True)
        return json.loads(result.stdout)

    jd, xhs, coolapk = jq_filters
    startup = {"images": [[{"url": "ad.jpg", "showTimes": 5}]], "showTimesDaily": 5,
               "code": 0, "login": {"enabled": True}, "home": [1, 2], "version": "test"}
    assert jq(jd, startup) == {**startup, "images": [], "showTimesDaily": 0}
    splash = {"code": 0, "data": {"ads_groups": [{"ads": [{"id": 1}]}], "normal_config": {"enabled": True}}, "trace": "keep"}
    assert jq(xhs, splash) == {**splash, "data": {**splash["data"], "ads_groups": []}}
    init = {"code": 0, "data": [{"entityId": 944, "title": "热搜"}, {"entityId": 945, "title": "开屏"},
            {"entityId": 6390, "title": "首页Tab"}, {"entityId": 20131, "entities": [{"title": "酷品"}]},
            None, 945, "945", {"entityId": "945"}, {"title": "未知模块"}, [945],
            {"entityId": 945, "title": "另一开屏项"}], "trace": {"keep": True}}
    expected_init = {**init, "data": init["data"][:1] + init["data"][2:-1]}
    assert jq(coolapk, init) == expected_init
    assert jq(coolapk, expected_init) == expected_init
    for unchanged in [None, [], [1], "text", 1, False, {}, {"data": None}, {"data": []}, {"data": "text"},
                      {"data": {"ads_groups": "unexpected"}}, {"data": {"normal_config": 1}},
                      {"images": None, "showTimesDaily": "unexpected"}]:
        assert jq(jd, unchanged) == unchanged
        assert jq(xhs, unchanged) == unchanged
        assert jq(coolapk, unchanged) == unchanged
    for unchanged in [{"data": [944, 6390, None, {}, {"entityId": 944}]}, {"data": 945}]:
        assert jq(coolapk, unchanged) == unchanged
    assert jq(jd, {"images": [], "showTimesDaily": 0}) == {"images": [], "showTimesDaily": 0}
    assert jq(xhs, {"data": {"ads_groups": []}}) == {"data": {"ads_groups": []}}

    config = sections((ROOT / "limelisest-loon-config.lcf").read_text())
    enabled = [s.split(",", 1)[0] for s in config["plugin"] if "enabled=true" in s]
    assert set(enabled) == {
        "https://kelee.one/Tool/Loon/Lpx/YouTube_remove_ads.lpx",
        "https://github.com/NSRingo/WeatherKit/releases/download/v2.0.1/iRingo.WeatherKit.plugin",
        "https://limelisest.github.io/loon-config/plugins/CN-Splash-Only.plugin",
    }
    assert len(enabled) == 3
    assert "GNU GENERAL PUBLIC LICENSE" in (ROOT / "licenses/GPL-2.0.txt").read_text()
    print(f"PASS: {len(handlers)} handlers; {len(positive)} splash URLs; {len(negative)} excluded URLs; jq preservation; 3 enabled plugins")
    print("Static checks only; native Loon parsing and iPhone behavior not tested.")


if __name__ == "__main__":
    main()
