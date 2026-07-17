---
title: Enforcement (active NIH timeline)
parent: Policy & Timeline
nav_order: 2
---

# Enforcement (active NIH timeline)

NIH enforces Common Forms via **eRA system validations**:

- **Common Forms are required** for application due dates on/after **Jan 25, 2026** and for JIT, RPPR, and Prior Approval submissions on/after **Jan 25, 2026**.
- For application due dates and JIT, RPPR, and Prior Approval submissions on/after **May 8, 2026**, system validations stop submissions not using compliant Common Forms.
- The practical fix for an eRA Common Forms error is usually to replace the attachment with a compliant, digitally certified SciENcv PDF and confirm that its ORCID PID matches the ORCID linked to the eRA Commons credential used in the submission.

```mermaid
stateDiagram-v2
    state "eRA validates Common Forms" as Validate
    state "Submission-stopping error" as Error
    state "Compliant SciENcv Common Forms" as Compliant
    [*] --> Validate: Submit package
    Validate --> Compliant: Certified SciENcv PDFs pass validation
    Validate --> Error: Legacy or non-compliant forms
    Error --> Compliant: Replace before submission can proceed
    Compliant --> [*]
```

See NIH notices [NOT-OD-26-018](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html) and [NOT-OD-26-079](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-079.html).

{: .warning }
> **Operational implication:** you need dedicated **individual certification steps** in your internal submission timeline. Delegates cannot certify for the named individual.

{: .note }
> **PDF handling:** keep each certified SciENcv Common Form unmodified unless the NIH Application Guide or NOFO expressly instructs otherwise. NIH’s participating-faculty biosketch attachment is one such exception: individually certified biosketches are combined and flattened for that specific attachment. Foreign appointment/employment contracts and annual MFTRP statements are separate flattened attachments, not edits to the SciENcv Common Form.

See [Submission lifecycle: application, JIT, RPPR, and Prior Approval]({{ site.baseurl }}{% link other-support/lifecycle-submission.md %}) for person-level attachment rules and exceptions.
