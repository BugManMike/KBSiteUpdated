---
type: Runbook
title: Filing and paying sales tax
description: Filing the Texas sales and use tax return from the state portal against the sales tax worksheet, paying it, and retaining proof of filing.
tags: [tax, payables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1sPAqf1QpsIOb1kQAwoL0yAswhpPK82iGsr9gRAP16aI
    resource: https://docs.google.com/document/d/1sPAqf1QpsIOb1kQAwoL0yAswhpPK82iGsr9gRAP16aI/edit
    title: How to File and Pay Sales Tax - Natran
status: draft
---

The figures filed here come from the sales tax worksheet built in
[recording sales tax](/finance/sales-tax-recording.md). **Do that first** — this procedure only
transcribes its output into the state return.

# 1. Open the return

Log in to the state tax portal and navigate to **Sales and Use tax** to file and pay.

From the **File and Pay Taxes** column → **File original return**. Check the period-ending month
matches the filing month → **Continue**.

Two screening questions come up. The answers, as documented:

| Question | Answer |
|---|---|
| Are you taking credit to reduce tax due on this return? | **No, I'm not taking credits** |
| Did you refund sales tax for this filing period on items exported outside the United States based on the Texas licensed customs broker export certification? | **No** |

# 2. File the report

Enter the data corresponding to the sales tax worksheet:

| Return field | Worksheet source |
|---|---|
| Total Texas sales | Gross receipts |
| Taxable sales | Balance subject to tax |
| Taxable purchases | `0` |

Filing early earns the **Timely Filing Discount**. **Copy the discount back into the sales tax
worksheet under 'Filing Discount'**, then **Continue**.

# 3. Pay

Select the payment type — the state's electronic payment system — review the **amount to pay**, and
continue. Enter the Natran bank account details, which are held in the *Important file*, **'Bank and
Loans'** tab. **Submit.**

# 4. Retain proof

**Print and save the report** as proof of filing, and upload the PDF to the folder for the reporting
month.

> **The payment type is written as "TextNet".** The Texas electronic payment system is **TEXNET**.
> Almost certainly a typo, but left as found rather than silently corrected — the label on the screen
> is what a new bookkeeper will match against.

> **The portal is called the "Franchise Tax Payment Portal" while the task is sales tax.** The state's
> single Webfile sign-on covers both, so the instruction works, but the name in this document points at
> the wrong tax. See also [franchise tax payment](/finance/franchise-tax-payment.md), which reaches the
> same portal by a different URL.

> The bank account details live in a spreadsheet referred to only as **the "Important file"**. The
> account numbers themselves are **not recorded here**. Worth noting that banking credentials for both
> companies sit in a shared file identified by nothing more specific than that name.

# Related

- [Recording sales tax](/finance/sales-tax-recording.md)
- [Franchise tax payment](/finance/franchise-tax-payment.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
