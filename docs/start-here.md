---
title: Start Here
nav_order: 2
---

# Start Here

NIH uses SciENcv to generate digitally certified PDFs for the biosketch and Current and Pending (Other) Support (CPOS).

## From account setup to certified PDFs

1. Confirm you can sign in to eRA Commons and SciENcv. [Link your ORCID iD to eRA Commons and check the match in SciENcv]({{ site.baseurl }}{% link getting-ready/orcid.md %}).
2. Organize the citations you plan to use in the biosketch. [My Bibliography]({{ site.baseurl }}{% link getting-ready/mybibliography.md %}) is one source.
3. Prepare the required forms yourself or [give staff delegated access]({{ site.baseurl }}{% link getting-ready/delegates.md %}).
4. The person named on each form signs in and certifies it personally. Keep passwords and verification codes private and have staff use their own delegated accounts.

```mermaid
flowchart TD
    accTitle: Account setup through individual certification
    accDescr: Link ORCID and eRA Commons, check the SciENcv PID, prepare citations, and draft the forms individually or with delegated help. The named person signs in and certifies.
    A["eRA Commons ID"] --> B["ORCID iD"]
    B --> C["Link ORCID in eRA Commons"]
    C --> D["Confirm matching SciENcv PID"]
    D --> E["Prepare biosketch citations"]
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
