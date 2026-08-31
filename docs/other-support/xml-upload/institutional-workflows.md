---
title: Institutional workflow patterns
parent: XML Upload & Automation
nav_order: 6
---

# Institutional workflow patterns

This page outlines practical ways departments and central offices are using XML upload to scale CPOS compliance.

## Pattern A: Admin-owned data, PI-owned certification (recommended)

1. Admin maintains a structured CPOS inventory (spreadsheet, database, ...)
2. Admin exports/upload-prep XML for each PI (one file per individual)
3. PI uploads XML into SciENcv CPOS document
4. PI reviews, completes missing fields, and certifies
5. Admin collects the SciENcv-generated certified PDF for submission packaging

## Pattern B: Hybrid drafting (admin seeds, PI edits)

- Admin uploads baseline XML (projects, dates, sources)
- PI adds narrative fields (objectives, overlap) and final effort estimates

## Pattern C: System integration

Some institutions generate SciENcv-ready CPOS XML directly from internal research administration systems (e.g., effort reporting, award management, disclosure tooling). If you do this:

- Use a **composite identifier** for de-duplication and updates; never merge on `awardnumber` alone because consortium subprojects and multi-project components may share an overall award number. Flag collisions for human review.
- Generate person-month rows deterministically (inclusive year range).
- Build a validation step (see validator script in this repo) before handing files to PIs.

## Governance tips

- Maintain a clear cutoff date for when updates are accepted before submission.
- Use an intake form for items that are hard to infer (consulting, in-kind, foreign appointments).
- Keep a copy of the exact XML uploaded, and the final certified PDF that was submitted.

```mermaid
swimlane-beta TB
    accTitle: Admin-owned data and PI-owned certification
    accDescr: The admin or institutional system prepares and validates a per-person XML file, the named individual uploads and reviews it in SciENcv and certifies the CPOS, and the admin collects and archives the final materials.

    subgraph admin [Admin or institutional system]
        inventory["Maintain structured CPOS inventory"]
        export["Create per-person XML export"]
        validate["Validate XML"]
        collect["Collect certified PDF for submission packaging"]
        archive["Archive XML and submitted PDF"]
    end

    subgraph person [Named individual]
        upload["Upload XML to SciENcv CPOS"]
        review["Review and complete entries"]
        certify["Certify CPOS"]
    end

    inventory --> export --> validate
    validate -->|Per-person XML| upload
    upload --> review --> certify
    certify -->|Certified PDF| collect --> archive
```
