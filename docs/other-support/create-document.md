---
title: Create CPOS in SciENcv
parent: Current & Pending (Other) Support (CPOS)
nav_order: 2
---

# Create CPOS in SciENcv

1. SciENcv → **Create New Document**
2. Choose format: **NIH Current and Pending (Other) Support (CPOS) Common Form**
3. Populate entries for active + pending support and any required in-kind support

## Optional: seed the document via XML upload

If an administrator can provide an XML file (for example, generated from a prior Other Support document or an institutional database), you can **upload XML to pre-populate the CPOS form** and then complete missing fields in the SciENcv UI.

- See: [XML Upload & Automation]({{ site.baseurl }}{% link other-support/xml-upload.md %})

```mermaid
flowchart TD
    accTitle: Create CPOS in SciENcv
    accDescr: CPOS creation starts in SciENcv, optionally uses XML upload to seed entries, and always requires UI review before certification.
    A["Create New Document"] --> B["NIH CPOS Common Form"]
    B --> C{"Use XML upload?"}
    C -- "Yes" --> D["Upload XML to pre-populate entries"]
    C -- "No" --> E["Enter support manually"]
    D --> F["Open each entry in SciENcv UI"]
    E --> F
    F --> G["Complete missing fields"]
    G --> H["Ready for certification"]
```

Next: [What to include (practical guidance)]({{ site.baseurl }}{% link other-support/what-to-include.md %})
