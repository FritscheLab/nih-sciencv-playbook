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

**Diagram summary:** Within MyNCBI, My Bibliography supplies product citations and delegate settings provide editing access for documents built in SciENcv.

```mermaid
block-beta
    columns 2
    block:account:2
        columns 2
        dashboard["MyNCBI account dashboard"]:2
        bibliography["My Bibliography<br/>Product citation library"]
        delegates["Delegate settings<br/>Admin editing access"]
        sciencv["SciENcv<br/>Biosketch and CPOS documents"]
        output["Certified PDFs"]
    end
    bibliography --> sciencv
    delegates --> sciencv
    sciencv --> output
```

![SciENcv dashboard placeholder]({{ "/assets/images/placeholder-sciencv-dashboard.svg" | relative_url }})
