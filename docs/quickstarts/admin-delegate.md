---
title: Administrator / Delegate (fast checklist)
parent: Quickstarts
nav_order: 2
---

# Administrator / Delegate quickstart

## Before you touch SciENcv

1. Ensure each PI/key person has:
   - eRA Commons ID
   - ORCID iD linked to **eRA Commons** (**required**)
   - MyNCBI/SciENcv access working; ORCID appears as the SciENcv **PID** and matches eRA Commons
2. Ask each PI to **add you as a delegate** in MyNCBI.
3. Confirm you have access to:
   - **SciENcv** delegation
   - **My Bibliography** delegation (needed to fix missing products/citations)

## Build the docs (delegate tasks)

- Create or update the combined SciENcv biosketch for **every person listed on the R&R Senior/Key Person Profile (Expanded)**, including every **Other Significant Contributor (OSC)** ([NIH Common Forms FAQ 57968](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm?anchor=57968) and [FAQ 57969](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm?anchor=57969)); create CPOS **when NIH requests it for the person's role, mechanism, and submission stage**
- Import from ORCID (when clean) to reduce manual entry
- Curate products (**up to 10 total**) and verify they align to narratives
- Paste narratives using only SciENcv's supported **Markdown** formatting; re-check character counts and the rendered preview
- Do a **PDF preview** for formatting/typos

For CPOS, check the NOFO and the applicable NIH Application Guide, JIT, RPPR, or Prior Approval instructions before requesting a document. A narrow exception matters for training grants: the NIH RPPR instructions treat **new training faculty** as new senior/key personnel and require their biosketch Common Form, NIH Supplement, CPOS, and any applicable supplemental documentation.

{: .note }
> **Recipient compliance check:** NIH recipients must provide Other Support disclosure training to all faculty and researchers identified as senior/key personnel, in addition to maintaining a written and enforced disclosure policy. This institutional training obligation is separate from the individual **Research Security Training (RST)** requirement.

For each application, verify under your institution’s process that every senior/key person’s RST completion date falls within the 12 months before submission. Also preserve time for the named person’s biosketch certification and the AOR’s separate institutional certification for covered individuals employed by the applicant organization.

## Hand-off to the named individual (required)

- Send each named individual your “ready to certify” note
- The named individual logs in, **certifies**, and downloads the requested PDFs (or lets you download after certification)
- For an RPPR, collect the separate annual MFTRP Section G.1 statement for every senior/key person; do not append it to a Common Form

See [Research-security certifications]({{ site.baseurl }}{% link policy/research-security-certifications.md %}) and the [submission-lifecycle matrix]({{ site.baseurl }}{% link other-support/lifecycle-submission.md %}).

```mermaid
swimlane-beta TB
    accTitle: Admin delegate quickstart workflow
    accDescr: The admin or delegate prepares and checks the documents, then hands them to the named individual for review and certification before collecting the certified PDFs.

    subgraph admin [Admin or delegate]
        setup["Audit setup and confirm delegate access"]
        draft["Create the documents NIH requests for this role and stage"]
        prepare["Curate Products and narratives"]
        check["Check RST, stage requirements, and PDF previews"]
        notify["Send ready-to-certify notice"]
        collect["Collect certified PDFs"]
    end

    subgraph person [Named individual]
        certify["Review and certify in own account"]
    end

    setup --> draft --> prepare --> check --> notify
    notify -->|Ready for review| certify
    certify -->|Certified PDFs| collect
```

Next: [Delegates (how to collaborate)]({{ site.baseurl }}{% link getting-ready/delegates.md %})
