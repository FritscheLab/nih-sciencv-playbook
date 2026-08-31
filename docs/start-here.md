---
title: Start Here
nav_order: 2
---

# Start Here

## Why this exists

NIH's biosketch and Current and Pending (Other) Support workflows use a **data-driven system** centered on SciENcv. Each required Common Form must be a **digitally certified PDF generated in SciENcv**.

## The “minimum viable compliance” path

1. Everyone who needs a biosketch gets:
   - **eRA Commons ID**
   - **ORCID iD**, linked to **eRA Commons** (**required**)
   - **MyNCBI/SciENcv** access working; ORCID appears as the SciENcv **PID** and matches eRA Commons
2. Publications are curated in **My Bibliography**
3. A delegate (admin) is assigned where helpful
4. PI logs in to **certify** the final PDFs

```mermaid
flowchart TD
    accTitle: Minimum viable compliance path
    accDescr: The minimum path links ORCID and eRA Commons, checks the SciENcv PID, cleans My Bibliography, drafts documents, and ends with individual certification.
    A["eRA Commons ID"] --> B["ORCID iD"]
    B --> C["Link ORCID in eRA Commons"]
    C --> D["Confirm matching SciENcv PID"]
    D --> E["Clean My Bibliography"]
    E --> F{"Delegate helping?"}
    F -- "Yes" --> G["Delegate drafts and checks"]
    F -- "No" --> H["Individual drafts"]
    G --> I["Named individual certifies"]
    H --> I
    I --> J["Certified SciENcv PDFs"]
```

## Where to go next

- If you’re a PI: [PI / faculty quickstart]({{ site.baseurl }}{% link quickstarts/pi.md %})
- If you’re a delegate/admin: [Administrator / delegate quickstart]({{ site.baseurl }}{% link quickstarts/admin-delegate.md %})
- If you’re building department-wide support: [Submission planning & tracker]({{ site.baseurl }}{% link transition/department-plan.md %})
