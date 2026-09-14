---
type: Runbook
title: Holding service on past-due accounts
description: The daily Collect or Do Not Service loop — flagging past-due appointments, pushing unserviced subscriptions out of the job pool, and pulling them back once the balance clears.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-29T18:09:06Z
sources:
  - id: 1mFcV0-7dxgczuCzcNSeSSFN6TQrZkYf9rz5v2mxM3BQ
    resource: https://docs.google.com/document/d/1mFcV0-7dxgczuCzcNSeSSFN6TQrZkYf9rz5v2mxM3BQ/edit
    title: Account Receivable Process
  - id: 1gnrmNiWb_iddmS_cJvn7e1K30lZCPsjzdcHv5nQ_AG0
    resource: https://docs.google.com/document/d/1gnrmNiWb_iddmS_cJvn7e1K30lZCPsjzdcHv5nQ_AG0/edit
    title: Account Receivable Process
status: draft
---

Split out of [accounts receivable daily operations](/finance/accounts-receivable-daily.md) on
2026-07-29 — it is a distinct concept with its own lifecycle, not a step in the receivables
checklist.

**Three daily sub-processes, present only in the 2026 version of the source.** Two documents in the
same Drive folder carry the title *Account Receivable Process* and are not copies; both are recorded
in `sources` above, and neither title records which is which. The 2023 version does not contain this
material at all.

**The three form a loop:** hold service, push the subscription out of the job pool, then pull it
back when the balance clears. Each runs once a day off its own saved report.

# Collect or Do Not Service

Once a day. Pestroutes → **Customers** → saved report **`Audit - Past due appointment`**.

Check the **next day's** appointments for customers **15 days or more past due**.

- **Residential: 30 days old on the account. Commercial: 45 days.**
- **Some customers have special Net Billing terms** — check subscriptions and notes, they may get
  longer.

For those that qualify, open the appointment, add the flag **`Collect or Do Not Service`**, and add
notes telling the technician to collect payment or not service.

> **"15 days or more past due" and "residential 30 days / commercial 45 days" are two different
> measures** — one is invoice age, the other account age. The document does not say whether both must
> be true or the second overrides the first. **This decides whether a customer gets served**, so it
> is worth stating unambiguously.

> **TODO: the field half of this process is undocumented.** Nothing in the corpus covers how
> technicians are trained on the flag, what the appointment card shows them, or what happens when a
> flagged account is serviced anyway. Those are the open questions on Linear **NLDR-100**, which also
> names customer 35283 as an account that stayed on the schedule without the flag. Do not infer the
> field procedure from this document — it describes the office side only.

# Custom Date Not Serviced Collections

Once a day. Saved report **`Audit - Appointment Collect Flag`**.

Check the **previous day** for not-serviced appointments still carrying a past-due balance. For each:

1. Customer account → **Subscriptions** tab.
2. For each subscription that could not be serviced, **set a Custom Date a few months out** so it
   leaves this month's job pool.
3. **Info** tab → add the generic flag **`Collections: Collections`**.

# Remove Custom Dates for Paid Accounts

Once a day. Saved report **`Audit - Collection Custom Date`**.

Look for customers now at a **zero balance**. Check **Notes** or **Admin** tabs for why the custom
date was set. **If it was for a past-due balance**, remove the custom date from each subscription
that needs servicing, then remove the **`Collections: Collections`** flag from the Info tab.

> **This is the step that gets forgotten** — without it a paying customer stays out of the job pool
> for months. It has no trigger other than running the report daily.

# Related

- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md) — the checklist this
  was split out of; declined payment info, auto-pay batches, check entry and deposit.
- [Collections calling process](/finance/collections-calling-process.md) — the call cadence that
  escalates a balance toward a demand letter and an agency.
- [Collections call and text scripts](/finance/collections-scripts.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md) — the harder stop
  once an account is written off: a red note reading `DO NOT SERVICE ACCOUNT THIS CUSTOMER IS SENT TO
  COLLECTIONS`.
- [Recording bad debt](/finance/bad-debt-recording.md)
- [DSO tracking](/finance/dso-tracking.md)
