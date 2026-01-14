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

## Source material

This site is reorganized and expanded from a long-form internal guide:
- See **Appendix → Original long-form guide**.

