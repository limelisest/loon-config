# Sources

This template is self-maintained and intentionally lightweight.

## Referenced upstream projects

- Loon official/example config format: https://github.com/Loon0x00/LoonExampleConfig
- blackmatrix7/ios_rule_script: https://github.com/blackmatrix7/ios_rule_script
  - License: GPL-2.0 as reported by GitHub repository metadata.
  - Usage here: direct raw URL references in `loon.lcf`; upstream rule contents are not copied into this repository.
  - Referenced categories: `AdvertisingLite` (disabled), `Direct`, `China`, `Apple`, `Microsoft`, `GitHub`, `Telegram`, `OpenAI`, `Anthropic`, `Gemini`, `YouTube`, `Netflix`, `Disney`, `Spotify`, `TikTok`, `ProxyLite`.
- luestr/ShuntRules: https://github.com/luestr/ShuntRules
  - Used as a design reference for merged `.lsr`-style Loon rule organization.
  - Its README states the data source is `blackmatrix7/ios_rule_script`.

## Licensing / maintenance notes

- Prefer referencing upstream raw URLs instead of copying content.
- Record upstream project, URL, license, and reason for inclusion.
- Avoid large all-in-one MITM/script plugins unless enabled per app.
- Keep local `rules/*.lsr` files small and reserved for personal overrides.

## General references

- GitHub licensing guidance: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
