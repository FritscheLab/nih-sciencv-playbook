---
title: Transition from the old NIH biosketch
parent: NIH Biosketch (Common Form + Supplement)
nav_order: 7
---

# Transition from the old NIH biosketch

## If you previously used Word

- No automatic import from Word
- Move data upstream:
  - ORCID (education/positions)
  - My Bibliography (citations/products)
- Copy narratives into SciENcv and replace old reference lists or citation markers with brief parenthetical references to selected products, when useful

## If you previously used SciENcv (old format)

- Create a new Common Form document
- You may copy from an older document, but:
  - Select up to 5 closely related products and up to 5 other significant products
  - Replace full bibliographic citations and hyperlinked references in the narratives with brief parenthetical references to selected products (lead author/year or PMID/PMCID)

```mermaid
flowchart TD
    accTitle: Old biosketch transition path
    accDescr: Legacy Word and older SciENcv biosketch content moves into upstream data sources and the new Common Form document.
    A{"Old biosketch source"} -- "Word template" --> B["Move education and positions to ORCID or manual entry"]
    A -- "Old SciENcv format" --> C["Copy from existing SciENcv document"]
    B --> D["Move citations and products to My Bibliography"]
    C --> D
    D --> E["Create new NIH Biosketch Common Form"]
    E --> F["Select up to 10 products<br/>up to 5 per bucket"]
    F --> G["Use brief parenthetical references<br/>no full citations or hyperlinks"]
```
