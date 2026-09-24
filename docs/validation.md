# Validation

## Application file refresh — 25 September 2026

- Replaced the CV download with the latest supplied `LB_CV-v3.pdf` and the self-introduction download with the supplied 17-slide `HNU_BoLiu_v1.pptx`.
- SHA-256 comparisons confirm that both published assets match their supplied source files exactly.
- Updated the visible PPTX size from 31 MB to 24 MB.

## Hunan University scholarship evidence — 22 September 2026

- The supplied university proof explicitly lists First Prize Scholarships in 2024 and 2025.
- Both bilingual award entries now point to one WebP proof image. The student ID, national ID and verification QR code are excluded from the published image; the original PDF stays outside the site.

## Research vision and application materials — 19 September 2026

- Both homepages show Spatiotemporal Intelligence first as current research, followed by Spatial Understanding, Embodied Intelligence and Human–AI Interaction as PhD directions.
- Sidebar CV links resolve to the supplied v3 PDF; both PhD notices expose the self-introduction PPTX with a download attribute.
- SHA-256 comparisons confirm that site assets and generated downloads match the user-supplied PDF and PPTX exactly.
- Jekyll production build, all 28 generated pages, 26 sitemap routes, local resources and anchors, and whitespace checks passed.

## Target management project — 18 September 2026

- Added English and Chinese `target-manage` detail pages, with links from each homepage and Projects list.
- Seven project records now generate 42 homepage preview cards, 28 HTML pages and 26 unique sitemap routes.
- The supplied architecture image is served as WebP, with localized image descriptions. The personal-role line is omitted when no role is provided.
- Jekyll production build, generated-site resource and anchor validation, bilingual route checks and Git whitespace checks passed.

## Previous validation

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
- All 20 awards have evidence images. The 2024 and 2025 HNU scholarship entries use one university-issued proof with ID numbers hidden; the 2023–2024 FZU scholarship retains its existing CV-record image; the smart-city entry uses project presentation material.
- Hobbies: 16 hobby photos plus 4 volunteering photos, with the part-time role and stated dates.
- Healthcare and C-V2X covers were checked against the user’s supplied images and extracted from the matching original materials.
- Production build, all local resource / anchor checks, JavaScript syntax and whitespace checks passed.

## Homepage and project revision

- Four homepage preview regions in both languages, with 41 linked cards (10 publications, 6 projects, 20 awards, 5 hobbies / volunteering entries).
- Anonymous repositories present for MOTION and AgentApp; public source-code links present for Healthcare V2 and C-V2X.
- New positioning-error-analysis project has English and Chinese detail routes; MAEDE remains in Publications only.
- Revised AgentApp, UniMob and positioning-analysis cover images were visually inspected against the source figures.
- Live YouTube playback and responsive browser interaction were not tested; embed markup, IDs, accessibility attributes and destination mapping were checked in generated HTML.
- Every external HTTP/HTTPS anchor opens in a new tab with `noopener noreferrer`; internal navigation and downloadable site resources stay in the current tab.
- Electronic Keyboard replaces Music in both language variants. Publication GitHub and anonymous-code links use the same burgundy icon button as project source-code links.
- The sidebar contains the official Hunan University emblem and no longer displays the short profile-note sentence.
- LLMApp is Published; UniMob links to arXiv:2602.19694; AI Voice Assistant and Walking Stick expose their supplied GitHub repositories.
