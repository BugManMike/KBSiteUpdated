---
type: Runbook
title: Windows PC setup
description: Full build of a company Windows device — OS setup bypassing a Microsoft account, the GCPW enrollment script, registering the serial as company-owned, then the per-user software, web app, printer and scan folder setup.
tags: [google-workspace, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 13xBwownIeTuL7yRpeDrG4HtnuEZX1KDS-ELOawWESLw
    resource: https://docs.google.com/document/d/13xBwownIeTuL7yRpeDrG4HtnuEZX1KDS-ELOawWESLw/edit
    title: Windows PC setup
status: draft
---

Two halves. **Initial device setup** runs once per device. **User setup** repeats every time
the device is assigned to someone.

> **Prerequisite: Windows 10 Pro or Windows 11 Pro.** A Home-edition device can be upgraded
> via the Microsoft Store, which costs money — check the edition before starting.

> **This procedure overlaps [device enrollment](/it/devices/endpoint-central-device-enrollment.md)
> and the two do not agree.** That document says a new device gets three things: registration
> as company-owned in Workspace, GCPW, and the **ManageEngine Endpoint Central agent** — with
> everything else done through ManageEngine. This procedure installs Chrome and GCPW via a
> PowerShell script and **never mentions the Endpoint Central agent at all**, then installs
> software and web apps by hand. This document was last modified 2025-09; the IT
> single-source-of-truth is 2026-07. **The manual steps below are very likely superseded by
> ManageEngine deployment** — see [software deployment
> packages](/it/devices/software-deployment-packages.md) — but that has not been confirmed, so
> both are recorded. IT to reconcile.

# Initial device setup

## Step 1 — OS setup

The goal is a **local** account named `Admin`, with no Microsoft account attached.

**Windows 11**

1. Location **United States**; keyboard **US**; **skip** the second keyboard.
2. Setup checks for updates and may reboot.
3. When asked to name the device, click **Skip** — setup assigns a name automatically.
4. **Set up for personal use.**
5. At the Microsoft account screen: **Sign-in options** → **Offline account**. Skip the screens
   pushing a Microsoft account.
6. Enter **Admin** as the name.
7. Create a password you will remember and answer the security questions.
8. **Accept** the privacy settings and allow a few minutes to finish.

**Windows 10**

1. Boot and select language, location, keyboard.
2. *Pro:* **Offline Account** → **Limited experience**.
3. *Home:* temporarily disconnect Ethernet and do not join wifi. Select **I don't have
   internet** → **Continue with limited setup**. This bypasses the Microsoft account and
   creates a local account.
4. Enter **Admin** as the name, create a password and security questions.
5. Proceed through the rest; customisation screens can be skipped or left at defaults.
6. Once you can sign in, join wifi or reconnect Ethernet. Choose **Do Not Allow your PC to be
   discoverable**.

## Step 2 — Run the enrollment script

The script downloads and installs a company-managed Chrome plus GCPW. See
[GCPW deployment](/it/devices/gcpw-deployment.md) for how GCPW is managed centrally.

Download it from
`https://drive.google.com/drive/folders/17itXfV2rCpLfogXJHdGq6WxpWoonlyqL` and **save it to
the Downloads folder**. Ignore any warnings. The script is credited to a public gist by
Jordigg.

Search Windows for **Windows PowerShell** and choose **Run as Administrator** — the process
will not work otherwise. Then:

```
Cd C:\Users\Admin\Downloads
```

```
powershell.exe -ExecutionPolicy Unrestricted -NoLogo -NoProfile -Command "& '.\gcpw_enrollment.ps1' -MDMvalue 1"
```

A security warning is normal — press **R + Enter** to run. It finishes with *MDM Enrollment
confirmation completed successfully*.

You should now see Chrome installed and an **Add work account** option on the lock screen
(`Windows+L`).

> **The source's closing quote mark is a typographical one** (`1”`), which PowerShell will
> reject. Corrected to a straight quote above — this is a transcription fix to a shell command,
> not a change to the procedure.

## Step 3 — Sign into Windows

1. Click **Add work account**.
2. Sign in with company email and password.
3. Accept any privacy settings.

## Step 4 — Register the device as company-owned

**Once per device.** Already-registered devices show as company owned; unregistered ones show
as user owned.

First find the serial: `admin.google.com` → **Devices** → **Mobile & endpoint** → **Devices**
→ sort by **First Sync** newest-first → open the device → copy the **serial number**.

**Option 1 — admin console.** Devices → Mobile & endpoint → Devices → the icon in the
upper-right to open **Import company owned devices** → select **Windows** → **Download import
template** → add the serial → save as CSV → **Upload File** → **Import**.

**Option 2 — GAM.** Faster but needs GAM installed and Super Admin permissions. See
[GAM setup and commands](/it/google-workspace/gam-setup-and-commands.md).

```
CD c:\NATRAN-GAM
gam create device serial_number ####### device_type WINDOWS
```

> **Two different GAM install paths are documented across the corpus.** This says
> `c:\NATRAN-GAM`; [GAM setup and commands](/it/google-workspace/gam-setup-and-commands.md)
> says `C:\GAMCONFIG` and `C:\GAMWORK` with `C:\GAMADV-XTD3` on the PATH, and a different GAM
> distribution (GAMADV-XTD3 versus GAM-team/GAM). IT to confirm which install is current.

Workspace converts the device to Company Owned. **This registration is what
[Context-Aware Access](/it/google-workspace/context-aware-access.md) checks** — an unregistered
device gets blocked from company data.

# User setup

## Step 5 — First login

GCPW should have synced by now.

1. `Windows+L` for the lock screen.
2. **Add Work Account**.
3. Sign in with the new user's credentials.
4. The user accepts the Terms and Conditions.

> **The user will be locked out if they have not set up 2-Step Verification.** See
> [2-Step Verification](/it/google-workspace/two-step-verification.md).

## Step 6 — Install software

- Jabra headset software
- [Google Drive for desktop](https://www.google.com/drive/download/)
- Snipaste *(recommended)*

## Step 7 — Web apps

**Chrome (required).** Open Chrome, select **Link accounts** if prompted, close and reopen,
then set it as the default browser.

**Google Drive for Desktop (required).** Find the Drive icon in the system tray and sign in
via the browser. If Chrome is already default it signs in automatically.

**Google Chat, Google Meet (recommended).** Visit the site, wait for the install prompt, then
right-click the taskbar icon → **Pin to taskbar**.

> The icon sometimes reverts to the Chrome icon when the app is closed. Repeat the pin and it
> sticks the second time.

**Kanbanchi (optional).** Sign in, then use the install icon in the URL bar → **Install** →
pin to taskbar.

**Call Tracking Metrics (required for call handling representatives).** Open CTM from company
bookmarks → install icon in the URL bar → **Install** → pin to taskbar. **Whitelist the site
and turn on notifications.**

Also pin the Snipping Tool and Calculator.

> **The source's Windows-app list reads "Snipping toop" and "Calcuator"** — typos, transcribed
> as intended.

> **CTM here, RingCentral elsewhere.** This step installs Call Tracking Metrics as the phone
> app. [Windows device user removal](/it/devices/windows-device-user-removal.md), from a
> different source document, installs **RC Phone Desktop** (RingCentral) instead, with detailed
> notification and headset settings. See [RingCentral voicemail
> setup](/it/telephony/ringcentral-voicemail-setup.md) for the wider legacy-system question.

## Step 8 — Printer

1. Find the printer's **MAC address** on the device — a string like `2C:54:91:88:C9:E3`.
2. On the Windows device, search **Add A Printer**.
3. **Add a printer or scanner** — Windows detects printers on the company network.
4. Select the printer **matching the MAC address** and **Add device**.
5. Right-click the printer → test print.

> **This is not how printers are deployed now.** [ManageEngine printer
> deployment](/it/printers/manage-engine-deployment.md) pushes printers by **fixed IP** through
> Endpoint Central precisely so nobody installs them by hand. This manual MAC-address method
> is probably superseded. IT to confirm.

## Step 9 — Scan folder

1. Share the **Scan** folder with the user.
2. The user opens `drive.google.com` → **Shared with me** → drags the Scan folder into
   **My Drive**. This syncs it to their device.
3. In **File Explorer** → **Google Drive (G:)** → **My Drive** → right-click **Scan** →
   **Pin to Quick Access**.

> **Troubleshooting.** An error opening the folder usually means the user is signed out of the
> Google Drive desktop app. Recheck Step 7.

# Screenshots

Written against interface screenshots that did not survive conversion. Steps that referenced
an unnamed icon or button — notably the *Import company owned devices* icon in Step 4 — are
thinner here than in the original.

# Related

- [Device enrollment](/it/devices/endpoint-central-device-enrollment.md)
- [GCPW deployment](/it/devices/gcpw-deployment.md)
- [Windows device user removal](/it/devices/windows-device-user-removal.md)
- [2-Step Verification](/it/google-workspace/two-step-verification.md)
