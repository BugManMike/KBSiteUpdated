---
type: Runbook
title: Forwarding vendor invoices into Bill.com
description: Forwarding an invoice email to the Bill.com intake address with a Gmail template that carries the vendor, GL code and branch classification.
tags: [bill-com, payables, email]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 17frL_8xOPR83PGZR6P_ZNvqqvlIkQS6Vzva_1DQ0OBA
    resource: https://docs.google.com/document/d/17frL_8xOPR83PGZR6P_ZNvqqvlIkQS6Vzva_1DQ0OBA/edit
    title: How to forward invoices to Bill.com
status: draft
---

Vendor invoices arrive by email and enter Bill.com by being forwarded to its intake address. The
forward carries a Gmail template that supplies the coding Bill.com cannot infer.

Two things must be open before starting:

- the **Gmail account the vendor sent the invoice to**
- the **Accounts Payable Notes Sheet** — the cheat sheet that maps products to GL codes

# 1. Forward the invoice

Locate the email with the invoice attachment and review the attachment. Then **Forward**, and address
it to the Bill.com intake address `natrangreen@bill.com`.

# 2. Insert the template

**More options → Templates.** Which template to use depends on the invoice classification and where
the product ships to.

# 3. Fill in the details

| Field | What goes in it |
|---|---|
| **Vendor Name** | The entity the invoice came from and who will be paid. |
| **GL Code** | The account the cost belongs to. Look it up in the Accounts Payable Notes Sheet — the **veseris** tab. |
| **Invoice Number** | From the attached invoice. |
| **Total Amount** | The full sum payable on the invoice. |
| **Classify As** | **Houston** or **Austin**, taken from the ship-to address on the invoice. |

# 4. Send and confirm

Review that the coding is right and the attachment is still attached, then **Send**.

Then log in to Bill.com, open the **Inbox**, and confirm the invoice arrived and was processed.

> The GL-code lookup is documented as one specific tab — **veseris** — of the Accounts Payable Notes
> Sheet. Veseris is a single distributor, so that tab cannot be the right lookup for every vendor.
> Either the sheet has a tab per vendor and the procedure names only the one the author happened to be
> using, or codes for other vendors are found some other way. **Whoever owns the Accounts Payable
> Notes Sheet should say which.**

> The procedure names a template but does not say how many templates exist or what distinguishes
> them, beyond "classification of invoice and where the product ships to". A new bookkeeper cannot
> pick a template from this document alone.

# Related

- [Entering a bill from the Bill.com inbox](/finance/bill-com-bill-entry.md)
- [Processing bill payments in Bill.com](/finance/bill-com-bill-payments.md)
- [Where vendors send invoices](/finance/invoice-submission-address.md)
