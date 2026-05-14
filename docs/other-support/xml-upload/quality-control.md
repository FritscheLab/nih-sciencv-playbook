---
title: Quality control + validation checklist
parent: XML Upload & Automation
nav_order: 3
---

# Quality control + validation checklist

Use this checklist before uploading to SciENcv, and again before final certification by the named individual.

## 1) Content checks (policy-driven)

- **No personal information**: do not include home address, personal phone numbers, personal email, etc.
- Ensure each award or in-kind resource reflects **actual commitments and resources**.
- For *consulting*, confirm whether it meets the Common Form disclosure triggers and (if so) treat it as an `award` entry under proposals/active projects.
- For *in-kind contributions*, confirm the in-kind item meets the reporting threshold and includes a time commitment.

## 2) Structure checks (upload-driven)

- Root element is exactly `<profile>`.
- Exactly one `<funding>` block.
- Every `<support>` entry includes a non-empty `<contributiontype>` set to `award` or `inkind`.
- Dates are in `YYYY-MM-DD` (use day `01` if you only have month/year).
- Award amounts are digits only (no `$`, no commas).
- Each `<personmonth>` has a 4-digit `year` attribute.
- Person-month values may be blank for upload triage, but if effort is truly zero, use `0` and confirm the value in the SciENcv UI.

## 3) Post-upload checks (SciENcv UI)

After uploading:

- Open each entry in the SciENcv CPOS UI.
- Resolve any red exclamation icons for missing required fields.
- Confirm that effort and overlap text display as expected.

## Optional: run the lightweight validator in this repo

This repo includes a browser-based tool and a CLI script to catch common formatting issues:

- Browser tool: [Open the validator]({{ site.baseurl }}/tools/) and drag/drop your XML.
- CLI script:

```bash
python tools/validate_cpos_xml.py path/to/your_cpos.xml
```

Both checks cover:
- XML well-formedness
- missing/invalid `<contributiontype>`
- date formats
- award amount formatting
- person-month years and numeric values

It does not perform full XSD validation (SciENcv is the source of truth).

```mermaid
flowchart TD
    accTitle: CPOS XML quality control stages
    accDescr: XML quality control has policy-driven content checks, upload-driven structure checks, and post-upload SciENcv UI checks.
    A["Source material"] --> B["Content checks"]
    B --> C{"Reportable and appropriate?"}
    C -- "No" --> D["Revise or remove item"]
    C -- "Yes" --> E["Structure checks"]
    D --> B
    E --> F{"Upload-ready XML?"}
    F -- "No" --> G["Fix XML or run validator"]
    F -- "Yes" --> H["Upload to SciENcv"]
    G --> E
    H --> I["Post-upload UI checks"]
    I --> J["Certification-ready CPOS"]
```
