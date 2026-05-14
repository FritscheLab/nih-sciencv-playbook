---
title: Create the biosketch document in SciENcv
parent: NIH Biosketch (Common Form + Supplement)
nav_order: 2
---

# Create the biosketch document in SciENcv

1. Log in to MyNCBI and open **SciENcv**
2. Click **Create New Document**
3. Choose:
   - **Format:** NIH Biosketch (Common Form + Supplement)
   - **Starting point (data source):**
     - **External source (ORCID)** to import education/employment (fastest when ORCID is clean)
     - **Start with existing SciENcv document** (helpful if you had an older biosketch)
     - **Blank** (slowest but most controlled)

{: .note }
> ORCID import saves time but can import duplicates or outdated entries—always review and edit.

```mermaid
flowchart TD
    accTitle: Biosketch starting point choice
    accDescr: A decision path for choosing whether to start the SciENcv biosketch from ORCID, an existing SciENcv document, or a blank document.
    A["Create New Document"] --> B["NIH Biosketch format"]
    B --> C{"Best starting point?"}
    C -- "Clean ORCID data" --> D["External source: ORCID"]
    C -- "Useful prior SciENcv document" --> E["Existing SciENcv document"]
    C -- "Need maximum control" --> F["Blank document"]
    D --> G["Review imported entries"]
    E --> G
    F --> H["Enter sections manually"]
    G --> I["Complete Common Form sections"]
    H --> I
```

Next: [Common Form sections (step-by-step)]({{ site.baseurl }}{% link biosketch/common-form-sections.md %})
