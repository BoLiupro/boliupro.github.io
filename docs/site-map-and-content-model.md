# Site Map and Content Model

## Audience and research story

The main audience is prospective PhD supervisors and research collaborators. The site explains Bo Liu’s progression from graph learning and diffusion, through semantic reasoning with LLMs, to personalized, retrieval-augmented and collaborative agents. Spatial, human-centered and embodied intelligence are framed as future interests.

## Site map

| English | Chinese | Purpose |
| --- | --- | --- |
| `/` | `/zh/` | Profile, About Me, Fall 2027 PhD notice, four research interests, seven recent news items |
| `/publications/` | `/zh/publications/` | 10 visual paper entries in the requested research order; each retains its status badge |
| `/projects/` | `/zh/projects/` | Six research / engineering projects, including three video demos |
| `/projects/<id>/` | `/zh/projects/<id>/` | Individual project story, framework or prototype, results where available, related papers and real resources |
| `/awards/` | `/zh/awards/` | Year-based awards timeline with certificate or supporting-record images |
| `/hobbies/` | `/zh/hobbies/` | Music, hiking, cycling, basketball and part-time volunteer-teaching photo galleries |
| `/news/` | `/zh/news/` | Complete news archive |

`/cn/` redirects to `/zh/`. The language switch always links to the equivalent page, including project details. `404.html`, `robots.txt` and `sitemap.xml` support discovery and missing-page navigation.

## Shared content model

### Profile

`email`, `secondary_email`, `github`, `scholar` are shared. The `en` and `zh` blocks contain role, college, center, location, photo alt text, CV label and profile note.

### Publication

- `id`: stable slug used for local assets, anchors and project relationships.
- `title`, optional `title_zh`: manuscript title; formal English titles remain in the Chinese list where no official Chinese title exists.
- `authors`: ordered names; the renderer automatically bolds exactly `Bo Liu`.
- `venue`, `year`, optional `volume`: bibliography details.
- `status`: `published`, `accepted`, `minor-revision`, or `under-review`.
- `group`: `published` (published / accepted) or `review` (revision / review).
- `summary.en`, `summary.zh`, `alt.en`, `alt.zh`: localized descriptions and accessible image text.
- `pdf`, `cover`: existing local file paths.
- Optional `doi`, `github`, `project`: real destinations only; missing resources produce no empty buttons.

Statuses never change automatically with the calendar. Update `status` and `group` together when a paper changes state, then add a news item if appropriate.

### Project

- `id`, `cover`, `tags`: identity and visual metadata.
- `en`, `zh`: title, summary, role, category, image description, optional video caption.
- Optional `papers`: publication IDs, resolved into paper cards on the detail page.
- Optional `video`, `report`, `github`, `external`: available resources.
- Optional `contain`: keeps framework images visible in full within cards.
- Two Markdown collection documents store localized long-form content and explicit `permalink` / `translation` fields.

Project records cover agentic code intelligence, MAEDE, an AI voice assistant, a connected walking stick, Healthcare, and C-V2X positioning. MOTION and AgentApp appear only in Publications. Use Overview, Motivation, Method and Results when supported. Video, gallery, dataset and code sections should appear only when the corresponding material exists.

### News

`date` is an ISO date or month, `display.en/zh` controls the visible label, and `text.en/zh` accepts Markdown. Keep the list sorted newest first. A month-only date does not invent a precise day.

### Award

Year groups contain `items` with `title.en/zh`, `organization.en/zh`, optional `note.en/zh`, and `evidence` containing an image, localized label and alt text, and optional PDF/source link. Missing certificates use a literal CV excerpt clearly labeled as a CV record. Academic-year periods stay in notes; the timeline uses the end year for scholarship periods.

### Hobby

`id`, `title.en/zh`, `description.en/zh`, and `photos[]` with `src` and `alt.en/zh`. Images are inline, without detail pages or click-through galleries.

## Add a new project

1. Put optimized assets under `assets/images/projects/` and any available demonstration under `assets/videos/`.
2. Add one localized record to `_data/projects.yml`.
3. Add `_projects/<id>-en.md` and `_projects/<id>-zh.md`, following an existing document’s front matter.
4. Add related publication IDs if relevant.
5. Build and run `scripts/check_site.py` to check both routes and resource links.

## Design tokens and behavior

Maximum width: 1180 px. White background, charcoal text, muted burgundy accent. Compact desktop sidebar; a stacked profile and expandable navigation on mobile. The header is sticky. Research interests are light bordered cards; publications and projects use figure-and-text rows; news and awards remain simple lists. Images load lazily except for the portrait. Videos use `preload="none"` and never autoplay. Content is fully rendered without JavaScript; JavaScript adds only the mobile menu.

## September 2026 content update

Publication order: MOTION → AgentApp → LLMApp → UniMob → RAG²-MP → CSTNet → MAEDE → MoE-LLM → HPDM → R2-Transfer. This manual data order takes precedence over status grouping.

The homepage research narrative uses four stages: graph/diffusion models; LLM semantic reasoning; retrieval-augmented and personalized agents; multi-agent reasoning over evolving graphs.

Volunteer teaching is stored in `_data/volunteering.yml` and appended to Hobbies, with bilingual dates, school, description, and four photos.
