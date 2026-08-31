---
title: Examples + edge cases
parent: XML Upload & Automation
nav_order: 5
---

# Examples + edge cases

## Example 1: Multi-year award with a single annual effort value

**Input (messy):**

> New pending R01, title ... start 07/2026 end 06/2030, ... effort 1.2 calendar months per year, amount $1,200,000, overlap none.

**Expected XML pattern:**
- `supporttype` = `pending`
- `contributiontype` = `award`
- `startdate` = `2026-07-01`
- `enddate` = `2030-06-01`
- `<personmonth year="2026">1.2</personmonth>` through `2030` (inclusive)

## Example 2: In-kind computing resource with unknown end date

**Input:**

> Current in-kind: HPC cluster access provided as a non-cash contribution by an external entity, not intended for use on the project or proposal for which this disclosure is being submitted (est. $30,000/year), received 10/2025. The contribution requires the individual's time, but the person-month amount is not yet quantified.

**Expected XML pattern:**
- `contributiontype` = `inkind`
- `supporttype` = `current`
- Confirm it is not a broadly available institutional core or shared resource
- `projecttitle` and `awardnumber` can be empty
- `inkinddescription` describes the resource
- If the resource were intended for that project or proposal, it would be routed to Facilities & Other Resources or Equipment instead of CPOS in-kind
- Emit `<personmonth year="2025"></personmonth>` even if effort is blank

## Example 3: Updating a uniquely identified existing entry

**Update instruction:**

> For the University A / NIH entry with award number R01 AA123456, start date 2024-07-01, and current title "Original Title," change the title to "Revised Title" and note that the project ended before the CPOS snapshot date.

**Expected behavior:**
- Find the single entry matching the award number, source, start date, and prior title
- Overwrite the `<projecttitle>`
- Do **not** invent a `completed` status (valid values are only `current` or `pending`)
- If the project is no longer current or pending as of the CPOS reporting date, **remove it from the CPOS upload** rather than changing `supporttype`

## Example 4: Duplicate entries from merged sources

If both the PI and admin provide the same support item in PART 1, collapse it only when a composite identity matches:

- with an award number: `awardnumber + projecttitle + supportsource + startdate`
- without an award number: `projecttitle + supportsource + location + startdate`

Do not merge on award number alone. Consortium subprojects and multi-project components can share the overall award number; preserve distinct entries and review collisions.

## Example 5: Missing effort

SciENcv can accept a file where effort values are blank, but **the year must still be present**. If the effort is truly zero, use `0`; if it is unknown or not ready for upload, leave the value blank and resolve it in SciENcv.

```xml
<commitment>
  <personmonth year="2025">0</personmonth>
  <personmonth year="2026"></personmonth>
  <personmonth year="2027"></personmonth>
</commitment>
```

## Example 6: Full XML file (dummy data)

This is a complete, valid file using the simple upload template with one award entry.

```xml
<?xml version="1.0" encoding="utf-8"?>
<profile>
  <identification>
    <id idtype="orcid">0000-0002-1825-0097</id>
    <account accounttype="eRA-Commons">JDOE1</account>
    <name>
      <firstname>Jane</firstname>
      <middlename>Marie</middlename>
      <lastname>Doe</lastname>
    </name>
  </identification>
  <employment>
    <position>
      <positiontitle>Senior Researcher</positiontitle>
      <organization>
        <orgname>Science &amp; Technology Inst</orgname>
        <city>Ann Arbor</city>
        <stateorprovince>MI</stateorprovince>
        <country>USA</country>
      </organization>
      <startdate><year>2015</year></startdate>
    </position>
  </employment>
  <funding>
    <support>
      <projecttitle>Advanced Study of Polymer Dynamics</projecttitle>
      <awardnumber>NSF-2026-5589</awardnumber>
      <supportsource>National Science Foundation</supportsource>
      <location>University of Michigan</location>
      <contributiontype>award</contributiontype>
      <awardamount>150000</awardamount>
      <inkinddescription>None</inkinddescription>
      <overallobjectives>To investigate the long-term stability of biodegradable plastics.</overallobjectives>
      <potentialoverlap>None.</potentialoverlap>
      <startdate>2026-01-01</startdate>
      <enddate>2027-12-31</enddate>
      <supporttype>current</supporttype>
      <commitment>
        <personmonth year="2026">3.5</personmonth>
        <personmonth year="2027">3.5</personmonth>
      </commitment>
    </support>
  </funding>
</profile>
```
