---
type: Runbook
title: Group email moderation
description: What a "Moderator's spam report" email means and how to approve or reject held messages in Google Groups.
tags: [google-workspace, email]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1xtRrheMwn5ljYJrU-ppBzw3TFavOEVGUEF_0I637T0U
    resource: https://docs.google.com/document/d/1xtRrheMwn5ljYJrU-ppBzw3TFavOEVGUEF_0I637T0U/edit
    title: Approve or reject moderations email in Keeping or Group emails
status: draft
---

An email in Keeping with the subject **"Moderator's spam report"** means a Keeping or group email
was marked as spam. **The message is held, not delivered** — it resends on approval.

# Approve or reject

1. Sign into `groups.google.com`.
2. Click the group name.
3. Under **Conversations** on the left, click **Pending**.
4. Click a message to read it.
5. For a single message, use **Approve message** or **Reject message** in the message entry.

For several at once, check the boxes and choose one of:

| Action | Effect |
|---|---|
| **Approve messages** | Delivers the selected messages |
| **Reject messages** | Discards them |
| **Approve author** | Approves the messages **and auto-approves all that author's future posts** |
| **Reject author** | Bans the author from the conversation and reports the messages as spam |

> **Approve author is the consequential one.** It lets that author post directly to the group in
> future and **supersedes group-level moderation and posting permissions**. It is not simply
> "approve, but faster" — it is a standing permission change. Use it only for a sender you want
> permanently trusted on that group.

Google's own documentation covers this at
`support.google.com/groups/answer/2466386`.

# Related

- [Keeping shared inbox setup](/it/google-workspace/keeping-shared-inbox.md)
- [Google Groups membership](/it/google-workspace/google-groups.md)
