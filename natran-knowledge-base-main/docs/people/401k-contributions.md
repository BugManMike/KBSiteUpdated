---
type: Runbook
title: 401(k) participant administration
description: Adding, deactivating and terminating 401(k) participants on the provider's employer portal, and submitting each cycle's contribution amounts.
tags: [principal, benefits, payroll]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1Wa06VQGTiUnB5YmzLyssPpZqE2AZ4WaSnZDcTXLkAd0
    resource: https://docs.google.com/document/d/1Wa06VQGTiUnB5YmzLyssPpZqE2AZ4WaSnZDcTXLkAd0/edit
    title: 401K contributions instructions for Principal.com
status: draft
---

The 401(k) is administered on **Principal**'s employer portal. Three lifecycle actions plus the
per-cycle contribution submission.

# Add a participant

1. Log in to Principal **as Employer**.
2. **Participants → Manage Participants → Manually Add & Update Participants.**
3. Enter the participant's **SSN** and click **Add**.
4. Enter name, date of birth and date of employment. **Leave Country as `*select*`.**
5. Check the confirmation box and **Submit**.

**Enter this immediately after the 401(k) form is signed.** Then email the PEO and the representative
about contributions. **For new hires, the policy begins 90 days following the first of the month.**

# Make a participant inactive

For someone already in the plan records who stops deferrals:

1. Log in as Employer.
2. **Participants → Manage Participants → Manually Add and Update Participants.**
3. Enter the SSN or name in **Existing Participant** and **Continue**.
4. **Other Employment Information.**
5. Set **Actively Participating in Plan** to **No**.
6. **I confirm → Submit.**

**If the employee has an account balance they cannot be made inactive**, even if they stop deferring.

# Terminate a participant

1. Log in → **Participants → Manage Participants → Manually Add & Update Participants**.
2. **List of Participants →** search for the employee.
3. Under **Personal Information**, enter country, physical address and email address, check the
   confirmation box and submit.
4. Under **Employment Dates & Termination**, set:
   - **Benefit Event:** Termination
   - **Termination Reason:** Permanent Layoff
   - **Benefit Effective Date:** `mm/dd/yyyy`
   - **Benefit Event Date:** last physical day worked
   - **Qualified Domestic Relations Order:** No
   - **Pennsylvania Elective Deferral Taxed:** No
   - **Hours Worked in Termination Year:** from timeclock records
5. Get the hours from **uAttend → Reports → Timecard Reports**, running from **January 1** to the
   last paycheck — noting that the paycheck cycle cuts through the end of the pay period.
6. **Print**, confirm changes and **Submit**.

> **"Termination Reason: Permanent Layoff" is given as a constant, for every departure.** A
> resignation is not a layoff. This is a filed benefits record, and the reason field is being used as
> a fixed value rather than a fact. **HR should confirm this is intended** — see
> [Google Workspace account offboarding](/it/google-workspace/account-offboarding.md) for the rest of
> the offboarding path.

# Submit contribution amounts

1. **Principal → Participants → Contributions & Loan Payments.**
2. **Manually Enter Data → Start a New Submission.**
3. Enter the **paycheck date**, select the **tax year**, check the contributions box, **Continue**.
4. Enter contribution amounts against each name, taken from the **PEO's Detail Deductions by
   Deduction Code report**.
5. **Save & continue.**
6. Enter the **total amounts from both company reports**.
7. Check **I Confirm** and **Submit**.
8. **Print the detail report twice**, attach and file with the payroll reports.
9. Confirm and submit.

> **"Both company reports" is Natran and Advantage Pro Services** — the 401(k) submission spans both
> entities, like the [intercompany transactions](/finance/intercompany-transactions.md) and the
> [health benefit allocation](/finance/health-benefit-allocation.md). Neither company is named in
> this step; the reader is expected to know.

> **This procedure names a fourth payroll or timekeeping system.** Contribution amounts come from a
> **PEO's** deduction report, hours come from **uAttend**, payroll runs in **Gusto** — see
> [payroll journal recording](/people/payroll-journal-recording.md) — and rates come from **PrismHR**
> in [calculating a technician's PTO rate](/people/technician-pto-rate.md). Four systems, no stated
> relationship between them. This is the single most tangled area the ingestion has found.

# Related

- [Benefits enrolment](/people/benefits-enrolment.md)
- [Payroll journal recording](/people/payroll-journal-recording.md)
- [Health benefit vendors](/finance/health-benefit-vendors.md)
