---
type: Runbook
title: Tech referral form → Chat notification workflow
description: The n8n workflow that posts "TECH REFERRAL FORM" emails into Google Chat — exact node parameters, full-body message formatting, and rebuild steps.
tags: [n8n, notifications, email]
resource: https://n8n.srv1090686.hstgr.cloud/workflow/4N3Nwf2jxhICTZrO
generated:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
sources:
  - resource: https://n8n.srv1090686.hstgr.cloud/workflow/4N3Nwf2jxhICTZrO
    title: "n8n workflow: TECH REFERRAL FORM → Google Chat notification (ID 4N3Nwf2jxhICTZrO)"
verified:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
  note: Read from the saved workflow definition on the live n8n instance.
status: draft
---

Workflow **"TECH REFERRAL FORM → Google Chat notification"**, ID `4N3Nwf2jxhICTZrO`,
Active as of 2026-07-28. When a **"TECH REFERRAL FORM"** email arrives — a lead referred
by a field technician — this workflow posts it into Google Chat space `AAAAB4nawjQ` with
a one-click dialer link if a phone number is found.

The five-node shape, mail-source rationale, keeping.com exclusion, duplicate suppression,
and troubleshooting are shared with the HubSpot workflow and documented once in the
[email → Chat notification design](/it/automation/email-to-chat-notification-design.md).
This runbook records what is specific to this workflow — the differences from the
[HubSpot workflow](/it/automation/hubspot-form-chat-notification.md) are called out
explicitly.

# Workflow-specific parameters

| Setting | Value (HubSpot workflow differs where noted) |
|---|---|
| Subject filter (IMAP rule and IF condition) | contains `TECH REFERRAL FORM` |
| Wait before posting | **1 minute** (HubSpot: 3 minutes) |
| Body trim | **none — full body posted** (HubSpot: trimmed at "View at HubSpot") |
| Body length cap | 3500 characters (HubSpot: 800) |
| Chat message header | `🛠️ *TECH REFERRAL FORM*` |

# Node-by-node

Execution order: `IMAP Trigger (keeping@natran.com)` → `Only Once Per Email` →
`Is Tech Referral Form?` → `Wait 1 Minute` → `Notify Google Chat`.

**IMAP Trigger** — `emailReadImap` v2, credential "IMAP account" (`e0CKLlUF8kenOJej`,
shared with the HubSpot workflow), mailbox `INBOX`, mark-as-read, `resolved` format.
Custom email rules:

```
{{ JSON.stringify(["UNSEEN", ["SUBJECT", "TECH REFERRAL FORM"], ["SINCE", $now.minus(1, "days").toFormat("dd-LLL-yyyy")]]) }}
```

**Only Once Per Email** — `removeDuplicates` v2, `removeItemsSeenInPreviousExecutions`,
dedupe key `{{ $json.messageId }}`.

**Is Tech Referral Form?** — `if` v2.2, three AND-ed conditions:

1. Subject (`$json.Subject || $json.subject || $json.headers.subject`) **contains**
   `TECH REFERRAL FORM`.
2. Email Date, ISO-normalized (now substituted if absent), **after**
   `{{ $now.minus(1, 'days').toISO() }}`.
3. From address, lowercased, **notRegex** `[@.]keeping\.com`.

False branch is unconnected — non-matching mail is silently dropped.

**Wait 1 Minute** — `wait` v1.1, `timeInterval`, amount 1, unit minutes.

**Notify Google Chat** — `httpRequest` v4.2, `POST` to `<GOOGLE_CHAT_WEBHOOK_URL>`
(space `AAAAB4nawjQ`; URL carries `key`+`token`, treat as secret), authentication
`none`, JSON body, single field `text`.

# Message formatting

The message opens with `🛠️ *TECH REFERRAL FORM*` and From / To / Subject / Received
lines (with `$json.headers.*` fallbacks), then the **entire** email body — no trimming,
unlike the HubSpot workflow, because the referral form email has no boilerplate footer:

```
{{ ($json.textPlain || $json.text || $json.textHtml || '').toString().trim().substring(0, 3500) }}
```

**Phone detection** (shared normalization rules in the
[design doc](/it/automation/email-to-chat-notification-design.md)) — this workflow's
implementation scans the entire body with a global regex, manually rejecting matches
with a digit immediately before or after; digit strings longer than 11 are rejected
rather than truncated (HubSpot workflow keeps the last 11); it returns on the first
valid match. On a hit it appends a blank line, then
`⚠️ *Telephone number detected in Form.*` and
`📞 https://natran-sales.vercel.app/call-center?phone=1XXXXXXXXXX`; otherwise nothing.
Placeholder numbers like `(111) 111-1111` intentionally still match.

# Rebuild from scratch

Identical to the [HubSpot workflow's rebuild steps](/it/automation/hubspot-form-chat-notification.md)
with three substitutions: subject string `TECH REFERRAL FORM` (in both the IMAP custom
rules and the IF condition), Wait of 1 minute, and the message format above (full body
to 3500 chars, ⚠️-style phone line, 🛠️ header). The IMAP credential and the Chat
webhook are shared — build the HubSpot workflow's prerequisites first and reuse them.
Test with a fresh, unread email; each test email works only once (dedupe); expect the
post ~1 minute after pickup.
