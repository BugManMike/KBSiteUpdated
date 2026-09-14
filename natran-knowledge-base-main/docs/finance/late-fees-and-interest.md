---
type: Runbook
title: Applying late fees and interest
description: The two batch runs on the first of each month that charge a $35 late fee and 1.5% monthly interest to accounts 15 to 365 days overdue.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 11qVsssILqtzJRX5G49ueFkpljlryN7kd4viJ0D_4lT8
    resource: https://docs.google.com/document/d/11qVsssILqtzJRX5G49ueFkpljlryN7kd4viJ0D_4lT8/edit
    title: How to apply late fees and interest
status: draft
---

**Run on the 1st of each month, and repeat for each branch.**

Two separate batch runs, identical except for the fee applied at the last step.

# The filter, common to both

1. **Billing** → **Collections**.
2. **Days Overdue** → **Custom Range** → enter **15 to 365 days**.
3. **Advanced Filters** → **Exclude Flags** → select **Do not charge late fees** → **Refresh**.

The `Do not charge late fees` flag on an account is what exempts it. Nothing else does.

# 1. Charge the late fee

**Actions** → **Add fees**:

- **Fee service type:** Late fee charge
- **Fixed amount:** **$35**
- **Proceed to Verification** → review the fees being charged → **Confirm Fees**

# 2. Charge interest

Re-apply the same filter, then **Actions** → **Add fees**:

- **Fee service type:** Monthly interest fee assessed on past due account
- **% of Balance:** **1.5%**
- **Proceed to Verification** → review → **Confirm Fees**

> **The 365-day upper bound silently drops the oldest debt.** An account 366 days overdue falls out of
> the filter and stops accruing both the fee and the interest. That may be intentional — debt that old
> is usually [written off and sent to an agency](/finance/sending-accounts-to-collections.md) — but the
> document does not say so, so it reads as an arbitrary range.

> **Interest is charged as a percentage of the balance, and the late fee is added to the balance
> first.** Running step 1 before step 2, as written, means the month's $35 fee is inside the base that
> 1.5% is calculated on. Whether that is intended is worth confirming, since it compounds fees on fees.

> The fee amounts — **$35** and **1.5% monthly** — are recorded here as the operating procedure has
> them. Whether they match what the customer agreement authorises is **not something this document
> establishes**, and it is the kind of thing a chargeback or a dispute turns on. See
> [chargeback disputes](/finance/chargeback-disputes.md), where the rebuttal relies on the signed
> agreement.

# Related

- [Waiving fees and applying account credit](/finance/applying-account-credit.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [Collections calling process](/finance/collections-calling-process.md)
