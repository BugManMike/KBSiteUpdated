---
type: Runbook
title: Journalizing SBA loan interest
description: Splitting the monthly SBA EIDL payment between principal and interest from the lender's payoff balance, and recording it as a Corporate-class expense.
tags: [quickbooks, bookkeeping, payables]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1xKJ-sQaXCepHZ75_XxeNATAbXe0gHLbbCnS2SrLSeu8
    resource: https://docs.google.com/document/d/1xKJ-sQaXCepHZ75_XxeNATAbXe0gHLbbCnS2SrLSeu8/edit
    title: How to Journalize interest entries for SBA Loan
status: draft
---

The **SBA loan is paid monthly on the 10th**, as a single amount that has to be allocated between
principal and interest.

> **Run this on the 18th of the month**, so the payment made on the 10th has posted on the lender's
> site.

# Step 1. Get the new principal balance

1. Log in to the **SBA lending portal**.
2. **View Summary** from the dashboard.
3. Note the **Payoff Balance** — this is the principal **after** the month's payment posted.

# Step 2. Get the old principal balance

1. QuickBooks → **Reports → Balance Sheet**.
2. **Report Period:** This month. **Compare another period:** check **Previous period** and
   **$ Change**.
3. Under **Long-term Liability**, find the **SBA EIDL Loan** account.
4. **Confirm no payment has been posted yet this month** — the balance should be unchanged from the
   previous month. If so, that balance is the old principal.

# Step 3. Post the expense

**New → Expense**, with:

- **Payee:** SBA Loan
- **Payment account:** `11216 First United Checking`
- **Payment date:** the payoff date shown on the SBA site
- **Reference:** `SBA <Month>`
- **Class:** Corporate

| Category | Amount |
|---|---|
| `SBA EIDL Loan` | old principal balance − new payoff balance |
| `7440 Other Expenses:Interest - Loan` | total monthly payment − the principal figure above |

**Save.**

> **The whole entry depends on step 2's precondition holding, and the check for it is weak.** "No
> payment posted yet" is inferred from the balance being unchanged month to month. If a payment was
> posted *and* an offsetting error existed, or if the previous month was never closed, the balance
> test still passes and the split is wrong in both directions — understating principal and
> overstating interest by the same amount.

> **Everything is classed Corporate**, so none of the SBA interest reaches Houston or Austin. That
> is consistent with [corporate class proration](/finance/corporate-class-proration.md), which
> splits Corporate-class transactions between branches at month end and **must run last** — but
> nothing in either document says whether SBA interest is meant to be included in that proration or
> deliberately left at Corporate.

> **The source works through a specific month's figures**, including the loan's payoff balance and
> monthly payment. Those are one month's numbers, not standing facts, and will not match when you
> run this.

# Related

- [Journalizing vehicle loan interest](/finance/vehicle-loan-interest.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) — step 7
- [Intercompany transactions](/finance/intercompany-transactions.md)
