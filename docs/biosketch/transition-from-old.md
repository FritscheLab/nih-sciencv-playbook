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
- Copy narratives into SciENcv and remove inline citations

## If you previously used SciENcv (old format)

- Create a new Common Form document
- You may copy from an older document, but:
  - Reduce citations to the new 10-product limit
  - Remove citation markers in Personal Statement and Contributions

```mermaid
flowchart TD
    accTitle: Old biosketch transition path
    accDescr: Legacy Word and older SciENcv biosketch content moves into upstream data sources and the new Common Form document.
    A{"Old biosketch source"} -- "Word template" --> B["Move education and positions to ORCID or manual entry"]
    A -- "Old SciENcv format" --> C["Copy from existing SciENcv document"]
    B --> D["Move citations and products to My Bibliography"]
    C --> D
    D --> E["Create new NIH Biosketch Common Form"]
    E --> F["Apply 10-product limit"]
    F --> G["Remove formal citation markers from narratives"]
```
