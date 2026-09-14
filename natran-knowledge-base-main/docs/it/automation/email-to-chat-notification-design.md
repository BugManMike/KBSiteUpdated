---
type: Reference
title: Email → Google Chat notification design
description: The shared design behind the n8n workflows that post lead emails into Google Chat — mail source, filtering rationale, duplicate suppression, phone-link convention, and troubleshooting.
tags: [n8n, notifications, email]
generated:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
sources:
  - resource: https://n8n.srv1090686.hstgr.cloud/workflow/kmoyKr160L6FQ3OW
    title: "n8n workflow: Office@natran.com Hubspot → Google Chat notification"
  - resource: https://n8n.srv1090686.hstgr.cloud/workflow/4N3Nwf2jxhICTZrO
    title: "n8n workflow: TECH REFERRAL FORM → Google Chat notification"
verified:
  by: Claude (Fable 5)
  at: 2026-07-28T23:42:50Z
  note: Read directly from the saved workflow definitions on the live n8n instance; not tested against production executions.
status: draft
---

Two n8n workflows on `https://n8n.srv1090686.hstgr.cloud` watch a mailbox for lead-related
emails and post them into Google Chat, because the team lives in Chat, not in a shared
inbox. They share one design; this document records it once. The per-workflow specifics
live in [HubSpot form → Chat notification](/it/automation/hubspot-form-chat-notification.md)
and [Tech referral form → Chat notification](/it/automation/tech-referral-chat-notification.md).

Both workflows post to the **same Google Chat space, ID `AAAAB4nawjQ`**, via an incoming
webhook. The webhook URL (`<GOOGLE_CHAT_WEBHOOK_URL>`) carries its `key` and `token` as
query parameters — **the whole URL is a secret** and is stored only inside the HTTP node
of each workflow, not as an n8n credential object.

# Why IMAP on keeping@natran.com

Lead mail is addressed to office@natran.com, but office@natran.com is a **Google Group,
not a mailbox** — there is nothing to connect IMAP to. keeping@natran.com is a real
Google Workspace mailbox that receives the group's mail, so both workflows connect there.

Both share a single n8n IMAP credential (name "IMAP account", ID `e0CKLlUF8kenOJej`):
host `imap.gmail.com`, user `keeping@natran.com`, authenticated with a Google app
password (`<IMAP_APP_PASSWORD>`). An app password was used instead of OAuth because it
avoids the Google Cloud OAuth-consent setup and token-refresh maintenance — a plain IMAP
credential is a single static secret. App passwords require 2-step verification on the
account and die when the account password or 2SV configuration changes.

**The Google Group rewrites the From header** of relayed mail, so the apparent sender is
unreliable. That is why *neither workflow filters on sender identity* — they filter on
the subject line. The only sender-based rule is the exclusion below.

# Shared pipeline shape

Both workflows are the same five nodes:

```
IMAP Trigger → Only Once Per Email → IF (subject/date/sender) → Wait → Notify Google Chat
```

- **IMAP Trigger** (`emailReadImap` v2) — watches `INBOX`, marks each fetched email as
  read (`postProcessAction: read`), parses to `resolved` format, and pre-filters
  server-side with a Custom Email Rules expression:
  `["UNSEEN", ["SUBJECT", "<subject>"], ["SINCE", <yesterday, dd-LLL-yyyy>]]`.
- **Only Once Per Email** (`removeDuplicates` v2) — operation
  `removeItemsSeenInPreviousExecutions`, dedupe key `{{ $json.messageId }}`. See
  duplicate suppression below.
- **IF** (`if` v2.2, AND, loose type validation) — three conditions: subject *contains*
  the workflow's phrase; email Date *after* `$now.minus(1, 'days')` (missing Date is
  substituted with now, which always passes); lowercased From *does not match regex*
  `[@.]keeping\.com`.
- **Wait** (`wait` v1.1, time interval) — sits between the IF and the Chat POST, so the
  delay applies only to emails that already passed all filters.
- **Notify Google Chat** (`httpRequest` v4.2) — `POST` to `<GOOGLE_CHAT_WEBHOOK_URL>`,
  auth `none` (the URL token is the auth), JSON body with a single `text` field built by
  an n8n expression.

Emails that fail the IF go to an unconnected false branch — silently discarded, but
already marked read and recorded by the dedupe node.

# The keeping.com exclusion regex

Mail sent *from* keeping.com itself (the service that also uses this mailbox) must not be
posted as leads. The IF uses `notRegex` `[@.]keeping\.com` rather than a plain "does not
contain keeping.com" **deliberately**: a contains-check would also swallow innocent
domains that merely end in the string, such as `bookkeeping.com` or `housekeeping.com`.
The regex requires the character immediately before `keeping.com` to be `@` or `.`, so
`user@keeping.com` and `user@mail.keeping.com` are excluded while `user@bookkeeping.com`
is not. The From value is lowercased before the test, making it effectively
case-insensitive. The regex is unanchored at the end, so `keeping.com.anything` would
also match; no known practical impact.

# Phone-number detection and the call-center link

Each message ends with an inline JavaScript expression that scans the email body for a
US phone number and, if found, appends a link:

```
https://natran-sales.vercel.app/call-center?phone=1XXXXXXXXXX
```

Normalization is identical in both workflows: strip all non-digits from the match; if 10
digits remain, prepend `1`; emit the link only for an 11-digit number beginning with `1`.
The pattern matched is a formatted US number — optional `+1`/`1` prefix, 3-digit area
code with optional parentheses, optional space/dot/dash separators.

**There is deliberately no validity check** — placeholder numbers such as
`(111) 111-1111` still match and still produce a link. Test submissions use such numbers,
and they must still be clickable. Implementation details differ per workflow; see each
runbook.

# Duplicate suppression, and why re-testing fails

The dedupe node keeps a persistent history (in n8n's database, scoped to that node in
that workflow) of every Message-ID it has passed. Combined with the trigger fetching only
`UNSEEN` mail and marking everything it touches read, a given email notifies at most once.

**Operational gotcha: re-testing with the same email is impossible** until the history is
cleared. Replaying a stored message keeps its Message-ID, so it is dropped silently. To
re-test, either send a genuinely new email (fresh Message-ID) or clear the node's
history: open the workflow, right-click **Only Once Per Email** → clear the node's
deduplication history. A test email must also be unread and less than a day old, or the
trigger and date filters drop it.

# Troubleshooting

**No notification arrives.** In order: (1) workflow Active? (2) email actually unread in
keeping@natran.com's INBOX with the exact subject substring — matching is case-sensitive
and literal; (3) already read? Anything that marks it read first (a human, another mail
client) means the trigger never sees it; (4) older than a day? Both the IMAP `SINCE` rule
and the IF date condition drop it; (5) sender a keeping.com address? Deliberately
excluded; (6) Message-ID already processed? Dedupe drops it silently; (7) check the
execution list — an item stopping at the IF false branch means a filter failed; (8)
remember the built-in delay (3 min / 1 min) before the post.

**Duplicate notifications.** The dedupe key is Message-ID, so true duplicates should be
impossible. Usually it is two *different* emails (a re-sent form gets a new Message-ID),
a cleared dedupe history with old unread mail present, or one email matching *both*
workflows' subjects — they share one Chat space.

**Chat POST fails.** Read the HTTP node error in the failed execution. 401/403/404 —
webhook rotated or deleted in the space; create a new webhook and update the node. 400 —
the built `text` expression produced an empty or invalid body; inspect the expression
output against the actual email item. Confirm the space `AAAAB4nawjQ` and its webhook
still exist.

**Trigger stops firing entirely.** Check the IMAP credential — Google app passwords are
revoked when the account password changes or 2SV is reconfigured. Execution list shows
connection errors.

# Known gaps

Everything above was read from the saved workflow definitions on 2026-07-28, not proven
against production traffic. Untested edge cases: HTML-only emails falling back to
`textHtml`, multiple phone numbers in one body, numbers split across lines. The IMAP
credential's port/TLS fields were not explicitly readable (host and user were; Gmail
defaults presumably apply). That keeping@natran.com receives the group's mail, and that
the group rewrites From, is business context n8n itself cannot confirm. Execution history
was not reviewed, so real-world failure rates and dedupe-hit rates are unknown. The
rationale for the two different Wait durations is undocumented.
