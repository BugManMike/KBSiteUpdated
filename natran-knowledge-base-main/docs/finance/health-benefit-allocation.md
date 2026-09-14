---
type: Runbook
title: Health benefit allocation
description: Splitting the monthly health benefit payments made from Natran's bank across both companies, by department, branch and shared-employee percentage.
tags: [quickbooks, bookkeeping, benefits]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 1kuLHFn6CbnzilC6qtNQAWLMKQqyt05PLOdT8sowJEuM
    resource: https://docs.google.com/document/d/1kuLHFn6CbnzilC6qtNQAWLMKQqyt05PLOdT8sowJEuM/edit
    title: Allocating Health Benefits Between Branches and Intercompany accounts
status: draft
---

**Health benefits for both APS and Natran employees are paid from Natran's bank account.** The total
then has to be distributed three ways: **by company** (APS / Natran), **by department** (direct
labour, sales, HR, managers and so on), and **by branch** (Houston / Austin — Natran only).

# 1. Set up the working file

Duplicate the template working file and save it in the **End-of-Month** folder under the month being
worked on.

# 2. Download each vendor's payment breakdown

Sign into each vendor site and download the monthly breakdown in CSV or Excel:

| Vendor | Portal |
|---|---|
| United Healthcare | `uhceservices.com` |
| Mutual of Omaha | `login.mutualofomaha.com` |
| Principal | `principal.com` |
| Healthiest You | `client.healthiestyou.com` |
| Clarity Benefits | `claritybenefitsolutions.com` |
| Transamerica | `transamerica.com` |

> **These six vendors do not match the benefits calendar.**
> [Benefits enrolment](/people/benefits-enrolment.md) names **MetLife** and **Guardian** on its
> open-enrollment calendar plus an unnamed health carrier — and neither MetLife nor Guardian appears
> here. Conversely five of these six appear nowhere in the HR documentation. **Between the two
> documents there is no complete list of what benefits the company actually offers.** HR and
> accounting hold different halves.
>
> Principal is also the 401k provider — see the Principal.com contribution procedure, covered in a
> later batch.

# 3. Paste into the vendor tabs

Copy each CSV into its vendor tab in the working file. **Column order must match the template
exactly** — do not let the columns interchange.

# 4. Check the APS / Natran tagging

**Every employee needs a GL code** for the tagging columns to populate.

If an employee has no GL code, go to the **`Tagging (do not edit)`** tab and assign one — creating a
new row for a new employee. **Take the department and class from the employee source-of-truth
file**, the same file behind
[employee expense accounts](/finance/employee-expense-accounts.md).

# 5. Split shared employees

For employees shared between Natran and APS, **confirm their sharing percentage** and split their
health benefits accordingly. **Create a new row for the intercompany share** and make sure its
tagging column is coded correctly too.

> The source works this through with a named employee at a 50/50 Natran/APS split, showing their
> premium halved. **The individual and the amount are not reproduced here** — the bundle does not
> carry personal compensation data. The mechanism is what matters: a shared employee produces two
> rows with different tagging, one per company.

> **Sharing percentages live nowhere in this bundle.** Step 5 says to "confirm" them without saying
> against what. If the authority is the employee source-of-truth spreadsheet, that should be stated;
> if it is institutional memory, that is a single point of failure on a recurring monthly entry.

# 6. Check the generated journal entries

The **`QB Entry`** tab is linked to the vendor tabs and regenerates a journal entry per vendor
whenever their data changes.

- **Verify total debits and credits balance**, and that amounts match what was invoiced and entered.
- **Columns A–C are APS. Columns E–G are Natran.**

# 7. Enter the journal entries into QuickBooks

# 8. Match the payments from the bank

When each vendor's payment appears in the bank feed, click **match** and locate the step 7 entries.
**Confirm the amount paid equals the amount journalized.**

> Step 8 is the real control in this procedure — everything before it is allocation arithmetic, and
> the bank match is what proves the total was right.

# Related

- [Benefits enrolment](/people/benefits-enrolment.md)
- [Intercompany transactions](/finance/intercompany-transactions.md)
- [Employee expense accounts](/finance/employee-expense-accounts.md)
