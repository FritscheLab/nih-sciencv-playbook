---
title: Long-form guide (current reference)
parent: Appendix
nav_order: 1
---

# Long-form guide (current reference)

This appendix is a continuous companion to the task-focused playbook. **Last reviewed against official NIH, eRA Commons, and NCBI/NLM sources: 2026-08-31.**

{: .warning }
> **Current enforcement status:** NIH requires applicable Common Forms for applications and for JIT, RPPR, and Prior Approval submissions. eRA system validations stop submissions that do not use compliant, digitally certified SciENcv forms.

# Comprehensive Guide to NIH Common Forms

## Executive summary

NIH Common Forms are a live operational requirement. eRA system validations stop submissions that do not use compliant Common Forms.

The current NIH model has three core pieces:

1. the **Biographical Sketch Common Form**;
2. the **NIH Biographical Sketch Supplement**; and
3. the **Current and Pending (Other) Support (CPOS) Common Form**.

For NIH, the Common Forms and the NIH supplement must be prepared in **SciENcv** to generate digitally certified PDF files for submission. The biosketch separates:

- the standardized, portable disclosure data in the **Biographical Sketch Common Form**; and
- the NIH-specific qualitative narrative in the **NIH Biographical Sketch Supplement**.

The most important operational points are:

- The **ORCID iD linked to the eRA Commons Personal Profile** is required, and the same ORCID must appear as the **Persistent Identifier (PID)** in the SciENcv Common Form.
- The **NIH Biographical Sketch Supplement** is completed in the **second section of the same SciENcv interface** used for the Common Form.
- The **Biographical Sketch Common Form** has **no NIH page limit**; the meaningful constraints are field-level instructions and character limits inside the supplement.
- The **Personal Statement** is limited to **3,500 characters**.
- The **Honors** section is limited to **15 entries**.
- The **Contributions to Science** section allows **up to 5 contributions**, each limited to **2,000 characters**.
- The Common Form allows **up to 5 closely related products and up to 5 other significant products**; users do not need to fill all 10 slots. Either supplement narrative may use brief parenthetical references to any selected product.
- **Current and Pending (Other) Support is not automatically part of every initial application package.** For many NIH applications, it is requested later in the lifecycle, often during **Just-in-Time (JIT)**.
- Each individual must **personally certify** their own Common Form output in SciENcv. Delegates can prepare records, but they cannot certify them.
- A downloaded SciENcv Common Form may be **renamed**, but the default is to keep it unmodified. Explicit exceptions use separate NIH-directed handling, including a compiled/flattened participating-faculty attachment, flattened foreign-contract copies uploaded separately, and flattened annual MFTRP statements. The Common Form signature date must be **within 12 months** of submission.

---

## Part I: Current policy and system requirements

NIH adopted the Common Forms as part of the federal disclosure-standardization effort associated with **NSPM-33** and the OSTP memorandum on use of common disclosure forms. Current NIH requirements are collected on the NIH Common Forms hub, in the applicable Guide Notices, and in the final form instructions.

### 1.1 Current form structure

The NIH biosketch uses separate structured and narrative components:

- **Biographical Sketch Common Form** = structured disclosure data
- **NIH Biographical Sketch Supplement** = NIH-specific narrative assessment
- **CPOS Common Form** = structured support disclosure used when NIH requests current and pending support

NIH expects these documents to be produced through the SciENcv workflow rather than by freehand editing a Word or PDF template.

### 1.2 Current lifecycle handling

| Submission stage | Current operational rule |
| --- | --- |
| Application | Attach the combined Biosketch Common Form and NIH Supplement for every individual listed on the R&R Senior/Key Person Profile, including senior/key personnel and Other Significant Contributors. Attach CPOS only when the NOFO or Application Guide requires it for that person and mechanism. |
| JIT | Submit information only when NIH requests it. Use the separate person-level fields for each applicable biosketch, CPOS, and foreign supporting document. The PD/PI may upload and save; only a Signing Official submits JIT. |
| RPPR | Use Section D person-level fields when a participant's role or support status triggers an attachment. Handle annual MFTRP statements separately in Section G.1. |
| Prior Approval | Use the eRA Commons Prior Approval Module and follow the selected request type. A Change of PD/PI requires a biosketch and CPOS for each proposed PD/PI. |

NIH's current Common Forms FAQs explicitly confirm the application biosketch population, including Other Significant Contributors.

### 1.3 Research Security Training and Common Forms timing

For current applications, each senior/key person listed on the application must:

- complete qualifying **Research Security Training (RST)** within the **12 months before application submission**; and
- personally certify completion through the **SciENcv biosketch**.

The Authorized Organization Representative (AOR) provides the separate institutional certification through the application signature for covered senior/key personnel employed by the applicant organization. Qualifying training covers cybersecurity, international collaboration, foreign interference, proper use of funds, disclosure, conflict of commitment, conflict of interest, and **risks of malign foreign talent recruitment programs, including the prohibition on NIH senior/key personnel participating**. NIH recognizes the government-wide modules and the SECURE Center's condensed module, while allowing another training that covers all required topics. See the [current NIH RST FAQ](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm?anchor=57984).

NIH also explicitly notes that, based on NIH's **Just-in-Time** policy, NIH **does not collect Current and Pending (Other) Support at the time of application** in the ordinary case.

### 1.4 MFTRP prohibition and certifications

An individual who is currently party to a **malign foreign talent recruitment program (MFTRP)** is ineligible to serve as senior/key personnel on an NIH grant or cooperative agreement.

At application:

- each senior/key person certifies through the SciENcv biosketch that they are not currently party to an MFTRP; and
- the AOR certifies through the application signature that senior/key personnel were informed of and complied with the individual certification requirement.

For NIH RPPRs, the recipient must collect a separate annual MFTRP statement from each senior/key person using NIH's required language: “I [insert name] certify that, at the time of submission, I am not a party to a malign foreign talent recruitment program.” Upload it in **RPPR Section G.1**, flatten the separate statement PDF, and name it `MFTRPcert_[Name].pdf`. Do not append that statement to, or use it to flatten, the biosketch or CPOS Common Form.

### 1.5 Other Support disclosure training is a separate recipient obligation

NIH recipients must provide training to all faculty and researchers identified as senior/key personnel on Other Support disclosure responsibilities, in addition to maintaining a written and enforced disclosure policy. This continuing recipient obligation is distinct from application-specific RST completion and certification and from the MFTRP certifications.

{: .note }
> **Practical institutional guidance:** track the obligations separately. If an institution chooses to use one course toward both training requirements, document that its content covers each requirement; NIH does not state a general equivalency rule in these notices.

---

## Part II: Identity, system roles, and account setup

### 2.1 Required identity checks: eRA Commons link and SciENcv PID

For NIH, the persistent identifier (PID) used on the Common Forms must be an **ORCID iD**, and that ORCID iD must be linked to the individual's **eRA Commons Personal Profile**.

Confirm that the ORCID iD displayed in the Common Form PID field matches the ORCID linked in the personal profile associated with the eRA Commons username entered in the application credential field. The PID can be populated by linking ORCID in MyNCBI/SciENcv, signing into SciENcv with ORCID, or manually entering the ORCID iD in the Common Form.

### 2.2 What each system does

The practical workflow spans three systems:

- **eRA Commons** establishes NIH identity and stores the ORCID link used for validation.
- **SciENcv** is the required preparation system for NIH Common Forms and the NIH supplement.
- **MyNCBI / NCBI account services** provide the account layer through which SciENcv is accessed.

For NIH documentation, the investigator's ORCID must appear correctly as the **Persistent Identifier** in the SciENcv-generated Common Form and match the ORCID linked in eRA Commons.

### 2.3 High-value setup checks

Before drafting the biosketch or CPOS, verify:

- the investigator has a working **eRA Commons** account;
- the investigator has an **ORCID iD**;
- the ORCID iD is linked in the **eRA Commons Personal Profile**;
- the same ORCID iD appears as the **PID** in the SciENcv Common Form;
- SciENcv access is working;
- the investigator or delegate can open the relevant Common Form interface.

### 2.4 A common ORCID edge case

The eRA Commons help page notes that one reason ORCID linking may fail is that the investigator has **multiple Commons accounts** and the ORCID iD is already linked to another one. eRA's **Consolidate Accounts** guidance describes a workflow from the account-consolidation prompt or the person menu in Commons. The user selects a primary login; eRA says the organizations and roles associated with the accounts are preserved, and the eRA Service Desk reviews and completes the request.

{: .note }
> **Practical post-consolidation check:** after eRA confirms completion, log in with the retained credentials and review the Personal Profile, affiliations, roles, and ORCID link. Then confirm that the same ORCID appears as the SciENcv Common Form PID. Contact the eRA Service Desk if the ORCID remains incorrect or profile data is missing.

---

## Part III: The Biographical Sketch Common Form

The Biographical Sketch Common Form is the structured federal form used to disclose the investigator's identity, professional preparation, appointments/positions, and products.

### 3.1 General characteristics

For NIH:

- there is **no page limit** for the Biographical Sketch Common Form;
- the form must be prepared in **SciENcv**;
- the individual must certify it;
- the Common Form and NIH supplement are completed through **one user interface**; and
- the combined output is required for every person listed on the application's R&R Senior/Key Person Profile, including Other Significant Contributors.

The Common Form instructions also remind users **not to include personal information** such as home address, personal phone numbers, driver's license number, marital status, or hobbies.

### 3.2 Professional Preparation

NIH's Common Form instructions say to list professional preparation in reverse chronological order by start date and to include:

- education and training;
- all postdoctoral and fellowship training, each listed separately; and
- the baccalaureate degree or other initial professional education.

For each entry, users must provide the organization, location, degree (if applicable), start date, completion or expected completion date, and field of study.

### 3.3 Appointments and Positions

This section is one of the most important compliance areas because it captures domestic and foreign appointments and positions.

NIH's Common Form instructions define appointments and positions broadly enough to include titled academic, professional, or institutional positions whether or not remuneration is received, and whether the role is full-time, part-time, or voluntary. This explicitly includes **adjunct, visiting, and honorary** roles.

Senior/key persons must identify all domestic and foreign professional appointments and positions **outside of the primary organization** for a period of up to **three years** from the date the application is submitted to the agency for funding consideration.

### 3.4 Products: the 5 + 5 model

The Products section allows two buckets of evidence:

1. **up to 5 products closely related to the proposed project**; and
2. **up to 5 other significant products** that highlight the individual's Contributions to Science.

These are maximums, not quotas: a user may select fewer than 10 products. The two buckets also do not impose a rigid narrative mapping. Either the **Personal Statement** or **Contributions to Science** may use a brief parenthetical reference to **any selected product**, regardless of which bucket contains it.

{: .note }
> **Practical strategy, not an NIH requirement:** select products that function as evidence for specific claims rather than as an undifferentiated list of favorite papers. Closely related products often support project-specific points, while other significant products often illustrate broader contributions, but do not force that pattern.

### 3.5 What counts as a product

NIH makes clear that acceptable products are broader than traditional journal articles. Products may include:

- publications, conference papers, and presentations;
- websites or other Internet sites;
- technologies or techniques;
- inventions, patents, patent applications, and licenses; and
- other products such as data, databases or datasets, physical collections, audio/video products, software, models, educational aids or curricula, instruments or equipment, research material, interventions, or new business creation.

### 3.6 Product metadata expectations

Each product must be **citable and accessible** and must comply with NIH's hypertext policy. NIH instructs users to include the available citation information, including:

- author names;
- product title;
- publication or release date;
- website URL;
- another persistent identifier, if available; and
- other relevant citation information.

If one of those elements truly does not apply, NIH instructs users to enter **N/A**.

---

## Part IV: The NIH Biographical Sketch Supplement

The NIH Biographical Sketch Supplement is the NIH-specific narrative companion to the Common Form. SciENcv collects it in the **second section of the Biographical Sketch Common Form interface**, so the user completes both pieces through one workflow.

The supplement contains three required NIH-specific elements:

- **Personal Statement**
- **Honors**
- **Contributions to Science**

### 4.1 Personal Statement

The Personal Statement asks the investigator to describe why they are well-suited for their role on the project. NIH gives examples of appropriate content:

- relevant aspects of training;
- previous experimental work on the specific or related topic;
- technical expertise;
- collaborators or scientific environment; and
- past performance in this or related fields, including ongoing and completed research projects from the past three years that the investigator wants to highlight.

These rules matter especially here:

- Brief **in-text, parenthetical references** may point to any product selected in the Common Form.
- NIH recommends a lead-author/year reference, such as `(Collins et al., 2026)`, or a **PMID/PMCID**.
- Do **not** include full bibliographic citations or hyperlinked references.
- The Personal Statement is limited to **3,500 characters**.

NIH also explicitly allows users to:

- explain factors that affected past productivity, such as family care responsibilities, illness, disability, or military service; and
- indicate whether they published or created research products under another name.

For certain subsets of applicants, NIH adds special guidance. For example, applicants for dissertation research awards such as **R36** should also describe career goals, intended career trajectory, and interest in the specific research areas designated in the NOFO.

### 4.2 Honors

The Honors section lists relevant academic and professional achievements and honors. NIH specifically notes that:

- students, postdoctorates, and junior faculty should include scholarships, traineeships, fellowships, and development awards, as applicable; and
- clinicians should include clinical licensure and specialty board certifications, as relevant.

The Honors section is limited to **no more than 15 entries**. If there are no honors to report, enter **Nothing to Report** in both the Honor and Name of Organization fields, enter the current year in the required Year field, and leave End Year blank.

### 4.3 Contributions to Science

For Contributions to Science, NIH instructs users as follows:

- **All senior/key persons should complete the section.**
- If no contributions will be provided, enter **N/A**.
- Users may describe **up to 5 contributions**.
- Graduate students and postdoctorates may wish to highlight **2 or 3** contributions rather than forcing a full set of 5.
- Figures, tables, and graphics are **not allowed**.
- Each contribution is limited to **2,000 characters**.

For each contribution, NIH says the user should indicate:

- the historical background that frames the scientific problem;
- the central finding(s);
- the influence of the finding(s) on the progress of science or the application of those findings to health or technology; and
- the investigator's specific role in the described work.

### 4.4 How to reference selected products

Both the **Personal Statement** and **Contributions to Science** may use brief parenthetical references to **any product selected in the Common Form**. The reference is not limited to one product bucket, and there is no five-product-per-contribution reference rule.

NIH recommends identifying the product by lead author and year or by **PMID/PMCID**. For example:

> This work established the assay used here (Smith et al., 2024; PMID: 12345678).

Do not insert a full bibliographic citation, references list, or hyperlinked reference in either supplement narrative box.

---

## Part V: Current and Pending (Other) Support (CPOS)

### 5.1 The first rule: distinguish "required format" from "required now"

A common source of confusion is that two statements are true at the same time:

1. **Whenever NIH requires current and pending support, use the CPOS Common Form prepared in SciENcv.**
2. **Many NIH applications do not include current and pending support at the initial application stage.**

The NIH Application Guide states that applicants should **not** use the "Current and Pending Support" attachment upload for NIH or other PHS agency submissions **unless otherwise specified in the NOFO**. Instead, NIH may request that information later in the pre-award cycle, usually through **Just-in-Time (JIT)**.

### 5.2 Important application-stage exception for mentored career development awards

The NIH Application Guide includes an explicit exception for **mentored career development** applications:

- the **mentor and co-mentor(s)** must provide CPOS; and
- the **candidate does not** provide CPOS.

This is the most important application-stage exception to teach clearly because it reverses the assumption many users bring from R-series applications.

### 5.3 Person-level collection across JIT, RPPR, and Prior Approval

The Common Forms requirements determine the **format when an attachment is requested**. NIH does not collect both the biosketch and CPOS for every person at every stage.

For **Just-in-Time (JIT)**:

- submit JIT information only when NIH specifically requests it;
- use the separate person-level fields for each applicable biosketch, CPOS, and foreign supporting document;
- the PD/PI may upload and save JIT information, but JIT authority cannot be delegated; and
- only a Signing Official (SO) can submit JIT information to NIH.

For **RPPR Section D**, use the person's role and support status to determine the attachments:

| Participant condition | Biosketch Common Form + NIH Supplement | CPOS | Foreign supporting documentation |
| --- | --- | --- | --- |
| New senior/key person | Required | Required | If applicable |
| Existing senior/key person with new or changed active support | No, unless otherwise requested | Required | If applicable |
| New Other Significant Contributor | Required | Not required | Not required |
| New training faculty member reported in a Training RPPR | Required | Required | If applicable |

The last row is a narrow Training RPPR rule: the current RPPR instructions treat **new training faculty** as new senior/key personnel and require their biosketch, Supplement, CPOS, and applicable supplemental documentation. It does not make all Program Directors, training faculty, or training-grant oversight personnel routine CPOS submitters. Annual MFTRP statements are handled separately in **RPPR Section G.1**, not in Section D or inside a Common Form.

For **Prior Approval**, distinguish the general submission rule from request-specific attachments. Under [NOT-OD-26-026](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-026.html), all Prior Approval requests for NIH grant and cooperative-agreement awards use the **eRA Commons Prior Approval Module** and must be initiated and submitted by a recipient Signing Official. The evidence depends on the request type. For a **Change of PD/PI**, the proposed PD/PI's effort may not be zero; each proposed PD/PI needs one certified biosketch and one certified CPOS; and applicable foreign supporting documentation is uploaded separately.

### 5.4 What the CPOS Common Form is for

NIH's CPOS instructions say current and pending support is used to assess:

- the individual's capacity and possible **conflicts of commitment**;
- potential **scientific overlap**; and
- potential **budgetary overlap/duplication**.

The CPOS Common Form instructions also state that a **separate submission** must be provided for:

- each proposal;
- each active project; and
- each reportable in-kind contribution.

There is **no page limitation** for the CPOS Common Form, although certain fields do have character limits.

### 5.5 What must be reported

The CPOS instructions and [NIH GPS §2.5.1](https://grants.nih.gov/grants/policy/nihgps/HTML5/section_2/2.5.1_just-in-time_procedures.htm) together establish that reportable support can include:

- resources and/or financial support from domestic and foreign entities;
- active and pending projects;
- reportable consulting activities;
- in-kind contributions; and
- foreign appointments/employment and related foreign activities/resources that fall within NIH reporting rules.

NIH GPS §2.5.1 states that broadly available **institutional core facilities or shared equipment** should not be included in Other Support; those belong in **Facilities and Other Resources** instead.

The same page also states that Other Support does **not** include:

- training awards;
- prizes; or
- true gifts where there is no expectation of time, services, specific research activities, money, or other return commitment.

### 5.6 Consulting: the current NIH trigger list

NIH says consulting activities must be disclosed under the **proposals and active projects** section when **any** of the following are true:

- the consulting activity requires the senior/key person to **perform research**;
- the consulting activity does **not** involve performing research, but is related to the senior/key person's research portfolio and may affect funding, alter time or effort commitments, or otherwise affect scientific integrity; or
- the consulting entity provided a contract that requires the senior/key person to conceal or withhold confidential financial or other ties between the senior/key person and the entity.

### 5.7 In-kind contributions

The CPOS instructions require disclosure of in-kind contributions when they:

- are **non-cash contributions provided by an external entity**;
- are **not intended for use on the project or proposal for which the disclosure is being submitted**;
- have an estimated value of **$5,000 or more**; and
- require a **commitment of the individual's time**.

If there is **no associated time commitment**, the in-kind contribution does **not** need to be reported.

Describe an in-kind resource intended for use on that project or proposal in **Facilities & Other Resources** or **Equipment**, as applicable, rather than as CPOS in-kind support.

Examples of potentially reportable in-kind support include externally provided laboratory space, equipment, data or data sets, supplies, goods and services, and employee or student resources. Broadly available institutional core facilities and shared equipment are not reported as CPOS in-kind support.

### 5.8 Supporting documentation for foreign appointments and employment

NIH's CPOS Common Form instructions say institutions must submit copies of contracts specific to senior/key-personnel **foreign appointments and/or employment** with a foreign institution for foreign activities and resources that are reported in CPOS. If those materials are not in English, recipients must provide **translated copies**.

The instructions also clarify an important exclusion: this requirement does **not** include **personal service contracts** or **employment contracts for fellows supported by foreign entities**.

The supporting documentation is not appended inside the SciENcv-generated CPOS PDF. Flatten the contract copy and submit it separately through the designated person-level supporting-documentation field in the relevant NIH module, such as JIT, RPPR, or Prior Approval.

### 5.9 Who is generally excluded from Other Support reporting

NIH GPS §2.5.1 states that Other Support information is requested for all senior/key personnel in an application **except**:

- Program Directors, training faculty, and other individuals involved in the oversight of training grants; and
- individuals categorized as **Other Significant Contributors**.

This describes the covered population when NIH collects Other Support; it does not mean CPOS belongs in every initial application.

The NIH GPS likewise excludes Program Directors, training faculty, and other individuals involved in training-grant oversight from its listed progress-report group. Apply that as a general rule, not an absolute one: as described above, the current RPPR instructions specifically treat **new training faculty in a Training RPPR** as new senior/key personnel and require their biosketch, Supplement, CPOS, and applicable supplemental documentation.

### 5.10 Advanced NIH-specific CPOS edge cases

The current CPOS instructions also include several advanced cases that matter for some institutions:

- **Joint University / VA appointments:** entries should be organized by appointment, and reporting should use person-months rather than equivalent total professional effort.
- **Consortium/contractual arrangements and multi-project awards:** use the overall project's award number and support source, but report the subproject title, total subproject amount for its full performance period, person-months, and other details. Do not substitute the overall project's full amount for the subproject amount.
- **Mentored Career Development Awards with subsumed effort:** the CPOS instructions provide specific wording for reporting complementary effort that is subsumed under the CDA.
- **Zero effort:** SciENcv allows entry of zero person months for Proposals/Active Projects and In-Kind Contributions when accurate for a particular year.

These are real NIH instruction-level requirements, not informal institutional conventions, so they should be checked directly against the CPOS instructions when they apply.

---

## Part VI: Delegate workflow and certification

### 6.1 Delegates can prepare, but the individual must certify

The practical division of labor remains:

- a delegate may prepare or update the record in SciENcv; but
- the investigator must personally certify the form.

That is true for the biosketch Common Form / NIH supplement workflow and for CPOS.

### 6.2 What certification means operationally

The certified PDF downloaded from SciENcv is the submission artifact NIH expects.

For both the Biographical Sketch Common Form and the CPOS Common Form:

- the PDF may be **renamed** after download;
- the PDF content must **not** be altered;
- users should **not** print to PDF, flatten, optimize, or otherwise regenerate the Common Form **unless the Application Guide, NOFO, or lifecycle instructions explicitly require a special attachment format**; and
- the signature date must be within the past **12 months** when the document is submitted to NIH.

If anything changes in the document, or if the certification becomes too old, the correct fix is to go back into SciENcv, update the data, and **re-certify**.

Keep the attachment types distinct:

| Attachment | Required handling |
| --- | --- |
| SciENcv biosketch or CPOS Common Form | Rename if needed, but otherwise keep the certified PDF unmodified unless NIH instructions expressly say otherwise |
| Participating-faculty biosketch attachment | Combine the individually certified forms and flatten the compiled attachment as NIH instructs |
| Foreign appointment/employment contract copy | Flatten and upload separately in the designated supporting-documentation field; do not append it to CPOS |
| Annual MFTRP RPPR statement | Flatten the separate statement and upload it in Section G.1 as `MFTRPcert_[Name].pdf`; do not append it to a Common Form |

### 6.3 Why flattening is a real submission risk

NIH's Common Forms workflow depends on machine-readable data created by SciENcv. Flattening or re-printing a Common Form can strip or damage the metadata NIH systems rely on to recognize the file as a compliant SciENcv-generated form. The safe default for the Common Form itself is therefore **do not flatten**. Apply the explicit separate-attachment or compilation exceptions in the table above exactly as NIH instructs.

---

## Part VII: Common mistakes and edge cases

### 7.1 Assuming CPOS always belongs in the initial application package

This is one of the most common workflow mistakes. NIH's Application Guide says not to include current and pending support at the application stage unless the NOFO or a mechanism-specific Application Guide instruction says otherwise. For example, mentored career development applications require CPOS for mentor/co-mentor(s), not for the candidate. Many NIH users will first need CPOS during **JIT** rather than initial submission.

### 7.2 Overstating the ORCID requirement

The official NIH/eRA identity checks that can be verified directly are:

- obtain an **ORCID iD**; and
- link it to the **eRA Commons Personal Profile**; and
- confirm the same ORCID appears as the **PID** in the SciENcv Common Form.

NIH says the SciENcv PID can be populated through MyNCBI/SciENcv account linking, signing in with ORCID, or manual entry in the Common Form PID field. The key validation risk is mismatch between the Common Form PID and the ORCID linked to the eRA Commons credential used in the submission.

When multiple Commons accounts create the conflict, use eRA's **Consolidate Accounts** workflow or contact the eRA Service Desk, then perform the practical post-consolidation profile and PID check described in Part II.

### 7.3 Conflating CPOS with foreign-component reporting

CPOS disclosure and foreign-component reporting overlap, but they are not the same workflow. NIH states that **most instances of foreign co-authorship represent a foreign component**, although minor or indirect contributions may not. In **all cases**, recipients should report foreign co-authorship to the funding NIH Institute or Center **as soon as they become aware of it** so NIH can determine what steps, if any, are needed.

As a practical workflow, route the matter through institutional review and the funding IC even when no CPOS entry is required. Separately disclose any support, resource, appointment, affiliation, or commitment that NIH requires in CPOS.

### 7.4 Using the wrong kind of product reference in the supplement

Either the Personal Statement or Contributions to Science may use a brief parenthetical reference to any selected Common Form product. Use lead-author/year or PMID/PMCID. Do not insert full bibliographic citations, a references list, or hyperlinked references in the supplement narrative boxes.

### 7.5 Under-reporting foreign relationships or consulting arrangements

Users should review the CPOS consulting trigger list and the foreign appointment/employment supporting-documentation rules directly when those situations apply.

### 7.6 Consortium and subaward workflows

In multi-site applications, the lead institution cannot rely on locally editing another institution's records. Each external person listed on the R&R Senior/Key Person Profile, including an OSC, must provide a compliant, certified combined biosketch for the lead site to assemble. Collect CPOS from an external participant only when NIH requests it for that person's role and submission stage.

---

## Part VIII: Operational recommendations for institutions

1. **Build biosketches early, but do not put CPOS on the critical path unless the mechanism and submission stage actually require it.**
2. **Verify ORCID-in-eRA and the SciENcv PID early.** The Common Form PID should match the ORCID linked to the eRA Commons credential.
3. **Select products before polishing narratives.** The supplement works best when the Personal Statement and Contributions to Science are written against a settled product list.
4. **Schedule certification windows close to submission.** Certification cannot be delegated.
5. **Track RST, MFTRP, and Other Support disclosure training as separate controls.** They have different populations, evidence, timing, and submission points.
6. **Use an attachment-by-person lifecycle checklist.** Confirm the role, mechanism, stage, and current instructions before requesting a biosketch, CPOS, foreign contract, or MFTRP statement.
7. **Re-check the official NIH, eRA, and NCBI/NLM pages quarterly.** Form-directory and help pages can change, and the NIH Common Forms hub remains the primary source for current policy status.

---

## Selected official references used for this refresh

- NIH. [*Common Forms for Biographical Sketch and Current and Pending (Other) Support*](https://grants.nih.gov/policy-and-compliance/implementation-of-new-initiatives-and-policies/common-forms-for-biosketch).
- NIH. [*Common Forms FAQs*](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm), including the current [application biosketch population](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm?anchor=57968) and [RST topics](https://grants.nih.gov/faqs#/common-forms-biographical-sketch-current-pending-support.htm?anchor=57984).
- NIH Guide Notices [NOT-OD-26-079](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-079.html), [NOT-OD-26-018](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html), [NOT-OD-26-017](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-017.html), [NOT-OD-26-026](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-026.html), [NOT-OD-25-133](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-133.html), and [NOT-OD-26-084](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-084.html).
- NIH. [*Biographical Sketch Common Form*](https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form), [*NIH Biographical Sketch Supplement*](https://grants.nih.gov/grants-process/write-application/forms-directory/nih-biographical-sketch-supplement), and [*Current and Pending (Other) Support Common Form*](https://grants.nih.gov/grants-process/write-application/forms-directory/cpos-common-form).
- NIH final PDF instructions for the [Biosketch Common Form](https://grants.nih.gov/sites/default/files/Common%20Form%20NIH%20Biographical%20Sketch_FINAL.pdf), [NIH Supplement](https://grants.nih.gov/sites/default/files/NIH%20Biographical%20Sketch%20Supplement_FINAL.pdf), and [CPOS Common Form](https://grants.nih.gov/sites/default/files/Common%20Form%20NIH%20Current%20and%20Pending%20%28Other%29%20Support_FINAL.pdf).
- NIH. [*R&R Senior/Key Person Profile (Expanded) Form*](https://grants.nih.gov/grants/how-to-apply-application-guide/forms-i/general/g.240-r%26r-seniorkey-person-profile-%28expanded%29-form.htm), [*NIH GPS §2.5.1 Just-in-Time Procedures*](https://grants.nih.gov/grants/policy/nihgps/HTML5/section_2/2.5.1_just-in-time_procedures.htm), and [*NIH RPPR Instruction Guide*](https://grants.nih.gov/sites/default/files/rppr_instruction_guide.pdf).
- NIH. [*FY2027 Extramural LRP Application Instruction Guide*](https://grants.nih.gov/sites/default/files/Extramural-LRP-Application-Instruction-Guide.pdf).
- eRA Commons. [*Just-in-Time Screen*](https://www.era.nih.gov/erahelp/commons/commons/status/jit.htm), [*Change of PD/PI Prior Approval*](https://www.era.nih.gov/erahelp/commons/commons/prior_approval%20module/Change_of_PI.htm), [*The ORCID iD*](https://www.era.nih.gov/erahelp/commons/PPF_Help/8_2_orcid.htm), and [*Consolidate Multiple eRA Commons Accounts*](https://www.era.nih.gov/register-accounts/consolidate-multiple-accounts.htm).
- NCBI. [*My NCBI Help: SciENcv*](https://www.ncbi.nlm.nih.gov/books/NBK154494/) and [*SciENcv News & Updates*](https://www.ncbi.nlm.nih.gov/sciencv/newsupdates/).
