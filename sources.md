# Sources

This template is self-maintained and intentionally lightweight.

## Referenced upstream projects

- Loon official/example config format: https://github.com/Loon0x00/LoonExampleConfig
- Example LCF/filter configurations reviewed:
  - https://github.com/eulac-dev/Proxy/blob/main/Loon/config/loon.lcf
  - https://github.com/wsyangzy/proxy-scripts/blob/main/loon.lcf
- blackmatrix7/ios_rule_script: https://github.com/blackmatrix7/ios_rule_script
  - License: GPL-2.0 as reported by GitHub repository metadata.
  - Usage here: direct CDN/raw URL references in `loon.lcf`; upstream rule contents are not copied into this repository.
  - Referenced categories: `AdvertisingLite` (disabled), `Direct`, `China`, `Apple`, `Microsoft`, `GitHub`, `Google`, `Telegram`, `OpenAI`, `Anthropic`, `Gemini`, `YouTube`, `Netflix`, `Disney`, `Spotify`, `TikTok`, `ProxyLite`.
- luestr/ShuntRules: https://github.com/luestr/ShuntRules
  - Used as a design reference for merged `.lsr`-style Loon rule organization.
  - Its README states the data source is `blackmatrix7/ios_rule_script`.

## CDN / import notes

- Main config is served from GitHub Pages: `https://limelisest.github.io/loon-config/loon.lcf`.
- Upstream rules use jsDelivr URLs such as `https://cdn.jsdelivr.net/gh/...` to reduce first-import failures caused by `raw.githubusercontent.com` access.
- Local override rules/plugins are served from GitHub Pages.

## Licensing / maintenance notes

- Prefer referencing upstream URLs instead of copying content.
- Record upstream project, URL, license, and reason for inclusion.
- Avoid large all-in-one MITM/script plugins unless enabled per app.
- Keep local `rules/*.lsr` files small and reserved for personal overrides.

## General references

- GitHub licensing guidance: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
