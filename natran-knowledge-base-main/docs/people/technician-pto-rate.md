---
type: Runbook
title: Calculating a technician's PTO rate
description: Deriving an hourly rate for a production-paid technician from twelve months of wages, so paid time off can be valued.
tags: [prismhr, compensation, pto]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1c4qGx5i__XHN4DwTDnHyg1KGVYKONgus3W3-MDE324c
    resource: https://docs.google.com/document/d/1c4qGx5i__XHN4DwTDnHyg1KGVYKONgus3W3-MDE324c/edit
    title: How to calculate technician PTO rate
status: draft
---

**Production technicians have no set hourly rate**, so one has to be derived before paid time off
can be valued. The method is twelve months of earnings, less bonuses, divided by 2080.

# Step 1. Pull the wages

1. Sign in to **PrismHR** (`eos.prismhr.com`).
2. Search for the **Pay Code Summary Report**.
3. Set the **Pay Date Range** to the period you need.
4. Under **Sort By**, select **By Employee, Paycode**.
5. Click **Employee ID**, search for the employee, select them and click **Done**.
6. Click **Run**. The results break their wages down for the range.

# Step 2. Derive the rate

1. Take the **most recent 12 months** of wages from step 1.
2. **Deduct bonuses and overtime hours.**
3. **Divide by 2080.** The result is the rate to use for paid time off.

**Under twelve months' service:** count the weeks worked, multiply by 40, and divide by that number
instead of 2080.

> **The source says "deduct out any bonuses and overtime hours" — mixing a dollar amount with an
> hours count.** Deducting bonus *dollars* from total wages is clear; "overtime hours" cannot be
> subtracted from a wage total without first converting to dollars. Presumably overtime *pay* is
> meant. Transcribed as written; payroll should confirm.

> **This is the third timekeeping or payroll system in the corpus.** The rate is pulled from
> PrismHR here, time is kept in uAttend — see
> [logging an attendance event](/people/attendance-event-logging.md) — and payroll is run in Gusto,
> per [payroll journal recording](/people/payroll-journal-recording.md). Which is authoritative for
> a technician's earnings is not stated anywhere.

# Related

- [Technician production pay](/people/technician-production-pay.md)
- [PTO — office hourly](/people/pto-office-hourly.md)
- [Employment classification, hours and pay](/people/employment-classification.md)
- [Processing missed pay](/people/missed-pay-processing.md)
