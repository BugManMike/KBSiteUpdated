---
type: Reference
title: Approved coupon codes
description: The eight approved codes for crediting a customer account, what each one means, and the case-sensitivity rule.
tags: [fieldroutes, credit, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1z0GslGHvLBa0xNgleRGRGy8JubzXPEbZCTFp0iZoei8
    resource: https://docs.google.com/document/d/1z0GslGHvLBa0xNgleRGRGy8JubzXPEbZCTFp0iZoei8/edit
    title: Coupon Codes
status: draft
---

**Every credit applied to a customer account carries a coupon code**, so that credits can be tracked
by reason. These are the approved codes.

> **All codes are case-sensitive.** Use them exactly as written.

| Code | When to use it |
|---|---|
| `Waive cancellation fees` | A manager has approved waiving the cancellation fee. |
| `Goodwill credit` | Crediting a customer to wipe their bill. |
| `Billing error` | Double charge, or incorrect billing generally. |
| `Bad debt` | **Collection write-off only** — see [recording bad debt](/finance/bad-debt-recording.md). |
| `Late fee reversal` | Waiving late fees and finance charges. **NSF fees are excluded.** |
| `Misc adjustment` | Only when no other code applies. **A detailed explanation is required.** |
| `Managerial Approval` | A Branch or Service Manager has asked shared services to apply a credit or waive a balance. |
| `REFERRAL40` | Applying a referral code. **Management use only.** |

# Applying one

1. **Invoices → Add Payment →** select **Coupon/Credit**.
2. Enter the value in **Payment Amount** and again in **Confirm Amount**.
3. Enter one of the codes above as the **Coupon Code**.
4. Click **Record Coupon**.

The fuller version of this mechanism, including applying a credit against specific invoices, is in
[waiving fees and applying account credit](/finance/applying-account-credit.md).

> **This is a partial answer to the approval gap flagged across batch 4b.** The code vocabulary does
> capture a *reason* — which [waiving fees and applying account credit](/finance/applying-account-credit.md)
> said was missing. But two codes (`Waive cancellation fees`, `Managerial Approval`) assert that a
> manager approved something **without recording which manager, when, or up to what value**, and
> `Misc adjustment` requires "a detailed explanation" with no field named to put it in. **So the
> reason is now coded and the approver is still not.** Whoever owns receivables should close the
> second half.

> **`REFERRAL40` is the only code that names a rate**, and it is the only one restricted to
> management, but nothing states what the referral programme is or which referral it settles. It is
> not obviously either the [employee referral bonus](/people/employee-referral-bonus.md) or the
> [lead referral bonus](/people/lead-referral-bonus.md), both of which pay the *referrer* rather than
> crediting a customer.

> **The heading in the source reads "Apply coupon to referring customer"** but the steps are the
> generic credit procedure, used for all eight codes. Titled here for what it does.

# Related

- [Waiving fees and applying account credit](/finance/applying-account-credit.md)
- [Applying late fees and interest](/finance/late-fees-and-interest.md)
- [11-month customer retention credit](/finance/retention-credit-11-month.md)
- [Weekly credit report](/finance/weekly-credit-report.md)
- [Recording bad debt](/finance/bad-debt-recording.md)
