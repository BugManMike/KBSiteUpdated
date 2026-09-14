---
type: Runbook
title: Payroll journal recording
description: Turning the Gusto payroll journal into a QuickBooks journal entry — GL coding by role and branch, advances, child support, and the commission split between branches.
tags: [gusto, payroll, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 16dCwe-VNtkmXAjKUY6icjVbK-7-bUegZF2n9ZOte2oY
    resource: https://docs.google.com/document/d/16dCwe-VNtkmXAjKUY6icjVbK-7-bUegZF2n9ZOte2oY/edit
    title: Natran Payroll Recording Process
status: draft
---

Payroll is prepared **every two weeks**. Recording it means sorting every wage and benefit
contribution to the correct **GL code** and the correct **branch** (Houston or Austin), then posting
one journal entry to QuickBooks.

This is the **ledger** half of payroll. Producing the pay run is the
[biweekly payroll checklist](/people/payroll-checklist.md).

# Step 1. Check for code changes

Review email and chat for promotions or position changes. If there are any, update the
**Code for QB Gusto** tab with the new position's GL codes, taking them from the **employee
source-of-truth** spreadsheet.

# Step 2. Pull the Gusto payroll journal

1. Sign in to **Gusto** and **Switch Company** to **Natran LLC** with payroll admin access.
2. **Reports → Payroll Journal.** Set **Individual payroll details**, and check:
   detailed employee information, detailed employment information, employee earnings breakdown,
   employer tax breakdown, employee tax breakdown, deductions and contributions, detailed totals,
   reimbursements.
3. **Date range:** custom, set to the payroll's **payout date**. **Employees:** all.
   **Grouped by:** employee.
4. Generate as **CSV**.
5. Paste the whole CSV into **cell A1** of the **UploadGustoReport** tab of the payroll working file.

*Check that the payroll column headers land in row 10.*

# Step 3. Code any new employees

1. Open the **Gusto Report-HELPER** tab and look at **column C**. **An empty column C means a new
   employee with no GL codes.**
2. For each, add a row to **Code for QB Gusto**:

| Column | Contents |
|---|---|
| A | Last name, exactly as on the Gusto payroll journal |
| B | First name, exactly as on the Gusto payroll journal |
| C | `=A(x)&" "&B(x)` — drag the formula down |
| D | Department name, exactly as on the payroll journal |
| E | Branch classification, from the employee source-of-truth file |
| F onward | GL codes — copy the whole row from an existing employee with the same coding |

The role-to-account mapping is in
[employee expense accounts](/finance/employee-expense-accounts.md).

# Step 4. Employee advances

Open the **payroll notes** sheet to see who has an outstanding advance. If Gusto has tracked the
repayment as an employee deduction, **exclude it from deductions and enter it manually as a credit to
the Employee advances account.**

# Step 5. Child support deductions

Check the deduction column headers on the **UploadGustoReport** tab for child support. **Credit each
employee's deduction separately to the Child Support account.**

# Step 6. Split sales commission between branches

Commission is **paid the month after it is earned.**

1. Open the **monthly payrolls** folder and the month the commission was *earned*.
2. Open `TEMPLATE: Natran monthly bonuses and commissions (Month)` → **Inside Sales** tab.
3. In the **JE for Upload - Do NOT edit** tab, manually amend the existing formulas:
   - **add** the Austin total to `6010 Sales Commission Regular` (Class: **Austin**)
   - **add** the Houston total to `6010 Sales Commission Regular` (Class: **Houston**)
   - **deduct** both totals from `6010 Sales Commission Regular` (Class: **Corporate**)

# Step 7. Balance

Confirm debits and credits balance.

# Step 8. Upload to QuickBooks

1. On the **sample_journalentry_import_tax** tab, set the **Journal No** and **Date** to the payout
   date.
2. Download the **Final Entry** tab as CSV.
3. **QuickBooks Natran → gear icon → Import Data → Journal entries →** upload the CSV → **Submit**.

> **Step 6 asks a bookkeeper to hand-edit formulas inside a tab named "Do NOT edit".** The
> instruction is to append terms to the end of existing formulas in three cells, every cycle. That is
> the most fragile step in the finance corpus: it is unversioned, unreviewed, silently breaks the
> sheet if mistyped, and there is no check afterwards beyond step 7's balance test — which would
> still pass if the Houston and Austin figures were swapped.

> **Child support deductions are handled in a procedure with no confidentiality note.** The step
> requires reading per-employee deduction columns. Nothing in the document says who may see the
> payroll journal or where the working file may be stored. **HR and payroll should confirm the
> handling.** No values have been copied into this bundle.

> **Two separate spreadsheets are described as the source of truth for an employee's branch and GL
> code** — the "employee source of truth" file in steps 1 and 3, and the **Code for QB Gusto** tab,
> which is a hand-maintained copy of it. They will drift.

# Related

- [Biweekly payroll checklist](/people/payroll-checklist.md)
- [Employee expense accounts](/finance/employee-expense-accounts.md)
- [Health benefit allocation](/finance/health-benefit-allocation.md)
- [Calculating salesperson commissions](/people/sales-commission-calculation.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
