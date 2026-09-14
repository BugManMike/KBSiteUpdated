---
type: Runbook
title: Calculating salesperson commissions
description: Running the monthly commission worksheet — importing Fieldroutes sales data, adding salespeople and profiles, and handling prior-period initials and chargebacks.
tags: [fieldroutes, compensation, commissions]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 11QcA7IDqlDxYQEPmRVkNb6gFo5YGi_n5Z8p9agcTmcg
    resource: https://docs.google.com/document/d/11QcA7IDqlDxYQEPmRVkNb6gFo5YGi_n5Z8p9agcTmcg/edit
    title: How to calculate salesperson commissions
status: draft
---

Commissions are calculated in a **Commission Worksheet** spreadsheet that reads Fieldroutes sales
data and applies each salesperson's rate, chargebacks and adjustments.

> **Commission is only earned once the agreement is signed *and* the initial payment is received.**
> That single rule is what drives the prior-period mechanism and most of the FAQ below.

# Produce a commission report

1. Open the **Commission Worksheet** and **make a copy**.
2. Run the Fieldroutes reports and import the sales data. *(The source links a Scribe walkthrough
   for this step rather than listing it — see the conflict note below.)*
3. *(Optional)* Add subscription IDs under **PriorPeriodInitialPayment** for any paid initials owed
   from earlier months.
4. Select the **CommissionReport** tab and enter the **salesperson's name** and the **start and end
   dates** for the month. The sheet calculates sales values, finds the employee's rate, and
   computes chargebacks and commission.

# Pay a commission missed because the initial was unpaid

1. Select the **PriorPeriodInitialPayments** tab.
2. **Enter the Fieldroutes subscription ID** in the yellow fields. The sheet pulls the sales data in
   and adds it to that month's commission.

# Add a new salesperson

1. Open the worksheet's **employeeLookup** tab.
2. Add the name in **`Last, First`** format. **It must match Fieldroutes exactly.**
3. Select the **Commission Profile** matching their employee agreement — see
   [employee agreement map](/people/employee-agreement-map.md).
4. Set **Use Contract Value** to **TRUE**. `FALSE` is legacy only; no new salesperson uses it.

# Add a commission profile

Rates live on the **commissionProfile** tab. Add a new column, name the profile in the header row,
and enter a rate against each sales-value band in the first column. For a flat rate, use the same
percentage on every row.

# Known behaviours

| Symptom | Cause |
|---|---|
| Subscription ID added but value still zero | The initial was never actually paid — check the Unpaid Initial report. |
| Initial missing from the Unpaid Initial report | It was written off as **bad debt**, which makes it permanently ineligible. Check the subscription's cancel reason. |
| Initial shows paid but pays no commission | Same cause — cancelled for bad debt and written off or sent to collections. |

**Excluding upgrade and downgrade cancels.** When a customer is upgraded or downgraded the original
subscription is cancelled as `SOLDALTER-UPGRADE` or `SOLDALTER-DOWNGRADE`. Further cancel reasons can
be added to the worksheet's exclusion list.

**Excluding a subscription from chargeback.** Flag it in Fieldroutes with **Exclude from sales
commission chargebacks**. Per the source, this is *"at the discretion of management and only when it
can be shown that proven processes were not followed."*

> **Bad debt silently destroys commission.** Writing an account off — see
> [recording bad debt](/finance/bad-debt-recording.md) and
> [sending accounts to collections](/finance/sending-accounts-to-collections.md) — makes the
> salesperson permanently ineligible for that sale, with no notification anywhere in either process.
> Three of the four FAQ entries in the source are people discovering this after the fact.

# Two vintages, two different worksheets — unresolved

> **Three documents in the wiki describe this same task, and they do not agree on which spreadsheet
> to use.**
>
> - **This document** (*How to calculate salesperson commissions*, last edited January 2024) uses a
>   **Commission Worksheet** with `employeeLookup`, `commissionProfile` and
>   `PriorPeriodInitialPayments` tabs.
> - **Sales Commission** (last edited June 2023) and **Sales commission proces** *(sic)* (May 2023)
>   are near-identical to each other and use a **different spreadsheet**, the *Natran sales
>   commission report*, with `UploadSales`, `uploadChargebacks`, `displaySettings`,
>   `calculateChargebacks` and `printReport` tabs. Both carry a banner reading *"This article is in
>   need of updates… Consult with management for guidance on latest processes."*
>
> This document is the newest and the only one not self-flagged as stale, so it has been treated as
> canonical. **But the two older documents carry the full step-by-step for importing the Fieldroutes
> reports, which this one replaces with a link to an external Scribe recording** — so the detailed
> import procedure now exists only against the older worksheet. **Whoever owns payroll needs to
> confirm which spreadsheet is live and retire the other two documents.**

# Related

- [Lead referral bonus](/people/lead-referral-bonus.md)
- [Payroll journal recording](/people/payroll-journal-recording.md)
- [Technician production pay](/people/technician-production-pay.md)
- [Recording bad debt](/finance/bad-debt-recording.md)
