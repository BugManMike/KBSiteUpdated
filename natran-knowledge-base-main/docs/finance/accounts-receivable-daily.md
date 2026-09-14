---
type: Runbook
title: Accounts receivable daily operations
description: The recurring receivables work — fixing declined payment info, running auto-pay batches, and entering and depositing checks.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1mFcV0-7dxgczuCzcNSeSSFN6TQrZkYf9rz5v2mxM3BQ
    resource: https://docs.google.com/document/d/1mFcV0-7dxgczuCzcNSeSSFN6TQrZkYf9rz5v2mxM3BQ/edit
    title: Account Receivable Process
  - id: 1gnrmNiWb_iddmS_cJvn7e1K30lZCPsjzdcHv5nQ_AG0
    resource: https://docs.google.com/document/d/1gnrmNiWb_iddmS_cJvn7e1K30lZCPsjzdcHv5nQ_AG0/edit
    title: Account Receivable Process
status: draft
---

> **Two documents in the same folder carry this exact title, and they are not copies.** Both are
> recorded above. The 2026 version adds three daily past-due sub-processes and an equipment pickup
> step; the 2023 version has the TSI submission procedure and a cadence note the newer one dropped.
> **Neither is complete.** Differences are flagged at each point below. **One should be retired after
> merging what the other has.**

# Fix declined payment info

Pestroutes → **Billing** → top right **Update Actions** → select **Fix Payment Info** and
**Soft Decline** → **Update**.

> **The 2023 version adds: "This process is to be completed every Wednesday and Friday at 9 am."**
> The 2026 version gives no cadence at all. That schedule appears nowhere else in the corpus.

# Run batches

Pestroutes → **Billing → Batch Charges**. This charges all accounts on auto-pay.

**Run batches for each branch, daily.**

# Check payments

**Entering a check:**

1. Customer card → **Invoices → +Add Payment → Check**.
2. Enter the payment amount, then **confirm the same amount again**.
3. **Check number — exactly as written on the customer's check.**
4. If the customer specified an invoice, select **Apply first** and choose that invoice number.

**Depositing them:**

1. **Billing → Payment History → Checks** → date range → **Export to CSV**.
2. **Print the list and paperclip it to the physical checks.**
3. **Give the list and the checks to Mike Arndt.**

> The paper handoff is the control — the printed list is what gets matched against the bank in
> [month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) step 14, where Pestroutes
> check payments are reconciled to "Remote Deposit" entries.

> The 2026 version titles this section **"ACH Check Payments"** while the 2023 version says
> **"Check Payments"**. The steps are identical and describe physical checks, not ACH. The newer
> title looks like an error.

# Hold service on past-due accounts

**Moved out of this document 2026-07-29** — see
[holding service on past-due accounts](/finance/holding-service-past-due-accounts.md). It is the
daily *Collect or Do Not Service* loop: flag the appointment, push the subscription out of the job
pool, pull it back when the balance clears. It also runs once a day, so it belongs in the daily
cadence alongside the steps above; it was split out because it is a distinct concept with its own
lifecycle rather than another item on this checklist.

# Related

- [Holding service on past-due accounts](/finance/holding-service-past-due-accounts.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md)
- [Collections calling process](/finance/collections-calling-process.md)
- [DSO tracking](/finance/dso-tracking.md)
- [A/R and payroll agent duties](/finance/ar-payroll-agent-duties.md)
