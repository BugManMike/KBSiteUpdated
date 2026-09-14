---
type: Runbook
title: Sentricon install budgeting
description: Costing the month's completed Sentricon initials into the budget, and refreshing renewal actuals from the tech scorecard.
tags: [budgeting, fieldroutes, bookkeeping]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1PJ53P9MYAvZZ7abMa-yN3sSfXrtaWlGUtbrMfSPed-A
    resource: https://docs.google.com/document/d/1PJ53P9MYAvZZ7abMa-yN3sSfXrtaWlGUtbrMfSPed-A/edit
    title: Budget for Sentricon Installs
status: draft
---

Sentricon material cost is budgeted from the **count of completed initials**, at a fixed cost each.

# Step 1. Run the reports

1. **Customers → Saved Reports → `Budgeting - Sentricon Initials HTX`**.
2. Under the **Service Appointment** filter, set the start and end date to the month you need.
3. **Run Report.**
4. Repeat for **`Budgeting - Sentricon Initials ATX`**.

# Step 2. Cost the initials

**Initial material cost = number of completed initials × $295.**

*The source's example: 20 initials × $295 = $5,900.*

Then, in the **adjustmentTable** of the active budget:

| Column | Enter |
|---|---|
| A (expense) | `5308 Sentricon Materials` |
| B, C | start and end date of the month |
| E (value) | the initial material cost |
| F (branch) | the branch name |
| H (notes) | e.g. `20 X Sentricon Initial Costs February 2022` |

# Step 3. Update renewal actuals

Active Sentricon services are tracked on the **tech scorecard**, under the
**filterSentriconRenewal** tab, as two colour-coded tables.

1. Open **filterSentriconRenewal** on the tech scorecard.
2. Open the **annualTable** in the active budget.
3. **Copy the data across — the colour coding matches.**

> **The $295 unit cost is hardcoded into the procedure** and appears nowhere else in the corpus. It
> is a supplier price in a document last touched in 2022, with no note of where it comes from, who
> confirms it, or when it was last checked against what Corteva actually invoices — see
> [submitting Sentricon initial information for billing](/finance/sentricon-initial-billing.md).
> **The budget owner should confirm the current cost and record its source.**

> **The step numbering skips 3.** The source runs Step 1, Step 2, then Step 4. Renumbered here; no
> content appears to be missing.

> **"Copy the colour-coded section into the matching colour-coded areas" is the whole of step 3.**
> A monthly copy-paste between two spreadsheets, matched by cell colour, with no check that the
> ranges still line up. Colour is not a stable key — reordering either sheet breaks it silently.

# Related

- [Submitting Sentricon initial information for billing](/finance/sentricon-initial-billing.md)
- [Submitting a Sentricon renewal for billing](/finance/sentricon-renewal-billing.md)
- [Production versus materials](/operations/production-vs-materials.md)
- [Budgeting for a vehicle purchase](/operations/fleet/vehicle-purchase-budgeting.md)
