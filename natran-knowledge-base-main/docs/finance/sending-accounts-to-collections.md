---
type: Runbook
title: Sending accounts to collections
description: Writing an account off in Fieldroutes, submitting it to the collection agency, and recovering company equipment from the property.
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

Reached after the escalation ladder in
[collections calling process](/finance/collections-calling-process.md) runs out — **day 100**, per
that document.

# Which agency

> **The corpus names two, and does not say which is current.**
>
> - **TSI** (`my.tsico.com`) — the 2023 document gives a full submission procedure.
> - **ARM** — the 2026 document has an ARM section linking a separate procedure, and
>   [collections calling process](/finance/collections-calling-process.md) says
>   *"Day 100 — Remit debt to ARM collections."*
>
> **The 2026 document does both**: its intro says to "move collection-ready customers to TSI" while
> its body section is headed ARM. So the newer document points at both agencies in the same breath.
>
> Best reading: **ARM is current and TSI is legacy**, on the strength of the calling process naming
> ARM at day 100. **But that is inference, and this decides where customer debt gets sent.** Confirm
> before submitting anything.

# Submitting to TSI

From the 2023 document. Retained because **the newer document dropped the procedure without
replacing it** — it links an ARM document that sits outside the enumerated wiki tree and has not been
read.

1. `my.tsico.com` → **Dashboard → Profit Recovery → Submit Accounts**.
2. **Debtor Type** — Individual or Business.
3. First and last name, **Attention (both spouses)**, phone, email.
4. **Reference #** — use invoice numbers.
5. **Date of Debt** — the last day the customer was serviced.
6. Add any additional contact info.
7. **Review before Starting the service.**
8. **Start Service → Profit Recovery.**

# Writing it off in Fieldroutes

Once submitted:

1. Customer card → **Invoice → Coupon/Credit**.
2. **Payment Amount** — the total balance.
3. **Description:** `BAD DEBIT WRITE-OFF` plus the date.
4. **Customer Payment Notes:** `ACCOUNT SENT TO COLLECTIONS`.
5. **Payment Flags:** select **Write Off**.
6. **Add a Red Note:** `DO NOT SERVICE ACCOUNT THIS CUSTOMER IS SENT TO COLLECTIONS`.

> `BAD DEBIT` is a typo for *BAD DEBT* in both source documents. **Left as written** — it is the
> literal string used in existing records, and changing it would break the search that
> [DSO tracking](/finance/dso-tracking.md) relies on when it filters coupon codes for bad debts.
> Worth fixing deliberately, in both the docs and the data, rather than piecemeal.

> The red note wording differs between versions — the 2023 one reads `DO NOT THE SERVICE ACCOUNT...`.
> Use the 2026 wording above.

# Recover the equipment

**Only in the 2026 version.** If applicable, **schedule an equipment pickup** for any:

- **RBS**
- **Mosquito Traps**
- **Sentricon Stations**

> This is the step with money attached — those are company assets sitting on the property of someone
> who has stopped paying. **The 2023 version omits it entirely.** Anyone following the older document
> writes off the debt and leaves the hardware behind.

# Then record it

The write-off feeds bad debt reporting — see [DSO tracking](/finance/dso-tracking.md) step 4, which
filters Payment History on coupon codes for bad debts.

# Related

- [Collections calling process](/finance/collections-calling-process.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [DSO tracking](/finance/dso-tracking.md)
