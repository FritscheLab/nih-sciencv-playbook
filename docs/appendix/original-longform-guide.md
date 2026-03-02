---
title: Long-form guide (current reference)
parent: Appendix
nav_order: 1
---

# Long-form guide (current reference)

This appendix keeps a long-form companion to the playbook for readers who want one continuous explanation of the NIH Common Forms transition. It was refreshed against official NIH and eRA Commons sources on **2026-03-02**.

{: .note }
> This file originally preserved an early draft. It now reflects the current official NIH/eRA guidance that could be verified as of 2026-03-02.

{: .warning }
> **Current enforcement status:** NIH implemented the Common Forms framework for application due dates and for JIT, RPPR, and Prior Approval submissions on or after **January 25, 2026**. However, NIH is still in a **leniency period through May 2026**. During this period, NIH encourages use of the Common Forms and SciENcv, but system validations remain at the **warning** level and NIH continues to accept the legacy NIH biosketch and other support format pages. NIH has said a later Guide Notice will announce when warnings become errors.

# The Comprehensive Implementation Guide to the 2026 NIH Common Forms

## Executive summary

The NIH Common Forms transition is now a live operational requirement, but the practical reality in early 2026 is more nuanced than the original rollout language suggested.

The current NIH model has three core pieces:

1. the **Biographical Sketch Common Form**;
2. the **NIH Biographical Sketch Supplement**; and
3. the **Current and Pending (Other) Support (CPOS) Common Form**.

For NIH, the Common Forms and the NIH supplement must be prepared in **SciENcv** to generate digitally certified PDF files for submission. The biosketch is no longer a single manually edited narrative document. Instead, NIH now separates:

- the standardized, portable disclosure data in the **Biographical Sketch Common Form**; and
- the NIH-specific qualitative narrative in the **NIH Biographical Sketch Supplement**.

The most important operational points are:

- The **ORCID iD linked to the eRA Commons Personal Profile** is the documented NIH persistent identifier requirement.
- The **NIH Biographical Sketch Supplement** is completed in the **second section of the same SciENcv interface** used for the Common Form.
- The **Biographical Sketch Common Form** has **no NIH page limit**; the meaningful constraints are field-level instructions and character limits inside the supplement.
- The **Personal Statement** is limited to **3,500 characters**.
- The **Honors** section is limited to **15 entries**.
- The **Contributions to Science** section allows **up to 5 contributions**, each limited to **2,000 characters**.
- **Current and Pending (Other) Support is not automatically part of every initial application package.** For many NIH applications, it is requested later in the lifecycle, often during **Just-in-Time (JIT)**.
- Each individual must **personally certify** their own Common Form output in SciENcv. Delegates can prepare records, but they cannot certify them.
- The downloaded PDF may be **renamed**, but it must **not** be edited, printed-to-PDF, flattened, or otherwise altered. The signature date must be **within 12 months** of submission.

---

## Part I: Policy landscape and implementation status

NIH adopted the Common Forms as part of the federal disclosure-standardization effort associated with **NSPM-33** and the OSTP memorandum on use of common disclosure forms. NIH's implementation details are collected on the NIH Common Forms hub and in **NOT-OD-26-018**. The later timing adjustment is in **NOT-OD-26-033**.

### 1.1 What changed structurally

The old NIH biosketch model blended structured profile data and NIH-specific narrative in one document. The new model splits those functions:

- **Biographical Sketch Common Form** = structured disclosure data
- **NIH Biographical Sketch Supplement** = NIH-specific narrative assessment
- **CPOS Common Form** = structured support disclosure used when NIH requests current and pending support

This matters because NIH now expects the documents to be produced through a systems workflow rather than by freehand editing a Word or PDF template.

### 1.2 Effective dates and current operational reality

The formal implementation date remains **January 25, 2026**.

| Submission scenario | On or before Jan. 24, 2026 | On or after Jan. 25, 2026 | Current operational note |
| --- | --- | --- | --- |
| Application due date | Legacy NIH biosketch / other support pages | Common Forms + NIH supplement, when those attachments are required for that application scenario | NIH is still accepting legacy pages during the leniency period through May 2026 |
| JIT | Legacy pages | Common Forms + NIH supplement | Warning-level validations through May 2026 |
| RPPR | Legacy pages | Common Forms + NIH supplement | Warning-level validations through May 2026 |
| Prior Approval | Legacy pages | Common Forms + NIH supplement | Warning-level validations through May 2026 |

The major correction to the earlier draft is the enforcement timeline. NIH no longer states that warnings became hard-stop errors on **February 6, 2026**. Instead, NIH extended the warning-only leniency period through **May 2026** and said a later Guide Notice will announce the date when warnings become errors.

### 1.3 Research Security Training and Common Forms timing

NIH explained that the leniency-period extension allows better alignment between Common Form certifications and the separate **Research Security Training (RST)** requirement for covered individuals. NIH also explicitly notes that, based on NIH's **Just-in-Time** policy, NIH **does not collect Current and Pending (Other) Support at the time of application** in the ordinary case.

---

## Part II: Identity, system roles, and account setup

### 2.1 The required identity element: ORCID linked to eRA Commons

For NIH, the persistent identifier (PID) used on the Common Forms must be an **ORCID iD**, and that ORCID iD must be linked to the individual's **eRA Commons Personal Profile**.

That is the official NIH/eRA requirement that matters most for compliance. As a practical matter, institutions may also use other account-linking steps to streamline SciENcv workflows, but the requirement that NIH explicitly states is the **ORCID-to-eRA Commons** link.

### 2.2 What each system does

The practical workflow spans three systems:

- **eRA Commons** establishes NIH identity and stores the ORCID link used for the PID.
- **SciENcv** is the required preparation system for NIH Common Forms and the NIH supplement.
- **MyNCBI / NCBI account services** provide the account layer through which SciENcv is accessed.

In its implementation notice, NIH also reminds users to **associate their ORCID iD account and eRA Commons account with SciENcv**. For NIH documentation purposes, the most important compliance check is still that the investigator's ORCID appears correctly as the **Persistent Identifier** in the SciENcv-generated Common Form.

### 2.3 High-value setup checks

Before drafting the biosketch or CPOS, verify:

- the investigator has a working **eRA Commons** account;
- the investigator has an **ORCID iD**;
- the ORCID iD is linked in the **eRA Commons Personal Profile**;
- SciENcv access is working;
- the investigator or delegate can open the relevant Common Form interface.

### 2.4 A common ORCID edge case

The eRA Commons help page notes that one reason ORCID linking may fail is that the investigator has **two Commons accounts** and the ORCID iD is already linked to the other one. The official remedy is to contact the **eRA Service Desk**.

---

## Part III: The Biographical Sketch Common Form

The Biographical Sketch Common Form is the structured federal form used to disclose the investigator's identity, professional preparation, appointments/positions, and products.

### 3.1 General characteristics

For NIH:

- there is **no page limit** for the Biographical Sketch Common Form;
- the form must be prepared in **SciENcv**;
- the individual must certify it;
- the Common Form and NIH supplement are completed through **one user interface**.

The Common Form instructions also remind users **not to include personal information** such as home address, personal phone numbers, driver's license number, marital status, or hobbies.

### 3.2 Professional Preparation

The Professional Preparation section is broader than many legacy biosketch users expect. NIH's Common Form instructions say to list professional preparation in reverse chronological order by start date and to include:

- education and training;
- all postdoctoral and fellowship training, each listed separately; and
- the baccalaureate degree or other initial professional education.

For each entry, users must provide the organization, location, degree (if applicable), start date, completion or expected completion date, and field of study.

### 3.3 Appointments and Positions

This section is one of the most important compliance areas because it captures domestic and foreign appointments and positions.

NIH's Common Form instructions define appointments and positions broadly enough to include titled academic, professional, or institutional positions whether or not remuneration is received, and whether the role is full-time, part-time, or voluntary. This explicitly includes **adjunct, visiting, and honorary** roles.

The current NIH Common Form instruction is more precise than some earlier summaries: senior/key persons must identify all domestic and foreign professional appointments and positions **outside of the primary organization** for a period of up to **three years** from the date the application is submitted to the agency for funding consideration.

### 3.4 Products: the 5 + 5 model

The Products section allows two buckets of evidence:

1. **up to 5 products closely related to the proposed project**; and
2. **up to 5 other significant products** that highlight the individual's Contributions to Science.

The Supplement then gives the individual a place to explain those contributions while pointing back to the products listed here.

This is the single biggest strategic change from the legacy NIH biosketch model. Users should select products that function as **evidence for specific claims**, not just an undifferentiated list of favorite papers.

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

Two rules matter especially here:

- **Do not provide citations in the NIH Biographical Sketch Supplement.**
- The Personal Statement is limited to **3,500 characters**.

NIH also explicitly allows users to:

- explain factors that affected past productivity, such as family care responsibilities, illness, disability, or military service; and
- indicate whether they published or created research products under another name.

For certain subsets of applicants, NIH adds special guidance. For example, applicants for dissertation research awards such as **R36** should also describe career goals, intended career trajectory, and interest in the specific research areas designated in the NOFO.

### 4.2 Honors

The Honors section lists relevant academic and professional achievements and honors. NIH specifically notes that:

- students, postdoctorates, and junior faculty should include scholarships, traineeships, fellowships, and development awards, as applicable; and
- clinicians should include clinical licensure and specialty board certifications, as relevant.

The Honors section is limited to **no more than 15 entries**.

### 4.3 Contributions to Science

The current NIH instructions are more specific and more helpful than many older biosketch habits:

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

### 4.4 How to refer to products without formal citations

NIH allows the user to reference **up to 5 products** from the **Other Significant Products** section of the Common Form that are relevant to the contribution being described.

NIH also says there is **no specific format** required for those references. NIH recommends referring to the **title**, using the **author's last name**, the **publication/source**, and/or the **year** for ease of reference.

That means a compliant and reviewer-friendly contribution can say something like:

> See *Title of Product* (Smith, 2024).

What NIH does **not** want here is a formal references list or bibliography inside the supplement narrative boxes.

---

## Part V: Current and Pending (Other) Support (CPOS)

### 5.1 The first rule: distinguish "required format" from "required now"

A common source of confusion is that two statements are true at the same time:

1. **Whenever NIH requires current and pending support on or after January 25, 2026, the required format is the CPOS Common Form prepared in SciENcv.**
2. **Many NIH applications do not include current and pending support at the initial application stage.**

The NIH Application Guide states that applicants should **not** use the "Current and Pending Support" attachment upload for NIH or other PHS agency submissions **unless otherwise specified in the NOFO**. Instead, NIH may request that information later in the pre-award cycle, usually through **Just-in-Time (JIT)**.

### 5.2 Important application-stage exception for mentored career development awards

The NIH Application Guide includes an explicit exception for **mentored career development** applications:

- the **mentor and co-mentor(s)** must provide Current and Pending (Other) Support pages; and
- the **candidate does not** provide those pages.

This is the most important application-stage exception to teach clearly because it reverses the assumption many users bring from R-series applications.

### 5.3 What the CPOS Common Form is for

NIH's CPOS instructions say current and pending support is used to assess:

- the individual's capacity and possible **conflicts of commitment**;
- potential **scientific overlap**; and
- potential **budgetary overlap/duplication**.

The CPOS Common Form instructions also state that a **separate submission** must be provided for:

- each proposal;
- each active project; and
- each reportable in-kind contribution.

There is **no page limitation** for the CPOS Common Form, although certain fields do have character limits.

### 5.4 What must be reported

The CPOS instructions and NIH Other Support page together establish that reportable support can include:

- resources and/or financial support from domestic and foreign entities;
- active and pending projects;
- reportable consulting activities;
- in-kind contributions; and
- foreign appointments/employment and related foreign activities/resources that fall within NIH reporting rules.

The NIH Other Support page also continues to state that broadly available **institutional core facilities or shared equipment** should not be included in Other Support; those belong in **Facilities and Other Resources** instead.

The same page also states that Other Support does **not** include:

- training awards;
- prizes; or
- true gifts where there is no expectation of time, services, specific research activities, money, or other return commitment.

### 5.5 Consulting: the current NIH trigger list

The newer CPOS instructions are more explicit than the older shorthand many institutions still use. NIH says consulting activities must be disclosed under the **proposals and active projects** section when **any** of the following are true:

- the consulting activity requires the senior/key person to **perform research**;
- the consulting activity does **not** involve performing research, but is related to the senior/key person's research portfolio and may affect funding, alter time or effort commitments, or otherwise affect scientific integrity; or
- the consulting entity provided a contract that requires the senior/key person to conceal or withhold confidential financial or other ties between the senior/key person and the entity.

### 5.6 In-kind contributions

The CPOS instructions require disclosure of in-kind contributions when they:

- have an estimated value of **$5,000 or more**; and
- require a **commitment of the individual's time**.

If there is **no associated time commitment**, the in-kind contribution does **not** need to be reported.

Examples of potentially reportable in-kind support include laboratory space, equipment, data or data sets, supplies, goods and services, and employee or student resources.

### 5.7 Supporting documentation for foreign appointments and employment

NIH's CPOS Common Form instructions say institutions must submit copies of contracts specific to senior/key-personnel **foreign appointments and/or employment** with a foreign institution for foreign activities and resources that are reported in CPOS. If those materials are not in English, recipients must provide **translated copies**.

The instructions also clarify an important exclusion: this requirement does **not** include **personal service contracts** or **employment contracts for fellows supported by foreign entities**.

Operationally, the supporting documentation is submitted through the relevant NIH module (for example, JIT, RPPR, or Prior Approval) rather than appended inside the SciENcv-generated CPOS PDF.

### 5.8 Who is generally excluded from Other Support reporting

The NIH Other Support page states that Other Support information is requested for all senior/key personnel in an application **except**:

- Program Directors, training faculty, and other individuals involved in the oversight of training grants; and
- individuals categorized as **Other Significant Contributors**.

In progress reports, NIH likewise excludes Program Directors, training faculty, and other individuals involved in the oversight of training grants from the listed Other Support reporting group.

### 5.9 Advanced NIH-specific CPOS edge cases

The current CPOS instructions also include several advanced cases that matter for some institutions:

- **Joint University / VA appointments:** entries should be organized by appointment, and reporting should use person-months rather than equivalent total professional effort.
- **Mentored Career Development Awards with subsumed effort:** the CPOS instructions provide specific wording for reporting complementary effort that is subsumed under the CDA.

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
- users should **not** print to PDF, flatten, optimize, or otherwise regenerate the file **unless the Application Guide or NOFO explicitly instructs a special submission format**; and
- the signature date must be within the past **12 months** when the document is submitted to NIH.

If anything changes in the document, or if the certification becomes too old, the correct fix is to go back into SciENcv, update the data, and **re-certify**. One official example of a special submission format is the **Participating Faculty Biosketches** attachment in certain training grant application workflows, where NIH instructs applicants to combine individually certified forms into a single PDF and flatten that compiled attachment for submission.

### 6.3 Why flattening is a real submission risk

NIH's Common Forms workflow depends on machine-readable data created by SciENcv. Flattening or re-printing the PDF can strip or damage the metadata NIH systems rely on to recognize the file as a compliant SciENcv-generated Common Form. The safe default is therefore **do not flatten** unless NIH's application instructions for a specific attachment explicitly tell you to do so after individual certification.

---

## Part VII: Common mistakes and edge cases

### 7.1 Treating the old February 6, 2026 date as current policy

This is no longer correct. The current official status is the leniency period through **May 2026**, with a later Guide Notice promised for the warning-to-error date.

### 7.2 Assuming CPOS always belongs in the initial application package

This is one of the most common workflow mistakes. NIH's Application Guide says not to include current and pending support at the application stage unless the NOFO says otherwise. Many NIH users will first need CPOS during **JIT** rather than initial submission.

### 7.3 Overstating the ORCID requirement

The official NIH/eRA requirement that can be verified directly is:

- obtain an **ORCID iD**; and
- link it to the **eRA Commons Personal Profile** so it appears correctly as the PID.

This appendix does not treat any additional account-linking step as an NIH validation requirement unless NIH or eRA explicitly states it.

### 7.4 Writing formal citations inside the supplement narrative boxes

The supplement instructions are explicit: **do not provide citations in the NIH Biographical Sketch Supplement**. Instead, use plain-language references to the products listed in the Common Form.

### 7.5 Under-reporting foreign relationships or consulting arrangements

The current NIH instructions are more detailed than older institutional summaries. Users should review the CPOS consulting trigger list and the foreign appointment/employment supporting-documentation rules directly when those situations apply.

### 7.6 Consortium and subaward workflows

In multi-site applications, the lead institution cannot rely on locally editing another institution's records. Each external senior/key person must ultimately provide their own compliant, certified SciENcv output for the lead site to assemble.

---

## Part VIII: Practical rollout recommendations for institutions

1. **Build biosketches early, but do not put CPOS on the critical path unless the mechanism and submission stage actually require it.**
2. **Verify ORCID-in-eRA first.** That is the documented NIH requirement that matters most for Common Forms identity.
3. **Select products before polishing narratives.** The supplement works best when the Personal Statement and Contributions to Science are written against a settled product list.
4. **Schedule certification windows close to submission.** Certification cannot be delegated.
5. **Re-check the official NIH and eRA pages quarterly.** The implementation timeline already changed once, and NIH has not yet published the final warning-to-error date.

---

## Selected official references used for this refresh

- NIH. *Common Forms for Biographical Sketch and Current and Pending (Other) Support*. Updated February 5, 2026. https://grants.nih.gov/policy-and-compliance/implementation-of-new-initiatives-and-policies/common-forms-for-biosketch
- NIH. *NOT-OD-26-018: NIH's Implementation of Common Forms for Biographical Sketch and Current and Pending (Other) Support for Due Dates on or after January 25, 2026*. Released December 2, 2025. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html
- NIH. *NOT-OD-26-033: Adjusted Timeline for NIH's Implementation of Common Forms*. Released February 4, 2026. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-033.html
- NIH. *Biographical Sketch Common Form*. Last updated January 12, 2026. https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form
- NIH. *NIH Biographical Sketch Supplement*. Last updated January 12, 2026. https://grants.nih.gov/grants-process/write-application/forms-directory/nih-biographical-sketch-supplement
- NIH. *Current and Pending (Other) Support (CPOS) Common Form*. Last updated January 12, 2026. https://grants.nih.gov/grants-process/write-application/forms-directory/cpos-common-form
- NIH. *Advice on Application Sections*. Accessed 2026-03-02. https://grants.nih.gov/grants-process/write-application/advice-on-application-sections
- NIH. *R&R Senior/Key Person Profile (Expanded) Form*. Accessed 2026-03-02. https://grants.nih.gov/grants/how-to-apply-application-guide/forms-i/general/g.240-r%26r-seniorkey-person-profile-%28expanded%29-form.htm
- NIH. *Other Support*. Last updated July 30, 2025. https://grants.nih.gov/grants-process/write-application/forms-directory/other-support
- eRA Commons. *The ORCID iD*. Revised February 17, 2026. https://www.era.nih.gov/erahelp/commons/PPF_Help/8_2_orcid.htm
- NIH. *Common Form for Biographical Sketch* (PDF instructions). Accessed 2026-03-02. https://grants.nih.gov/sites/default/files/Common%20Form%20NIH%20Biographical%20Sketch_FINAL.pdf
- NIH. *NIH Biographical Sketch Supplement* (PDF instructions). Accessed 2026-03-02. https://grants.nih.gov/sites/default/files/NIH%20Biographical%20Sketch%20Supplement_FINAL.pdf
- NIH. *Common Form for Current and Pending (Other) Support* (PDF instructions). Accessed 2026-03-02. https://grants.nih.gov/sites/default/files/Common%20Form%20NIH%20Current%20and%20Pending%20%28Other%29%20Support_FINAL.pdf
