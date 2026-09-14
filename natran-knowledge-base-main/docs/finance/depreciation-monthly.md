---
type: Runbook
title: Booking monthly depreciation
description: Reading the month's change in the auto loan accounts by branch and posting the depreciation journal entry.
tags: [quickbooks, bookkeeping, vehicles]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1NNAMKjsxiJeWaL5yuPsT9hAXto7gFvVo1q3AMoRJhc4
    resource: https://docs.google.com/document/d/1NNAMKjsxiJeWaL5yuPsT9hAXto7gFvVo1q3AMoRJhc4/edit
    title: How to Book Depreciation every month| Natran
status: draft
---

**Natran and Advantage Pro Services both depreciate over five years, following the vehicle's loan
amortization.**

> **Book depreciation only after every payment for the month being closed has been posted.** The
> figure is derived from the change in the loan balances, so a missing payment produces a wrong
> entry rather than an obvious error.

# Step 1. Find the month's depreciation

1. QuickBooks → **Reports → Balance Sheet**.
2. Set **Report Period** to **Last Month**, and under **Compare another period** check **Previous
   period** and **$ Change**.
3. Open **`27300 Auto Loans`** and confirm every vehicle note-payable account has its payment posted.
4. Once confirmed, **Customize**:
   - **Rows/Columns → Columns: Classes**
   - **Filter →** check **Class**, select **Houston** and **Austin** only
5. **Run report.**
6. Back in `27300 Auto Loans`, note the **$ Change** column totals **for each branch**.

# Step 2. Post the journal entry

**New → Journal entry.**

- **Journal Date:** last day of the month being closed
- **Journal no:** `mm/yy Depreciation`

| | Account | Class | Amount |
|---|---|---|---|
| Debit | `7450 Other Expenses:Depreciation Expense` | Houston | Houston $ Change total |
| Debit | `7450 Other Expenses:Depreciation Expense` | Austin | Austin $ Change total |
| Credit | `12900 Accumulated Depreciation` | — | Houston + Austin |

> **Depreciation is being derived from loan principal movement, not from an asset schedule.** The
> method works only while every vehicle is financed, financed over exactly the depreciable life, and
> still carrying a loan. **A vehicle bought outright, one whose loan is paid off, or one whose loan
> term differs from five years will depreciate wrongly or not at all.** The budget process assumes a
> separate `depreciationSchedule` tab exists — see
> [budgeting for a vehicle purchase](/operations/fleet/vehicle-purchase-budgeting.md) — which
> suggests there is an asset schedule this entry does not read. **Whoever owns the books should
> confirm the basis.**

> **The credit carries no class** while both debits do. The month-end review's
> [P&L class check](/finance/pl-class-assignment.md) only tests profit-and-loss accounts, so an
> unclassed balance-sheet credit would not be caught there.

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) — step 8, new property, plant and equipment
- [Journalizing vehicle loan interest](/finance/vehicle-loan-interest.md)
- [Checking P&L transactions have classes](/finance/pl-class-assignment.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
