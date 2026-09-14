---
type: Runbook
title: Revenue recording
description: Exporting itemised revenue from Pestroutes, formatting it through the upload template, and posting it as a monthly journal entry.
tags: [quickbooks, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1TVPwsmAcJRZxKPxrxd8GqldwkO0oME_ylQnGnfjuDkE
    resource: https://docs.google.com/document/d/1TVPwsmAcJRZxKPxrxd8GqldwkO0oME_ylQnGnfjuDkE/edit
    title: Recording of revenue from Pestroutes
status: draft
---

Revenue moves from Pestroutes to QuickBooks through a formatting spreadsheet rather than directly.
Run once per branch.

# 1. Itemise the revenue

**In Pestroutes:** Reporting → **Billing by Service Type** → date range → the branch →
**Export to Excel**.

**Set up the working copy:**

1. Open the **Revenue Invoice Format for Upload to Quickbooks** template.
2. **File → Make a copy**, saved into the correct month's End-of-Month folder.
3. Rename the month tabs in the copy.
4. Paste the exported data into the **`(Month)-Pestroutes`** tab. **Do not edit column J.**
5. Enter the branch per line item in **column I**.
6. **The check: cell `B1` on the Pestroutes tab should read `0`.** That is the validation — a
   non-zero value means the paste or the branch tagging is wrong.
7. On the **`(Month)-For Upload`** tab, update the month name in column A and set the dates in
   columns C and D to the **last day of the month being closed**.

# 2. Post the journal entry

**QuickBooks → New → Journal entry.**

| Field | Value |
|---|---|
| Journal date | last day of the month being closed |
| Journal number | `(Month) Sales Invoice` |

Enter the data from the **`(Month)-For Upload`** tab.

> **This is a manual re-key, not an import.** The template produces upload-formatted rows, and the
> [corporate class proration](/finance/corporate-class-proration.md) procedure shows QuickBooks
> does support CSV journal import via **Gear → Import Data**. Whether revenue is typed by hand
> deliberately or just never switched over is not stated — but the tab is literally named
> *For Upload*, which suggests import was the intent.

> The source's step 2 says to enter the data "based on the data appearing on Number 7" while its own
> step 7 is the *For Upload* tab reference in step 1. The numbering is off by one section; the
> intent is clear.

# Related

- [Accounts receivable close](/finance/accounts-receivable-close.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
