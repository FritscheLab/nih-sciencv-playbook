---
title: Quarterly Checklist (Maintainers)
nav_order: 17
nav_exclude: true
---

# Quarterly Checklist (Maintainers)

Use this once per quarter to keep the playbook aligned with current NIH/eRA guidance.

## 1) Verify source-of-truth pages

- Check all relevant Guide Notices newer than **NOT-OD-26-079** for effective-date or validation changes. Verify former hub links actually resolve to relevant policy content; the old hub redirects to a general Forms Directory as of October 2, 2026.
- Compare the forms-directory pages with the **direct final Biosketch, Supplement, and CPOS PDFs**. Confirm the up-to-5 + up-to-5 Product limits and the parenthetical narrative-reference rule have not changed.
- Compare the OMB control numbers and dates on the current form PDFs and in the [OIRA record for NIH's use of the Common Forms](https://www.reginfo.gov/public/do/PRAViewRCF?ref_nbr=202507-0925-001CF). On November 19, 2026, the two Common Forms displayed **3145-0279 / April 30, 2027**, matching the active OIRA record. The Supplement displayed **0925-0001 / December 31, 2027** and **0925-0002 / November 30, 2027**. Follow NIH's current preparation and submission instructions.
- Recheck **NOT-OD-26-017** and the current Common Forms RST FAQ for the 12-month completion window, individual biosketch certification, AOR certification population, recognized training resources, and all required topics, including MFTRP risks and the NIH senior/key-person prohibition.
- Recheck **NOT-OD-26-018**, the RPPR guide, and current FAQs for MFTRP statement text, electronic signatures/dates, reuse, final/interim scope, flattening, and `MFTRPcert_[Name].pdf` filenames. Track the [FAQ/guide conflict about separate statements]({{ site.baseurl }}{% link policy/research-security-certifications.md %}) until NIH reconciles it.
- Keep the recipient **Other Support disclosure-training requirement** separate from application RST.
- Check **NOT-OD-26-084**, NIH's September 29, 2026 co-authorship scenarios, and any newer foreign-component guidance for reporting and prior-approval rules.
- Review the NIH Application Guide and current FAQs for the application biosketch population, including all people listed on the R&R Senior/Key Person Profile and Other Significant Contributors.
- Review the current RPPR guide/transcript, eRA JIT help, and Prior Approval help for person-, role-, and stage-specific attachment changes. Track any FAQ/RPPR conflict internally until NIH reconciles it.
- Review the current LRP hub, notices, and application guide before each annual LRP cycle; confirm required and optional mentor-team biosketches without generalizing program-specific ASSIST materials to other mechanisms.
- Check eRA ORCID help and account-consolidation guidance, including post-consolidation role/affiliation behavior.
- Check for SciENcv signing-certificate changes independently of the individual's 12-month certification window. Follow up on official confirmation of the [September 2026 institutional alert]({{ site.baseurl }}{% link troubleshooting/september-2026-certificates.md %}).
- Compare NLM CPOS XML guidance and both official XML samples with the CLI/browser validator rules, including real calendar dates and person-month values from 0–12 with at most two decimals.

## 2) Review high-impact playbook pages

- ORCID setup + troubleshooting pages
- Certification, RST, MFTRP, and disclosure-training pages
- PI quickstart + complete walkthrough
- CPOS overview, lifecycle matrix, and what-to-include
- Biosketch Products and Supplement-reference pages/templates
- XML validator, tests, mirror, and generated cheat sheet
- Appendix long-form guide status note

## 3) Update docs and templates

- Distinguish **application due dates** from JIT/RPPR/Prior Approval **submission dates**.
- Confirm CPOS is requested only for the applicable person, role, mechanism, and stage.
- Confirm narrative examples use brief lead-author/year or PMID/PMCID references, not full citations or hyperlinks.
- Keep Common Forms unmodified by default while preserving explicit participating-faculty, foreign-contract, and MFTRP attachment exceptions.
- Label practical institutional workflow advice separately from official requirements.
- Add an `Unreleased` changelog note for edits in progress

## 4) Publish and spot-check

- Update `docs/changelog.md`
- Run `git diff --check`, the XML validator tests, mirror comparison, and a Jekyll build when dependencies are available
- After changing diagrams or shared rendering code, run the repository's Mermaid visual QA and inspect desktop and mobile captures.
- Rebuild/redeploy GitHub Pages
- Spot-check key live pages for correctness and formatting
