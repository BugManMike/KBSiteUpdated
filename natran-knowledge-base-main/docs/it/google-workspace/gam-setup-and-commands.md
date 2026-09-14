---
type: Reference
title: GAM setup and commands
description: What GAM is, its two local directories, how to switch between the Natran and APS tenants, and the delegation commands in regular use.
tags: [gam, google-workspace, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1O097Wcy1uVZ3uqLJYsFXly0ti5ndsmenJjb_dCVlgNg
    resource: https://docs.google.com/document/d/1O097Wcy1uVZ3uqLJYsFXly0ti5ndsmenJjb_dCVlgNg/edit
    title: GAM commands
status: draft
---

**GAM (Google Apps Manager)** is a command-line tool for managing Google Workspace domain and
user settings. It is installed **locally on Windows devices**, not centrally.

The distribution in use is **GAMADV-XTD3** (`github.com/taers232c/GAMADV-XTD3`). A condensed
command reference is at `sites.google.com/view/gam--commands/`. Support runs through the
official GAM public chat group.

Installing GAM requires **administrative access**. For a new install, follow the GAMADV-XTD3
wiki.

# Directories

| Directory | Contents |
|---|---|
| `C:\GAMCONFIG` | Configuration and authorization files — what makes GAM work |
| `C:\GAMWORK` | Working directory. Output files land here — e.g. running a contacts backup saves the result here |

# Migrating an install to a new Windows device

1. Download and install the MSI from the
   [latest release page](https://github.com/taers232c/GAMADV-XTD3/releases). Make sure it is the
   MSI — you may need **Show all** to find it.
2. On the new device, create `C:\GAMCONFIG` and `C:\GAMWORK`.
3. Copy the contents of those folders from the source computer.
4. Update the environment variables: Control Panel → **System** → **Advanced system settings** →
   **Environment Variables**.
   - Under **Path** (System variables), add `C:\GAMADV-XTD3` if it is not already there.
   - Add a new variable: name `GAMCFGDIR`, value `C:\GAMCONFIG`.

> **A conflicting install path exists elsewhere.** [Windows PC
> setup](/it/devices/windows-pc-setup.md) Step 4 runs GAM from `c:\NATRAN-GAM` and links the
> *different* `GAM-team/GAM` distribution rather than GAMADV-XTD3. The two are not the same tool
> and their command syntax differs in places. IT to confirm which install is current before
> anyone follows either path.

# Switching between tenants

GAM is set up for **both** the `natran.com` and `advantageproservices.com` Workspace tenants.

| Command | What it does |
|---|---|
| `gam select *natran* save` | Switch to the Natran instance |
| `gam select *aps* save` | Switch to the Advantage Pro Services instance |
| `gam showsections` | Show which domain you are operating from — the active one has an asterisk |

> **Run `gam showsections` before anything destructive.** GAM's selected tenant persists via
> `save`, so a command typed hours later runs against whichever domain was last selected. The
> source's description of the `aps` command is truncated mid-sentence ("This will switch you y"),
> so the two switch commands are documented asymmetrically.

> Advantage Pro Services is a separate company. Its tenant is reachable from the same GAM install
> documented in the Natran knowledge base — the same cross-company overlap flagged in
> [email signature template structure](/it/google-workspace/email-signature-template-structure.md).

# Commands in regular use

| Area | Command | Effect |
|---|---|---|
| Gmail | `gam user john@natran.com delegate to jane@natran.com` | Gives Jane delegated access to John's Gmail — she can read and send on his behalf |
| Gmail | `gam user john@natran.com delete delegate jane@natran.com` | Removes that delegation |
| Gmail | `gam user john@natran.com print delegates` | Lists everyone with delegated access to John |
| Contacts | `gam user john@natran.com create contactdelegate jane@natran.com` | Delegates John's contacts to Jane; she gets a section at `contacts.google.com` to edit them |
| Contacts | `gam user john@natran.com delete contactdelegate jane@natran.com` | Removes the contact delegation |

Inbox delegation is a step in
[Workspace account provisioning](/it/google-workspace/account-provisioning.md) — delegate to the
user's manager and other interested parties.

> The source capitalises one command as `Gam user ...`. GAM is case-insensitive on the executable
> name, so this is cosmetic.

# Other documented uses of GAM

- Deploying email signatures — [email signature deployment](/it/google-workspace/email-signature-deployment.md)
- Registering a device as company-owned — [Windows PC setup](/it/devices/windows-pc-setup.md)

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Email signature deployment](/it/google-workspace/email-signature-deployment.md)
