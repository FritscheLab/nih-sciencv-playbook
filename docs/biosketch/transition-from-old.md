---
title: Reuse prior biosketch content
parent: NIH Biosketch (Common Form + Supplement)
nav_order: 7
---

# Reuse prior biosketch content

Use prior material as a drafting source, then rebuild and certify the current combined biosketch in SciENcv.

## Starting from a Word document

- No automatic import from Word
- Move data upstream:
  - ORCID (education/positions)
  - My Bibliography (citations/products)
- Copy narratives into SciENcv and replace old reference lists or citation markers with brief parenthetical references to selected products, when useful

## Starting from an earlier SciENcv document

- Create a current combined NIH biosketch document
- You may copy from an earlier document, but:
  - Select up to 5 closely related products and up to 5 other significant products
  - Replace full bibliographic citations and hyperlinked references in the narratives with brief parenthetical references to selected products (lead author/year or PMID/PMCID)

```mermaid
flowchart TD
    accTitle: Reuse prior biosketch content
    accDescr: Content from a Word document or earlier SciENcv biosketch can seed the current combined biosketch while structured data moves to its reusable sources.
    A{"Prior biosketch source"} -- "Word document" --> B["Move education and positions to ORCID or manual entry"]
    A -- "Earlier SciENcv document" --> C["Copy from existing SciENcv document"]
    B --> D["Move citations and products to My Bibliography"]
    C --> D
    D --> E["Create current combined NIH biosketch"]
    E --> F["Select up to 10 products<br/>up to 5 per bucket"]
    F --> G["Use brief parenthetical references<br/>no full citations or hyperlinks"]
```
