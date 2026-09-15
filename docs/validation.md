# Validation

Validated on 15 September 2026.

- Jekyll 3.10 production build with strict front matter: passed.
- 26 generated HTML files: 24 content routes plus a 404 page and the legacy Chinese redirect.
- XML sitemap: 24 unique content routes.
- Both publication pages: all 10 papers present.
- All local page links, PDF links, images, YouTube destinations and local fragment anchors: resolved.
- Both language variants: correct HTML language and alternate-page metadata.
- Every content page: one main heading; no duplicate HTML IDs.
- All image descriptions present; YouTube iframes have descriptive titles, lazy loading, fullscreen support and no autoplay parameter.
- All three supplied YouTube IDs appear on their corresponding detail pages and in each language’s Projects demo gallery.
- No generated page contains the template author’s identity, tracking service or unresolved Liquid markup.
- Development notes, scripts, license and README are excluded from the generated public site.
- JavaScript syntax and Git whitespace checks: passed.

Images and video poster frames were visually inspected during preparation. Browser interaction and viewport screenshot testing were not performed.

The Mac’s system Ruby is 2.6. Temporary compatible build dependencies were installed under `/tmp/bo-site-gems`; this does not change the website’s runtime architecture. On a fresh machine, use the README’s Bundler workflow with a newer Ruby.


## Follow-up revision checks

- Exact publication order checked in both languages: MOTION, AgentApp, LLMApp, UniMob, RAG²-MP, CSTNet, MAEDE, MoE-LLM, HPDM, R2-Transfer.
- Removed MOTION / AgentApp / MAEDE project routes are absent from generated output; their paper records remain.
- Homepage: four research stages, both email addresses, three institutional links, two underlined advisor links, YouTube channel link, SVG envelope/GitHub/YouTube icons and the short CV label.
- News: full paper titles in quotation marks, italicized full journal names, acknowledgments and closing emoji.
- All 20 awards have evidence images. The 2025 HNU scholarship and the 2023–2024 FZU scholarship retain their existing CV-record images; the smart-city entry uses project presentation material.
- Hobbies: 16 hobby photos plus 4 volunteering photos, with the part-time role and stated dates.
- Healthcare and C-V2X covers were checked against the user’s supplied images and extracted from the matching original materials.
- Production build, all local resource / anchor checks, JavaScript syntax and whitespace checks passed.

## Homepage and project revision

- Four homepage preview regions in both languages, with 41 linked cards (10 publications, 6 projects, 20 awards, 5 hobbies / volunteering entries).
- Anonymous repositories present for MOTION and AgentApp; public source-code links present for Healthcare V2 and C-V2X.
- New positioning-error-analysis project has English and Chinese detail routes; MAEDE remains in Publications only.
- Revised AgentApp, UniMob and positioning-analysis cover images were visually inspected against the source figures.
- Live YouTube playback and responsive browser interaction were not tested; embed markup, IDs, accessibility attributes and destination mapping were checked in generated HTML.
