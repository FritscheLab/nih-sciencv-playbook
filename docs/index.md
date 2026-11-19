---
title: Home
nav_order: 1
---

# NIH Common Forms (SciENcv) Playbook

Use this playbook to prepare NIH forms in SciENcv, whether you are an investigator, another person named on a form, or the staff member helping prepare it.

- **NIH biosketch:** Biographical Sketch Common Form and NIH Biographical Sketch Supplement
- **Current and Pending (Other) Support (CPOS):** a separate Common Form

This independent guide links to the official instructions in [References]({{ site.baseurl }}{% link references.md %}).

{: .warning }
> **Use certified SciENcv PDFs.** eRA validation stops submissions that lack compliant forms. Check [which forms to attach at each submission stage]({{ site.baseurl }}{% link other-support/lifecycle-submission.md %}) and [who must complete the research-security certifications]({{ site.baseurl }}{% link policy/research-security-certifications.md %}).

## Choose your quickstart

- [PI / faculty (15-minute checklist)]({{ site.baseurl }}{% link quickstarts/pi.md %})
- [Administrator / delegate (fast checklist)]({{ site.baseurl }}{% link quickstarts/admin-delegate.md %})
- [Co-I / key personnel (fast checklist)]({{ site.baseurl }}{% link quickstarts/key-personnel.md %})

{: .warning }
> **Reusing a saved SciENcv PDF?** Check whether the [September 2026 signing-certificate rollover]({{ site.baseurl }}{% link troubleshooting/september-2026-certificates.md %}) affects your attachment.

## Prepare and certify your forms

Check that the ORCID iD linked in eRA Commons matches the persistent identifier on the SciENcv form. Allow time for each person named on a form to review and certify it in their own account.

```mermaid
stateDiagram-v2
    direction TB
    accTitle: Common Forms readiness lifecycle
    accDescr: Readiness progresses from identity and data preparation through drafting, named-individual certification, and delivery of an unmodified submission-ready package.
    state "Identity and access ready" as Identity
    state "Reusable data ready" as Data
    state "SciENcv drafts complete" as Drafts
    state "Awaiting named-individual certification" as Awaiting
    state "Certified PDFs" as Certified
    state "Submission-ready package" as Ready
    [*] --> Identity
    Identity --> Data: identifiers linked and matched
    Data --> Drafts: records cleaned
    Drafts --> Awaiting: content and scope checked
    Awaiting --> Certified: individual certifies
    Certified --> Ready: preserve Common Forms
    Ready --> [*]
```

See the [complete walkthrough]({{ site.baseurl }}{% link complete-walkthrough.md %}) for the steps from account setup through submission.
