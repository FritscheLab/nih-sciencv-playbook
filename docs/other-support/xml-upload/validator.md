---
title: Browser XML validator
parent: XML Upload & Automation
nav_order: 4
---

# Browser XML validator

Use this tool to check for the most common CPOS XML upload issues before SciENcv.
It runs entirely in your browser; files are not uploaded anywhere.

[Open the browser-based validator]({{ site.baseurl }}/tools/)

If you prefer a command-line check, see the script in `tools/validate_cpos_xml.py`.

```mermaid
flowchart LR
    accTitle: Browser validator workflow
    accDescr: The browser validator checks CPOS XML locally, reports common issues, and sends corrected XML back to SciENcv upload review.
    A["Load or paste XML"] --> B["Run browser validation"]
    B --> C{"Issues found?"}
    C -- "Yes" --> D["Fix XML or normalize"]
    D --> B
    C -- "No" --> E["Upload to SciENcv"]
    E --> F["Review entries in SciENcv UI"]
```
