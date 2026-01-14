---
title: Original long-form guide (source)
parent: Appendix
nav_order: 1
---

# Original long-form guide (source)

This page contains the original long-form source document that this site reorganizes.

---

# **The Comprehensive Implementation Guide to the 2026 NIH Common Forms: SciENcv Workflows, Strategic Compliance, and Technical Architecture**

## **Executive Summary: The Structural Transformation of Federal Research Disclosure**

The United States federal research enterprise is undergoing its most significant administrative transformation in decades. Effective January 25, 2026, the National Institutes of Health (NIH) will mandate the use of "Common Forms" for Biographical Sketches and Current and Pending (Other) Support.1 This shift is not merely a cosmetic update to form templates; it represents the operationalization of the National Security Presidential Memorandum 33 (NSPM-33), a directive aimed at harmonizing disclosure requirements across federal funding agencies to strengthen research security and standardize data collection.1

For the research administrator, the principal investigator (PI), and the compliance officer, this mandate forces a migration from static, manually edited Word documents to a dynamic, database-driven ecosystem centered on the Science Experts Network Curriculum Vitae (SciENcv).2 The "Common Form" architecture bifurcates the traditional biosketch into two distinct components: a standardized federal profile (The Biographical Sketch Common Form) and an agency-specific qualitative supplement (The NIH Biographical Sketch Supplement).2 This report serves as an exhaustive, expert-level guide to navigating this transition. It dissects the technical requirements of the digital identity infrastructure, details the granular mechanics of form creation within SciENcv, and analyzes the strategic implications of the new content constraints.

The stakes of this transition are high. The NIH has signaled a strict enforcement regime: initial warnings for non-compliance will rapidly escalate to hard stops (errors) by February 6, 2026, preventing the submission of applications that fail to utilize the certified SciENcv output.6 Furthermore, the requirement for personal digital certification by the PI—explicitly prohibiting delegation of the final signature—introduces a new critical path in the proposal submission timeline that institutions must account for immediately.2

---

**Part I: The Policy Landscape and the Architecture of Harmonization**

To effectively manage the transition to the Common Forms, one must understand the underlying logic of the "Common Disclosure" initiative. The previous system, characterized by agency-specific formats (NIH, NSF, DoD), created administrative burden and ambiguity regarding disclosure overlaps. The OSTP’s guidance on the implementation of NSPM-33 sought to resolve this by creating a single, interoperable data standard.1

### **1.1 The Bifurcated Document Model**

The fundamental innovation of the 2026 mandate is the separation of "identity data" from "qualitative assessment." Under the legacy format (Form H and prior), a biosketch was a single document containing both the researcher's employment history and their narrative contributions to science. The new architecture splits these functions to allow for cross-agency portability of the data.

#### **1.1.1 The Biographical Sketch Common Form**

The Common Form is the federal standard. It is designed to be "agency-agnostic" to a degree, holding the verifiable facts of a researcher's career. Its primary components—Professional Preparation (education), Appointments, and Products—are structured to allow data portability. If a researcher applies to the National Science Foundation (NSF) and later to the NIH, the core data residing in the Common Form remains consistent, reducing the need for re-entry.3 This document is heavily regulated by character limits and field definitions agreed upon by the National Science and Technology Council (NSTC).

#### **1.1.2 The NIH Biographical Sketch Supplement**

Recognizing that the generic Common Form could not capture the nuance required for biomedical peer review, the NIH introduced the "Supplement." This is a purely qualitative document that appends to the Common Form. It houses the "Personal Statement," "Contributions to Science," and "Honors".4 This separation is crucial for systems architecture: the Common Form handles the *data* (who you are, what you produced), while the Supplement handles the *argument* (why you are qualified, how you impacted the field).

### **1.2 Timeline and Enforcement Mechanisms**

The transition timeline is rigid and binary, centered on the implementation date of January 25, 2026\.

| Submission Type | Due Date | Required Format |
| :---- | :---- | :---- |
| **Grant Application** | On or before Jan 24, 2026 | Legacy NIH Biosketch Format |
| **Grant Application** | On or after Jan 25, 2026 | Common Form \+ NIH Supplement (via SciENcv) |
| **RPPR (Progress Report)** | Submitted on or after Jan 25, 2026 | Common Form \+ NIH Supplement (via SciENcv) |
| **Just-in-Time (JIT)** | Submitted on or after Jan 25, 2026 | Common Form \+ NIH Supplement (via SciENcv) |
| **Prior Approval Request** | Submitted on or after Jan 25, 2026 | Common Form \+ NIH Supplement (via SciENcv) |

2

It is critical to note the implication for ongoing awards. A grant awarded in 2024 using the legacy biosketch format will require the conversion of all Key Personnel biosketches to the new Common Form format for its 2026 RPPR.3 This creates a massive "technical debt" for institutions, as hundreds or thousands of active biosketches must be migrated to SciENcv before the Spring 2026 progress report cycle begins.

The enforcement mechanism is automated within the eRA Commons validation layer.

* **Phase 1 (Jan 25 – Feb 5, 2026):** Submissions using incorrect forms or lacking proper ORCID links will generate a **Warning**. The application will proceed to review, but the warning serves as a final notice.6  
* **Phase 2 (Feb 6, 2026 onwards):** The warning elevates to an **Error**. eRA systems will reject the application package entirely if the XML validation fails to detect the specific metadata tags present in a certified SciENcv PDF.6

---

**Part II: The Digital Identity Infrastructure**

The successful generation of a Common Form Biosketch is the final step in a data supply chain that begins outside of the NIH. The system relies on a "triad" of digital identity platforms: **ORCID** (the persistent identifier), **eRA Commons** (the agency portal), and **MyNCBI/SciENcv** (the generator). If the connections between these three nodes are not established and maintained, the SciENcv interface will fail to populate, forcing error-prone manual entry.

### **2.1 ORCID: The Backbone of Professional Preparation**

The Open Researcher and Contributor ID (ORCID) has evolved from a recommended best practice to a mandatory compliance tool. For the Common Form, the ORCID iD is not just a label; it is a data source. The NIH explicitly requires that the ORCID iD be displayed in the "Persistent Identifier" section of the Common Form, and SciENcv is programmed to pull education and employment data directly from the ORCID registry.2

#### **2.1.1 Establishing and Curating the ORCID Record**

Researchers must treat their ORCID profile as a legal document.

1. **Registration:** The investigator must register for an ORCID iD at orcid.org. This is a one-time process yielding a unique 16-digit identifier.9  
2. **Data Population (The "Works" Section):** To facilitate the "Products" section in the biosketch, investigators should populate their ORCID "Works" section. The most efficient method is the "Search & Link" wizard, which connects ORCID to trusted databases like Scopus, CrossRef, or Europe PMC. This allows for the bulk import of publication metadata (DOI, PMID, Journal Title) into the ORCID record.9  
   * *Strategic Insight:* Populating ORCID prevents the need to manually type citation data into SciENcv later. It also ensures that the metadata is standardized, reducing the risk of citation errors in the grant application.  
3. **Data Population (Employment and Education):** The "Professional Preparation" section of the Common Form draws heavily from ORCID. Users should ensure that their degree dates, institution names, and locations are accurate in ORCID to ensure a clean import.10

#### **2.1.2 The "Double Handshake" Requirement**

A frequent point of failure in the setup process is the confusion between linking ORCID to eRA Commons versus linking it to SciENcv. **These are two separate technical actions, and both are required.**

* **Handshake 1: ORCID to eRA Commons:** This link validates the researcher's identity to the funding agency.  
  * *Action:* The PI logs into eRA Commons \-\> Personal Profile \-\> ORCID ID section \-\> "Create or Connect your ORCID iD." This authorizes NIH to read the ORCID record.9  
  * *Consequence:* Without this link, the application will trigger a validation error upon submission.7  
* **Handshake 2: ORCID to SciENcv:** This link allows the SciENcv tool to "read" the data to build the form.  
  * *Action:* The PI logs into MyNCBI \-\> Account Settings \-\> Linked Accounts \-\> "Add Account" \-\> Search for ORCID \-\> Authorize.11  
  * *Consequence:* Without this link, the "External Source" feature in SciENcv will be disabled, forcing manual data entry.10

### **2.2 MyNCBI and My Bibliography: The Citation Engine**

While ORCID handles bio-data well, **My Bibliography** (a tool within MyNCBI) remains the definitive source for managing NIH-compliant citations. This is particularly important for verifying compliance with the NIH Public Access Policy (the requirement that NIH-funded papers be deposited in PubMed Central).

#### **2.2.1 Configuring My Bibliography**

The "Products" section of the Common Form allows for citations to be pulled from My Bibliography.

* **Populating from PubMed:** Users should log into My Bibliography and use the "Add from PubMed" search feature. This retrieves the official NLM metadata, including the PMCID status.  
* **Handling Non-Journal Products:** The Common Form encourages the listing of non-paper products (software, datasets, protocols). These must be added to My Bibliography manually using the "Add Citation \-\> Manual" or "Upload RIS" feature.  
  * *Strategic Insight:* For PIs with extensive non-standard outputs (e.g., engineers or data scientists), leveraging the RIS upload from reference managers like EndNote is significantly faster than manual entry.9

---

**Part III: The Biographical Sketch Common Form – Technical Execution**

Once the digital infrastructure is linked, the creation of the document occurs within SciENcv. This section details the technical execution of the **Common Form** component, analyzing the specific constraints and strategies for each field.

### **3.1 Creating the Document Container**

1. **Access:** The user (or delegate) navigates to the "Manage SciENcv" dashboard.  
2. **Initiation:** Click "Create New Document."  
3. **Metadata:**  
   * **Document Name:** Assign a recognizable title (e.g., "Jones\_R01\_Resub\_2026").  
   * **Format Selection:** Select **"NIH Biosketch"** (or "Biographical Sketch Common Form" depending on the specific SciENcv interface update version).  
   * **Data Source:** Select **"External source: ORCID"**. This triggers the system to pull the Professional Preparation and Appointments data immediately, populating the shell.10

### **3.2 Section 1: Professional Preparation (Formerly Education)**

This section replaces the "Education/Training" block. It is a structured table of degrees and training.

* **Data Flow:** If the ORCID link was selected, this table populates automatically.  
* **Manual Intervention:** The user must review the import. Common issues include duplicate entries for the same degree (e.g., "PhD" and "Ph.D.") or missing completion dates. These can be edited directly in the SciENcv interface using the "Edit" pencil icon.  
* **Scope:** Unlike the old form, which focused primarily on degrees, "Professional Preparation" in the Common Form syntax is broad enough to include postdoctoral training, which should be listed here rather than in "Positions" if it was a training role.2

### **3.3 Section 2: Appointments and Positions**

This section is the primary audit log for Conflict of Commitment. The Common Form requirement is more rigorous than previous iterations.

* **Requirement:** Users must list **all** domestic and foreign professional appointments and positions. This includes:  
  * Academic appointments.  
  * Industry roles.  
  * Non-profit board memberships (if professional).  
  * Foreign honorary titles or adjunct positions.  
* **Lookback Period:** The form requires positions held outside the primary organization for up to three years prior to the application.5  
* **Technical Execution:** SciENcv pulls this from ORCID or existing profiles. The user must ensure *completeness*. Omitting a foreign affiliation here, even an unpaid one, can be grounds for an investigation into undisclosed foreign support.2

### **3.4 Section 3: Products (The Strategic Pivot)**

The "Products" section represents the most drastic change in grantsmanship strategy. The previous allowance (up to 4 citations per contribution \+ 4 in personal statement \= \~24 citations) has been slashed to a strict **10 products total**.

The section is divided into two rigid buckets:

#### **3.4.1 Bucket A: Products Most Closely Related to the Proposed Project**

* **Limit:** Up to 5 citations.  
* **Function:** These are the *only* citations that can be referenced in the Personal Statement (located in the Supplement).  
* **Strategy:** Selection here is not just about "best papers"; it is about "evidentiary papers." If the Personal Statement claims the PI has expertise in *Technique X*, there must be a paper in this bucket demonstrating *Technique X*.  
* **Technical Step:** In SciENcv, the user clicks "Select citations," which opens a window to My Bibliography. The user checks up to 5 boxes. These are then frozen into this section.5

#### **3.4.2 Bucket B: Other Significant Products**

* **Limit:** Up to 5 citations.  
* **Function:** These serve as the evidentiary basis for the "Contributions to Science" section in the Supplement.  
* **Strategy:** This requires a "portfolio approach." Since the user can no longer list 4 papers for *each* contribution, these 5 papers must represent the breadth of the investigator's career. A common strategy is to select one "landmark" paper for each of the 5 Contributions described in the Supplement.1

---

**Part IV: The NIH Biographical Sketch Supplement – Narrative Strategy**

While the Common Form is data-centric, the Supplement is narrative-centric. This document is appended to the Common Form in the final PDF output but is edited in a separate tab or section within the SciENcv interface.6

### **4.1 The Personal Statement (No Citations Allowed)**

* **Constraint:** Maximum **3,500 characters** (including spaces).15  
* **The Citation Ban:** The text field in SciENcv does not support linking or footnotes. The instructions explicitly state **"No citations allowed"** in the text.2  
* **Writing Strategy:** The narrative must use referential language. Instead of writing "Recent work shows X (Doe et al., 2024)," the investigator must write "As demonstrated in the products closely related to the proposed project..." or "My recent analysis of X (see Product 1\) established that..."  
  * *Implication:* This forces the Personal Statement to be strictly tightly coupled with the "Closely Related Products" list. You cannot discuss a finding if the supporting paper isn't one of the 5 listed in the Common Form section.2  
* **Content Focus:** The statement must address suitability for the *specific* project. With the character limit, generic biographical fluff must be excised. Focus on technical expertise, leadership of similar projects, and access to resources.16

### **4.2 Contributions to Science**

* **Constraint:** Maximum **5 contributions**. Each contribution is limited to **2,000 characters**.1  
* **Structure:**  
  1. **Header:** A short title (e.g., "Development of Novel Kinase Inhibitors").  
  2. **Narrative:** A description of the problem, the finding, and the impact.  
  3. **Reference:** A sentence linking the contribution to the "Other Significant Products" list. e.g., "This body of work is exemplified by the foundational study listed as Product \#3 in the Other Significant Products section.".5  
* **Strategic Adjustment:** In the legacy format, PIs often used the "Contributions" section to list distinct bodies of work with separate citation lists. Now, with only 5 "Significant Products" allowed *total* (in the Common Form), the Contributions narrative must be written to highlight the impact of those specific 5 products. It reduces the ability to claim "breadth" via volume of citations; breadth must now be established via the narrative description of impact.1

### **4.3 Honors**

* **Constraint:** Maximum **15 entries**.8  
* **Location:** Moved from the main biosketch to the Supplement.  
* **Selection:** SciENcv may pull dozens of awards from ORCID. The user (or delegate) must curate this list down to the top 15 most relevant honors. Prioritize national/international awards over internal institutional grants or travel awards.

---

**Part V: The Delegate Workflow and Digital Certification**

A massive operational shift in the 2026 mandate is the restriction on who can finalize the document. The workflow transforms from a solitary administrative task to a collaborative digital handshake.

### **5.1 The Role of the Delegate (Administrator)**

NIH policy and federal law prohibit anyone other than the account holder from logging in with their credentials. Therefore, research administrators must be assigned as **Delegates** to legally access and edit a PI's SciENcv profile.

#### **5.1.1 Establishing Delegation**

1. **PI Action:** The PI logs into their MyNCBI account \-\> Account Settings \-\> Delegates \-\> "Add a Delegate."  
2. **Input:** The PI enters the administrator’s email address.  
3. **Confirmation:** The administrator receives an email. They must click the link and log in to their *own* MyNCBI account to accept the delegation.18  
   * *Best Practice:* PIs should grant delegation rights for both **SciENcv** (to build the form) and **My Bibliography** (to curate the citations). Without the latter, the delegate cannot fix missing PMCID problems or add new papers to the "Select Citations" window.19

#### **5.1.2 What the Delegate Can Do**

* Create new documents.  
* Import data from ORCID/eRA.  
* Select citations for the "Products" sections.  
* Copy/paste text into the Personal Statement and Contributions fields.  
* Check for errors (e.g., character count overflows).

#### **5.1.3 What the Delegate Cannot Do**

* **Certify the Document.** The "Certify" button is physically hidden or disabled when viewing a profile as a delegate.8  
* **Sign the MFTRP Statement.** The certification includes a legal attestation regarding Malign Foreign Talent Recruitment Programs. This requires the principal's direct action.2

### **5.2 The Certification Workflow (The PI's Responsibility)**

The workflow must be designed to accommodate the PI's intervention at the final stage.

1. **Drafting:** The Delegate builds the biosketch in SciENcv.  
2. **Notification:** The Delegate notifies the PI (via email/Slack) that "The Jones R01 Biosketch is ready for certification."  
3. **PI Access:** The PI logs into SciENcv.  
4. **Review:** The PI reviews the PDF preview.  
5. **Certification:** The PI clicks the **"Certify"** button at the bottom of the screen.  
   * *System Action:* This applies a digital signature, a timestamp, and locks the dataset.  
6. **Download:** The PI (or the delegate, *after* certification) downloads the PDF.2

**Critical Warning \- The "Flattening" Error:** Administrators must never "print to PDF" or "flatten" the certified biosketch. The file generated by SciENcv contains invisible XML metadata that the eRA Commons machine-reading software uses to validate the form. If the PDF is flattened, the XML is stripped, and the application will be rejected with a "Form System Error".2

---

**Part VI: Migration and Transition Strategy**

Institutions face a "bulk migration" challenge. Every active researcher will need a new biosketch for their first proposal or RPPR in 2026\.

### **6.1 Migrating from Legacy SciENcv Profiles**

If a PI already has a biosketch in SciENcv (old format):

1. **Create New:** Select "Biographical Sketch Common Form."  
2. **Source:** Select **"Start with existing document"** and choose the old biosketch.  
3. **The Mapping Gap:**  
   * *Education/Positions:* These map relatively well.  
   * *Citations:* The old form likely had \~20 citations. The new form allows 10\. The system will not know which 10 to pick. The user must manually deselect citations to meet the 5+5 limit.  
   * *Narratives:* The user must edit the Personal Statement and Contributions to remove any inline citations (e.g., "(1)") that were present in the old text, as these are now prohibited.1

### **6.2 Migrating from Word Documents**

For PIs who have never used SciENcv:

1. **No Direct Import:** There is no way to upload a Word doc and have it parse.  
2. **Step 1:** Populate ORCID first (as described in Part II). This handles the data entry for Education/Positions.  
3. **Step 2:** Populate My Bibliography with the citations from the Word doc.  
4. **Step 3:** Copy/Paste the narratives from Word into the SciENcv text boxes.  
   * *Warning:* Word often hides special characters (smart quotes, em-dashes) that count strangely in web forms. Always check the character count *inside* SciENcv after pasting.15

---

**Part VII: Troubleshooting and Edge Cases**

### **7.1 Common Validation Errors**

| Error Message | Root Cause | Solution |
| :---- | :---- | :---- |
| **"Invalid Form Format"** | PDF was flattened or printed. | Download the original certified PDF from SciENcv again. Do not save as "Optimized PDF." 2 |
| **"Missing Persistent Identifier"** | ORCID iD field is blank. | PI must link ORCID in their eRA Commons profile AND in the SciENcv profile settings. 6 |
| **"Certification Required"** | Document submitted without PI signature. | PI must log in to SciENcv and click the "Certify" button; delegate cannot do this. 8 |
| **"Character Limit Exceeded"** | Text includes hidden HTML or Word formatting. | Paste text into Notepad (plain text) first, then into SciENcv to strip formatting. 15 |

### **7.2 The Consortium/Subaward Problem**

In multi-site grants, the lead institution needs biosketches from sub-sites.

* **The Challenge:** The lead institution's administrator cannot delegate into the sub-site PI's account.  
* **The Workflow:** The sub-site PI must generate and certify their own biosketch in their own SciENcv account. They then email the certified PDF to the lead institution.  
* **Verification:** The lead administrator should open the PDF and check for the digital certification timestamp before bundling it into the application.2

### **7.3 Malign Foreign Talent Recruitment Programs (MFTRP)**

The Common Form includes a specific checkbox or attestation regarding MFTRP.

* **Definition:** These are foreign-state-sponsored programs designed to acquire US technologies.  
* **Liability:** By certifying the biosketch, the PI is making a federal statement that they are not a party to such a program. This creates False Claims Act liability.  
* **Institutional Review:** Many institutions are implementing internal "attestation forms" that PIs must sign *before* they certify in SciENcv, ensuring the institution has a record of the disclosure review.2

---

**Part VIII: Strategic Recommendations for Grantsmanship**

The structural constraints of the Common Form necessitate a change in how researchers sell their expertise.

1. **The "Anchor Paper" Strategy:** With only 5 "Other Significant Products" available to support 5 "Contributions to Science," researchers should select one definitive "anchor paper" for each contribution area. The narrative should explicitly name this product (e.g., "See Product 3") to create a verifiable link between the claim and the evidence.5  
2. **Front-Loading Impact:** In the Personal Statement, since citations are banned, the first paragraph must immediately establish credibility using the "Closely Related Products" as a foundation. "My expertise in \[Field\] is evidenced by the foundational work listed in the Closely Related Products section..."  
3. **Utilizing the "Product" Definition:** The Common Form allows for "Products," not just "Publications." If a software tool, patent, or dataset is highly relevant to the grant, it should replace a mid-tier journal article in the "Closely Related" section. This signals practical capability to the reviewers.1

---

**Part IX: Conclusion**

The implementation of the NIH Common Forms represents a definitive shift toward a digital, interoperable, and secure research ecosystem. While the initial learning curve for SciENcv and the certification workflow is steep, the long-term benefit is a standardized data environment that reduces redundancy and enhances compliance.

For the January 2026 deadline, the path to success lies in preparation: establishing ORCID links now, cleaning up My Bibliography data immediately, and socializing the "PI Certification" requirement well in advance of the first deadline. By treating the biosketch not as a document to be typed, but as a dataset to be managed, the research community can navigate this transition with minimal disruption to the scientific mission.

#### **Works cited**

1. NIH's Implementation of Common Forms for Biographical Sketch and Current and Pending (Other) Support for Due Dates on or after January 25, 2026., accessed January 13, 2026, [https://osr.ucsf.edu/news/nihs-implementation-of-common-forms-for-biographical-sketch-and-current-and-pending-other-support](https://osr.ucsf.edu/news/nihs-implementation-of-common-forms-for-biographical-sketch-and-current-and-pending-other-support)  
2. NOT-OD-26-018: NIHs Implementation of Common Forms for Biographical Sketch and Current and Pending (Other) Support for Due Dates on or after January 25, 2026 \- NIH Grants and Funding, accessed January 13, 2026, [https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html)  
3. Common Forms for Biographical Sketch and Current and Pending (Other) Support | Grants & Funding, accessed January 13, 2026, [https://grants.nih.gov/policy-and-compliance/implementation-of-new-initiatives-and-policies/common-forms-for-biosketch](https://grants.nih.gov/policy-and-compliance/implementation-of-new-initiatives-and-policies/common-forms-for-biosketch)  
4. NOT-OD-24-163: NIHs Adoption of Common Forms for Biographical Sketch and Current and Pending (Other) Support by May 25, 2025, accessed January 13, 2026, [https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-163.html](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-163.html)  
5. NIH Biographical Sketch Format \- Office of Sponsored Research \- UCSF, accessed January 13, 2026, [https://osr.ucsf.edu/nih-biographical-sketch-format](https://osr.ucsf.edu/nih-biographical-sketch-format)  
6. Biographical Sketch Common Form | Grants & Funding, accessed January 13, 2026, [https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form](https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form)  
7. NIH Announces January 25, 2026 Implementation Date for Common Forms (NOT-OD-26-018) \- National Training Grant Community of Practice, accessed January 13, 2026, [https://ntgcop.org/news/715957/NIH-Announces-January-25-2026-Implementation-Date-for-Common-Forms-NOT-OD-26-018.htm](https://ntgcop.org/news/715957/NIH-Announces-January-25-2026-Implementation-Date-for-Common-Forms-NOT-OD-26-018.htm)  
8. NIH Implementation of the Common Forms for Biosketches and Current and Pending (Other) Support \- Effective January 25, 2026, accessed January 13, 2026, [https://ora.stanford.edu/resources/disclosure-resources/national-institutes-health-nih/nih-implementation-common-forms](https://ora.stanford.edu/resources/disclosure-resources/national-institutes-health-nih/nih-implementation-common-forms)  
9. SCiENcv & Common Forms \- Research Support \- Yale University, accessed January 13, 2026, [https://research-support.yale.edu/sponsored-projects/office-of-sponsored-projects/policies-compliance/sciencv-common-forms](https://research-support.yale.edu/sponsored-projects/office-of-sponsored-projects/policies-compliance/sciencv-common-forms)  
10. SciENcv: Integrating with ORCID \- YouTube, accessed January 13, 2026, [https://www.youtube.com/watch?v=G\_cKSRr7TJ4](https://www.youtube.com/watch?v=G_cKSRr7TJ4)  
11. accessed January 13, 2026, [https://ora.stanford.edu/sciencv](https://ora.stanford.edu/sciencv)  
12. Creating Biosketches using SciENcv, accessed January 13, 2026, [https://rcra.emory.edu/\_includes/documents/sections/research-security/sciencv-epc-flyer.pdf](https://rcra.emory.edu/_includes/documents/sections/research-security/sciencv-epc-flyer.pdf)  
13. Using SciENcv and ORCID to Create Your Biosketch Common Form | NC State University Libraries, accessed January 13, 2026, [https://www.lib.ncsu.edu/sciencv-for-biosketches](https://www.lib.ncsu.edu/sciencv-for-biosketches)  
14. Common Forms Overview & SciENcv Introduction \- Research Support, accessed January 13, 2026, [https://research-support.yale.edu/sites/default/files/2025-04/Common\_Forms\_Overview\_%26\_SciENcv\_Introduction\_Survey-February\_13\_2025.pdf](https://research-support.yale.edu/sites/default/files/2025-04/Common_Forms_Overview_%26_SciENcv_Introduction_Survey-February_13_2025.pdf)  
15. NIH Common Form Biosketch & Biosketch Supplement | Office of Research Administration, accessed January 13, 2026, [https://ora.stanford.edu/resources/disclosure-resources/national-institutes-health-nih/nih-common-form-biosketch-biosketch](https://ora.stanford.edu/resources/disclosure-resources/national-institutes-health-nih/nih-common-form-biosketch-biosketch)  
16. Create Biosketches | NIAID: National Institute of Allergy and Infectious Diseases, accessed January 13, 2026, [https://www.niaid.nih.gov/grants-contracts/create-biosketches](https://www.niaid.nih.gov/grants-contracts/create-biosketches)  
17. NIH Biographical Sketch Supplement\_PREVIEW\_DO NOT USE, accessed January 13, 2026, [https://grants.nih.gov/sites/default/files/NIH%20Biographical%20Sketch%20Supplement\_PREVIEW.pdf](https://grants.nih.gov/sites/default/files/NIH%20Biographical%20Sketch%20Supplement_PREVIEW.pdf)  
18. Using SciENcv Frequently Asked Questions \- National Science Foundation, accessed January 13, 2026, [https://nsf-gov-resources.nsf.gov/files/SciENcvFAQs.pdf](https://nsf-gov-resources.nsf.gov/files/SciENcvFAQs.pdf)  
19. Adding Delegates to SciENcv \- Office of Sponsored Programs, accessed January 13, 2026, [https://osp.gatech.edu/sites/default/files/inline-files/Adding%20Delegates%20to%20SciENcv.pdf](https://osp.gatech.edu/sites/default/files/inline-files/Adding%20Delegates%20to%20SciENcv.pdf)  
20. SciENcv: How to Prepare and Edit NSF and NIH Biosketches and NSF Current and Pending documents Part 1, Creating and Populati \- University of Colorado Boulder, accessed January 13, 2026, [https://www.colorado.edu/ocg/media/126](https://www.colorado.edu/ocg/media/126)  
21. NIH's Implementation of Common Forms for Biographical Sketch and Current and Pending (Other) Support | Research | WashU, accessed January 13, 2026, [https://research.washu.edu/announcements/nihs-implementation-of-common-forms-for-biographical-sketch-and-current-and-pending-other-support/](https://research.washu.edu/announcements/nihs-implementation-of-common-forms-for-biographical-sketch-and-current-and-pending-other-support/)
