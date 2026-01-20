---
title: Overview (what XML upload is)
parent: XML Upload & Automation
nav_order: 1
---

# Overview (what XML upload is)

SciENcv supports **Data Ingest (XML file upload)** to help users pre-populate CPOS entries in the SciENcv interface.

{: .warning }
> XML upload is a data-entry accelerator, not a submission bypass. NIH still requires a **SciENcv-generated, digitally certified PDF**, and the individual (not a delegate) must certify.

## Two upload rules that commonly break files

- `<contributiontype>` must be present and non-empty. Use `award` for proposals/active projects and `inkind` for in-kind contributions.
- In `<commitment>`, each `<personmonth>` must include a `year="YYYY"` attribute even if the value is blank.

Next:
- [AI-assisted CPOS XML generator prompt]({{ site.baseurl }}{% link other-support/xml-upload/ai-prompt.md %})
- [Quality control + validation checklist]({{ site.baseurl }}{% link other-support/xml-upload/quality-control.md %})
