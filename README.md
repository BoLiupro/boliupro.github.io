# Bo Liu Academic Homepage

A bilingual academic website for Bo Liu (刘博), Hunan University. Built on the existing Jekyll / GitHub Pages template, with a compact profile, a research narrative, visual publications, project pages, awards, and photo galleries.

## Local preview

Use Ruby 3.1 or newer with Bundler (recommended):

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000`. For a production check:

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py _site
```

The site uses GitHub Pages-compatible Jekyll 3.10 and no custom plugins. Ruby 2.6 can build it with older compatible transitive dependencies, but a current Ruby is preferable.

## GitHub Pages

The configured site address is `https://boliupro.github.io`. In the repository’s **Settings → Pages**, choose **Deploy from a branch**, your website branch, and **/(root)**. Commit and push the source when ready. There is no custom-domain CNAME. The generated `_site/` folder is excluded from Git.

This delivery changes local website files; it does not commit, push, or change your live deployment.

## Editing content

| Content | Source |
| --- | --- |
| English / Chinese About Me | `index.md` / `zh/index.md` |
| PhD notice and research interests | `_data/home.yml` |
| Email, Scholar, GitHub, affiliations | `_data/profile.yml` |
| Navigation and interface translations | `_data/ui.yml` |
| 10 publications, authors, statuses and links | `_data/publications.yml` |
| Project cards | `_data/projects.yml` |
| Project detail pages | `_projects/<id>-en.md`, `_projects/<id>-zh.md` |
| News, newest first | `_data/news.yml` |
| Awards | `_data/awards.yml` |
| Hobbies and image captions | `_data/hobbies.yml` |
| Styles and mobile menu | `assets/css/main.css`, `assets/js/main.js` |

Keep English and Chinese content together in the data files. Shared factual fields (authors, status, year, files) appear only once. Only add resource buttons when the destination exists. Homepage news is limited to seven items; the complete archive lives at `/news/` and `/zh/news/`.

## Materials

- `assets/images/`: portrait, 10 paper illustrations, project images, optimized photo galleries.
- `assets/files/papers/`: all 10 supplied manuscripts.
- `assets/files/projects/`: selected undergraduate project reports.
- `assets/videos/`: three compressed MP4 demonstrations, loaded on demand.
- `assets/files/Bo-Liu-CV.pdf`: the supplied PDF CV. The website additionally includes three papers from the newer Word CV.

See [site map and content model](docs/site-map-and-content-model.md), [English homepage copy](docs/english-homepage-copy.md), and [content provenance and remaining details](docs/content-notes.md).

The template’s license is preserved in `LICENSE`; original author content and tracking have been removed from the published pages.
