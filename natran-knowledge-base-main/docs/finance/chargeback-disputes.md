---
type: Runbook
title: Chargeback dispute and rebuttal
description: Responding to a credit card chargeback end to end — finding the dispute, freezing the account, submitting a rebuttal with the signed agreement, and adjusting the account on the outcome.
tags: [transfirst, disputes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1TQDhSyhkEki_Dvi6YI0euBQJc9YN-a-F6O55BZe-h2w
    resource: https://docs.google.com/document/d/1TQDhSyhkEki_Dvi6YI0euBQJc9YN-a-F6O55BZe-h2w/edit
    title: Chargeback dispute & rebuttal process
status: draft
---

**What a chargeback is.** A credit card chargeback — or "merchant dispute" — is initiated by a
cardholder asking for a refund on a transaction they believe was unauthorized or not as described. The
card issuer or acquiring bank can also start one, for fraud, processing errors or card-network rule
violations. The issuer investigates and may reverse the transaction, returning funds to the cardholder.
**If the chargeback succeeds the company is liable for the disputed amount plus fees and penalties.**
As the merchant, the company is responsible for investigating and responding.

# 1. Find the dispute

1. Sign in at <https://translink.transfirst.com/>.
2. Under **Chargeback/Retrieval Report**, select **Detail**.
3. Search by **Cardholder Number** or **Date Range** — the criteria come from the notification email
   from merchant services.

# 2. Locate the account

The dispute letter carries the original transaction date and amount plus a partial card number
including the last four digits. That is enough to find the account.

1. Fieldroutes → **Billing** → **Payment History**.
2. Select the **Transaction Date** from the dispute letter and enter the last four in the **Last 4 #'s**
   field.
3. **Refresh.**
4. Find the matching amount and customer name.
5. **Review the notes on the account for known issues.** Consult management as needed.

# 3. Research

1. Review the notes on the account.
2. **Confirm a signed agreement is on file.**
3. **Decide with management whether the dispute has merit or a rebuttal should be submitted.**
   - **Accepting the dispute** — no response needed. If service is still active, ask management whether
     to cancel.
   - **Submitting a rebuttal** — continue to step 4.

# 4. Freeze the account and notify the customer

The point of this step is to stop servicing an account that is in dispute.

1. Flag the account **Merchant service dispute** — the saved report **EOW: Chargeback disputes** runs
   weekly off this flag.
2. Add a **red note**:

   > Customer has disputed a credit card transaction. Do not schedule or service location. Consult with
   > management if there's any questions.

3. **Billing** → **Billing Info** → change the auto-pay dropdown to **No Auto Pay**.
4. Freeze active subscriptions: **Admin** → **Freeze** → cancel reason **Chargeback Dispute**. These
   may need unfreezing if the dispute resolves — see step 6.
5. Email the customer: **Notes** → **Send Email** → category **Chargeback Response Email**.

**Subject:** Response regarding your recent credit card dispute

> Hello,
>
> We hope this message finds you in good health. We are writing to provide you with important
> information regarding a recent dispute we received from your credit card and/or bank.
>
> To ensure a smooth resolution and prevent any further complications, we have taken the following
> steps:
>
> 1. Any auto-pay settings have been temporarily disabled for your convenience.
> 2. While we work to resolve the dispute in question, we have suspended your service temporarily. As a
>    result, any currently scheduled appointments will be canceled. Rest assured, we'll do our best to
>    resolve this matter promptly.
>
> We understand that unforeseen issues can arise, and we kindly ask you to get in touch with us to help
> us resolve this matter. Our dedicated customer care team is ready to assist you and address any
> inquiries you may have.
>
> In addition, we want to bring to your attention a couple of other points:
>
> - As part of the dispute process, your bank or credit card company may have withdrawn funds from our
>   bank account, which has resulted in a deficit in your account balance. This portion may be
>   considered outstanding and could be subject to late fees and interest, as outlined in your
>   contract.
> - Given that the matter has already been disputed with your credit card and/or bank, we will require
>   written confirmation from them stating that the matter has been resolved and that funds have been
>   returned to our bank account.
>
> We kindly request that you reach out to us at your earliest convenience so that we can work together
> to swiftly resolve this issue. Your patronage is highly valued, and we are committed to ensuring a
> satisfactory resolution for you.
>
> Thank you for your attention to this matter, and please do not hesitate to contact us if you have any
> questions or concerns.
>
> Sincerely,
> Customer Care Department
> Natran Green Pest Control
> 713-900-1994

# 5. Submit the rebuttal

1. Click **Send**.
2. **Contact Name** — your own name.
3. **Reference number** — the Fieldroutes customer ID.
4. Select the rebuttal reason. Typical ones:
   - Full/partial refund issues
   - No record of cancellation or failure to follow policy
   - Service was rendered, no credit due
   - Addressed cardholder's specific claims in rebuttal
5. Select **Online Rebuttal** from the Action dropdown.
6. Write a brief description in the cover sheet field explaining why the dispute is being challenged.
   The example given: *"Customer signed 12-month contract and is responsible for a monthly fee as per
   their signed agreement. Signed agreement is attached."* Consult management.
7. **Attach the signed agreement** → **Upload Text & File to Case** → confirm with **Yes**.

# 6. The outcome

A determination arrives from merchant services **within a few weeks**, saying whether the rebuttal was
won or lost.

## If lost

Merchant services have already pulled the funds and returned them to the customer, so the balance is
still due.

- **Customer Account** → **Invoices** → open the disputed transaction → **Actions** → **Reverse
  Payment** → **Continue**. **Not refund** — no money is moving; this records that the amount is owed
  again.
- **Consult management** on whether to continue service, keep it frozen, or unfreeze. Case by case.
- Decide whether the balance goes to
  [collections](/finance/sending-accounts-to-collections.md).
- Update the red note:

  > Chargeback dispute was lost and the customer balance was sent to collection. Do not schedule or
  > service location. Consult with management if there's any questions.

## If won

- **No payment reversal.**
- Consult management on continuing or cancelling service. Case by case.
- **Unfreeze subscriptions and reschedule cancelled appointments.**
- Re-activate auto-pay if the customer is in good standing and continuing.
- Remove or update the red note. If the customer had cancelled before the chargeback, note that the
  dispute was settled but the customer may need to provide another payment method.

# Final step

**Remove the Merchant service dispute flag.** It exists only to track active disputes.

> **Winning the rebuttal and keeping the customer are treated as separate decisions, both "case by
> case", with no guidance either way.** Management is consulted at four separate points with no stated
> criteria. That is workable for a rare event; it does mean two operators would handle the same
> chargeback differently.

> The source embeds a **Scribe walkthrough** for reversing a payment. The recording itself does not
> survive into this bundle — the reversal steps are written out in full above.

# Related

- [Handling returned ACH payments](/finance/returned-ach-payments.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md)
- [Transworld dispute process](/finance/transworld-disputes.md)
- [Applying late fees and interest](/finance/late-fees-and-interest.md)
