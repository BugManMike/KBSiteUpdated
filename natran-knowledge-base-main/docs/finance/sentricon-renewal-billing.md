---
type: Runbook
title: Submitting Sentricon renewals to Corteva
description: The monthly renewal submission to Corteva, including the pending-cancel review and inactive-site audit that stop the company paying to renew subscriptions it no longer has.
tags: [fieldroutes, vendor-billing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1tA1f-BoWFiLOI0xFcUtETEA8XB1KTNUAzA7u2Jl4H3g
    resource: https://docs.google.com/document/d/1tA1f-BoWFiLOI0xFcUtETEA8XB1KTNUAzA7u2Jl4H3g/edit
    title: How to submit a Sentricon renewal to Corteva for billing
status: draft
---

**Sentricon systems renew annually, but the report runs monthly** — each month's worth of renewals is
submitted electronically to Corteva, who then bill for them.

The first two steps exist to stop the company **paying Corteva to renew subscriptions it is about to
lose or has already lost.** Run this before
[submitting new installations](/finance/sentricon-initial-billing.md).

# 1. Review pending cancels

Check that nothing being renewed is already pending cancellation.

1. **Customers** → **Saved Reports** → **Pending Sentricon Cancels**.
2. Review the report. **If the initial date for any pending cancel falls in the same month, raise it
   with management** and ask whether to renew.

# 2. Audit for inactive sites

This ensures only active Sentricon subscriptions get paid for.

1. Fieldroutes → **Reporting** → **Sentricon**.
2. Select **Sentricon Disconnected Site** on the left.
3. Under the **Active** column, look for sites still showing active. **If there are none, go to step
   3.**
4. For each active site: **click the Site ID number** → **Inactivate** → **Save Changes** → back arrow
   to the previous page.
5. **Refresh** and confirm every site now shows `False`.

# 3. Run the report and submit

Fieldroutes → **Reporting** → **Sentricon** → **Sentricon UI pages** → the **Renewals** tab.

1. **Select Branch** and choose a branch.
2. Enter the **start date** and **end date** for the month being reported.
3. A list of units ready for renewal appears. **Select All**, or tick individual sites.
4. **Untick any pending-cancel account management does not want renewed** — from step 1.
5. **Save Renewed** submits the units to Corteva for billing.
6. **Repeat for every remaining branch.**

# Billing turnaround

An electronic bill usually arrives **within 24 hours** of submitting.

> The document is titled and framed as a **renewal** process, but step 2 has the operator
> **inactivating disconnected Sentricon sites** in Fieldroutes — a data-correction task with
> consequences beyond this month's billing. It is in the right place for the billing outcome; it is
> worth knowing that the monthly billing run is also when site records get cleaned up.

> **"Select All" in step 3 is the default, and the exclusions in step 4 are manual.** The safe ordering
> would be the reverse. Anyone who runs step 3 without having read step 1 renews the pending cancels.

# Related

- [Submitting Sentricon installations to Corteva](/finance/sentricon-initial-billing.md)
- [Entering a bill from the Bill.com inbox](/finance/bill-com-bill-entry.md)
