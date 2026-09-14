---
type: Runbook
title: Refunding partial payments
description: Refunding part of an invoice — the partial refund in Authorize.net, then reversing the full payment in Fieldroutes and discounting the invoice back to zero.
tags: [authorize-net, refunds]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1vzZmzG2OnqhZNfVOC-E8I4YWUJxCh5_3ONQRr0RLerA
    resource: https://docs.google.com/document/d/1vzZmzG2OnqhZNfVOC-E8I4YWUJxCh5_3ONQRr0RLerA/edit
    title: Refund Process for Partial Payments
status: draft
---

A partial refund is when a customer is refunded **part** of their invoice rather than all of it.
Fieldroutes has no partial-refund action, so the money moves in the gateway and the CRM is then made to
agree with it by reversing the whole payment and discounting the difference.

# Steps

1. **In Authorize.net, do the partial refund.** The gateway is where the money actually moves.
2. **In Fieldroutes, open the customer's account and reverse the full payment** the customer made.
3. **Discount the original invoice by whatever was refunded.**

   **Use the subtotal, not the gross** — the discount automatically removes the matching tax
   adjustment. In the source's worked example the discount entered is **$100** while the actual refund
   was **$108**, the difference being sales tax.
4. **Create a coupon and discount the invoice down to zero.**
   - Invoices → **Add Payment**
   - Enter the coupon details needed to bring the invoice balance to zero
5. **Add a note on the customer's account** explaining what happened.

> **The note example is missing.** The source ends on "Here's an example:" with nothing after it, so the
> wording of the account note is not recorded anywhere. Given steps 2 to 4 leave a reversal, a discount
> and a coupon on the account, **the note is the only thing that explains why** — and it is the one part
> nobody wrote down.

> **A three-entry workaround stands in for a partial refund.** Reversing the full payment, discounting
> the subtotal, then couponing the remainder to zero reaches the right balance, but it does not leave a
> record that reads as "partial refund" to anyone looking later. It also means the refunded tax is
> handled implicitly, by the discount mechanism, rather than being stated.

> **Step 1 links to a separate ACH/eCheck refund procedure** elsewhere in the wiki. That document was
> not part of this batch, so the gateway-side detail is not yet in the bundle — only the Fieldroutes
> side is complete here.

# Related

- [Waiving fees and applying account credit](/finance/applying-account-credit.md)
- [Handling returned ACH payments](/finance/returned-ach-payments.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
