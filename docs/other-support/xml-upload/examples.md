---
title: Examples + edge cases
parent: XML Upload & Automation
nav_order: 4
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

> Current in-kind: HPC cluster access (est. $30,000/year), received 10/2025, effort not known yet.

**Expected XML pattern:**
- `contributiontype` = `inkind`
- `supporttype` = `current`
- `projecttitle` and `awardnumber` can be empty
- `inkinddescription` describes the resource
- Emit `<personmonth year="2025"></personmonth>` even if effort is blank

## Example 3: Updating an existing entry by award number

**Update instruction:**

> Change award number R01 AA123456 title to "Revised Title" and mark as completed.

**Expected behavior:**
- Find the entry with matching `<awardnumber>`
- Overwrite the `projecttitle` and set `supporttype` to `completed`

## Example 4: Duplicate entries from merged sources

If both the PI and admin provide the same support item in PART 1, de-duplication should collapse them into one entry using:
- `awardnumber` (preferred)
- else `projecttitle + supportsource + startdate`

## Example 5: Missing effort

SciENcv can accept a file where effort values are blank, but **the year must still be present**. Use:

```xml
<commitment>
  <personmonth year="2026"></personmonth>
  <personmonth year="2027"></personmonth>
</commitment>
```
