# Validation

Validated on 15 September 2026.

- Jekyll 3.10 production build with strict front matter: passed.
- 26 generated HTML files: 24 content routes plus a 404 page and the legacy Chinese redirect.
- XML sitemap: 24 unique content routes.
- Both publication pages: all 10 papers present.
- All local page links, PDF links, images, video sources and fragment anchors: resolved.
- Both language variants: correct HTML language and alternate-page metadata.
- Every content page: one main heading; no duplicate HTML IDs.
- All image descriptions present; videos have controls, load on demand and do not autoplay.
- All three demonstration videos: H.264 video and AAC audio, with complete source durations retained.
- No generated page contains the template author’s identity, tracking service or unresolved Liquid markup.
- Development notes, scripts, license and README are excluded from the generated public site.
- JavaScript syntax and Git whitespace checks: passed.

Images and video poster frames were visually inspected during preparation. Browser interaction and viewport screenshot testing were not performed.

The Mac’s system Ruby is 2.6. Temporary compatible build dependencies were installed under `/tmp/bo-site-gems`; this does not change the website’s runtime architecture. On a fresh machine, use the README’s Bundler workflow with a newer Ruby.


## Follow-up revision checks

- Exact publication order checked in both languages: MOTION, AgentApp, LLMApp, UniMob, RAG²-MP, CSTNet, MAEDE, MoE-LLM, HPDM, R2-Transfer.
- Removed MOTION / AgentApp project routes are absent from generated output; their paper records remain.
- Homepage: four research stages, both email addresses, three institutional links, two advisor links, SVG envelope/GitHub icons and the short CV label.
- News: full paper titles in quotation marks, full journal names, acknowledgments and closing emoji.
- All 13 awards have evidence images. Four are explicitly labeled CV records; the smart-city entry uses project presentation material.
- Hobbies: 16 hobby photos plus 4 volunteering photos, with the part-time role and stated dates.
- Healthcare and C-V2X covers were checked against the user’s supplied images and extracted from the matching original materials.
- Production build, all local resource / anchor checks, JavaScript syntax and whitespace checks passed.
