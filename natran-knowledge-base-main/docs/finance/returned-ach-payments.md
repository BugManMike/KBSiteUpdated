---
type: Runbook
title: Handling returned ACH payments
description: Finding settled ACH returns in Authorize.net, reversing the payment, charging the $25 NSF fee, notifying the customer, and deciding whether ACH stays allowed on the account.
tags: [authorize-net, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1Zi-h5o5gJ-MPYMsvg3LYE0W-7KsVUvzxlpgc-HoqOX4
    resource: https://docs.google.com/document/d/1Zi-h5o5gJ-MPYMsvg3LYE0W-7KsVUvzxlpgc-HoqOX4/edit
    title: How to check for returned ACH payments
status: draft
---

The return shows up in the payment gateway, not in the CRM — so this always starts in Authorize.net
and works back to the customer.

# 1. Find the returns

1. Sign in at <https://login.authorize.net/>.
2. **Reports** at the top of the page.
3. **Returns** on the left.
4. **Settled Returns** from the dropdown.
5. Select the start and end date.
6. **Run Report** — this lists the ACH payments that were returned.
7. **Click the Original Trans ID** to get the customer's name.

# 2. Reverse the payment

1. Find the customer in Fieldroutes by name or address from step 1.
2. Check the **Invoice** history.
3. Locate the ACH payment matching the date and amount.
4. Click the transaction to open the payment screen.
5. **Actions** → **Reverse Payment** → **Continue**.

# 3. Add the NSF fee

**Invoices** → **+ New Invoices** → **$25** → service type **NSF Fee** → **Create**.

# 4. Note the account

**Add Note** → note type **Billing Notes**. **Make the reason match what Authorize.net states** —
Insufficient Funds, Account Closed, Invalid Account Number, and so on:

> ACH transaction was returned for Insufficient Funds on MM/DD/YY. Payment was reversed and customer
> charged a $25 NSF fee.

# 5. Contact the customer

**First check whether this account has had previous returned ACH payments** — it changes what happens
in step 6.

Email via **Notes** → **Send Email**, subject **Your recent payment was returned**, category **NSF
returned payment**:

> Dear Customer,
>
> We hope this message finds you well. We're writing to inform you that your recent ACH payment was
> returned by your bank. Unfortunately, as a result, a $25 Non-Sufficient Funds (NSF) fee has been
> applied to your account. To prevent further charges, we've temporarily deactivated your auto-pay
> settings.
>
> To avoid any service disruptions please contact our office at 713-900-1994. Any of our customer care
> agents can assist you with updating your payment information. You can also update your payment
> information by visiting <https://natrangreen.pestportals.com/> and selecting the "Wallet" option.
>
> We apologize for any inconvenience this may cause and appreciate your prompt attention to this
> matter. Thank you for your understanding and cooperation.
>
> Sincerely,
> Billing Department
> Natran Green Pest Control
> 713-868-5588 ext. 3

# 6. Update the payment method

- **Update the payment method.** If the customer has repeated insufficient-funds history, **get a
  credit card instead**.
- **If the customer had a reasonable explanation** — changed banks, new account number, forgot to tell
  us — update the bank account on file and **delete the old one**.
- **If ACH can no longer be accepted**, add a **red note**: *"ACH Payments are not allowed due to
  repeated return payments."*

> **The email gives the customer two different phone numbers** — 713-900-1994 in the body and
> 713-868-5588 ext. 3 in the signature. One of them is wrong, or one is a legacy number.
> **Customer-facing, so worth fixing at source.**

> **The email says auto-pay has been "temporarily deactivated" but no step in this procedure
> deactivates it.** Either the reversal does it automatically, or the customer is being told something
> untrue. The [chargeback procedure](/finance/chargeback-disputes.md) has an explicit "change the
> auto-pay dropdown to No Auto Pay" step; this one does not. **Needs confirming.**

> **"Repeated" is never defined** — step 6 turns on whether the history counts as repeated, and the
> judgement is left to the operator with no threshold.

# Related

- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [Chargeback dispute and rebuttal](/finance/chargeback-disputes.md)
- [Applying late fees and interest](/finance/late-fees-and-interest.md)
