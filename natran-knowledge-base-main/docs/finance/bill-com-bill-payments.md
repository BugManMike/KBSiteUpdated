---
type: Runbook
title: Processing bill payments in Bill.com
description: Filtering unpaid bills down to those approved, then reviewing and confirming payment so Bill.com releases it on the process date.
tags: [bill-com, payables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1UAHQ_Rb7bCTDk6DxGduRLKxvaLyVPsz52EIE0PR7jdg
    resource: https://docs.google.com/document/d/1UAHQ_Rb7bCTDk6DxGduRLKxvaLyVPsz52EIE0PR7jdg/edit
    title: How to process bill payments
status: draft
---

Only **approved** bills get paid. The filter in step 2 is what enforces that.

# 1. Open the unpaid bills

Sign in to Bill.com → **Bills** → **unpaid bills**.

# 2. Filter to approved

Show filter options → **Approval Status** → **Approved** → apply the filter.

# 3. Select and review

Click the invoice number to open the bill, and check the **process date**, **payment amount** and
**payment account**.

# 4. Review and pay

**Review & Pay.** The payment amount, process date and payment account can still be edited here.
Review the payment details, then confirm.

# 5. Confirm what happened

Once processed, the bill shows the full process and payment details. Bill.com updates the status as
the payment progresses, and **the vendor receives it on the process date** — not on the day it was
confirmed.

> The document treats the **Approved** filter as the whole of approval control but never says who
> approves a bill, against what limit, or how a bill reaches Approved. The approval step itself is
> undocumented; only the act of filtering for its result is written down. **Whoever owns AP should
> document the approval rule**, since it is the control that separates entering a bill from paying
> one.

# Related

- [Entering a bill from the Bill.com inbox](/finance/bill-com-bill-entry.md)
- [Setting up vendor payment details in Bill.com](/finance/bill-com-vendor-payment-setup.md)
- [Accounting schedule of events](/finance/accounting-schedule-of-events.md)
