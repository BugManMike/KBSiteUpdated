---
type: Runbook
title: Recording ad spend from prepaid to expense
description: The monthly journal entries that move Google Ads, Google Local Services and Bing Ads spend out of the prepaid balance-sheet accounts into classified expense.
tags: [quickbooks, bookkeeping, marketing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1f0dMsHURcz6RauI_OT6ESvdSit5YIpTthDRuP2QK9Vo
    resource: https://docs.google.com/document/d/1f0dMsHURcz6RauI_OT6ESvdSit5YIpTthDRuP2QK9Vo/edit
    title: Enter Google Ad & Bing Ads expense into Quickbooks
status: draft
---

**Why this entry exists.** Google and Bing charge the credit card **in advance** and hold the funds in
a prepaid account. Those charges land on the balance sheet as **Prepaid Google Ads** and **Prepaid
Bing Ads**, and the balance draws down as the platforms spend it. Each month a matching journal entry
moves the spent portion out of prepaid and into the right expense account, classified by branch.

Worked through: if Google charges $10,000 and spends $8,673 on Houston campaigns and $1,053 on
Austin, the entry puts an $8,673 Google Ads expense on the P&L against Houston and $1,053 against
Austin. The closing prepaid balance is then $274, which should be the following month's opening
balance.

**The check that makes it worth doing:** at the end of each month the closing balance on Google or
Bing should equal the closing balance on the QuickBooks balance sheet. If it does, every dollar is
accounted for.

A video walkthrough exists at <https://youtu.be/tSdZt6klS6g>.

# Google Ads

## 1. Find the monthly spend

1. Log in at <https://ads.google.com> — access has to be granted.
2. Select the **Natran CORP Ads** account.
3. **Tools & Settings** → **Transactions** under Billing.
4. Find the current month and note the **Net cost**.
5. **Campaigns** lists each campaign and its spend.
6. **Adjustments** lists adjustments.

## 2. Enter the net cost and campaign spend

In QuickBooks: **New** → **Journal Entry**, dated the **1st of the month**.

| Line | Account | Column | Amount | Class |
|---|---|---|---|---|
| 1 | Prepaid Google Ads | Credits | Net cost from step 1 | Corporate |
| 2 | `6025 - Advertising Google Ads` | Debit | Campaign cost | Houston, Austin or Corporate |

Put the campaign name in the **Description** field on the expense line.

## 3. Enter adjustments

Add a line: **Prepaid Google Ads**, adjustment amount in **Credits**, class **Corporate**.

# Google Local Services Ads

**This differs from the regular Google Ads entry, and presently applies only to Austin.**

1. Log in at <https://ads.google.com/local-services-ads/>.
2. Select the Austin local-services account.
3. **Billing** → under **Transactions**, pick the date range.
4. Download the **Statement**.
5. Copy the **Total New Activity** amount — that is what the entry is for.
6. In QuickBooks, **New** → **Journal Entry**.
7. Date it the **last day of the month** being worked on (e.g. 2/28/23).
8. Number it with your initials, month, year and `GLA` — `MTA Feb 2023 GLA`.
9. **Prepaid Google Local Ads**, **Credits** equal to the statement amount, class **Corporate**.
10. **`6025 Advertising - Google Ads`**, debit equal to the same amount, class **Austin**. QuickBooks
    may fill this line automatically.
11. **Attach the PDF statement.**
12. **Save.**

> Google Local Services Ads is credited out of its own prepaid account — **Prepaid Google Local
> Ads** — but debited to the **same expense account** as regular Google Ads, `6025`. So the P&L cannot
> distinguish local-services spend from search spend. That may be deliberate; it does mean the two
> channels cannot be compared from the books alone.

> The date convention **contradicts the regular Google Ads entry above** — that one is dated the
> **1st** of the month, this one the **last day**. Both describe the same monthly close. **Someone
> should pick one**, since mixed dating makes the prepaid roll-forward harder to tie out.

# Bing Ads

## 1. Find the monthly spend

1. Log in at <https://ads.bing.com>.
2. **Campaigns** on the left sidebar.
3. Select the month.
4. Find the **Spend** column.

## 2. Enter the campaign spend

In QuickBooks, open **the same journal entry** used for Google and add lines:

| Line | Account | Column | Amount | Class |
|---|---|---|---|---|
| 1 | Prepaid Bing Ads | Credits | Overall total from the bottom of the Spend column | Corporate |
| 2 | `6024 - Advertising Bing Ads` | Debit | Campaign cost | Houston, Austin or Corporate |

Campaign name goes in the **Description** field.

# Related

- [Reviewing N94 ad data before invoicing](/finance/n94-invoice-data-review.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
- [Corporate class proration](/finance/corporate-class-proration.md)
