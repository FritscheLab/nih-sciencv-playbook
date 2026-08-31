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

When a document is ready, the delegate can select **Send Notification** in SciENcv to alert the account owner by email. The named individual then reviews and certifies the document from their own account.

Official workflow source: [My NCBI Help — SciENcv](https://www.ncbi.nlm.nih.gov/books/NBK154494/).

```mermaid
sequenceDiagram
    accTitle: SciENcv delegate setup and certification handoff
    accDescr: The investigator grants delegate access, the admin accepts and prepares the documents, SciENcv sends the certification notification, and the investigator certifies from their own account.
    actor Investigator
    participant MyNCBI
    participant Admin as Admin / delegate
    participant SciENcv
    Investigator->>MyNCBI: Add delegate
    MyNCBI-->>Admin: Delegate invitation
    Admin->>MyNCBI: Accept invitation
    Admin->>SciENcv: Draft and preview documents
    Admin->>SciENcv: Send Notification
    SciENcv-->>Investigator: Ready-to-certify email
    Investigator->>SciENcv: Certify from own account
```

Next: [Certify + download (individual-only step)]({{ site.baseurl }}{% link biosketch/certify-and-download.md %})
