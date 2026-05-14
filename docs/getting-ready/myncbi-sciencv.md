---
title: MyNCBI + SciENcv basics
parent: Getting Ready (accounts + data)
nav_order: 3
---

# MyNCBI + SciENcv basics

SciENcv is accessed through **MyNCBI**.

## Where things live

- **MyNCBI**: your NCBI account dashboard
- **SciENcv**: where you build the Common Forms + NIH Supplement
- **My Bibliography**: your citation library used to populate “Products”
- **Delegates**: where a PI grants editing access to an admin

```mermaid
flowchart LR
    accTitle: MyNCBI and SciENcv workspace map
    accDescr: MyNCBI contains SciENcv, My Bibliography, and delegate settings that together support Common Form preparation.
    A["MyNCBI account"] --> B["SciENcv"]
    A --> C["My Bibliography"]
    A --> D["Delegates"]
    B --> E["Biosketch and CPOS documents"]
    C --> F["Products for biosketch"]
    D --> G["Admin drafting access"]
    E --> H["Certified PDFs"]
    F --> E
    G --> E
```

![SciENcv dashboard placeholder]({{ "/assets/images/placeholder-sciencv-dashboard.svg" | relative_url }})
