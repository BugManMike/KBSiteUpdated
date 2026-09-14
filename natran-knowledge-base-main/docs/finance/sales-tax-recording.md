---
type: Runbook
title: Recording sales tax
description: Building the monthly sales tax worksheet from the Fieldroutes sales tax report, by county and by branch, ready for filing.
tags: [fieldroutes, tax, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 11vmUX6sOajjxX-LDAQtLQUM1dmKlB-mM9BZRWtdQj9g
    resource: https://docs.google.com/document/d/11vmUX6sOajjxX-LDAQtLQUM1dmKlB-mM9BZRWtdQj9g/edit
    title: How to record Sales Tax of Natran
status: draft
---

Sales tax is levied by the state on the sale of goods and services within Texas, collected at the
point of sale and based on the sale price. This procedure produces the worksheet that
[filing and paying sales tax](/finance/sales-tax-filing.md) transcribes into the return.

# 1. Open the worksheet

**Duplicate last month's report** and update it for the current month. **Adjust the reporting period**
so it reflects the month actually being covered.

# 2. Run the sales tax report

In Fieldroutes: **Reporting** → the **Sales tax** section.

- **Custom range date:** last month
- **Group by:** County
- **Offices:** Houston Branch or Austin Branch, then refresh data

**Export as CSV.**

# 3. Save the report

Upload the downloaded report to the folder for the reporting month.

# 4. Copy the data across

Copy the data from the downloaded report into the **sales tax worksheet**. Paste it into the correct
row — **green rows are Houston, blue rows are Austin.**

# 5. Check the formulas

- Sales ties to **Revenue**
- Sales tax equals **Total Tax**
- The filing discount depends on how early payment is made

> **The branch colour coding is the only thing keeping the two branches apart** in the worksheet.
> Green for Houston and blue for Austin is a formatting convention, not a validated field, so pasting
> into the wrong row misfiles a branch's tax with nothing to catch it.

> The report is grouped **by county** but the worksheet is organised **by branch**. The document does
> not say how county rows map onto the two branch row groups, which is the one step where this could
> go wrong.

# Related

- [Filing and paying sales tax](/finance/sales-tax-filing.md)
- [Revenue recording](/finance/revenue-recording.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
