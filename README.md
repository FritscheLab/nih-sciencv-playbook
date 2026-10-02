# NIH Common Forms (SciENcv) Playbook (2026)

A docs-first, GitHub Pages–ready site to help **PIs, Co-Is, staff, and research administrators** complete NIH’s **Common Forms** requirements in **SciENcv**:

- **Biographical Sketch Common Form + NIH Biographical Sketch Supplement**
- **Current and Pending (Other) Support (CPOS) Common Form**

> **Compliance note:** NIH requires *digitally certified* PDFs generated from SciENcv. Keep each Common Form unmodified unless the Application Guide or NOFO expressly requires a special compiled/flattened attachment; foreign contracts and annual MFTRP statements are separate attachments.

> **September 2026 operational alert:** Institutional notices advise re-certifying affected older SciENcv PDFs and replacing submission attachments. See the [signing-certificate alert and steps](docs/troubleshooting/september-2026-certificates.md) for the dates, sources, and validation checks.

## Publish on GitHub Pages (recommended)

1. Create a new GitHub repo and upload the contents of this ZIP.
2. In GitHub: **Settings → Pages**
3. **Source:** Deploy from a branch  
   **Branch:** `main` (or your default branch)  
   **Folder:** `/docs`
4. Save. Your site will build automatically.

The site uses the **Just the Docs** Jekyll theme (remote theme), which is easy to host on GitHub Pages and includes built-in search.

Mermaid diagrams are enabled through the Just the Docs `mermaid` configuration in `docs/_config.yml`, using a pinned Mermaid release loaded by the theme.

## Local preview (optional)

Use Ruby 3.3 and Bundler. On macOS with Homebrew, install Ruby and put it on the current shell's path:

```bash
brew install ruby@3.3
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
```

From the repository root, install the locked dependencies into the ignored local vendor directory, then start the preview:

```bash
cd docs
bundle config set --local path ../.vendor/bundle
bundle install
bundle exec jekyll serve
```

For a build without a preview server, use `bundle exec jekyll build --destination /tmp/nih-sciencv-playbook-site` from `docs/`.

## Mermaid visual QA

The [browser capture tool](tools/mermaid-qa/README.md) uses the site's pinned Mermaid version and the built Jekyll pages. It captures every diagram at desktop and mobile widths and records rendering errors, displayed label sizes, and SVG accessibility metadata. Install its dependencies with `npm ci --prefix tools/mermaid-qa`; it requires Node.js 22.12 or newer and an installed Chrome or Chromium browser.

Inspect the captured images to assess overlap, connector routing, contrast, and readability. A successful render alone does not establish a visual pass.

## Maintainers

- Update content in `docs/` (Markdown).
- Add new links to `docs/references.md`.
- Track important changes in `docs/changelog.md`.
- If you update `tools/index.html`, run `tools/sync_docs_tools.sh` to publish it to `docs/tools/index.html` for GitHub Pages.

## Source material

This site is reorganized and expanded from a long-form internal guide:
- See **Appendix → Long-form guide (current reference)**.
