---
title: Maintain & extend this guide
nav_order: 16
---

# Maintain & extend this guide

## Recommended operating model

- **One repo, one site**: all guidance in `docs/`
- Use **pull requests** for edits (even if just one maintainer) to preserve history
- Add updates to `Changelog`

## Adding your institution’s SOPs

- Add your local SOP links under:
  - `References`
  - Role-based quickstarts
  - Department workflows

## Quarterly review checklist

Use the [quarterly checklist]({{ site.baseurl }}{% link quarterly-checklist.md %}) to verify official sources at least once a quarter.

- Newest relevant NIH **Common Forms Guide Notices** and direct form instructions; verify the destination of any former hub link before relying on it
- **NOT-OD-26-018**, the current Common Forms FAQs, and any newer notices
- NIH forms-directory pages for **Biographical Sketch Common Form**, **NIH Biographical Sketch Supplement**, and **CPOS Common Form**
- eRA Commons help for **ORCID**
- NLM Support Center articles for **CPOS XML upload** and **upload errors**
- My NCBI **SciENcv Help** and **SciENcv News & Updates**
- NIH Application Guide pages that affect **when CPOS is attached at application stage**
- OMB/NSF activity affecting the Common Forms information collection, including renewal or replacement instructions
- Institutional submission alerts, including the September 2026 signing-certificate rollover; seek official confirmation and keep these distinct from NIH policy

After content changes:

- Update `docs/changelog.md`
- Rebuild/redeploy GitHub Pages
- Spot-check the published site (home page, ORCID page, biosketch supplement page, CPOS overview, appendix, and FAQ) to confirm the live site matches the repo

## Screenshot policy

Use screenshots your institution is allowed to publish. Crop out names, account identifiers, and other personal details. Label workflow diagrams as illustrations, and link to official help for current interface examples.
