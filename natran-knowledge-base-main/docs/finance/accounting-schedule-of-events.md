---
type: Reference
title: Accounting schedule of events
description: The bookkeeping calendar — which process runs daily, bi-weekly, monthly or ad hoc, and who owns each one.
tags: [quickbooks, bookkeeping, payroll]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1fcrW81bOC_i5aKzZav3yiWRtGg3HPfXAT_UDvv4BinY
    resource: https://docs.google.com/document/d/1fcrW81bOC_i5aKzZav3yiWRtGg3HPfXAT_UDvv4BinY/edit
    title: Accounting wiki.page — Schedule of Events
status: draft
---

The accounting function's recurring calendar. **Almost every line is owned by the bookkeeper**;
the exceptions are noted.

> This came from a file named `wiki.page`, which elsewhere in the wiki is a navigation shell. This
> one is not — it is the only real content among the six `wiki.page` files, and it is the closest
> thing the accounting function has to a process index.

# Daily, by weekday

| Due | Process | Owner |
|---|---|---|
| Mon | Update revenue in Quickbooks | Bookkeeper |
| Mon | Journalize interest entries for vehicle payments | Bookkeeper |
| Tue | Attach Divvy receipts | Bookkeeper |
| Wed | Send bills from inbox to Bill.com; Bill.com bill management | Bookkeeper |
| Thu | Bill.com payment process | Bookkeeper |
| Fri | Weekly credits | Bookkeeper |
| Fri | DSO update | Bookkeeper |
| Fri | Check for ACH returns | Bookkeeper |

> The heading in the source reads "Daily Process" but the rows are assigned to specific weekdays,
> so it is a weekly cycle rather than a daily one. Two Monday items and three Friday items.

# Bi-weekly

| Process | Owner |
|---|---|
| Payroll recording process | Bookkeeper |

Bi-weekly matches the pay cycle in
[employment classification](/people/employment-classification.md).

# Monthly

**First week:**

- End-of-month bookkeeping review — see [month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- Check for open or pending appointments in Pestroutes
- Submit Sentricon information for billing
- Sales commission

**Rest of the month, unscheduled within it:**

- Prepare and pay sales tax for Natran Austin and Houston
- Pay the Wex/Exxon fuel bill
- Pay United Health Care
- Pay Mutual of Omaha
- Upload King Ranch bills to Bill.com
- Review the N94 digital invoice and confirm billing accuracy
- Journalize the month's revenue entries
- Finalize the accounts receivable balance
- Record bad debt
- Record Bing Ads, Google Ads and Google Local Ads per statement
- Enter Wex fuel bills into Bill.com
- Check Quickbooks for uncategorized expenses
- Check all P&L transactions have classes — Houston, Austin, Corporate
- Allocate health benefits between branches and intercompany accounts
- Journalize interest entries for the SBA loan
- Journalize depreciation for fixed assets
- Journalize APS's intercompany transactions into the Natran Quickbooks account
- Prorate the Corporate branch transactions between ATX and HTX
- Expiring credit card process

**The end-of-month bookkeeping review appears twice** in the monthly list — once owned by the
bookkeeper alone, and once jointly by Michael Arndt and the bookkeeper.

> Whether that is a first pass plus a review, or a duplicated row, is not stated. Given the review
> is a 17-step deep dive, a bookkeeper pass followed by a joint sign-off is plausible — but the
> source does not say so.

# Ad hoc

| Process | Owner |
|---|---|
| Pay franchise tax payment | Michael Arndt |
| Responding to a credit card dispute | *(unassigned)* |
| W9 and 1099 filing | Bookkeeper |

# Ordering matters here

The monthly list is not in dependency order, but several items depend on each other:

- **Prorating the Corporate class must come last.** Its own procedure warns in capitals that all
  transactions must be recorded and reviewed first. See
  [corporate class proration](/finance/corporate-class-proration.md).
- **Checking that all P&L transactions have classes** must precede the proration, since the
  proration acts on the Corporate class.
- **Uncategorized expenses** must be cleared before the P&L is meaningful.
- **Finalising the AR balance** and **recording bad debt** are both inputs to the AR close.

> The source presents these as a flat checklist. **A first-time reader could work it top to bottom
> and get the wrong answer.** Worth reordering, or annotating with dependencies.

> **The table is followed by roughly 90 empty rows** in the source — an artifact of the document
> being built as a table rather than a list.

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Accounts receivable close](/finance/accounts-receivable-close.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
- [A/R and payroll agent duties](/finance/ar-payroll-agent-duties.md)
