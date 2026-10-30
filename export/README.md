# Export the guide as PDF

The Markdown chapters remain the source of truth. This folder supplies a reusable LaTeX layout and a build that renders every Mermaid figure, rewrites chapter links into PDF links and produces a complete book.

## Build on GitHub

Open the repository's **Actions** tab, choose **Export guide PDF**, and run the workflow on the intended branch. After a successful run, download either artifact:

- **home-technology-guide-pdf** contains the finished PDF.
- **home-technology-guide-latex** contains the generated guide.tex, metadata and vector figure PDFs for further editing or compilation.

The workflow also runs when chapters, export files or the workflow itself change on main or in a pull request. It does not publish the guide or change repository visibility. Artifact access follows repository permissions, and downloads expire after the configured retention period.

## Build locally

Requirements: Python 3.10 or later, Node.js 22 or later, Pandoc 3.1.3 or later, XeLaTeX with the packages used in template.tex, and Latin Modern and DejaVu fonts. No Python packages are required.

On Ubuntu 24.04, the workflow's apt package list provides the document dependencies. On macOS, install equivalent tools through your normal package manager or TeX distribution. These are build dependencies, not household service requirements.

From the repository root:

```bash
npm ci --prefix export
cd export
npx puppeteer browsers install chrome-headless-shell
cd ..
python3 export/build.py
```

Alternatively set PUPPETEER_EXECUTABLE_PATH to an installed compatible Chrome executable. The GitHub workflow uses the runner's installed Chrome. Browser installation can require additional platform libraries; follow Puppeteer's current instructions if startup reports a missing library.

The renderer uses a dedicated headless browser process to render repository diagrams. The included Puppeteer settings disable its sandbox for CI compatibility; they do not modify your everyday browser. Run builds only from source you trust.

Output: **build/pdf/home-technology-guide.pdf**. Intermediate Markdown, figure sources, generated LaTeX, figure PDFs and logs are also kept in build/pdf. They are ignored by Git.

## Customize the document

| File | Purpose |
| --- | --- |
| guide.json | Title, subtitle, edition, date, chapter order and part divisions |
| template.tex | A4 layout, cover, typography, chapter hierarchy, tables, headers and contents |
| mermaid.json | Shared print style for diagrams |
| puppeteer.json | Headless browser launch options |
| build.py | Navigation cleanup, internal links, figure conversion and compilation |
| package.json and package-lock.json | Pinned renderer and resolved dependencies |

Change the date in guide.json intentionally for a new edition. The manifest lists every included chapter explicitly; a new Markdown file is not automatically added to the book. Keep its order aligned with the README.

The template uses a restrained serif body, sans-serif headings, numbered chapters, running page numbers, a contents page, a list of figures and clickable links. Code wraps and tables can continue across pages. Mermaid diagrams become vector PDF figures rather than screenshots.

## Validation and caching

```bash
python3 export/build.py --prepare-only
python3 export/build.py --skip-diagrams
```

The first command validates the manifest and internal PDF links and prepares intermediate Markdown without running LaTeX or the browser. It requires the committed dependency lockfile to compute figure cache keys. The second reuses rendered figures and fails if a required cached figure is absent.

The normal build caches figures by their source, renderer lockfile and shared diagram configuration. Delete build/pdf to force a complete rebuild. The PDF is compiled three times to resolve the contents, figure list and cross references. Missing glyphs and unresolved references cause a failed build.

Visual review is still necessary after layout or content changes. Inspect dense tables, long URLs, code, and both tall and wide figures. A successful LaTeX build alone does not prove that every page is well laid out.

## Editable LaTeX and other editors

The generated guide.tex embeds the template and converted chapter text. Keep the figures subdirectory beside it and compile it with XeLaTeX, normally three passes for cross references. It can be imported as a LaTeX project with its figure files; it is not a linked Markdown editor.

Prefer editing the Markdown and rebuilding for normal updates. Edits made only to generated guide.tex will be replaced by the next build.

This export is documentation only. It does not deploy web applications, change DNS or apply Home Assistant configuration.
