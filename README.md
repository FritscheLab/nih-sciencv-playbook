# NIH Common Forms (SciENcv) Playbook (2026)

A docs-first, GitHub Pages–ready site to help **PIs, Co-Is, staff, and research administrators** complete NIH’s **Common Forms** requirements in **SciENcv**:

- **Biographical Sketch Common Form + NIH Biographical Sketch Supplement**
- **Current and Pending (Other) Support (CPOS) Common Form**

> **Compliance note:** NIH requires *digitally certified* PDFs generated from SciENcv. Do **not** “Print to PDF” / flatten the SciENcv output.

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

If you want to preview locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

## Maintainers

- Update content in `docs/` (Markdown).
- Add new links to `docs/references.md`.
- Track important changes in `docs/changelog.md`.
- If you update `tools/index.html`, run `tools/sync_docs_tools.sh` to publish it to `docs/tools/index.html` for GitHub Pages.

## Source material

This site is reorganized and expanded from a long-form internal guide:
- See **Appendix → Long-form guide (current reference)**.
