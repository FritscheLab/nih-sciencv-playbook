# NIH Common Forms (SciENcv) Playbook (2026)

A docs-first, GitHub Pages–ready site to help **PIs, Co-Is, staff, and research administrators** complete NIH’s **Common Forms** requirements in **SciENcv**:

- **Biographical Sketch Common Form + NIH Biographical Sketch Supplement**
- **Current and Pending (Other) Support (CPOS) Common Form**

Read the [published playbook](https://fritschelab.github.io/nih-sciencv-playbook/) or the [v1.10 release notes](docs/changelog.md#v110-october-2-2026).

> **Compliance note:** NIH requires *digitally certified* PDFs generated from SciENcv. Keep each Common Form unmodified unless the Application Guide or NOFO expressly requires a special compiled/flattened attachment; foreign contracts and annual MFTRP statements are separate attachments.

> **September 2026 operational alert:** Institutional notices advise re-certifying affected older SciENcv PDFs and replacing submission attachments. See the [signing-certificate alert and steps](docs/troubleshooting/september-2026-certificates.md) for the dates, sources, and validation checks.

## Publish on GitHub Pages (recommended)

The existing repository is configured for `https://fritschelab.github.io/nih-sciencv-playbook/` in `docs/_config.yml`.

1. Complete the publication checks below and commit the release changes.
2. In the repository's **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/docs**, and save if needed.
3. Push the reviewed commits to `main`. Check the **Pages build and deployment** run in **Actions**, then verify the published home page, release notes, diagrams, and XML validator.

GitHub documents this [branch-based publishing setup](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). For a fork or custom domain, update `url`, `baseurl`, the footer link, and `gh_edit_repository` in `docs/_config.yml` before publishing.

The site uses the **Just the Docs** Jekyll theme (remote theme), which is easy to host on GitHub Pages and includes built-in search.

Mermaid diagrams use the pinned release in `docs/_config.yml`. The local theme-component override supplies readable scrolling and SVG accessibility metadata after rendering.

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

## Publication checks

Run from the repository root after setting up the local dependencies:

```bash
git diff --check
python3 -m unittest discover -s tests -p 'test_validate_cpos_xml.py'
cmp tools/index.html docs/tools/index.html
(cd docs && bundle exec jekyll build --destination /tmp/nih-sciencv-playbook-site)
```

After diagram or rendering changes, also run the Mermaid visual QA below. Keep `Unreleased` as a placeholder and move completed changes into a dated release entry in `docs/changelog.md`. Review the source gaps and conflicts in `docs/references.md` before changing policy guidance.

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
