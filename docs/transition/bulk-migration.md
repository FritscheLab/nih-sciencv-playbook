---
title: Portfolio readiness (active awards + submissions)
parent: Department workflows
nav_order: 2
---

# Portfolio readiness (active awards + submissions)

Use a portfolio-level workflow to keep likely participants ready for upcoming applications, JIT requests, RPPRs, and Prior Approval submissions. Do not assume that every person or submission needs both forms; identify the required people and documents from the NOFO and applicable submission-stage instructions.

Tips:

- Start with the most active labs and frequent NIH submitters
- Prioritize people with near-term NIH submissions or reporting needs
- Keep reusable narratives, product lists, and support records current
- Standardize how you name SciENcv documents (`PI_LASTNAME_MECH_YYYYMMDD`)
- Track the named individual's review and certification separately for each required form

```mermaid
flowchart TD
    accTitle: Portfolio readiness triage
    accDescr: Portfolio readiness prioritizes near-term NIH submissions and active labs, then maintains reusable content and tracks required certification.
    A["Department portfolio"] --> B{"Near-term NIH submission or reporting need?"}
    B -- "Yes" --> C["Prioritize lab for preparation"]
    B -- "No" --> D{"Frequent NIH submitter?"}
    D -- "Yes" --> C
    D -- "No" --> E["Maintain routine readiness"]
    C --> F["Identify required people and forms"]
    F --> I["Update reusable narratives, products, and support records"]
    I --> G["Prepare applicable SciENcv Common Forms"]
    G --> H["Track certification status"]
```
