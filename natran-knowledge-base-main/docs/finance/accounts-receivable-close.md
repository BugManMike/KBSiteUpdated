---
type: Runbook
title: Accounts receivable close
description: The three month-end journal entries that bring Pestroutes collections, coupons and the AR balance into QuickBooks.
tags: [quickbooks, bookkeeping, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1wVihtkkOEAST6zt4aqhnvH-TbF4oUsCmhLJl8cgXEek
    resource: https://docs.google.com/document/d/1wVihtkkOEAST6zt4aqhnvH-TbF4oUsCmhLJl8cgXEek/edit
    title: Natran Accounts Receivable Closing Process
status: draft
---

Three entries, all dated the **last day of the month being closed**, all against a single
catch-all QuickBooks customer named **`Trade`**. Every step is done **once per branch** — Houston
then Austin.

# 1. Collections — the cash suspense entry

**In Pestroutes:** Billing → Payment History → date range → select the branch.

**Compute net collections: Total Collected minus Total Coupons.** The coupons are backed out here
and booked separately in step 2, so they are not double-counted.

**In QuickBooks:** New → **Receive Payment**.

| Field | Value |
|---|---|
| Customer | `Trade` |
| Payment date | last day of the month being closed |
| Deposit to | `Cash Suspense` |
| Amount received | net collections from above |

**Apply payments chronologically to the invoices**, and confirm the applied total equals the amount
received. Save and close, then repeat for the other branch.

# 2. Coupons — the credit memo

**In Pestroutes:** Billing → Payment History → date range → branch → **Payment Methods → Coupon**
→ Refresh.

**In QuickBooks:** New → **Credit Memo**.

| Field | Value |
|---|---|
| Customer | `Trade` |
| Date | last day of the month |
| Credit Memo no. | `(Month) Coupons` |
| Line items | **two**, both `4910 Discounts` |
| Description | `Coupons` |
| Class | Austin on one line, Houston on the other |

Paste each branch's coupon total against its own class. **Download the CSV report for both branches
and attach them to the credit memo** — the attachment is the audit trail for the figures.

# 3. Ending balance adjustment

This reconciles what QuickBooks thinks AR is against what Pestroutes says it is, and books the
difference.

**Set up the working file.** In the AR Roll Forward spreadsheet: copy the previous month's formulas
into the new columns, **link each branch's beginning balance (row 3) to the previous month's ending
balance (row 10)**, and clear the new month's Sales, Sales Tax and Payments cells.

**Then pull four figures from Pestroutes, per branch:**

| Row | Where | What |
|---|---|---|
| Sales | Reporting → Billing by Service Type | **Billed Amount** under Invoice Stats |
| Sales Tax | Reporting → Billing by Service Type | **Taxes** amount under Invoice Stats |
| Payments | Billing → Payment History | **Total Collected** — **enter as negative** |
| AR Aging | Billing → Accounts Receivable, "As of" the last day of the month | Current, Over 30, Over 60, Over 90 |

Then **Accounts with Credits** → Credit Type **Both** → same as-of date → Refresh → copy
**Total Credits** into the Accounts with Credits column.

**Link the computed AR-end to row 17** of the AR Roll Forward file (`AR Balance as per PP`),
matching branch and month. **The adjustment calculates itself in row 7.**

> Note the Payments row uses **Total Collected**, not the net-of-coupons figure used in step 1.
> Coupons are handled by the step 2 credit memo, so the roll-forward wants the gross. Easy to get
> wrong.

**Book the adjustment.** QuickBooks → New → **Invoice**.

| Field | Value |
|---|---|
| Customer | `Trade` |
| Date | last day of the month |
| Invoice no. | `(Month) Adjustment` |
| Product/Service | `4905 Refunds and Exchange` — one line per branch |
| Class | Austin, Houston |
| Description | `Adjustment` |
| Amount | per branch, from row 7 |

> **An adjustment posted as an invoice against a fake customer is a plug.** It makes the books
> agree with Pestroutes without explaining the variance. Nothing in the procedure asks why the
> adjustment is non-zero, or sets a threshold above which someone should investigate. **If the
> figure is ever large, that is a signal being written off rather than read.** Worth adding a
> tolerance check.

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Revenue recording](/finance/revenue-recording.md)
- [DSO tracking](/finance/dso-tracking.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
