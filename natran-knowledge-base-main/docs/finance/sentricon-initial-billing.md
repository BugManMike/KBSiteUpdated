---
type: Runbook
title: Submitting Sentricon installations to Corteva
description: The monthly submission of new Sentricon installations to Corteva for billing, including the linear-footage and installation-type checks that determine what Corteva charges.
tags: [fieldroutes, vendor-billing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 18ObOSE0GndAdK_OXwvLDQvPf0QSr6O5h9JGyd0UgtEA
    resource: https://docs.google.com/document/d/18ObOSE0GndAdK_OXwvLDQvPf0QSr6O5h9JGyd0UgtEA/edit
    title: How to submit Sentricon Initial information to Corteva for billing
status: draft
---

**Corteva manufactures Sentricon and requires new installations to be submitted every month.** What
gets submitted determines what Corteva bills, so the review steps matter more than the submission
itself.

# 1. Run the renewal process first

[Submitting Sentricon renewals to Corteva](/finance/sentricon-renewal-billing.md) runs **before** this
one.

# 2. Open the Sentricon report

Fieldroutes → **Reporting** → the **Sentricon** section at the top of the page → **Sentricon UI Page**
on the left → the **Communication** tab.

**Select Branch** changes which branch you are looking at → **OK**.

# 3. Review and correct linear footage

The **Total Site Volume** column is the linear footage around the property.

**Where linear footage was never entered it defaults to 1.** Any row showing `1` must be fixed before
submitting.

# 4. Confirm the installation type

Sentricon sites are set up in Fieldroutes under different install types, and **Corteva charges
different amounts for each**, so the type has to be right:

| Install type | What it means |
|---|---|
| **Other Type 1 Installation** | The **preventative** type — the majority of installations. |
| **Standard Installation** | The **curative** type, for active termite infestations. |

- Most sites should be grouped under **Other Type 1 Installation**.
- Any site set up as **Standard Installation** should carry additional fees for **AG (Above Ground)
  packs**. Open the customer subscription and confirm the customer was charged. Consult management with
  questions.
- **If AG packs are missing from a Standard Installation site, report it to management for coaching and
  training.**

# 5. Check sites over 400 linear feet

Any site over 400 linear feet is checked for accuracy:

1. Find the **customer's account**.
2. Open **Documents** and locate the **termite disclosure**.
3. Find the reported linear footage: the **Sentricon Monitoring subscription** → **Actions** →
   **Sentricon Site** → the **linear footage field**.
4. **The linear footage on the site must match the termite disclosure.**

# 6. Print the report

Print and retain a copy in the end-of-month folder, and share it with the branch manager for review.

# 7. Submit

**Approve and Send**, then confirm. An invoice arrives shortly afterwards, ready for payment.

# If Approve and Send is greyed out

The Sentricon credentials need refreshing: **Reporting** → **Sentricon** → **Sentricon Credentials** →
**Generate New Password** → **Save Credentials**.

> The 400-linear-foot check is described as a threshold for verification, but the document never says
> **what to do when the site and the termite disclosure disagree** — only that they must match. The
> resolution step is missing, and it is the case most likely to need one.

> Steps 4 and 5 both catch billing errors that originate in how a technician or salesperson set the
> site up in Fieldroutes. This procedure corrects them **at the point of vendor billing, monthly** —
> there is nothing upstream preventing them. That is worth knowing when the same corrections keep
> recurring.

# Related

- [Submitting Sentricon renewals to Corteva](/finance/sentricon-renewal-billing.md)
- [Entering a bill from the Bill.com inbox](/finance/bill-com-bill-entry.md)
