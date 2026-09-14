---
type: Runbook
title: Lien notice process
description: Preparing and sending a notarised lien notice to a customer with a balance over 90 days old, built from the account balance summary.
tags: [fieldroutes, receivables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1HvrlKf6IczQse680YplHQS_RLFXvNtlULgJ5Jcy5Gas
    resource: https://docs.google.com/document/d/1HvrlKf6IczQse680YplHQS_RLFXvNtlULgJ5Jcy5Gas/edit
    title: Lien Notice Process
status: draft
---

An escalation for balances over 90 days old, running off the same aged-receivables report as
[collections](/finance/collections-calling-process.md).

# 1. Run the over-90-day report

1. Fieldroutes → **Billing** → **Accounts Receivable** → **Advanced Filters** → **Balance Age** →
   **90+ Days old** → **Refresh**.
2. Open the account from the **customer ID**.
3. **Invoices** → **account balance summary**.
4. Customise the date range **from the oldest unpaid invoice to the current date**, then **Apply** and
   **Refresh** to bring up the invoice summary. **Print it.**

# 2. Create the follow-up task

Create a task with a **due date 3 days out**, in the form:

> 3/21/22 Lien Notice sent please follow up on 3/24/22

# 3. Prepare the notice

1. Find **"Lien Notice Template Natran"** in Google Docs.
2. Fill in the customer information.
3. **Print it, have the owner sign it, and get it notarised.**
4. **Scan the account balance summary and the lien notice together.**

# 4. Email the notice

The notice is emailed to the customer in this form — the bracketed fields are the ones filled per
customer:

> \[date\]
>
> This email will serve as formal notice to you that you are in default of your obligation to pay the
> sum of \[amount\] for goods and services supplied to you by NATRAN GREEN PEST CONTROL at your
> request. This amount relates to:
>
> \[service address\]
>
> This amount has been overdue since \[date\] and you have failed to pay despite repeated requests for
> payment by Natran Green Pest Control. There will be NO more negotiations on this matter.
>
> Unless payment of the above amount is received by us in full immediately, we will have no alternative
> but to exercise whatever rights and remedies we have under Texas law to enforce such payment of debt,
> including but not limited to institution of legal proceedings against you to recover the debt without
> further notice to you and this letter may be tendered in court as evidence of your failure to pay,
> liens against the above properties under Texas Property Code §§53.056, 53.057, and 53.058, and any
> other rights I have to recover the above amount, together with accrued interest and legal expenses.
>
> A lien will be filed Friday and a copy of the liens will be sent to the property in question, the
> registered owner, and the builder on record.
>
> Kindly govern yourself accordingly.

> **The source has a real customer's data left in the template.** The letter is stored not as a blank
> form but as a **sent example**, complete with a service address, a balance figure and the overdue
> date. Those were **not transcribed** — replaced with bracketed placeholders above. **The source
> document should be cleaned up**, because as it stands anyone opening the template sees one customer's
> address and debt, and anyone working quickly could send the next notice with the previous customer's
> details still in it.

> **This letter asserts statutory lien rights and threatens litigation, and the process has no legal
> review step.** It cites Texas Property Code §§53.056–53.058, which sit in the mechanic's and
> materialman's lien chapter and carry their own notice deadlines and perfection requirements. Whether
> those provisions are available for residential pest control services — and whether "a lien will be
> filed Friday" is accurate — is **a question for counsel, not for this document.** Recorded exactly as
> found. **Confirm with an attorney before sending another one.**

> **The signatory is named by first name only** in the source, and the notice is notarised, so who is
> authorised to sign matters. Recorded here as "the owner"; the process should name the role.

> The task-note example is transcribed with its original **2022 dates**, since it demonstrates the
> format rather than a current date.

# Related

- [Collections calling process](/finance/collections-calling-process.md)
- [Sending accounts to collections](/finance/sending-accounts-to-collections.md)
- [Accounts receivable daily operations](/finance/accounts-receivable-daily.md)
