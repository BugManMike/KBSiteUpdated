---
type: Runbook
title: Checking P&L transactions have classes
description: The month-end check that no profit-and-loss transaction is left unclassed, and how to assign a branch to the ones that are.
tags: [quickbooks, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1Dm6JnmFZpcN0ZE66XlUHREyK9wSlJ7nJ0WSyV3mzgXo
    resource: https://docs.google.com/document/d/1Dm6JnmFZpcN0ZE66XlUHREyK9wSlJ7nJ0WSyV3mzgXo/edit
    title: How to check all P&L transactions have classes
status: draft
---

Natran has two branches, **Austin** and **Houston**. At the end of every month the bookkeeper checks
that **every expense and revenue carries a class.**

# Step 1. Find the unclassed transactions

1. QuickBooks → **Reports → Profit and Loss by Class**.
2. Set **Report Period** to **This year to date**.
3. **Run report.**
4. Look for a **`Not Specified`** class column. **If there is one, go to step 2.**

# Step 2. Assign classes

Work through every account with a balance under **Not Specified**, opening each and setting each
transaction's class to **Houston**, **Austin** or **Corporate**.

**Finding the right branch:** check the attached receipt or invoice. The **Memo/Description** often
helps too — card users frequently note the branch there.

> **The report is year-to-date but the check is monthly**, so the same historic unclassed
> transactions reappear every month until someone fixes them. There is no way to tell this month's
> omissions from last month's leftovers.

> **Corporate is offered as a class here but is not a branch**, and anything left in it gets split
> across the two branches later by
> [corporate class proration](/finance/corporate-class-proration.md) — which **must run last** in the
> close. Assigning Corporate as a fallback for "I can't tell which branch" therefore silently
> redistributes the cost by whatever ratio the proration uses, rather than leaving it visible as
> unresolved.

> **This check covers the P&L only.** Balance-sheet entries are not tested — including the
> unclassed credit in [booking monthly depreciation](/finance/depreciation-monthly.md).

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) — step 3, review expenses and classification
- [Corporate class proration](/finance/corporate-class-proration.md)
- [Clearing uncategorized expenses](/finance/uncategorized-expenses.md)
- [Splitting Divvy materials charges](/finance/divvy-materials-split.md)
