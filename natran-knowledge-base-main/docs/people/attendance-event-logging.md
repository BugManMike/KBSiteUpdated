---
type: Runbook
title: Logging an attendance event
description: How a manager records a planned or unplanned attendance event as a zero-hour benefit entry in uAttend, and the description conventions that make it useful.
tags: [uattend, attendance]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:19:05Z
sources:
  - id: 1iPcJuB02GlBgZw7ptR_SmkJxW70zBsD9uc9h63OGork
    resource: https://docs.google.com/document/d/1iPcJuB02GlBgZw7ptR_SmkJxW70zBsD9uc9h63OGork/edit
    title: How do I document an employee attedance event in Uattend?
status: draft
---

Notes in uAttend track attendance events that would otherwise be invisible in the time-off
request process — out sick, doctor or dentist visits, and similar.

**The direct manager logs these**, not the employee, and **all** time off events are logged —
including planned ones already approved elsewhere.

> **Three timekeeping systems appear across this corpus and nothing reconciles them:**
>
> | System | Where it appears | Apparent role |
> |---|---|---|
> | **Gusto / Gusto Wallet** | [Time off requests](/people/time-off-requests.md), the standard iPhone app set | Time off requests, timeclock, paystubs |
> | **uAttend** | This document | Manager-side attendance event notes |
> | **EOSG / PrismHR** | Onboarding texts, the technician resource page, the injury process | PEO portal — W-2, I-9, direct deposit, paystubs |
>
> This document's FAQ compounds it by referring to *"the HR Prism system"* as the place approved
> time off events are made. The handbook meanwhile tells employees to submit absences through
> "the employee portal" without naming one. **HR to state which system is authoritative for
> what.** A manager following this document and an employee following the Gusto document are
> recording the same absence in two places, and neither knows about the third.

> **This uAttend tenant belongs to Advantage Pro Services, not Natran.** The sign-in URL is
> `v2.trackmytime.com/advantagepro`. Either Natran shares the APS uAttend account, or this
> document was copied from APS documentation and never repointed. Given Natran and APS are
> separate companies sharing some back-office systems — see
> [GAM setup and commands](/it/google-workspace/gam-setup-and-commands.md) — both are plausible.
> **HR and IT to confirm before a manager logs Natran attendance data into an APS system.**

# Log the event

1. Sign into `v2.trackmytime.com/advantagepro` with **supervisor** credentials.
2. **Timecards** at the top.
3. Search for the employee and click their name.
4. **Confirm you are in the right pay period** — use the `<` `>` arrows to change it.
5. Add an event:
   1. **Punch Type** → **Benefit**.
   2. Confirm the date.
   3. **Benefit Type** → **OTH - Other**.
   4. **Leave benefit hours at zero.**
   5. Add a description.
   6. **Save**.

**Zero hours is deliberate.** The entry is a record that something happened, not a payable
benefit — which is why it can be used for unplanned events without affecting pay.

# What the description should say

A useful description records **two things**:

- **Whether the event was planned or unplanned** — sick, left early, and so on.
- **Whether it was allowed** — called in, sent a text message, or **no-call-no-show**.

> That second axis is what makes the log worth keeping. The thresholds in
> [attendance and punctuality](/people/attendance-and-punctuality.md) — two unexcused absences in
> 30 days, three consecutive days without notice — can only be evidenced if each entry records
> whether proper notice was given. A description saying only "out sick" cannot support a
> disciplinary decision.

# Screenshots

The steps for searching an employee and adding an event referred to unnamed icons shown only in
screenshots, which did not survive conversion. The source also embeds a YouTube walkthrough.

# Related

- [Attendance and punctuality](/people/attendance-and-punctuality.md)
- [Time off requests](/people/time-off-requests.md)
