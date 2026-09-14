---
type: Runbook
title: Uploading King Ranch bills
description: Reconciling the King Ranch dealer portal against Bill.com to find un-entered invoices, then entering them to small tools and equipment.
tags: [bill-com, payables, inventory]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1tNLPCALPZUJt8LFwYn_M2IWvqVxBAOxOQwuwqOBtv24
    resource: https://docs.google.com/document/d/1tNLPCALPZUJt8LFwYn_M2IWvqVxBAOxOQwuwqOBtv24/edit
    title: Uploading KingRanch to Bill.com
status: draft
---

**King Ranch AG & Turf is where small tools and equipment are purchased.** Their invoices are not
emailed in, so they are pulled from the dealer portal and reconciled against what Bill.com already
has.

# 1. Find the invoices not yet entered

In the [King Ranch dealer portal](https://kingranchagturf.dealercustomerportal.com/customers/specials?external),
go to **Payment/Invoice History** and set:

- **Transaction range:** YTD
- **Transaction type:** Invoice

Then, in Bill.com, search the vendor name **King Ranch AG & Turf** from the top right. The **recent
bills** list on the vendor page is what you cross-check against — download only the portal invoices
that are missing from it.

# 2. Enter each bill

The vendor page is already open from step 1, so use **Create Bill** at the bottom right of it.

1. Click or drag in the downloaded invoices.
2. Bill.com auto-fills some fields. **Check the auto-filled figures against the downloaded invoice** —
   amount, vendor name, invoice number, date, due date.
3. **Account:** `5320 Small Tools and Equipment`, set in the Account column at the bottom of the page.
4. **Class:** **always Houston for this vendor** unless told otherwise.
5. **Save and Close**, top right.

> The account and class are hardcoded for this vendor — everything to `5320 Small Tools and
> Equipment`, everything to Houston. That is a coding shortcut, not a rule about what King Ranch
> sells. If Austin ever buys tools on this account, both the class and the reconciliation will be
> silently wrong. **Worth confirming with the bookkeeper** whether Austin purchases through King Ranch
> at all.

# Related

- [Entering a bill from the Bill.com inbox](/finance/bill-com-bill-entry.md)
- [Processing bill payments in Bill.com](/finance/bill-com-bill-payments.md)
