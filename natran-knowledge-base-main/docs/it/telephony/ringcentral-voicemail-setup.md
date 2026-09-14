---
type: Runbook
title: RingCentral voicemail setup
description: Recording the working-hours, away and after-hours voicemail greetings in a RingCentral extension, and why the after-hours one lives on a different screen.
tags: [ringcentral, telephony, voicemail]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1JVm1QG8GoxFY2MEtb4pD5S6IzEa8dr4hXiG80KihhbQ
    resource: https://docs.google.com/document/d/1JVm1QG8GoxFY2MEtb4pD5S6IzEa8dr4hXiG80KihhbQ/edit
    title: How to setup voicemail greetings for office users
status: draft
---

> **Is RingCentral still in use?** This is the open question hanging over this document and
> [the greeting scripts](/it/telephony/ringcentral-voicemail-scripts.md).
>
> **Evidence it is retired:** the IT single-source-of-truth (2026-07) names CallTrackingMetrics
> as "our telephony system" and never mentions RingCentral. The current [Windows PC
> setup](/it/devices/windows-pc-setup.md) installs CTM as the required phone app. All seven
> existing `ctm-*` concepts document CTM as the live system.
>
> **Evidence it lingers:** [Windows device user
> removal](/it/devices/windows-device-user-removal.md) still details RC Phone Desktop
> configuration, [Apple device self-service
> setup](/it/devices/apple-device-self-service-setup.md) tells users they will set up voicemail
> "again on your Ringcentral app", and this document was last modified 2024-03.
>
> **Nothing in the corpus records a migration.** If RingCentral is gone, these two documents and
> the RC Phone section should be marked `deprecated` and the stale cross-references removed. IT
> to confirm. Until then they are transcribed faithfully.
>
> **Update from the accounting ingestion — RingCentral is still being billed.**
> [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md) step 15 splits the
> RingCentral charge between Natran and APS **per user, every month**, via the Pro-rata working
> file. That is a live recurring cost, not a legacy artifact.
>
> So the likely answer is **not** that RingCentral was retired, but that **both systems run**:
> CallTrackingMetrics for call handling and tracking numbers, RingCentral for extensions or desk
> phones. That would explain why the current Windows build installs CTM while the older one
> installed RC Phone Desktop, and why the Apple setup still says voicemail is configured twice.
> **It also means these procedures are probably current, not stale.** Still needs IT to confirm —
> but the question has shifted from "is this dead?" to "what is each system for?"

These steps are for **RingCentral office users**. Technicians and others who mainly use the
RingCentral mobile app were covered by separate instructions, which the source links but does not
contain.

**Sign into `ringcentral.com` and make sure you are in the My Extension section**, not the Admin
Portal. Switch using the dropdown by your profile picture in the upper right.

The scripts to read are in
[RingCentral voicemail greeting scripts](/it/telephony/ringcentral-voicemail-scripts.md).

# Working hours greeting

1. **Settings** → **Phone**.
2. **Call rules and voicemail** at the top.
3. Under **Custom rules**, open **Default - working hours**.
4. Scroll to **If no one answers** and click it to open the **Voicemail** screen.
5. Set the Voicemail greeting to **Custom**.
6. Click the red button to open the recording screen.
7. Select **Computer Microphone** as the recording method — often selected already.
8. Click the red button to start and stop recording.
9. Upload the recording when done.
10. **Done** to save.

# Away message greeting

> **The source gives identical steps for the away message and the working-hours greeting** —
> both say to open **Default - working hours**. Following it literally would overwrite the
> greeting just recorded. The away message must live on a different rule, but the source does not
> say which. Its own explanatory sentence is also cut off mid-thought: *"The away message greeting
> is used for"*.
>
> **Do not follow this section as written.** IT to supply the correct rule.

# After-hours greeting

Mostly the same, but it lives on a **different screen** — there is no *Call rules and voicemail*
step:

1. **Settings** → **Phone**.
2. Scroll down and click **Voicemail greeting**.
3. Set it to **Custom**.
4. Red button to open the recording screen.
5. **Computer Microphone**.
6. Red button to start and stop.
7. Upload.
8. **Done**.

> Worth noticing why: the working-hours and away greetings are **call rules**, while the
> after-hours greeting is the **extension's default** voicemail greeting. That is a RingCentral
> structural distinction, not an inconsistency in the document.

# Screenshots

Every "click the red button" and "upload using the" step referred to an inline icon image. Those
are lost, so the button identities are unrecoverable from this text alone.

# Related

- [RingCentral voicemail greeting scripts](/it/telephony/ringcentral-voicemail-scripts.md)
- [RingCentral call monitoring](/it/telephony/ringcentral-call-monitoring.md)
- [CTM voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md)
