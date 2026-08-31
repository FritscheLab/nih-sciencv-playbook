---
title: Reusing prior support records
parent: Current & Pending (Other) Support (CPOS)
nav_order: 6
---

# Reusing prior support records

Prior Other Support documents, spreadsheets, and institutional disclosure records can help populate a CPOS, but they are source material rather than submission-ready forms.

When NIH requests CPOS for the person's role and submission stage:

1. Compare prior records with the current CPOS disclosure categories and instructions.
2. Reconcile projects, in-kind contributions, effort, dates, amounts, and required supporting documentation.
3. Create or update the CPOS in SciENcv and resolve any missing fields.
4. Have the named individual review and certify the final form.

Do not attach CPOS solely because prior support records exist. First confirm the document requirement through the NOFO and applicable application, JIT, RPPR, or Prior Approval instructions. Use the [submission-lifecycle matrix]({{ site.baseurl }}{% link other-support/lifecycle-submission.md %}) for the person-and-stage decision.

```mermaid
flowchart TD
    accTitle: Reusing prior support records for CPOS
    accDescr: When NIH requests CPOS for a person and stage, prior records become source material for a current SciENcv form that the named individual reviews and certifies.
    A["NIH submission involving this person"] --> B{"Is CPOS requested for this role and stage?"}
    B -- "No" --> C["Do not attach CPOS now"]
    B -- "Yes" --> D["Use prior support records as source material"]
    D --> E["Create or update CPOS in SciENcv"]
    E --> F["Resolve missing fields"]
    F --> G["Named individual reviews and certifies"]
    G --> H["Certified CPOS PDF"]
```
