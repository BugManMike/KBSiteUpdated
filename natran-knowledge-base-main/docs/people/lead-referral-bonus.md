---
type: Runbook
title: Lead referral bonus
description: How a technician or customer care agent is credited for referring a customer lead, and how the bonus report reaches payroll.
tags: [fieldroutes, compensation, commissions]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1IXUalLkXb9lCZ0FZL6Sdf5irQ5MUBXfsK91rGsgfIAU
    resource: https://docs.google.com/document/d/1IXUalLkXb9lCZ0FZL6Sdf5irQ5MUBXfsK91rGsgfIAU/edit
    title: Referral bonus
status: draft
---

**Technicians and customer care agents can refer qualified customer leads to the sales team and earn
a bonus** once the lead is won and the initial service is completed.

> **This is not the [employee referral bonus](/people/employee-referral-bonus.md).** That one pays
> $2,000 for referring a *person who gets hired*. This one pays for referring a *customer*. The two
> schemes share a name and nothing else.

# Step 1. Credit the referrer on the lead

Set the lead or subscription up as normal, and enter the technician's or agent's name in the
**Sales Rep 3** field.

# Step 2. Convert the lead

When the lead is ready to schedule, convert it to a subscription. **Sales Rep 3 carries over.** Once
the initial service is completed the subscription appears on the referral bonus reports.

# Step 3. Run the report

1. **Reports → Commissions.**
2. Select **Referral Bonus - Technician** or **Referral Bonus - Customer care** from the profile
   dropdown.
3. Select **Advanced** and enter **both offices**.
4. Choose the **date range** and click **Refresh**.
5. **Export to Excel** and send to payroll.

> **The bonus amount is not stated anywhere in the source** — only how to credit the referrer and
> how to produce the report. The value must be held in the commission profiles inside Fieldroutes.
> Anyone answering "what does a referral pay?" has nowhere in the documentation to look.

> **The credit depends entirely on someone remembering to fill in a free-text name field.** Sales
> Rep 3 is not validated against the employee list, so a misspelling, a nickname, or a blank means
> the referrer silently drops off the report. Compare
> [calculating salesperson commissions](/people/sales-commission-calculation.md), where the
> worksheet requires names to match Fieldroutes exactly.

# Related

- [Employee referral bonus](/people/employee-referral-bonus.md) — the separate hiring scheme
- [Calculating salesperson commissions](/people/sales-commission-calculation.md)
- [Fieldroutes user setup](/it/fieldroutes-user-setup.md) — where the referral bonus commission profile is assigned
- [Coupon codes](/finance/coupon-codes.md) — the `REFERRAL40` customer-side code
