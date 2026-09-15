#!/usr/bin/env python3
"""Validate the generated Jekyll site using Python's standard library."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.anchors = []
        self.h1 = 0
        self.images = []
        self.lang = None
        self.alternates = {}
        self.videos = []
        self.iframes = []
        self.previews = 0
        self.publications = 0
        self.publication_ids = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img':
            self.images.append(a)
        if tag == 'iframe':
            self.iframes.append(a)
        if tag == 'a':
            self.anchors.append(a)
        if tag == 'a' and 'preview-card' in a.get('class', '').split():
            self.previews += 1
        if tag == 'video':
            self.videos.append(a)
        if tag == 'article' and 'publication-card' in a.get('class', '').split():
            self.publications += 1
            self.publication_ids.append(a.get('id'))
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a.get('hreflang')] = a.get('href')
        for attr in ['href', 'src', 'poster']:
            if attr in a:
                self.links.append(a[attr])


root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []
pages = {}
for file in root.rglob('*.html'):
    text = file.read_text()
    pages[file] = Page(text)
    if re.search(r'\{[{%]|Hanlin|caihanlin|hc663|GuangLun|counter\.dev|lancecai|disqus', text, re.I):
        errors.append(f'{file.relative_to(root)}: unresolved template or old author content')

for file, page in pages.items():
    name = str(file.relative_to(root))
    redirect = name == 'cn/index.html'
    if not redirect and page.h1 != 1:
        errors.append(f'{name}: expected one h1, got {page.h1}')
    expected_lang = 'zh-CN' if name.startswith(('zh/', 'cn/')) else 'en'
    if page.lang != expected_lang:
        errors.append(f'{name}: language {page.lang!r} should be {expected_lang}')
    for id, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f'{name}: duplicate id {id}')
    for img in page.images:
        if not img.get('alt'):
            errors.append(f'{name}: missing image alt for {img.get("src")}')
    if page.videos:
        errors.append(f'{name}: local video player remains after YouTube migration')
    for iframe in page.iframes:
        if not iframe.get('src', '').startswith('https://www.youtube-nocookie.com/embed/') or not iframe.get('title') or iframe.get('loading') != 'lazy' or 'allowfullscreen' not in iframe or 'autoplay' in iframe.get('src', ''):
            errors.append(f'{name}: invalid YouTube embed or accessibility attributes')
    for anchor in page.anchors:
        destination = urlsplit(anchor.get('href', ''))
        if destination.scheme in ['http', 'https'] and destination.netloc != 'boliupro.github.io':
            relationship = set(anchor.get('rel', '').split())
            if anchor.get('target') != '_blank' or not {'noopener', 'noreferrer'}.issubset(relationship):
                errors.append(f'{name}: external link must open safely in a new tab: {anchor.get("href")}')
    if name not in ['404.html', 'cn/index.html'] and not {'en', 'zh-CN'}.issubset(page.alternates):
        errors.append(f'{name}: missing language alternates')
    for url in page.links:
        u = urlsplit(url)
        if u.scheme in ['mailto', 'tel', 'data']:
            continue
        if u.netloc and u.netloc != 'boliupro.github.io':
            continue
        path = unquote(u.path)
        if path.startswith('/'):
            target = root / path.lstrip('/')
        elif path:
            target = file.parent / path
        else:
            target = file
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.exists():
            errors.append(f'{name}: broken local resource {url}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{name}: missing anchor {url}')

for path in ['publications/index.html', 'zh/publications/index.html']:
    page = pages.get(root / path)
    if page is None or page.publications != 10:
        errors.append(f'{path}: must contain all 10 papers')
    elif page.publication_ids != ['motion', 'agentapp', 'llmapp', 'unimob', 'rag2-mp', 'cstnet', 'maede', 'moe-llm', 'hpdm', 'r2-transfer']:
        errors.append(f'{path}: publication order differs from the requested research sequence')

for prefix in ['', 'zh/']:
    for slug in ['motion', 'agentapp', 'maede']:
        if (root / prefix / 'projects' / slug).exists():
            errors.append(f'{prefix}projects/{slug}: removed paper-only project still published')
    homepage = pages.get(root / prefix / 'index.html')
    required_links = [
        'https://www.hnu.edu.cn/', 'https://csee.hnu.edu.cn/', 'https://nscc.hnu.edu.cn/',
        'https://csee.hnu.edu.cn/people/xiaozhu', 'https://tong89.github.io/tongli.github.io/',
        'mailto:liubo317@hnu.edu.cn', 'mailto:bobliu317@gmail.com',
        'https://www.youtube.com/channel/UC2O2Qyk9ewXtcT-T-8ghgEg',
    ]
    if homepage is None or not all(url in homepage.links for url in required_links):
        errors.append(f'{prefix}index.html: missing requested profile or advisor link')
    if homepage is None or homepage.previews != 41 or not all('preview-' + section in homepage.ids for section in ['publications', 'projects', 'awards', 'hobbies']):
        errors.append(f'{prefix}index.html: expected four preview rows with 10/6/20/5 items')
    publications = pages.get(root / prefix / 'publications/index.html')
    for link in ['https://anonymous.4open.science/r/MOTION-04C4', 'https://anonymous.4open.science/r/AgentApp-8202']:
        if publications is None or link not in publications.links:
            errors.append(f'{prefix}publications: missing anonymous repository {link}')
    for link in ['https://github.com/BoLiupro/UniMob', 'https://github.com/BoLiupro/RAG2-MP']:
        if publications is None or link not in publications.links:
            errors.append(f'{prefix}publications: missing requested repository {link}')
    demo_ids = {'ai-voice-assistant': 'L_CBSocY_cs', 'smart-walking-stick': 'bkAdHsDHf14', 'healthcare': 'saCQTR9whzI'}
    project_index = pages.get(root / prefix / 'projects/index.html')
    expected_embeds = ['https://www.youtube-nocookie.com/embed/' + value for value in demo_ids.values()]
    if project_index is None or [frame['src'] for frame in project_index.iframes] != expected_embeds:
        errors.append(f'{prefix}projects: demo gallery must contain the three supplied YouTube videos')
    for slug, video_id in demo_ids.items():
        detail = pages.get(root / prefix / 'projects' / slug / 'index.html')
        if detail is None or [frame['src'] for frame in detail.iframes] != ['https://www.youtube-nocookie.com/embed/' + video_id]:
            errors.append(f'{prefix}projects/{slug}: missing corresponding YouTube demo')
    for slug, repository in [('healthcare', 'HealthCare_V2'), ('c-v2x', 'C-V2X')]:
        detail = pages.get(root / prefix / 'projects' / slug / 'index.html')
        if detail is None or 'https://github.com/BoLiupro/' + repository not in detail.links:
            errors.append(f'{prefix}projects/{slug}: missing source code')
    if root / prefix / 'projects/positioning-error-analysis/index.html' not in pages:
        errors.append(f'{prefix}projects: missing positioning error analysis project')
    awards = pages.get(root / prefix / 'awards/index.html')
    if awards is None or len(awards.images) != 20:
        errors.append(f'{prefix}awards: expected evidence images for all 20 awards')
    hobbies = pages.get(root / prefix / 'hobbies/index.html')
    if hobbies is None or 'volunteering-title' not in hobbies.ids or len(hobbies.images) != 20:
        errors.append(f'{prefix}hobbies: missing volunteer section or gallery photos')

for file in root.rglob('*'):
    if file.is_file() and file.stat().st_size >= 100 * 1024 * 1024:
        errors.append(f'{file.relative_to(root)}: file exceeds 100 MiB')

for path in ['docs', 'scripts', 'LICENSE', 'README.md', 'CNAME', 'Gemfile']:
    if (root / path).exists():
        errors.append(f'Unexpected published development/template file: {path}')

try:
    sitemap = ET.parse(root / 'sitemap.xml')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [item.text for item in sitemap.findall('.//s:loc', ns)]
    if len(urls) != 24 or len(set(urls)) != 24:
        errors.append(f'Sitemap must contain 24 unique content pages; found {len(urls)}')
except (OSError, ET.ParseError) as exc:
    errors.append(f'Invalid sitemap: {exc}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; 24 sitemap routes; all local resources and anchors resolve.')
print('PASS: bilingual metadata, 10 papers per language, image descriptions, and lazy-loaded YouTube demos.')
print('PASS: requested paper order, profile links, 20 award evidence images, and volunteer galleries.')

print("PASS: four homepage preview rows, anonymous code links, YouTube channel, and project repositories.")
print('PASS: every external web link opens safely in a new tab; publication code buttons share one style.')
