---
title: Common errors (and fixes)
parent: Troubleshooting
nav_order: 1
---

# Common errors (and fixes)

## “Invalid form format” / form rejected

- Cause: PDF was printed/flattened
- Fix: re-download the original certified PDF from SciENcv

## “Missing persistent identifier”

- Cause: ORCID is not linked or the Common Form PID does not match eRA Commons
- Fix: link ORCID in **eRA Commons**, then confirm the same ORCID appears as the **SciENcv PID**. Populate the PID by linking ORCID in MyNCBI/SciENcv, signing in with ORCID, or entering it manually in the Common Form.

## “Certification required”

- Cause: the named individual did not certify
- Fix: the named individual must log in and certify (delegate cannot)

## Character limit exceeded

- Cause: hidden formatting from Word
- Fix: paste as plain text; re-check counts in SciENcv

```mermaid
flowchart TD
    accTitle: Common error remediation loop
    accDescr: Common errors are remediated by replacing edited PDFs, fixing identifier links, completing certification, or removing hidden formatting.
    A["Error message or warning"] --> B{"Category"}
    B -- "Invalid form format" --> C["Re-download original certified PDF"]
    B -- "Missing persistent identifier" --> D["Link ORCID in eRA and verify SciENcv PID"]
    B -- "Certification required" --> E["Named individual certifies"]
    B -- "Character limit exceeded" --> F["Paste plain text and shorten"]
    C --> G["Recheck submission package"]
    D --> G
    E --> G
    F --> G
```
