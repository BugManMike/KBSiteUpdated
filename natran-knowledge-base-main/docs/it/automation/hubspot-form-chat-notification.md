---
type: Runbook
title: HubSpot form → Chat notification workflow
description: The n8n workflow that posts HubSpot "New Form Submission" emails to office@natran.com into Google Chat — exact node parameters, message formatting, and rebuild steps.
tags: [n8n, notifications, email]
resource: https://n8n.srv1090686.hstgr.cloud/workflow/kmoyKr160L6FQ3OW
generated:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
sources:
  - resource: https://n8n.srv1090686.hstgr.cloud/workflow/kmoyKr160L6FQ3OW
    title: "n8n workflow: Office@natran.com Hubspot → Google Chat notification (ID kmoyKr160L6FQ3OW)"
verified:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
  note: Read from the saved workflow definition; re-verified after a session refresh, both reads identical.
status: draft
---

Workflow **"Office@natran.com Hubspot → Google Chat notification"**, ID `kmoyKr160L6FQ3OW`,
Active as of 2026-07-28. When HubSpot emails a **"New Form Submission"** notification (a
new inbound lead) to office@natran.com, this workflow posts it into Google Chat space
`AAAAB4nawjQ` with a one-click dialer link if a phone number is found.

The five-node shape, mail-source rationale, keeping.com exclusion, duplicate suppression,
and troubleshooting are shared with the tech-referral workflow and documented once in the
[email → Chat notification design](/it/automation/email-to-chat-notification-design.md).
This runbook records what is specific to this workflow.

# Workflow-specific parameters

| Setting | Value |
|---|---|
| Subject filter (IMAP rule and IF condition) | contains `New Form Submission` |
| Wait before posting | **3 minutes** |
| Body trim | everything from `View at HubSpot` downward removed |
| Body length cap | 800 characters |
| Chat message header | `📨 *New Form Submission*` |

# Node-by-node

Execution order: `IMAP Trigger (keeping@natran.com)` → `Only Once Per Email` →
`Is HubSpot Form Submission?` → `Wait 3 Minutes` → `Notify Google Chat`.

**IMAP Trigger** — `emailReadImap` v2, credential "IMAP account" (`e0CKLlUF8kenOJej`),
mailbox `INBOX`, mark-as-read, `resolved` format. Custom email rules:

```
{{ JSON.stringify(["UNSEEN", ["SUBJECT", "New Form Submission"], ["SINCE", $now.minus(1, "days").toFormat("dd-LLL-yyyy")]]) }}
```

**Only Once Per Email** — `removeDuplicates` v2, `removeItemsSeenInPreviousExecutions`,
dedupe key `{{ $json.messageId }}`.

**Is HubSpot Form Submission?** — `if` v2.2, three AND-ed conditions:

1. Subject (`$json.Subject || $json.subject || $json.headers.subject`) **contains**
   `New Form Submission`.
2. Email Date, ISO-normalized (now substituted if absent), **after**
   `{{ $now.minus(1, 'days').toISO() }}`.
3. From address, lowercased, **notRegex** `[@.]keeping\.com`.

False branch is unconnected — non-matching mail is silently dropped.

**Wait 3 Minutes** — `wait` v1.1, `timeInterval`, amount 3, unit minutes.

**Notify Google Chat** — `httpRequest` v4.2, `POST` to `<GOOGLE_CHAT_WEBHOOK_URL>`
(space `AAAAB4nawjQ`; URL carries `key`+`token`, treat as secret), authentication
`none`, JSON body, single field `text`.

# Message formatting

The message opens with `📨 *New Form Submission*` and From / To / Subject / Received
lines pulled from the parsed email with fallback chains, then the body:

```
{{ (($json.textPlain || $json.text || $json.textHtml || '').toString().split('View at HubSpot')[0]).trim().substring(0, 800) }}
```

HubSpot's notification email ends with a "View at HubSpot" call-to-action and footer
boilerplate — the split keeps only what precedes it, then truncates to 800 characters.

**Phone detection** (shared normalization rules in the
[design doc](/it/automation/email-to-chat-notification-design.md)) — this workflow's
implementation scans only the body *before* "View at HubSpot"; tries lines containing
`phone|mobile|cell|reached at` (case-insensitive) first, then the whole body; uses a
`(?!\d)` lookahead to avoid matching inside longer digit runs; and if the digit string
exceeds 11 digits keeps the **last 11**. On a hit it appends
`📞 *Call:* https://natran-sales.vercel.app/call-center?phone=1XXXXXXXXXX`; otherwise
nothing. Placeholder numbers like `(111) 111-1111` intentionally still match.

> **Source defect — drift between the two workflows:** this workflow's *message body*
> From/To extraction omits the `$json.headers.from` / `headers.to` fallback that the
> tech-referral workflow includes (this workflow's *IF condition* does include it). Looks
> like drift, not intent. Owner of the n8n instance to reconcile.

# Rebuild from scratch

1. Ensure keeping@natran.com receives office@natran.com's group mail; generate a Google
   app password for it (`<IMAP_APP_PASSWORD>`, requires 2SV).
2. In Chat space `AAAAB4nawjQ`: space settings → Apps & integrations → Webhooks → create
   an incoming webhook; copy the URL (`<GOOGLE_CHAT_WEBHOOK_URL>`).
3. In n8n, create the IMAP credential: host `imap.gmail.com`, user `keeping@natran.com`,
   password `<IMAP_APP_PASSWORD>`, SSL/TLS (port 993).
4. Build the five nodes with the parameters above, connected in order, execution order
   setting `v1` (default).
5. Test with a fresh, unread email — subject containing `New Form Submission`, sent
   within the last day, containing a phone number. Each test email works only once
   (dedupe); expect the post ~3 minutes after pickup.
6. Activate.
