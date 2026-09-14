---
type: Runbook
title: Splitting Divvy materials charges
description: The weekly pass that pulls COGS materials charges off the Divvy accounts, groups them per cardholder, and asks each one whether a charge needs splitting between service lines.
tags: [divvy, payables, inventory]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1L8QB2rk0vMvkRjHSx7WSrkVtsmOyIv2a5QzWivvPEMA
    resource: https://docs.google.com/document/d/1L8QB2rk0vMvkRjHSx7WSrkVtsmOyIv2a5QzWivvPEMA/edit
    title: Sort Materials-Divvy Charges
status: draft
---

A single Divvy charge can cover materials for more than one service line — a $500 charge might be
$250 of mosquito materials and $250 of rodent materials. **Only the cardholder knows the split**, so
this process gets the charges in front of them.

Run **weekly, on a Friday** — the date filter includes the current day.

# Steps

1. Open the QuickBooks **balance sheet**.
2. Open and **export to Excel** the `22203 Divvy` account, filtered to the **last 7 days including
   today**. **Repeat for the second Divvy Visa account.**
3. Paste both exports into the working file.
4. **Filter to COGS: Materials only.**
5. **Sort by Divvy user name.**
6. Copy each user's transactions onto **their own tab**.
7. **Email the Divvy users** so each can check whether any of their charges need splitting.

> The process ends at "send an email". **What happens to the answers is not documented** — nobody
> records who applies the split, in which system, or by when. As written this is a request with no
> completion step, so a reply could sit unactioned without anything catching it.

> The source names the second card by its **last four digits**. That was **not copied here** —
> "the second Divvy Visa account" is enough to find it in the chart of accounts, and card identifiers
> do not belong in the knowledge base.

# Related

- [Attaching Divvy receipts](/finance/divvy-receipt-attachment.md)
- [Production vs materials](/operations/production-vs-materials.md)
- [Clearing uncategorized expenses](/finance/uncategorized-expenses.md)
