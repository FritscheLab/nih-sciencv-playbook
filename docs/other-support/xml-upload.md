---
title: XML Upload & Automation
parent: Current & Pending (Other) Support (CPOS)
nav_order: 7
has_children: true
---

# XML Upload & Automation

SciENcv includes **Data Ingest (XML file upload)** for the **Current and Pending (Other) Support (CPOS) Common Form**. This capability is especially useful when a grants office wants to pre-populate a PI’s CPOS entries from:

- A legacy “Other Support” Word/PDF
- A campus system (e.g., internal grants database)
- Prior SciENcv exports
- Admin-collected intake notes

**Important:** XML upload is a *data-entry accelerator*, not a submission bypass. NIH still requires a **SciENcv-generated, digitally certified PDF**, and certification is done by the individual (not a delegate).

```mermaid
flowchart LR
    accTitle: XML upload automation boundary
    accDescr: XML upload can pre-populate CPOS data from multiple sources, but SciENcv review and individual certification remain required.
    A["Legacy Other Support"] --> D["CPOS XML upload file"]
    B["Campus system"] --> D
    C["Admin intake notes"] --> D
    D --> E["Upload to SciENcv"]
    E --> F["Review and complete entries in UI"]
    F --> G["Named individual certifies"]
    G --> H["SciENcv-generated PDF"]
```
