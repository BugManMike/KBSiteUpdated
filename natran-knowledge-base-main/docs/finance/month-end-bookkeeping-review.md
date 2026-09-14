---
type: Runbook
title: Month-end bookkeeping review
description: The seventeen-step deep dive into classification and expensing on the balance sheet and P&L, run monthly after reconciliation.
tags: [quickbooks, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1HujWo9OggFE2n_-VWSFUCMHBvgKobBzFanaPzIkNq1E
    resource: https://docs.google.com/document/d/1HujWo9OggFE2n_-VWSFUCMHBvgKobBzFanaPzIkNq1E/edit
    title: End-of-Month Bookkeeping Review
status: draft
---

A thorough review of classification and expensing on the balance sheet and income statement.
**This is an extension of the normal reconciliation, not a replacement — run it monthly after
reconciliation is complete.**

Everything below is in QuickBooks unless stated. Classes throughout are **Houston Branch**,
**Austin Branch** and **Corporate**.

# 1. Review accounts payable

**Reports → Accounts payable aging detail** (A/P aging detail).

Any bill **not listed under `current` may be past due**. Either pay it or check for a clerical
cause — double entry, already paid on a credit card. Have the bookkeeper correct it.

# 2. Review employee advances

Employee advances are a **balance sheet asset**: checks are issued directly to employees, coded as
an advance, and repaid through payroll.

**Reports → Balance Sheet**, reporting period ~12 months, **Display columns by Months**. Review
the line for **`11600 Employee Advances`** and confirm they are being paid down. Click the balance
for the detailed transaction report and check that debits and credits are consistent with advances
paid out and repayments deducted from payroll.

# 3. Review expenses and classification

**Reports → Profit & Loss**, last month, **Display columns by Classes**.

**The check that tells you it is done: net profit at the bottom shows zero in the Corporate
column.** Corporate expenses are allocated in full to branches, so a non-zero Corporate figure
means classification is incomplete.

Also look for a **`Not Specified`** column — that is where transactions with no class assigned
appear. Assign them properly.

> `Not Specified` (step 3) and `Not Categorized` (step 5) are **two different problems**. The first
> is a missing *class*; the second is a missing *expense category*. They appear in different places
> on the same report and are easy to conflate.

# 4. Enter digital ad spend

See the Google Ads and Bing Ads procedure — covered in a later ingestion batch.

# 5. Look for expenses that are not categorized

**Reports → Profit & Loss**, last month. Look for a line item called **`Not Categorized`**. Assign
a category and re-run.

See [uncategorized expenses](/finance/uncategorized-expenses.md) for the fuller procedure — these
are usually Divvy transactions that synced without a GL code.

# 6. Review intercompany costs

Intercompany expenses are shared between the two companies. Three reports:

**Expenses tagged as intercompany** — irregular expenses tagged for sharing.
**Reports → Custom Reports → `Intercompany Expense by Tag Group - PCO`**.

**Intercompany vendors** — vendors always treated as intercompany: utilities, janitorial, trash.

> **The source gives the same report name and steps for both**, so the second is either the same
> report filtered differently or the report name is wrong. As written, steps 1 and 2 of both are
> identical.

**Balance sheet** — **Reports → Balance Sheet**, look for **`Due To APS`**. That balance is what is
owed to the other company; **a check can be cut periodically to settle it.**

See [intercompany transactions](/finance/intercompany-transactions.md).

# 7. Review note-payable payments and interest

Three sub-checks.

**Are they being paid down?** Balance Sheet, last 12 months, columns by Months. Find
**Long-Term Liabilities** — note payables nest underneath. Compare each note's prior-month balance
to the current month. **The balance should reduce every month.** If it does not, the payment was
entered wrongly or missed.

**Are payments hitting the right class?** Balance Sheet, last month, columns by Class, then
**Customize → Filters → Class** and select Houston Branch, Austin Branch, Corporate and any other
active branch. Under Long-Term Liabilities — mostly **`27300 Auto Loans`** — **each note payable
should have a balance under one branch only.** If the balance is in one branch and the payment was
made in the other, it shows in both and needs fixing.

**Is interest consistent?** P&L, last 12 months, columns by Month. Find **`7440 Interest - Loan`**.
**Interest should be similar but declining each month** unless a new loan was issued. Inconsistency
means asking the bookkeeper.

# 8. New property, plant and equipment

Only if new fixed assets were bought — usually a vehicle or large equipment. Balance Sheet, last 12
months, columns by Months. Review **`12000 Property, Plant & Equipment`** for new line items.

# 9. New note payables

New PPE usually comes with a new note payable. Balance Sheet → Long-Term Liabilities → confirm the
new note appears. If not, contact the bookkeeper.

Steps 8 and 9 are a pair: a vehicle purchase should produce both an asset and a liability. See
[vehicle use policy](/operations/fleet/vehicle-use-policy.md) for the operational side.

# 10. Uncleared transactions report

Shows transactions that have not cleared the bank after reconciliation.

**Accounting → Chart of Accounts** → the bank account → dropdown → **View Register** →
**Run Report**. Then **Customize → Filters → Cleared → Uncleared**. Run, and select the date range.

# 11. Review American Express charges

> **American Express is a personal card.** Its charges are recorded as owner's drawings / personal
> expenses, not business expenses.

**Reports → Balance Sheet** → the First United checking account. Find payment transactions for the
American Express account — identifiable by the keywords **`AMEX EPAYMENT ACH PMT`**. Confirm all
are recorded under **`30411 Personal Expenses`**.

# 12. Review bank account debits and credits

**Accounting** → the bank account → dropdown → **Run Report**. Set the report period to the month.
**Group by → Transaction Type.** Review the expenses and debits.

# 13. Confirm the fuel bill was entered

Search for the **Chevron vendor** and open its transaction history. Confirm **one paid bill per
month** up to the month being closed.

> The source names the Chevron vendor by its full account number. Not reproduced here — the bundle
> does not carry account numbers. It is in the source if needed.

# 14. Check deposit audit against bank statements

1. Pestroutes → **Billing → Payment History**.
2. Left menu → **Check**. Set dates to the whole month being closed. Select **both** Austin and
   Houston.
3. In First United, open the Natran checking account and search **"Remote Deposit"**.
4. **Match the Pestroutes check payments to the deposits.** You have to click into each bank deposit
   to see its breakdown — a deposit is a batch, not a single check.

# 15. Split RingCentral intercompany per user

1. In the **Pro-rata** working file, go to row 7 and scroll right to the month being allocated.
2. Enter the amount RingCentral charged in that month's column on row 7. The split per user
   calculates automatically.
3. Split the charge in QuickBooks per the row 13 (Natran) and row 14 (APS) allocation.

> **This is evidence that RingCentral is still a live, billed service** — it is invoiced and
> allocated every month. That bears directly on the open question in
> [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md), which flags
> RingCentral as probably retired because CallTrackingMetrics is documented as the current phone
> system. **Both may be true — CTM for call handling, RingCentral still carrying extensions or
> numbers.** Worth resolving; a monthly cost is being allocated for it either way.

# 16. Confirm the AT&T charge

Search for AT&T charges paid in the month. **Natran should have 4 charges.**

> Why four is not explained. If the count is a fixed expectation it will drift as lines are added
> or removed.

# 17. Confirm payroll is journalized

Sign into **Gusto**, open the Natran admin account, **Pay** on the left menu. Under Payroll,
confirm all payroll transactions are recorded in QuickBooks.

# Screenshots

Several steps referenced interface screenshots that did not survive conversion — chiefly the report
customisation dialogs in steps 7, 10 and 12.

# Related

- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
- [Accounts receivable close](/finance/accounts-receivable-close.md)
- [Corporate class proration](/finance/corporate-class-proration.md) — run after this
- [Intercompany transactions](/finance/intercompany-transactions.md)
- [Employee expense accounts](/finance/employee-expense-accounts.md)
