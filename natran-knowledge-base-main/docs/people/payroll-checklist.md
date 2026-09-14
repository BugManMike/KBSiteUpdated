---
type: Runbook
title: Biweekly payroll checklist
description: The pay-run preparation cycle — timecards out on Monday, then the four Fieldroutes reports that decide what technicians actually get paid.
tags: [uattend, payroll, technicians]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 14teiKlR_Gh680kkwYI66xNWaLty9N1vnHWtJsFiMA7k
    resource: https://docs.google.com/document/d/14teiKlR_Gh680kkwYI66xNWaLty9N1vnHWtJsFiMA7k/edit
    title: Payroll checklist
status: draft
---

This is the **preparation** half of payroll — producing and correcting the inputs. Posting the
result to the ledger is [payroll journal recording](/people/payroll-journal-recording.md).

**Monday, every week:** print timecards from uAttend and distribute them to department managers for
review and correction of missed punches.

# Step 1. Print timecards from uAttend

1. Sign in to **uAttend**.
2. **Reports → Batch Report.**
3. Confirm the **pay period** is correct.
4. Check every employee needing a hard copy.
5. Click **Print PDF Batch**.
6. Save into the correct **Payroll Records** folder.
7. Print and distribute to department managers for employee review and correction.

# Step 2. Create the run's folders

Create two folders in the **Payroll Records** folder — one under **Tech reports**, and one under
*(the source sentence ends here — see the note below)*.

# Step 3. Unsigned Agreement report

1. **Fieldroutes → Customers reports → Saved Reports.**
2. Run **Payroll: Unsigned Agreements**.
3. Update the date range under **Service Appointment** and run again.
4. **Actions → Write to Excel.**
5. Save into the **Tech Reports** folder, renamed with the paycheck date —
   e.g. `Unsigned Agreement 2023-03-01`.

# Step 4. Collect or Do Not Service report

1. **Fieldroutes → Customers reports → Saved Reports.**
2. Run **Payroll: Collect or Do Not Service Report**.
3. Update the date range under **Service Appointment** and run again.
4. **Actions → Write to Excel.**
5. Save into the **Tech Reports** folder as `Unpaid balance <paycheck date>`.

See [holding service on past-due accounts](/finance/holding-service-past-due-accounts.md) for what
that flag means day to day.

# Step 5. Production reports

1. **Fieldroutes → Reporting → Commission.**
2. Change the **Profile** to **Tech Production**.
3. Set start and end dates to the pay period, and **Refresh**.
4. **Export to Excel**, saving to the Tech report folder as
   `Tech Production <paycheck date>`.

# Step 6. Zero out unpaid production

The production report has a tab per employee with the production payout for each job. **Using the
Collect or Do Not Service report and the Unsigned Agreements report, manually change the paid
production to zero.**

> **This is the step that costs technicians money, and it is entirely manual.** A technician is not
> paid production on a job where the agreement was never signed or the balance was not collected —
> neither of which is necessarily their doing. There is no reconciliation, no second check, and no
> record of which jobs were zeroed. See
> [technician production pay](/people/technician-production-pay.md) for the underlying pay basis.

# Step 7. Email the reports out

Send each technician their individual production report using the standing email draft. **Managers
are copied.**

# Source defects

> **The step numbering is broken.** The source runs Step 1, Step 2, then a *second* Step 1 (printing
> timecards), then Step 3. The order above follows the logical sequence; the second "Step 1" has been
> placed first because nothing else can happen before timecards are printed.

> **Step 2 is cut off mid-sentence** — *"One in the Tech reports folder and one in the"*. The second
> folder is never named. Whoever runs payroll knows; the document does not.

> **The document ends with a bare heading, "Monthly sales commission and referral bonuses", and no
> content.** Those procedures do exist —
> [calculating salesperson commissions](/people/sales-commission-calculation.md) and
> [lead referral bonus](/people/lead-referral-bonus.md) — but the checklist never links them, so
> anyone following this document alone stops before the monthly work.

> **uAttend is reached on an Advantage Pro Services tenant** (`/advantagepro`), not a Natran one.
> The same is true in [overtime alerts](/people/overtime-alerts.md). Whether Natran payroll should
> depend on an APS-tenanted system is an open scoping question — the same one raised by the
> [email signature template structure](/it/google-workspace/email-signature-template-structure.md).

# Related

- [Payroll journal recording](/people/payroll-journal-recording.md)
- [Technician production pay](/people/technician-production-pay.md)
- [Logging an attendance event](/people/attendance-event-logging.md)
- [Processing missed pay](/people/missed-pay-processing.md)
