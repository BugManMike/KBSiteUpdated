---
type: Runbook
title: Setting up vendor payment details in Bill.com
description: Adding an international contractor as a Bill.com vendor and attaching the USD bank details from their Wise account so they can be paid.
tags: [bill-com, payables, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1ROGSP51b5M9-iZgjkYoCW9MRLyJTX1253uU4xMC-8qY
    resource: https://docs.google.com/document/d/1ROGSP51b5M9-iZgjkYoCW9MRLyJTX1253uU4xMC-8qY/edit
    title: Payment Details Setup in Bill.com Process
status: draft
---

This is the setup path for **international contractors** — the virtual assistants — who are paid in
USD through a Wise account rather than a domestic bank.

# 1. Add the vendor

Log in to Bill.com → **Actions** (left side of the page) → **Add Vendor**.

- **Business Name / Legal Full name** — the vendor name
- **Vendor location** — **International**
- **Country** — the vendor's country
- **Address Line** — the vendor's local address
- **Contacts** — email address and phone number
- **Vendor type** — **Individual**

**Continue.**

# 2. Add the payment information

Continuing from step 1 leads to the *Add payment information* page.

1. Click **I'll enter the details myself**.
2. Change the vendor's **bank location** to **United States**.
3. Change the **Invoice Currency** to **United States Dollars**.
4. Confirm the bank details with the VA or vendor, taken from their **Wise USD currency account**.
5. Enter the **routing number**, **account number** and **account holder's name** from that Wise
   account.
6. **Save** — top right of the page.

The vendor location is International but the bank location is United States. That is not a
contradiction: Wise issues the contractor a USD receiving account with a US routing number, which is
what Bill.com pays into.

> **The source is mis-numbered.** Its second section is headed "Step 21" and opens by referring back
> to "number 10 from Step 1", so it is plainly **Step 2**. Corrected in this transcription; the source
> still reads `Step 21`.

> Bank account and routing numbers are **deliberately not recorded here**. They are per-vendor, they
> are confirmed with the vendor at the time of setup, and the knowledge base is not the place for
> them.

# Related

- [Processing bill payments in Bill.com](/finance/bill-com-bill-payments.md)
- [Forwarding vendor invoices into Bill.com](/finance/bill-com-invoice-intake.md)

> The wiki also holds a `VA Sign-up and Invoicing process-Finance` document covering the hiring side
> of the same contractors. It was **not** converted in this batch — it belongs with the VA
> onboarding material rather than with payables setup.
