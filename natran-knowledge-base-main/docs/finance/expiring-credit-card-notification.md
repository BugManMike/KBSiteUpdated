---
type: Runbook
title: Expiring credit card notification
description: The monthly email to active customers whose card on file is about to expire, run from the Fieldroutes expiring-cards report.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 10ZMD02MfcJsfnNzbyo5kienHakw2BBy_P0my8A39jYY
    resource: https://docs.google.com/document/d/10ZMD02MfcJsfnNzbyo5kienHakw2BBy_P0my8A39jYY/edit
    title: Expiring credit card notification
  - id: 1kA79MP_17iplRMY4Rfj57NOGeIRVU041-Un21vcOJkc
    resource: https://docs.google.com/document/d/1kA79MP_17iplRMY4Rfj57NOGeIRVU041-Un21vcOJkc/edit
    title: The Expired Credit Card Processs
status: draft
---

**Each month an email goes to active customers whose card on file is set to expire.** Frozen customers
do not need to be notified.

Catching the expiry before it happens is what stops the card failing and the account
[going past due](/finance/accounts-receivable-daily.md).

# 1. Run the report

1. **Reporting** → **Expiring Credit Cards**.
2. Set the **start date** and **end date** using **next month's dates**.
3. Change **Customer Status** to **Active**.
4. Select **all branches** in the **Offices** dropdown.
5. **Refresh**, then **Send Messages**.

# 2. Send the email

1. Change **Message Type** to **Email**.
2. Tick **Ignore Contact Preferences** and **Ignore Max Per Minute**.
3. **Email Subject:** `Your credit card is about to expire`
4. Select **Expired Credit Card** as the message type.
5. Paste the body below.
6. **Send Message.**

> Hello {{fname}},
>
> We noticed that the credit card you have on file will expire on {{expDate}}. To avoid any
> interruptions in service, please call us at 713-900-1994 or follow this link to update your credit
> card online:
>
> {{loginLink}}
>
> Select the Wallet option to update your credit card on file.
>
> We appreciate you choosing Natran Green Pest Control and look forward to servicing you soon!
>
> Warm regards,
> Customer Care
> 713-900-1994

`{{fname}}`, `{{expDate}}` and `{{loginLink}}` are Fieldroutes merge fields.

# Two documents, one process

> The wiki holds **two documents for this task**, and this concept is written from the newer of them.
>
> - **`Expiring credit card notification`** — last modified **January 2025**. The version transcribed
>   above.
> - **`The Expired Credit Card Processs`** — last modified **May 2022**. The same report path and the
>   same purpose, written as a recommendation rather than a procedure ("I would recommend using
>   email"), with a **different sample email**.
>
> **They disagree on the customer callback number** — the older template gives a number that does not
> appear anywhere in the newer one, and signs off from a **named individual with a job title** rather
> than from Customer Care. That personalisation is why the older one should not be reused: the template
> will keep sending a specific person's name and direct number after they change roles. The named
> individual and the superseded number were **deliberately not transcribed**.
>
> **The older document should be deleted or marked superseded at source**, so nobody picks the wrong
> one. Recorded here rather than resolved.

> In the newer source, a **stray hyperlink sits inside the subject-line text**, splitting the word
> "card" across a link to an unrelated document. A copy-paste artifact; the subject is transcribed
> above as the clean sentence it is meant to be.

# Related

- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
- [Handling returned ACH payments](/finance/returned-ach-payments.md)
- [Collections call and text scripts](/finance/collections-scripts.md)
