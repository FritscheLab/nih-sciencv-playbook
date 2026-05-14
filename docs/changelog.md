---
title: Changelog
nav_order: 13
---

# Changelog

## Unreleased

- Reserve this section for the next round of policy/FAQ refreshes so maintainers have a visible place to record changes before publishing a tagged update.

## v1.6 (May 2026)

- Refreshed enforcement wording so current pages lead with active **May 8, 2026** submission-stopping error behavior and omit leniency-period history from operational guidance.
- Updated official-source review dates to **2026-05-14**.

## v1.5 (May 2026)

- Enabled Mermaid rendering for the Just the Docs site with a pinned Mermaid version.
- Added inline workflow diagrams across policy, getting-ready, biosketch, CPOS, XML upload, transition, quickstart, walkthrough, and troubleshooting pages.

## v1.4 (May 2026)

- Fixed CPOS XML Validator + Normalizer false positives against NLM's blank upload template, hardened browser result rendering, tightened person-month numeric checks, and preserved moved in-kind text during auto-shortening.

## v1.3 (May 2026)

- Updated references and policy pages for **NOT-OD-26-079**: NIH leniency period ends **May 7, 2026**; system warnings become submission-stopping errors on **May 8, 2026**.
- Added **NOT-OD-26-017** / Research Security Training certification reminders for Common Forms certified before **April 22, 2026** and applications due on/after **May 25, 2026**.
- Updated ORCID setup language to require both the **eRA Commons ORCID link** and a matching **SciENcv PID**.
- Updated CPOS XML guidance to reflect NIH's April 22, 2026 zero person-month support for 2026-1 Common Forms.
- Refreshed `docs/references.md` against official NIH/eRA/NCBI/NLM/NSF sources; added missing official GPS, FAQ, disclosure-training, XML troubleshooting, and NSPM-33 links; and clarified source hierarchy so NIH hub/newest Guide Notice timing controls over lagging form pages, eRA controls ORCID enforcement language, NLM controls XML upload details, and NSF/OSTP provide policy context rather than NIH-specific requirements.

## v1.2 (Mar 2026)

- Updated policy/timeline language across the site to reflect NIH’s current **leniency period through May 2026**, with warning-level validations and a later Guide Notice expected for submission-blocking errors.
- Clarified ORCID requirements: link to **eRA Commons** is the documented NIH requirement; additional MyNCBI/SciENcv linked-account steps are framed as workflow support unless NIH/eRA states otherwise.
- Clarified CPOS timing and scope: CPOS is not assumed at initial application in all cases, added the mentored career-development mentor/co-mentor exception, and expanded consulting/in-kind/foreign-appointment guidance.
- Expanded certification guidance: named individual must certify; downloaded SciENcv PDFs may be renamed but must not be altered; re-certification is needed when content changes or signatures are older than 12 months at submission.
- Strengthened biosketch supplement/product guidance (Contributions to Science edge cases, product metadata expectations, and practical no-formal-citation reference patterns).
- Updated XML upload docs and examples to reinforce valid status values (`current`/`pending`), required post-upload QC in SciENcv, and date-format handling.
- Refreshed the Appendix long-form guide against official NIH and eRA Commons sources (review date: **2026-03-02**) and re-framed it as a **current reference** companion.
- Added maintainer operations support: new short quarterly checklist page, maintenance-page checklist links, and appendix-reference wording updates for consistency.

## v1.1 (Jan 2026)

- Added CPOS **XML Upload & Automation** section (includes AI prompt, QC checklist, and workflow patterns)
- Added lightweight XML validator script (`tools/validate_cpos_xml.py`)

## v1.0 (Jan 2026)

- Initial GitHub Pages structure using Just the Docs
- Role-based quickstarts, templates, and troubleshooting
