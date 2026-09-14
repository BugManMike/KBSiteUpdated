---
type: Runbook
title: Weekly credit report
description: Pulling billing by service type from Fieldroutes each week, filtering to discounted lines, and reporting the credit list onward.
tags: [fieldroutes, credit]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1VCpc3wetNvW0Euk_ojDIscIeW6RB9zZTCIIPXCNfSfc
    resource: https://docs.google.com/document/d/1VCpc3wetNvW0Euk_ojDIscIeW6RB9zZTCIIPXCNfSfc/edit
    title: Weekly Credit
status: draft
---

A weekly report of the discounts and credits applied to customer accounts.

# 1. Run the report

Fieldroutes → **Reporting** → **Billing by Service Type**:

- **Custom range date:** this month
- **Group by:** Service Type
- **Sub group:** Customer Name
- **Office:** one branch at a time, then refresh

# 2. Export

**Export to Excel.**

# 3. Review and copy

From the downloaded report, find the **Sub group entries** tab and copy the data into the **Credit
List** working sheet.

**Filter to everything that has a Discount**, and copy the result to the **Monthly tab**.

# 4. Send it on

Download the report and email it to the billing manager.

> **The cadence and the date range contradict each other.** The report is titled and scheduled as
> **weekly**, but the custom range is set to **this month**. Run weekly against a month-to-date range,
> each report re-reports everything already sent, and the "Monthly tab" then accumulates duplicates.
> **One of the two is wrong.**

> **The recipient is named by first name only** in the source, with no role or address. Recorded here as
> the billing manager, which is the inference the rest of the corpus supports — but **the source should
> name a role**, since a first name stops working the moment that person changes jobs.

> **What the recipient does with the report is not documented.** As with
> [applying account credit](/finance/applying-account-credit.md), credits are reported but never
> reviewed against an approval or a limit anywhere in the corpus.

# Related

- [Waiving fees and applying account credit](/finance/applying-account-credit.md)
- [11-month customer retention credit](/finance/retention-credit-11-month.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
