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
    %% accTitle: MyNCBI account and SciENcv document map
    %% accDescr: Within the MyNCBI account, My Bibliography supplies product citations and delegate settings provide admin editing access to SciENcv. SciENcv contains biosketch and CPOS documents and produces certified PDFs.
    columns 3
    block:account:3
        columns 3
        dashboard["MyNCBI account dashboard"]:3
        space:3
        bibliography["My Bibliography<br/>Product citation library"]
        space
        delegates["Delegate settings<br/>Admin editing access"]
        space:3
        sciencv["SciENcv<br/>Biosketch and CPOS documents"]:3
        space:3
        output["Certified PDFs"]:3
    end
    bibliography --> sciencv
    delegates --> sciencv
    sciencv --> output
```

See the [illustrated My NCBI Help guide to SciENcv](https://www.ncbi.nlm.nih.gov/sites/books/NBK154494/).
