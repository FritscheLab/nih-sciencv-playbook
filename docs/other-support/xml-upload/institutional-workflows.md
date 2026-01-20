---
title: Institutional workflow patterns
parent: XML Upload & Automation
nav_order: 5
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

- Treat **awardnumber** as the primary identifier for de-duplication and updates.
- Generate person-month rows deterministically (inclusive year range).
- Build a validation step (see validator script in this repo) before handing files to PIs.

## Governance tips

- Maintain a clear cutoff date for when updates are accepted before submission.
- Use an intake form for items that are hard to infer (consulting, in-kind, foreign appointments).
- Keep a copy of the exact XML uploaded, and the final certified PDF that was submitted.
