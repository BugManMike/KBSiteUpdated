---
type: Runbook
title: Clearing uncategorized expenses
description: Finding transactions that synced into QuickBooks without a GL code — usually from Divvy — and assigning one.
tags: [quickbooks, bookkeeping, divvy]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 158ofIm9fMDOd31GD3rIWgbjj75YN6wdiAJmeTGEgVWw
    resource: https://docs.google.com/document/d/158ofIm9fMDOd31GD3rIWgbjj75YN6wdiAJmeTGEgVWw/edit
    title: Checking Quickbooks for uncategorized expenses
status: draft
---

**Some transactions sync into QuickBooks without a GL code — mostly from Divvy.** The bookkeeper
assigns them one.

# Find them

1. QuickBooks → **Reports** on the left menu.
2. **Profit and Loss.**
3. Report period → **This Year-to-date**.
4. `Ctrl+F` and search for **`Uncategorized Expense`**.

**No search result means nothing to do.** A result means there are transactions needing a code.

# Assign codes

1. Click the amount to open the detailed per-transaction report.
2. Work through the list one by one and assign a GL code.
3. **Use the attached invoice** for an accurate code, or the **Memo/Description** field for context.

> "Refer to the attached invoice" only works if the invoice is attached. Divvy receipt attachment is
> a separate weekly task in the
> [accounting schedule of events](/finance/accounting-schedule-of-events.md) — Tuesdays. **If
> receipts have not been attached, this step has nothing to work from.** Run them in that order.

For the role-based expense accounts, see
[employee expense accounts](/finance/employee-expense-accounts.md).

# Note the two different problems

This clears **`Uncategorized Expense`** — a missing expense *category*. The
[month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) also looks for
**`Not Specified`**, which is a missing *class* (Houston / Austin / Corporate). Both appear on the
P&L and both need clearing, but they are different fields and different fixes.

The review searches the report period for **last month**; this searches **year to date**, which will
surface older stragglers too.

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Employee expense accounts](/finance/employee-expense-accounts.md)
