#!/usr/bin/env python3
"""Build the guide from Markdown with Pandoc, XeLaTeX and Mermaid CLI.

Only Python's standard library is required. All subprocesses use argument arrays;
no source text is executed as shell code. Generated files stay in build/pdf/.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / 'export'
OUT = ROOT / 'build' / 'pdf'
FIGURES = OUT / 'figures'


def run(args, **kwargs):
    print('+', ' '.join(map(str, args)), flush=True)
    subprocess.run(list(map(str, args)), check=True, **kwargs)


def slug(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def chapter_id(path):
    return 'ch-' + slug(Path(path).stem)


def read_config():
    config = json.loads((EXPORT / 'guide.json').read_text())
    paths = [c['path'] for c in config['chapters']]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate chapter in manifest')
    for path in paths:
        source = (ROOT / path).resolve()
        if not source.is_relative_to(ROOT) or not source.is_file():
            raise ValueError('Missing or unsafe chapter path: ' + path)
    return config


def source_body(path):
    text = (ROOT / path).read_text()
    # Site navigation is useful in GitHub but redundant in a book.
    text = re.sub(r'^.*\[Guide contents\].*\n?', '', text, flags=re.M)
    text = re.sub(r'\n---\s*\Z', '', text)
    return text.strip() + '\n'


def add_heading_ids(text, path):
    counts = {}
    def heading(m):
        level, title = m.group(1), m.group(2)
        key = chapter_id(path) if len(level) == 1 else chapter_id(path) + '--' + slug(title)
        n = counts.get(key, 0)
        counts[key] = n + 1
        if n:
            key += '-' + str(n)
        return level + ' ' + title + ' {#' + key + '}'
    # Work outside fenced code only.
    pieces = re.split(r'(^```[^\n]*\n[\s\S]*?^```\s*$)', text, flags=re.M)
    return ''.join(p if p.startswith('```') else re.sub(r'^(#{1,6}) (.+)$', heading, p, flags=re.M) for p in pieces)


def resolve_links(text, path, included):
    def replace(m):
        label, url = m.group(1), m.group(2)
        if re.match(r'^(?:https?:|mailto:)', url):
            return m.group(0)
        if url.startswith('#'):
            return '[' + label + '](#' + chapter_id(path) + '--' + url[1:] + ')'
        target, _, anchor = url.partition('#')
        dest = ((ROOT / path).parent / target).resolve()
        if dest == ROOT / 'README.md':
            return '[' + label + '](#guide-contents)'
        rel = dest.relative_to(ROOT).as_posix()
        if rel not in included:
            raise ValueError(f'PDF link target is not in the manifest: {path}: {url}')
        ident = chapter_id(rel) + ('--' + anchor if anchor else '')
        return '[' + label + '](#' + ident + ')'
    # The guide's links do not contain nested parentheses.
    pieces = re.split(r'(^```[^\n]*\n[\s\S]*?^```\s*$)', text, flags=re.M)
    return ''.join(p if p.startswith('```') else re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', replace, p) for p in pieces)


def extract_figures(text, path, next_index):
    figures = []
    pattern = r'(?:\*\*Figure\s*[—-]\s*([^\n]+?)\*\*\s*\n\n)?```mermaid\s*\n([\s\S]*?)\n```'
    def replace(m):
        index = next_index + len(figures)
        before = text[:m.start()]
        headings = re.findall(r'^#{1,6} (.+?)(?: \{#[^}]+\})?$', before, re.M)
        title = m.group(1) or (headings[-1] if headings else Path(path).stem.replace('-', ' '))
        code = m.group(2).strip() + '\n'
        config = (EXPORT / 'mermaid.json').read_bytes()
        digest = hashlib.sha256(code.encode() + config + (EXPORT / 'package-lock.json').read_bytes()).hexdigest()[:12]
        stem = f'figure-{index:02d}-{digest}'
        figures.append({'index': index, 'title': title, 'code': code, 'stem': stem, 'chapter': path})
        return f'![{title}](figures/{stem}.pdf){{#fig-{index}}}\n'
    return re.sub(pattern, replace, text), figures


def prepare(config):
    OUT.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    included = {c['path'] for c in config['chapters']}
    chapters, figures = [], []
    for item in config['chapters']:
        path = item['path']
        text = add_heading_ids(source_body(path), path)
        text = resolve_links(text, path, included)
        text, found = extract_figures(text, path, len(figures) + 1)
        # Keep a diagram section together and place the figure next to its prose.
        text = re.sub(r'(?m)^(## .+\n)\n(?=!\[)', r'\\clearpage\n\n\1', text)
        figures += found
        # Turn bare reference URLs into clickable links and normalize unusual dashes.
        text = re.sub(r'^(https?://\S+)[ \t]*$', r'<\1>', text, flags=re.M)
        if path == 'docs/references.md':
            text = re.sub(r'^\[(\d+)\] (.+)$', r'\n**\1 \2**\n', text, flags=re.M)
            text = re.sub(r'^<(https?://[^>]+)>$', r'- <\1>', text, flags=re.M)
        text = text.replace('\u2011', '-').replace('\u2013', '--')
        if item.get('part'):
            # Part names are plain author-controlled text, not arbitrary LaTeX.
            part = item['part']
            if not re.fullmatch(r'[A-Za-z0-9 ]+', part):
                raise ValueError('Part name must contain letters numbers and spaces only')
            chapters.append('\\part{' + part + '}\n')
        chapters.append(text)
    body = '\n\n'.join(chapters)
    anchors = set(re.findall(r'\{#([^}]+)\}', body)) | {'guide-contents'}
    for link in re.findall(r'\]\(#([^)]+)\)', body):
        if link not in anchors:
            raise ValueError('Unresolved PDF anchor: ' + link)
    (OUT / 'guide.md').write_text(body)
    (OUT / 'metadata.json').write_text(json.dumps({k: v for k, v in config.items() if k != 'chapters'}, indent=2))
    (OUT / 'figures.json').write_text(json.dumps(figures, indent=2))
    for fig in figures:
        (FIGURES / (fig['stem'] + '.mmd')).write_text(fig['code'])
    print(f'Prepared {len(chapters) - sum(bool(c.get("part")) for c in config["chapters"])} chapters and {len(figures)} figures; internal links checked.', flush=True)
    return figures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only', action='store_true', help='Prepare and validate Markdown without rendering')
    parser.add_argument('--skip-diagrams', action='store_true', help='Use already rendered figure PDFs; fail if missing')
    args = parser.parse_args()
    config = read_config()
    figures = prepare(config)
    if args.prepare_only:
        return
    for binary in ['pandoc', 'xelatex']:
        if not shutil.which(binary):
            raise SystemExit(f'Missing {binary}; see export/README.md')
    mmdc = EXPORT / 'node_modules' / '.bin' / ('mmdc.cmd' if os.name == 'nt' else 'mmdc')
    if not args.skip_diagrams and not mmdc.exists():
        raise SystemExit('Missing Mermaid CLI; run npm ci --prefix export')
    for fig in figures:
        pdf = FIGURES / (fig['stem'] + '.pdf')
        if pdf.exists() and pdf.stat().st_size:
            continue
        if args.skip_diagrams:
            raise SystemExit('Missing cached figure: ' + str(pdf))
        run([mmdc, '-i', FIGURES / (fig['stem'] + '.mmd'), '-o', pdf,
             '-b', 'white', '-c', EXPORT / 'mermaid.json',
             '-p', EXPORT / 'puppeteer.json'])
    run(['pandoc', 'guide.md', '--from=markdown+raw_tex+implicit_figures',
         '--metadata-file=metadata.json', '--template=' + str(EXPORT / 'template.tex'),
         '--top-level-division=chapter', '--number-sections', '--highlight-style=tango',
         '--resource-path=.', '--output=guide.tex'], cwd=OUT)
    # Explicit repeated passes resolve chapter links, contents and the figure list.
    for _ in range(3):
        try:
            run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'guide.tex'], cwd=OUT, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            log_path = OUT / 'guide.log'
            if log_path.exists():
                print('\n'.join(log_path.read_text(errors='replace').splitlines()[-45:]), file=sys.stderr)
            raise
    (OUT / 'guide.pdf').replace(OUT / 'home-technology-guide.pdf')
    log = (OUT / 'guide.log').read_text(errors='replace')
    serious = [line for line in log.splitlines() if 'Missing character:' in line or 'undefined references' in line]
    if serious:
        raise SystemExit('PDF requires review:\n' + '\n'.join(serious))
    print('Built ' + str(OUT / 'home-technology-guide.pdf'))


if __name__ == '__main__':
    main()
