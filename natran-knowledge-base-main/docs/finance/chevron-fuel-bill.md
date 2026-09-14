---
type: Runbook
title: Paying and recording the Chevron fuel bill
description: Paying the monthly Chevron fuel invoice from its portal, then entering it in Bill.com split between Houston and Austin using the allocation worksheet.
tags: [chevron, payables, fleet]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1-W_8IIMr8PqbC5q7Y9ZJ6vRZBmdxIclTlXaeaYnornI
    resource: https://docs.google.com/document/d/1-W_8IIMr8PqbC5q7Y9ZJ6vRZBmdxIclTlXaeaYnornI/edit
    title: Chevron Fuel Bill payment and recording process
status: draft
---

Chevron is the company fuel account. **Usage is billed at the end of each month**, and the invoice is
**due on the 22nd of the following month**. Payment happens in Chevron's portal; the recording and
branch split happen in Bill.com.

# 1. Pay the previous month's bill

Log in to the [Chevron business portal](https://www.chevrontexacobusinessmanager.com/transactions/search).

First **confirm the invoice is not already paid**: **Payments** → **Payment history**. The latest
payment should still be for the month before the one you are paying. The payment date recorded there
is the invoice due date, not the day it was keyed.

Then, from the dashboard:

1. **View Invoice** — note the amount due and the due date from the downloaded invoice.
2. Back on the dashboard, **Pay Now**.
3. Select the **minimum payment due**, and check it matches the downloaded invoice.
4. Choose the designated operating checking account as the paying bank.
5. Enter **the due date of the bill** as the payment date.
6. **Preview payment**, then confirm in the pop-up.

# 2. Build the branch allocation

1. In the Chevron portal, download both the **invoice** (*View Invoice*) and the **activity report**
   (*View Activity Report*).
2. **Merge them into one file** — invoice pages first, then the transaction report.
3. Open the **previous month's Chevron allocation file**, duplicate it, and rename it to the current
   month.
4. From **Transactions** in the portal, download the activity report as **CSV**, with the period
   customised to the month being billed.
5. Paste the CSV contents into **cell A3** of the allocation sheet.
6. Enter the **amount due** from the bill into **cell K1**.
7. **Cells N1 and N2 calculate the Houston and Austin shares.**

# 3. Enter and clear the bill

Log in to Bill.com → **Actions** → **Enter a Bill**.

1. Upload the merged file from step 2.
2. Set the vendor to the Chevron fleet account.
3. Double-check the auto-filled fields.
4. **Split the bill between Houston and Austin** using the amounts from cells N1 and N2.
5. **Review and pay → Mark as paid** — the payment already happened in step 1, so this only records
   it.
   - **Payment amount:** the invoice amount
   - **Chart of account:** `11216 First United Checking`
   - **Payment type:** Check
   - **Reference Number:** `ACH`
   - **Memo:** the invoice number
6. **Save.**

> **Payment type is recorded as Check while the reference number is recorded as `ACH`.** Those
> contradict each other. One of the two is a convention the bookkeeper understands and the other is
> wrong; the document does not say which. **Worth settling**, because payment type is what
> reconciliation matches on.

> **The worked example is internally inconsistent on the year.** The document says it is paying the
> **August 2024** bill, but the step that sets the CSV period says to customise the dates to
> **August 1–31, 2023**. The 2023 date is almost certainly a leftover from an earlier revision.

> The Chevron **account number**, and the identifier of the paying bank account, appear in the source
> and were **deliberately not copied here** — described by role instead. Both are selected from
> dropdowns by anyone who has portal access, so the procedure does not need them written down.

# Related

- [Processing bill payments in Bill.com](/finance/bill-com-bill-payments.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
