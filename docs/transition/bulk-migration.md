---
title: Bulk migration (active awards + RPPR)
parent: Transition & implementation
nav_order: 2
---

# Bulk migration (active awards + RPPR)

Even if an award started under the old biosketch format, RPPR/JIT submissions on/after Jan 25, 2026 will require Common Forms. Plan a department-wide conversion effort.

Tips:
- Start with the most active labs and frequent NIH submitters
- Create reusable narrative templates
- Standardize how you name SciENcv documents (PI_LASTNAME_MECH_YYYYMMDD)

```mermaid
flowchart TD
    accTitle: Bulk migration triage
    accDescr: Bulk migration prioritizes active NIH labs and near-term RPPR or JIT needs, then standardizes templates and document naming.
    A["Department portfolio"] --> B{"Near-term NIH JIT or RPPR?"}
    B -- "Yes" --> C["Prioritize lab for conversion"]
    B -- "No" --> D{"Frequent NIH submitter?"}
    D -- "Yes" --> C
    D -- "No" --> E["Schedule later cohort"]
    C --> F["Prepare reusable narratives and products"]
    F --> G["Create SciENcv Common Forms"]
    G --> H["Track certification status"]
```
