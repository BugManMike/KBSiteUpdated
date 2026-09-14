---
type: Runbook
title: DSO tracking
description: Pulling sales and AR aging from Fieldroutes each week to update the DSO score per branch, and recording bad debt alongside it.
tags: [fieldroutes, receivables, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1feSOrP6P0wdlCaUKmvEzw5eur_zj4BBdH3iQaxTzb6E
    resource: https://docs.google.com/document/d/1feSOrP6P0wdlCaUKmvEzw5eur_zj4BBdH3iQaxTzb6E/edit
    title: DSO NATRAN
status: draft
---

Days Sales Outstanding measures how long it takes to collect after a sale. It is updated **weekly**
— Fridays, per the
[accounting schedule of events](/finance/accounting-schedule-of-events.md) — and **per branch**.

Records go in the **DSO tab** of the Natran Collections Weekly Worksheet.

# 1. Record sales

Fieldroutes → **Reporting → Billing by Service Type**.

- Custom range: **last 30 days up to the date of recording**
- Select **Houston Branch** or **Austin Branch** → Refresh
- Record the **Billed Amount** into the worksheet's Sales section

# 2. Record AR aging

Fieldroutes → **Billing → Accounts Receivable**.

- Custom date: up to the date of recording → Refresh
- Record four figures: **Current, Over 30 days, Over 60 days, Over 90 days**
- **Switch branch from the lower right of the dashboard** and repeat

# 3. Review

The **DSO score calculates itself** once the figures are in. Then fill the records date table:

- The date of recording
- DSO score for **Houston, Austin, and the total**
- **Total Revenue** from total sales
- **Total Past Due**

The Natran total DSO is the **average** of the two branches.

# 4. Record bad debt

Fieldroutes → **Billing → Payment History → Coupon**.

- Filter coupon codes: select all **Bad Debts**
- Date range: **weekly, Monday to Friday**
- Select **both** branches → Refresh

The **Total Collected** figure is what gets recorded as bad debt.

> "Total Collected" on a write-off report is the sum of write-offs, not cash received. The label is
> Fieldroutes'; the figure is bad debt.

# The target does not match the metric

> [Collections calling process](/finance/collections-calling-process.md) states that **"a successful
> collection department will have an average DSO of 3 to 4 days"** and that below 3 is exceptional,
> citing Investopedia's standard DSO definition.
>
> **Those two things are inconsistent.** Standard DSO — receivables divided by revenue, times days in
> period — lands in the tens of days for a business billing monthly. A DSO of 3 days would mean
> customers pay almost on the day of service. Either the worksheet computes something other than
> standard DSO despite the name, or the target is wrong by an order of magnitude.
>
> **This matters because the number is being used to judge performance.** Whoever owns the worksheet
> should confirm which formula cell B-whatever actually uses. Recorded as found in both documents.

# Two procedures for the same task

> This document and the older
> [accounts receivable daily operations](/finance/accounts-receivable-daily.md) source both describe
> the DSO update, with small differences: this one is written against **Fieldroutes** and a **2024**
> worksheet, the other against **Pestroutes** and an unnamed "DSO sheet", and the other adds a step to
> record the past-due figure from the left of the sheet. Same process, two vintages. This is the newer.

# Related

- [Collections calling process](/finance/collections-calling-process.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [Accounts receivable close](/finance/accounts-receivable-close.md)
