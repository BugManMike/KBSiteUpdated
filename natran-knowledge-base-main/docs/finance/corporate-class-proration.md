---
type: Runbook
title: Corporate class proration
description: Prorating month-end Corporate-class transactions between the Houston and Austin branches via the Variance sheet and a CSV journal import.
tags: [quickbooks, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1kWWpD0dqSm57Xf758TKScakDrUVl_QdbSYdC1-bIQQs
    resource: https://docs.google.com/document/d/1kWWpD0dqSm57Xf758TKScakDrUVl_QdbSYdC1-bIQQs/edit
    title: How to Prorate the Corporate branch transactions between ATX and HTX
status: draft
---

During the month, transactions that cannot be attributed to Houston or Austin are recorded under the
**Corporate** class. At month end they are prorated between the branches.

> **Make sure all transactions are recorded and reviewed before prorating.** The source states this
> in capitals. **This step must run last** — see
> [accounting schedule of events](/finance/accounting-schedule-of-events.md), where the monthly list
> is not in dependency order.

This is what makes the month-end check work: the
[month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) confirms classification is
complete when **net profit shows zero in the Corporate column**. Corporate is emptied by this
proration, not by coding transactions to branches during the month.

# 1. Prepare the journal entry

1. Open the **Variance Sheet**.
2. **Extensions → GAccon for Quickbooks → Refresh → All Sheets.**
   - This pulls live QuickBooks data into the sheet. **It takes a while — let it finish.**
3. Once loaded, go to the **Variance** tab and set **cell `A1` to the first date of the month**
   being worked on. That drives the whole sheet and feeds the journal entry.
4. Go to the **`journalEntryExport`** tab → **File → Download → CSV**.

# 2. Import it into QuickBooks

1. Open **QuickBooks-Natran**.
2. **Gear icon** (top right) → **Import Data**.
3. Record type → **Journal Entry** → **Import** → **Upload**.
4. Select the downloaded CSV → **Next**.
5. **Map the CSV columns to the QuickBooks columns.**
6. **Next** → **Complete the Import**.

> The column mapping is the fiddly part and the source covers it in one line, relying on a
> screenshot that did not survive conversion. If the mapping is wrong the import either fails or
> posts to the wrong accounts.

> **QuickBooks supports CSV journal import, as used here.** Worth noting because
> [revenue recording](/finance/revenue-recording.md) keys its monthly journal entry by hand from a
> tab named *For Upload*. The capability exists; it just is not used there.

# What the proration basis is

> **Not documented.** The Variance sheet computes the split, but nothing states whether it is by
> revenue, headcount, technician count or something else — or who set it. **That basis is the whole
> substance of the allocation**, and it lives only in spreadsheet formulas. Worth writing down: it
> determines each branch's reported profitability.

# Related

- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
- [Intercompany transactions](/finance/intercompany-transactions.md)
