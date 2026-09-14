---
type: Runbook
title: Budgeting for a vehicle purchase
description: Entering a vehicle into the budget model twice — as an assumption before purchase, then moved to the debt and depreciation schedules after.
tags: [budgeting, vehicles, fleet]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1Wo8KRmqMFcu-OFXUurSkINHO42X52K3P6vJrb7l_MNE
    resource: https://docs.google.com/document/d/1Wo8KRmqMFcu-OFXUurSkINHO42X52K3P6vJrb7l_MNE/edit
    title: Budgeting for vehicle purchase and setup
status: draft
---

> **The source is labelled "This is a work in progress" and stops mid-procedure.** What follows is
> everything it contains. See the note at the bottom.

A vehicle is entered into the budget model **twice**: first as an assumption before it is bought,
then as actuals afterwards.

# Before purchase — assumptions

In the **FinancialModel** tab of the budget spreadsheet:

1. Under **Debt & Equity**, enter the **loan amount, interest rate and payment periods**.
2. Under **PPE & Other CapEx**, enter the **vehicle value and depreciation periods**.

# After purchase — actuals

1. **Remove the loan amount** from the FinancialModel tab and enter it in the **debtSchedule** tab.
2. **Remove the vehicle value** from the FinancialModel tab and enter it in the
   **depreciationSchedule** tab.

# Step 1. Add the vehicle to PPE assumptions

1. Open the **Budget & Campaigns** spreadsheet.
2. Find the **PPE & Other CapEx** section on the **FinancialModel** tab.
3. Open the **Debt** section.

> **The document ends here**, at "*You should see the following notes:*" followed by nothing. The
> summary above the numbered steps is complete and usable; the step-by-step walkthrough it was going
> to expand into does not exist. **Whoever owns the budget model needs to finish it or delete it** —
> a half-written procedure is worse than none, because the reader cannot tell where it stopped being
> deliberate.

> **The opening sentence reads "you will be setting X entries"** — a placeholder that was never
> filled in. From the content, the answer is two.

> **This procedure assumes a `depreciationSchedule` tab holds each vehicle's depreciation**, but
> [booking monthly depreciation](/finance/depreciation-monthly.md) derives depreciation from the
> movement in the loan accounts instead and never mentions a schedule. Either the schedule is
> budget-only and the books ignore it, or the two disagree. **The bookkeeper and the budget owner
> should reconcile them.**

# Related

- [Booking monthly depreciation](/finance/depreciation-monthly.md)
- [Journalizing vehicle loan interest](/finance/vehicle-loan-interest.md)
- [Vehicle use policy](/operations/fleet/vehicle-use-policy.md)
- [Sentricon install budgeting](/finance/sentricon-install-budgeting.md)
