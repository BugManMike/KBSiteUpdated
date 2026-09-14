---
type: Runbook
title: Processing missed pay
description: Paying an employee for wages they should have received, using the PrismHR net pay calculator and a matching retro-pay and advance entry.
tags: [prismhr, payroll, compensation]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 12f9pOh1jIq-T9jE0-kfV9CcoEMJhE1AOnyL5tYj_xss
    resource: https://docs.google.com/document/d/12f9pOh1jIq-T9jE0-kfV9CcoEMJhE1AOnyL5tYj_xss/edit
    title: How to process missed pay
status: draft
---

When an employee has missed pay, the net amount is calculated first and then entered as a **pair**
of offsetting payroll entries so the wages land on their paycheck correctly.

# Step 1. Calculate net pay

1. Sign in to **PrismHR** (`eos.prismhr.com`).
2. Search for the **Pay Check Calculator**.
3. Select **Net Pay** as the Calculation Type.
4. Search for the employee.
5. **Leave the deduction period blank.**
6. Select the **pay code type**.
7. In **Hours/Units to be Paid**, enter the hours — or **`1`** if paying a flat commission.
8. Enter the rate of pay or the commission amount.
9. The calculator returns **Total Gross Earnings** and **Net Pay**. Keep both.

# Step 2. Enter retro pay and the advance

On the time entry screen during payroll, make **two** entries:

1. **Total Gross Earnings** (step 1) into the employee's **Retro Pay** field.
2. **Net Pay** (step 1) into the **Advance** field.

Then continue the payroll submission as normal.

**Why two entries.** The gross earnings and the net-pay advance deduction wash each other out; the
difference between them is collected as taxes.

> **Nothing here records why the pay was missed, who authorised the correction, or any limit on the
> amount.** This is the same gap batch 4b found on
> [bill payments](/finance/bill-com-bill-payments.md) and
> [fee waivers](/finance/applying-account-credit.md) — an entry that moves money with no approver
> recorded. **Whoever owns payroll should decide whether a missed-pay correction needs an approver.**

# Related

- [Calculating a technician's PTO rate](/people/technician-pto-rate.md)
- [Payroll checklist](/people/payroll-checklist.md)
- [Payroll journal recording](/people/payroll-journal-recording.md)
