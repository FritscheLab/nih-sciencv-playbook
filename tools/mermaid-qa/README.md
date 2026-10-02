# Mermaid browser captures

This tool inventories Mermaid fences in `docs/`, opens the built pages in Chrome, and captures every diagram and its page at 1440 and 390 CSS pixels. It preserves the theme's wrappers, CSS, and initialization. Mermaid's CDN module requests are served from the installed, version-matched npm package.

Install Ruby/Jekyll dependencies using the repository README. Install Node.js 22.12 or newer and Chrome or Chromium if needed. Then run these commands from the repository root:

```bash
npm ci --prefix tools/mermaid-qa
```

Build the site from `docs/`:

```bash
bundle exec jekyll build --destination /tmp/nih-sciencv-playbook-site
```

Return to the repository root and capture the pages. On macOS:

```bash
node tools/mermaid-qa/capture.mjs \
  --site /tmp/nih-sciencv-playbook-site \
  --output /tmp/nih-mermaid-qa \
  --browser "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

On other systems, pass the full path to the installed Chrome or Chromium executable. The tool uses `puppeteer-core`, which does not install a browser.

Open the PNGs in the output's `screenshots/` directory. Each diagram has a screenshot of its scroll area at the page width and a `-full.png` capture of the complete SVG. The latter temporarily removes the scroll area's clipping for the screenshot; use the page/scroll-area images to assess integration. `inventory.json` records each source path, line, ordinal, type, and Mermaid source. `results.json` records browser/runtime versions, page and diagram widths, effective label sizes, scroll cues and keyboard focusability, SVG titles/descriptions and their ARIA associations, and errors. SVG copies are saved beside the screenshots. Output stays outside the published site.

The command exits unsuccessfully if a diagram is missing, Mermaid reports a runtime error, or the installed engine differs from `docs/_config.yml`. It does not grade visual quality. Inspect all diagram images for clipping, overlapping labels, routing, contrast, reading order, and mobile readability; use full-page images to assess integration. Font-size measurements are diagnostic observations, not a WCAG conformance test. Assistive-technology behavior needs separate testing.

If the site's Mermaid pin changes, update `package.json` and its lockfile together. Rebuild the site after source or CSS changes before taking new captures. The current path mapping follows Jekyll's default `.md` to `.html` route; custom permalinks would need corresponding changes in the capture tool.

The site overrides the theme's Mermaid component in `docs/_includes/components/mermaid.html`. It waits for rendering, then adds readable sizing, scroll cues, and SVG metadata through `docs/assets/js/mermaid-diagrams.js`. For block and mindmap diagrams in Mermaid 11.17.2, author metadata as `%% accTitle: ...` and `%% accDescr: ...` comments inside the fence; their grammar rejects the plain directives. Other types retain normal directives, with the integration supplying any metadata omitted by the renderer.
