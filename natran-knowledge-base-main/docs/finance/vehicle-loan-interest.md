---
type: Runbook
title: Journalizing vehicle loan interest
description: Splitting a monthly vehicle payment into principal and interest by comparing the lender's statement balance with the ledger, and finding the branch class from the fleet sheet.
tags: [quickbooks, bookkeeping, vehicles]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1E0krOgJZgShINlfabW0y8g0xPfqsM1jzJFNYh28lbCU
    resource: https://docs.google.com/document/d/1E0krOgJZgShINlfabW0y8g0xPfqsM1jzJFNYh28lbCU/edit
    title: Journalize interest entries for Vehicle payments
status: draft
---

Monthly vehicle amortizations debit the bank as a **single amount covering both principal and
interest**. The split has to be derived before the payment can be journalized.

# Step 1. Find the payment

1. QuickBooks → **Transactions → Bank transactions**.
2. Look for descriptions naming the **lender** — the source names Toyota, Amegy and Ford.
3. Click the transaction, then **Split**.

# Step 2. Derive principal and interest

1. Log in to the **lender's portal** and open **all accounts**.
2. Find the vehicle that was paid. **Confirm the payment date and amount match the bank** — there is
   usually a one-day difference.
3. **View the statement** and note the **last four digits of the VIN**.
4. Use those four digits to find that vehicle's **note payable balance** on the QuickBooks balance
   sheet.
5. **Principal = QuickBooks note payable balance − statement balance.**
6. **Interest = payment amount − principal.**
7. Enter both into the **Split** from step 1.

*Worked example from the source:* a note payable of `$18,171.93` against a statement balance of
`$17,664.76` gives principal of `$507.17`; a payment of `$597.00` less that principal gives interest
of `$89.83`.

# Step 3. Set the class

Open the **fleet sheet**, search for the **VIN** from the statement, and read **column G (Branch)**
for the QuickBooks class.

> **The split is only correct if the ledger balance is correct going in.** Principal is computed as
> the difference between two balances rather than read from an amortization schedule, so **any
> earlier error in the note payable account is silently rolled into this month's interest figure**
> and never surfaces. The lender statement usually shows the split directly; the source does not use
> it.

> **Three lenders are named in a transaction-description search**, which is how the payment is
> found. A fourth lender, or a description that changes format, produces no match and the payment is
> simply missed. Nothing cross-checks that every financed vehicle had a payment journalized this
> month — though [booking monthly depreciation](/finance/depreciation-monthly.md) depends on exactly
> that being true.

# Related

- [Booking monthly depreciation](/finance/depreciation-monthly.md)
- [Journalizing SBA loan interest](/finance/sba-loan-interest.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) — step 7, note-payable payments and interest
- [Budgeting for a vehicle purchase](/operations/fleet/vehicle-purchase-budgeting.md)
