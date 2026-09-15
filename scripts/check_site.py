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
        self.h1 = 0
        self.images = []
        self.lang = None
        self.alternates = {}
        self.videos = []
        self.publications = 0
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
        if tag == 'video':
            self.videos.append(a)
        if tag == 'article' and 'publication-card' in a.get('class', '').split():
            self.publications += 1
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
    for video in page.videos:
        if 'controls' not in video or video.get('preload') != 'none' or 'autoplay' in video:
            errors.append(f'{name}: video must have controls, load on demand, and not autoplay')
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
    if len(urls) != 28 or len(set(urls)) != 28:
        errors.append(f'Sitemap must contain 28 unique content pages; found {len(urls)}')
except (OSError, ET.ParseError) as exc:
    errors.append(f'Invalid sitemap: {exc}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; 28 sitemap routes; all local resources and anchors resolve.')
print('PASS: bilingual metadata, 10 papers per language, image descriptions, and on-demand videos.')
