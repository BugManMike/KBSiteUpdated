---
type: Reference
title: Employee expense accounts
description: Which GL account each role's wages are expensed to, and the pay type that goes with it, for both W2 employees and contract virtual assistants.
tags: [quickbooks, bookkeeping, compensation]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1aYAO7NH3dchwMNht3P_j2TiOJDdNr6H8jTAk4DtHMtA
    resource: https://docs.google.com/document/d/1aYAO7NH3dchwMNht3P_j2TiOJDdNr6H8jTAk4DtHMtA/edit
    title: Expense accounting for departments
status: draft
---

How employees are expensed, by department and role. **Entries in the employee source-of-truth
spreadsheet must follow these tables** — that spreadsheet is what the health benefit allocation and
payroll journalizing both read from.

# W2 employees

Hourly, production and salaried.

| Role | Expense account | Pay type |
|---|---|---|
| Apprentice | `5105 Service Wages Hourly` | Hourly (non-exempt) |
| Standard Tech | `5115 Service Wages Production` | Production |
| Speciality Tech | `5185 Speciality Tech Hourly` | Hourly (non-exempt) |
| Outside Sales | `6005 Sales Wages - Residential Outside sales` | Salary |
| Inside Sales | `6006 Sales Wages - Inside sales` | Hourly (non-exempt) |
| Marketing Manager | `6703 Marketing Wages` | Salary |
| Accounting | `71701 Accounting wages` | Hourly (non-exempt) |
| Customer Care | `71501 Customer care wages` | Hourly (non-exempt) |
| Human Resources | `71601 Human Resources wages` | Hourly (non-exempt) |
| Branch Manager | `71805 Branch Manager` | Salary |
| Field Service Managers | `71810 Field Service Managers` | Salary |
| Sales Manager | `6007 Sales Wages - Sales Manager` | Salary |
| General Management | `7125 Management / Supervisor Wage` | Salary |

**Notes from the source:**

- **Outside Sales — "This department is not currently active."**
- **Marketing Manager — "Typically a salaried position. Consult with management during hires."**

> **The three technician rows are the ones to read carefully.** Apprentice and Speciality Tech are
> *hourly*; only **Standard Tech** is **Production** — which is what puts them on the percentage
> basis in [technician production pay](/people/technician-production-pay.md). A Speciality Tech is
> not on production pay despite being a technician.

> **Outside Sales being inactive matters beyond this table.** There is a whole
> [PTO — outside sales](/people/pto-outside-sales.md) policy, and the recruiting templates advertise
> Austin outside sales roles with on-target earnings. Either the department was reactivated after
> this document was written, or several documents describe a role nobody holds. HR to confirm.

# Virtual assistants and contract workers

**Generally foreign contract workers who invoice for their labour.**

| Role | Expense account | Pay type |
|---|---|---|
| Sales Assistant | `6035 Sales virtual assistants` | Contract |
| Marketing Assistant | `6728 Marketing virtual assistants` | Contract |
| Customer Care | `71545 Customer care virtual assistants` | Contract |
| HR Assistant | `71640 Human Resources virtual assistants` | Contract |
| Accounting & Bookkeeping | `71740 Accounting virtual assistants` | Contract |
| Management Assistants | `71830 Management virtual assistants` | Contract |
| Office Assistants | `71930 Officer virtual assistants` | Contract |

> **Every W2 department has a parallel VA account**, and the numbering is deliberate — the VA account
> sits in the same range as its department's wage account. Customer Care is `71501` for W2 and
> `71545` for VAs.

> The source's sentence explaining VAs is cut off: *"They are not subject to the normal"* — presumably
> the normal payroll process. Transcribed as found. `71930 Officer virtual assistants` is also
> probably meant to read *Office*, matching its row label.

> **There is no account listed for Dispatch or Scheduling**, which exist as roles elsewhere in the
> corpus — see [Fieldroutes access control profiles](/it/fieldroutes-access-control-profiles.md).
> They may be expensed under Customer Care. Not stated.

# Related

- [Health benefit allocation](/finance/health-benefit-allocation.md)
- [Technician production pay](/people/technician-production-pay.md)
- [Employment classification, hours and pay](/people/employment-classification.md)
- [Uncategorized expenses](/finance/uncategorized-expenses.md)
