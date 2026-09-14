---
type: Runbook
title: Recording bad debt
description: The daily revenue-entry update and the month-end credit memo that put bad debt into QuickBooks, plus the journal entry that records recovered bad debt.
tags: [quickbooks, bookkeeping, write-offs]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1__WlxO9A7w-Ht-5jlOhzq_5he_VK-Mdm3rq0G3A5g0o
    resource: https://docs.google.com/document/d/1__WlxO9A7w-Ht-5jlOhzq_5he_VK-Mdm3rq0G3A5g0o/edit
    title: How to record Bad debts-Natran
status: draft
---

Bad debt originates in Fieldroutes as a **coupon** — writing an account off applies a coupon code
containing "bad debt" — and this procedure carries those coupons into QuickBooks. It runs at two
cadences.

**Distinct from [DSO tracking](/finance/dso-tracking.md)**, which records the weekly bad-debt figure
into the collections worksheet. This one posts it to the ledger.

# Daily

## 1. Run the payment history report

Fieldroutes → **Billing** → **Payment History**:

- **Custom range date:** this month
- **Payment methods:** Coupon
- **Office:** one branch at a time, then refresh
- **Coupon codes:** every code containing the words "bad debt"

## 2. Update the revenue journal entry

In QuickBooks, open the **daily revenue entry** and update the amounts for the **`4907 Bad Debts`**
account. **Save.**

**This entry is updated every day.**

# Month end

## 1. Run the payment history report

Same as above, with one addition:

- **Reversed payments: exclude reversed payments**

## 2. Write a credit memo

QuickBooks → **New** → credit memo for the month:

- **Customer name:** `Trade`
- **Credit memo date:** first day of the month
- Enter the amounts from Fieldroutes **per branch** → **Save**

## 3. Record bad debt recovered

Re-run the payment history report, this time with **Reversed payments: include reversed payments**.

**Sort by the type column** to group everything with a **Reversed** type, and **total the payment
amounts** for those rows. That total is bad debt that was subsequently collected.

QuickBooks → **New** → **Journal Entry** for the month:

| | Account |
|---|---|
| **Debit** | Cash suspense |
| **Credit** | `4907 Bad debts` (per branch) |

Enter the total from above → **Save**.

> **Step 3 of the month-end process is labelled with credit-memo fields inside a journal entry** — it
> repeats "Customer name: Trade" and "Credit memo date" from the previous step. A journal entry has
> neither field. Copy-paste carry-over from step 2; the debit and credit lines are the actual
> instruction.

> **The branch filter names "Natran Branch" or "Austin Branch".** Everywhere else in the corpus the
> two branches are **Houston** and **Austin** — see
> [DSO tracking](/finance/dso-tracking.md) and [sales tax recording](/finance/sales-tax-recording.md).
> Either "Natran Branch" is an old label for the Houston office or it is a mistake. **It decides which
> office's bad debt gets booked.**

> **`Trade` is a placeholder customer, not a real one.** Batch 4a flagged the same fake customer being
> used as the counterparty for the [AR ending-balance plug](/finance/accounts-receivable-close.md). It
> is now carrying two unrelated month-end adjustments, which makes anything posted against `Trade`
> hard to interpret later.

> **Bad-debt recovery is identified as a "Reversed" coupon payment.** A reversed write-off coupon is a
> plausible way to represent recovery, but it is the same signal a plain data-entry correction would
> produce. Nothing distinguishes "the customer paid after write-off" from "the write-off was keyed by
> mistake and undone", and the two need opposite accounting treatment.

# Related

- [DSO tracking](/finance/dso-tracking.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md)
- [Accounts receivable close](/finance/accounts-receivable-close.md)
- [Transworld dispute process](/finance/transworld-disputes.md)
