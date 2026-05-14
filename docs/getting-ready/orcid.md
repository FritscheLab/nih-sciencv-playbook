---
title: ORCID setup (required links + PID check)
parent: Getting Ready (accounts + data)
nav_order: 1
---

# ORCID setup (required links + PID check)

**Required for NIH Common Forms:** link your **ORCID iD to your eRA Commons Personal Profile** so it can be used as the Persistent Identifier (PID).

**Required before submission:** confirm the **same ORCID iD** appears in the **Persistent Identifier (PID)** field of the SciENcv Common Form. NIH says this can be done by linking ORCID in MyNCBI/SciENcv, signing into SciENcv with ORCID, or manually entering the ORCID iD in the PID field.

{: .note }
> Missing the **eRA Commons** link can create NIH/eRA compliance problems. Missing the SciENcv PID can also fail Common Form validation if the ORCID in the PDF does not match the ORCID linked to the eRA Commons credential used in the submission.

## Steps (PI does this)

1. Create ORCID: <https://orcid.org/register>
2. In **eRA Commons**: **Personal Profile → ORCID ID** → connect (**required**)
3. In **MyNCBI/SciENcv**: either link ORCID in **Account Settings → Linked Accounts**, sign in using ORCID, or manually enter the ORCID iD in the Common Form PID field
4. In **SciENcv**, confirm the ORCID shown as the **Persistent Identifier (PID)** matches the ORCID linked in **eRA Commons**.

```mermaid
flowchart TD
    accTitle: ORCID linking and PID check
    accDescr: The ORCID path connects one ORCID iD to eRA Commons and then confirms the same identifier appears in the SciENcv Common Form PID field.
    A["Create or use existing ORCID iD"] --> B["Connect ORCID in eRA Commons Personal Profile"]
    B --> C["Open MyNCBI / SciENcv"]
    C --> D{"ORCID appears as SciENcv PID?"}
    D -- "Yes, and it matches eRA" --> E["Ready for Common Forms"]
    D -- "No" --> F["Link ORCID in MyNCBI, sign in with ORCID, or enter PID manually"]
    F --> D
```

![ORCID linking placeholder]({{ "/assets/images/placeholder-orcid-linking.svg" | relative_url }})
