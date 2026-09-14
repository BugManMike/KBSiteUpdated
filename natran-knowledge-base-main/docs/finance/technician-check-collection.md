---
type: Runbook
title: Technician check collection
description: How a cheque handed to a technician in the field is recorded, banked by the branch, and posted to the customer's account.
tags: [fieldroutes, receivables, technicians]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1MEgZ9v5B8gdNzQnK_AvrYmHYeLbd_zpuVb1WPxWutWk
    resource: https://docs.google.com/document/d/1MEgZ9v5B8gdNzQnK_AvrYmHYeLbd_zpuVb1WPxWutWk/edit
    title: Technician check collection process
status: draft
---

A cheque collected in the field passes through three hands: the technician records it, the branch
banks it, and accounts receivable posts it.

# Technician

1. **Enter the cheque payment** against the customer's account in the Fieldroutes app.
2. **Write the customer ID on the cheque memo line.**
3. Drop the payment in the office's **designated receptacle**.

# Branch

> **The corporate office differs** — corporate **scans** cheques. Other branches deposit at a local
> bank branch.

1. Run the **Tech Collection Report** (Reporting → Tech Collection Report) and confirm every cheque
   is accounted for.
2. **Deposit weekly** at a branch of the company's bank.
3. **Photograph the deposit receipt** and send it to accounts receivable.

# Accounts receivable

Run the Tech Collection Report and **post the payment to the customer account.**

> **The source names the deposit bank account number in plain text.** It has not been copied into
> this bundle. **That number should be removed from the source document** — it sits in a wiki page
> readable by every technician, and a deposit account number plus the company name is enough to
> originate a debit. This is the same class of finding as the
> [HR email templates](/people/hr-email-templates.md).

> **The cheque is recorded twice and reconciled once.** The technician enters the payment in
> Fieldroutes at step 1, and AR "posts payment to the customer account" at the end — against the
> same report. Whether the second step is a duplicate entry, an approval, or a reconciliation is not
> stated. Somebody who does this every week knows; the document does not.

> **Nothing covers a cheque that never arrives.** Between the technician's receptacle drop and the
> branch's weekly bank run, custody is a physical box and a weekly report. There is no count, no
> sign-off, and no step for a cheque on the report that is not in the box.

# Related

- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [Holding service on past-due accounts](/finance/holding-service-past-due-accounts.md)
- [Checking for returned ACH payments](/finance/returned-ach-payments.md)
- [Equipment and inventory responsibility](/operations/fleet/equipment-and-inventory-responsibility.md)
