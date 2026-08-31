---
title: XML Upload & Automation
parent: Current & Pending (Other) Support (CPOS)
nav_order: 7
has_children: true
---

# XML Upload & Automation

SciENcv includes **Data Ingest (XML file upload)** for the **Current and Pending (Other) Support (CPOS) Common Form**. This capability is especially useful when a grants office wants to pre-populate a PI’s CPOS entries from:

- A prior Other Support Word/PDF
- A campus system (e.g., internal grants database)
- Prior SciENcv exports
- Admin-collected intake notes

**Important:** XML upload is a *data-entry accelerator*, not a submission bypass. NIH still requires a **SciENcv-generated, digitally certified PDF**, and certification is done by the individual (not a delegate).

**Diagram summary:** Source-data preparation can be automated outside SciENcv; upload, UI review, individual certification, and PDF generation remain inside SciENcv.

```mermaid
block-beta
    columns 2
    block:preparation
        columns 1
        prepHeading["Outside SciENcv<br/>Preparation may be automated"]
        sources["Prior records, campus systems,<br/>and admin intake notes"]
        xml["CPOS XML upload file"]
    end
    block:required
        columns 1
        requiredHeading["Inside SciENcv<br/>Required workflow"]
        ingest["Data Ingest upload"]
        review["Review and complete entries"]
        certification["Named individual certifies"]
        pdf["SciENcv-generated PDF"]
    end
    sources --> xml
    xml --> ingest
    ingest --> review
    review --> certification
    certification --> pdf
```
