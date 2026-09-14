---
type: Runbook
title: Intercompany transactions
description: Recording expenses APS pays on Natran's behalf as a receivable in APS's books and an expense plus liability in Natran's.
tags: [quickbooks, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1NmeCRG44PHqxZd3gG2Co5BzwRNfubMRiLxhkHIyRrFM
    resource: https://docs.google.com/document/d/1NmeCRG44PHqxZd3gG2Co5BzwRNfubMRiLxhkHIyRrFM/edit
    title: How to Journalize intercompany transactions into the Natran QB account
status: draft
---

**Advantage Pro Services sometimes pays Natran's expenses.** Each month the bookkeeper records
those as a **receivable in APS's books** and an **expense plus a liability in Natran's**.

Two companies, two QuickBooks files, one transaction — so it has to be entered twice, in mirror.

# 1. In APS's books — record the receivable

1. Sign into **APS QuickBooks**.
2. Consult the **intercompany list** spreadsheet. **Any vendor labelled `APS` in column C must be
   recorded as a receivable, not an expense.** Follow the split rule in **column H**.

The entry:

```
Debit:  Due from Natran
Credit: 11214 First United Bank Checking
```

3. Download the transaction breakdown: **Balance Sheet → Due From Natran → Export to Excel.**

# 2. In Natran's books — record the expense

1. Sign into **Natran QuickBooks**.
2. Create a journal entry from the transactions exported above:

```
Debit:  an Expense account
Credit: Due to APS
```

# Reading the balance

`Due To APS` on Natran's balance sheet is what Natran owes. **A check can be cut periodically to
settle it** — see [month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) step 6,
which also covers the two intercompany expense reports.

> **The Natran side is vague where the APS side is precise.** APS gets a named debit and credit
> account; Natran gets "an Expense account". Which expense account depends on what was bought, so
> the judgment sits with whoever posts it, with the intercompany list's column H as the only guide.

> **Nothing reconciles the two sides.** If `Due from Natran` in APS's books and `Due to APS` in
> Natran's ever diverge, no step here would catch it. A periodic tie-out between the two balances
> would be the obvious control.

# Other intercompany allocations

This procedure covers expenses APS paid for Natran. Two other allocations run separately:

- **Health benefits** are paid from Natran's bank for both companies' employees and split by
  company, department and branch — see
  [health benefit allocation](/finance/health-benefit-allocation.md).
- **RingCentral** is split per user monthly via the Pro-rata working file — see
  [month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) step 15.

> So intercompany flows run **both directions** and are handled by three different procedures with
> three different working files. There is no single view of the intercompany position.

# Related

- [Health benefit allocation](/finance/health-benefit-allocation.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
