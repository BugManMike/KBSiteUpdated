---
type: Reference
title: Technician production pay
description: How a production stop's value is split between technicians and multiplied by each one's production rate, and the separate hourly basis used for partial work.
tags: [compensation, technicians, payroll]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:19:05Z
sources:
  - id: 11BeR01a4kYtzM0A_SxmXAEqB9Rm9IpXf6Vee0l9jxsM
    resource: https://docs.google.com/document/d/11BeR01a4kYtzM0A_SxmXAEqB9Rm9IpXf6Vee0l9jxsM/edit
    title: Natran Employee Agreement
status: draft
---

Production technicians are paid a percentage of the value of the work they complete. Two
different bases apply depending on whether the work is a full stop or partial.

**These formulas come from the signed Employee Agreement.** An individual's production rate is
set in their own agreement — see
[employee agreement map](/people/employee-agreement-map.md).

# Full stops — split, then multiply

When multiple technicians complete a production stop, **the stop value is divided equally
between them first**, and each technician's share is then multiplied by *their own* production
rate.

The order matters. Splitting first means a technician's pay for a shared stop does not depend on
their colleagues' rates, only on how many people were on it.

**Three technicians, $1,000 stop:**

| Technician | Rate | Share | Pay |
|---|---|---|---|
| A | 19% | $333.33 | $63.33 |
| B | 18% | $333.33 | $60.00 |
| C | 17% | $333.33 | $56.67 |

**Two technicians, $1,000 stop:**

| Technician | Rate | Share | Pay |
|---|---|---|---|
| A | 18% | $500.00 | $90.00 |
| B | 17% | $500.00 | $85.00 |

**One technician, $1,000 stop:** at 18%, $1,000 × 18% = **$180.00**.

> The worked examples use rates of 17%, 18% and 19%. **These are illustrative, not a rate
> table** — the agreement gives no schedule of production rates by role or tenure. The actual
> rate is in the individual's employment agreement, and
> [Fieldroutes user setup](/it/fieldroutes-user-setup.md) confirms it is entered per-user as a
> **Tech Production ## Percent** commission profile.

# Partial work — hourly basis

When a production technician assists with partial work, pay is based on **$165 per hour**
multiplied by their production percentage. **The hours are set by the Sales Scheduling
Worksheet**, not by time actually spent.

**Example:** the worksheet allocates 1.5 hours. At $165/hour that is $247.50. A technician on a
17% production rate earns **$42.08**.

> $247.50 × 17% = $42.075, rounded to $42.08 in the source.

> **The Sales Scheduling Worksheet is the control point for partial-work pay**, which makes it a
> compensation document as well as a scheduling one. Whoever fills it in is setting what the
> technician earns. That worksheet is covered in the sales and scheduling batches.

# What this does not cover

- **No production rate schedule.** See above.
- **Hourly technicians** are on a different basis entirely — the **Hourly tech Uphelps only**
  commission profile per [Fieldroutes user setup](/it/fieldroutes-user-setup.md). Nothing in this
  source describes it.
- **How stop value is determined** is not defined here.
- **Overtime interaction.** Production pay is a percentage of work value, not an hourly rate, and
  the agreement does not say how it combines with the overtime entitlement in
  [employment classification](/people/employment-classification.md).

> Technicians' pay also depends on completing paperwork: the agreement states that failure to
> process all forms, work orders and contracts, and to follow procedures, **may delay their
> pay**.

# Related

- [Employment classification](/people/employment-classification.md)
- [Employee agreement map](/people/employee-agreement-map.md)
- [Fieldroutes user setup](/it/fieldroutes-user-setup.md) — where the rate is configured
