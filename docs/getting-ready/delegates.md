---
title: Delegates (how to collaborate)
parent: Getting Ready (accounts + data)
nav_order: 5
---

# Delegates (how to collaborate)

## Investigator: add a delegate

MyNCBI → **Account Settings → Delegates → Add delegate** → enter admin email.

## Admin: accept the invite

Log into **your own** MyNCBI account and accept.

## What delegates can and can’t do

Delegates can:
- Create and edit SciENcv documents
- Import data and curate Products
- Paste narratives, format entries, run previews

Delegates cannot:
- **Certify / sign** the final PDFs (the individual named on the form must do this from their own account)

```mermaid
sequenceDiagram
    actor Investigator
    participant MyNCBI
    participant Admin as Admin / delegate
    participant SciENcv
    Investigator->>MyNCBI: Add delegate
    MyNCBI-->>Admin: Delegate invitation
    Admin->>MyNCBI: Accept invitation
    Admin->>SciENcv: Draft and preview documents
    Admin-->>Investigator: Ready-to-certify note
    Investigator->>SciENcv: Certify from own account
```

Next: [Certify + download (individual-only step)]({{ site.baseurl }}{% link biosketch/certify-and-download.md %})
