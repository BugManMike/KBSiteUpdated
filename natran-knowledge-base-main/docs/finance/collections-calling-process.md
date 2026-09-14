---
type: Runbook
title: Collections calling process
description: Building the weekly collection worksheet from Fieldroutes, pacing the call list, and the contact cadence that escalates an account to a demand letter and then an agency.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1NptHVVct-tPOdGWdwiWVFBpPXmA7s7VF3BpRSq2TNGo
    resource: https://docs.google.com/document/d/1NptHVVct-tPOdGWdwiWVFBpPXmA7s7VF3BpRSq2TNGo/edit
    title: Collections Proven Process
status: draft
---

# 1. Build the weekly worksheet

1. Open the **Collection Weekly Report** spreadsheet.
2. Fieldroutes → **Billing → Collections**.
3. **Days Overdue → Custom Range → 0 through 365** → Refresh → **Actions → Export to CSV**.
4. **Switch office and repeat** for every branch.
5. Duplicate the **`TEMPLATE`** tab and rename it with the **start date of the week**.
6. Select **cell A3** → **File → Import** → the first CSV → **Replace Data at Selected Cell**.
7. Scroll to the **first empty cell in column A** → import the second CSV the same way. This merges
   both branches into one working list.
8. Sort by **column F, Z to A** — oldest collections at the top.

# 2. Pace the list

**Calls per day = people on the list ÷ working days in the week.**

Add **5 to 10 extra calls per day**, because you will want to contact the same customer more than
once. **Best practice: call again the next day if they promised to call back or said they were busy.**

# 3. Call and take notes

1. Open the customer card in Fieldroutes **before** calling.
2. **Confirm the balance is still outstanding.** Zero balance — mark paid and move on.
3. **Review notes for outstanding issues.** If there is one, consult management on when it will be
   resolved before chasing payment.
4. Call and text using [collections scripts](/finance/collections-scripts.md).
5. Add a note using the **Billing Notes Type**, recording **the date and method** of each attempt.
6. Update the worksheet.

> Step 3 is the one that protects the relationship — chasing a customer for money while an unresolved
> service complaint sits on their account is how a collection call becomes a cancellation.

# Contact cadence

| Past due | Contacts per week |
|---|---|
| 0–30 days | Minimum 1 |
| 30–60 days | Minimum 1 |
| 60–90 days | Minimum 2 |
| **Day 90** | **Send demand letter** |
| **Day 100** | **Remit debt to ARM collections** |

> The 0–30 and 30–60 bands both say "minimum 1 contact per week", so **the split between them does
> nothing.** Either the first band should be lighter or the second heavier.

> The table's day-90 demand letter and day-100 remittance sit alongside a FAQ answer saying accounts
> "freeze and be referred to collections" after 90 days, and another saying to contact weekly "for 8
> weeks" — which is 56 days, not 90. **Three timelines for one ladder.** The table is the most
> specific and is the one to follow.

See [sending accounts to collections](/finance/sending-accounts-to-collections.md), which flags that
the agency itself — ARM or TSI — is unresolved.

# Questions that come up

**Customer has paid.** Update the worksheet and Fieldroutes. Nothing further.

**Customer says they will pay online.** **Advise them they will have to pay the late fees if they pay
online. If you take payment now, you can waive the late fees.**

**Waiving late fees.** **Only when payment is made in full on the regular balance.** Needs Fieldroutes
permission — ask the system admin.

> That pair creates a real incentive: paying the collector is cheaper than self-serving online. Worth
> knowing it is deliberate rather than a quirk.

**PayPal, Venmo, Cash App.** **Not accepted** unless special arrangements are made. Consult
management; steer the customer to a credit card.

**How many attempts?** At least **once a week for 8 weeks**. Technicians will also attempt to collect
at time of service, and **will not service the account** if unsuccessful. After 90 days the account
freezes and goes to collections.

**Customer not responding.** **Call every number on the account.** Make a **minimum of 6 attempts**
before treating it as bad debt, then refer to management.

**Customer says they cancelled but a balance remains.** **If the balance predates cancellation it is
due and payable.**

**Customer says they mailed a check.** Note the pending payment in the worksheet and Fieldroutes. **If
it has not arrived by the following week, reach out again.**

**Customer says they paid the technician.** Contact the service manager to check whether the technician
is holding payment. Note it.

**Customer never pays.** Account frozen, balance written off as bad debt after 90 days, lien notice
sent, balance referred to an agency.

**Commercial account going out of business.** **Refer to management.**

**Am I succeeding?** Measured by DSO — see [DSO tracking](/finance/dso-tracking.md), which also flags
that the stated 3-to-4-day target is inconsistent with the standard DSO formula this document cites.

# Related

- [Collections scripts](/finance/collections-scripts.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md)
- [DSO tracking](/finance/dso-tracking.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
