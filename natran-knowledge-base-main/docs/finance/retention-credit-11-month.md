---
type: Runbook
title: 11-month customer retention credit
description: The monthly run that applies a $25 coupon to customers approaching their first anniversary, emails them, and flags the account so it is not credited twice.
tags: [fieldroutes, credit, marketing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1yJaeiXiadWkL2JZvaW9O0KnsMy9Vhy-oywXn3V_P2C0
    resource: https://docs.google.com/document/d/1yJaeiXiadWkL2JZvaW9O0KnsMy9Vhy-oywXn3V_P2C0/edit
    title: 11-month customer retention credit
status: draft
---

Part of the customer experience and retention programme: customers who have been with the company
**eleven months** get a **$25 credit** and an email about it, just before their annual agreement comes
up.

# 1. Run the report

1. **Customers** → **Saved Report** → **CR MTH 11 $25 Coupon**.
2. Under the **Customer Account** filter, set **Date Added** to the start and end date **eleven months
   ago**.

   The easy way to think about it: **next month, of last year.** In March 2022 the range is
   1 April 2021 to 30 April 2021. **Watch the year.**
3. Under the **Subscription** filter, set **Sold Date** to the same range.
4. **Run Report**, then **Save** it.

# 2. Exclude accounts that should not get one (optional)

Review the report for accounts that should not be credited — pending cancels, recurring service issues,
and similar.

1. Open the **Customer Card** by clicking the name on the report.
2. **Info** → under **Generic Flags** add **`EXCLUDE - CR 11 MNT Coupon`**.
3. Run the report again; flagged accounts drop off.

# 3. Apply the $25 coupon

**One account at a time**, from the report:

1. **Invoices** → **Add Payment** → **Coupon / Credit**.
2. **$25** as the payment amount, and again in confirm amount.
3. **`CR MTH 11`** in both the **Coupon Code** and **Description** fields.
4. **Record Coupon.**

**If a customer appears twice on the report, credit them once.**

# 4. Confirm the coupons

1. **Billing** → **Payment History** → **Coupon**.
2. Add **Houston Branch** and **Austin Branch** to the **Office** filter.
3. **Refresh.**
4. **Review for duplicates.**
5. **Export to CSV** and save.
6. Email the file to your manager.

# 5. Email the customers

From the step 1 report. **Follow this exactly — done wrong, the email goes to every customer.**

1. **Actions** → **Send email from template**.
2. Template: **CR 11 MTH Email from CEO**.
3. Category: **CR 11 MTH**.
4. Subject: **"Thanks! A $25 credit has been applied to your account."**
5. **Send.**

# 6. Flag the accounts

From the same report:

1. **Actions** → **Add/Remove flag**.
2. Select **CR 11 MTH Coupon**.
3. Confirm Add/Remove is set to **Add**.
4. **Apply.**

> **The flag that prevents double-crediting is applied last**, after the coupon and the email. Anything
> that interrupts the run between steps 3 and 6 leaves credited accounts unflagged, and the date-range
> report will not catch them because it selects on Date Added, not on the flag. **The duplicate check in
> step 4 is the only guard**, and it is manual.

> **Two similar-looking flags do different jobs** — `EXCLUDE - CR 11 MNT Coupon` suppresses the credit,
> `CR 11 MTH Coupon` records that it was given. Note the inconsistent abbreviation, **MNT against MTH**.
> Easy to pick the wrong one from a dropdown.

> **The credit is applied by hand, per account, with the amount typed twice.** For a monthly cohort
> this is the most error-prone step in the procedure, and the source acknowledges no way to batch it.

# Related

- [Waiving fees and applying account credit](/finance/applying-account-credit.md)
- [Weekly credit report](/finance/weekly-credit-report.md)
