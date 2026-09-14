---
type: Runbook
title: Keeping shared inbox setup
description: Inviting a user to Keeping, the setup and preference steps they complete themselves, and what the Chrome extension does.
tags: [keeping, google-workspace, onboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1ige_I7YNEvFt8kzup7OAohdCreVHIwK-yRHLell73gg
    resource: https://docs.google.com/document/d/1ige_I7YNEvFt8kzup7OAohdCreVHIwK-yRHLell73gg/edit
    title: Setup Keeping.com account
  - id: 1tquo5rTwvaJbO8koh1jTJySmuJo_iKcz_LZpR4m8iCs
    resource: https://docs.google.com/document/d/1tquo5rTwvaJbO8koh1jTJySmuJo_iKcz_LZpR4m8iCs/edit
    title: Keeping setup
status: draft
---

Keeping is a shared inbox that lives **inside** the user's regular Gmail inbox. Teams use it to
assign customer emails, change status, comment and track progress.

> **Two source documents cover this**, in different wiki folders, with the same invite procedure
> written twice. One adds the user-side setup and preferences; the other adds a note about the
> Chrome web app. Merged here. **IT should delete one of the originals** — as it stands the two
> disagree on the sign-in URL (`keeping.com` versus `app.keeping.com`) and on whether the Chrome
> extension needs installing.

# Step 1 — Invite the user (admin)

1. Sign into `app.keeping.com` with administrator credentials.
2. **Agents** in the left navigation.
3. **Invite Team Member**.
4. Enter the user's email address, first and last name.
5. Select **Agent** as the role.
6. **Check all mailboxes** — typically all of them.
7. **Send Invitation**.

The user has to accept the invitation before anything else works.

> **Make sure the user is not exposed to sensitive inboxes** — recruiting and HR. That
> constraint comes from
> [Workspace account provisioning](/it/google-workspace/account-provisioning.md) and cuts
> directly against step 6's "check all mailboxes". **The two cannot both be right.** IT to
> settle which mailboxes a standard Agent should receive.

# Step 2 — User setup

The user does these themselves:

1. Open the invitation email and follow the link.
2. **Sign in with Google** → select their email address.
3. **Check all the boxes** and approve permissions.
4. **Check all the boxes** to accept the Terms of Use and Privacy Policy on the welcome screen →
   **Submit**.
5. **Accept**.
6. Install the Keeping Chrome extension → **Add to Chrome** → confirm the prompts.

> **The two sources disagree on step 6.** One walks the user through installing the extension;
> the other says *"the web app is automatically installed when they sign into their Chrome
> profile so this step can be skipped."* Try signing in first and only install manually if the
> extension is absent.

# Step 3 — User preferences

Also done by the user:

1. **Preferences** in the sidebar.
2. Check all boxes under **Push ticket into my Gmail Inbox**.
3. Under **Notification Settings**, click **Enable Notifications** and allow the Chrome prompts.

> Step 2 here is the same setting called *"push to inbox"* in
> [Workspace account provisioning](/it/google-workspace/account-provisioning.md), which notes it
> "needs to be done by user" — consistent across sources.

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Group email moderation](/it/google-workspace/group-email-moderation.md)
- [Email forwarding](/it/google-workspace/email-forwarding.md) — offboarded accounts forward into Keeping
