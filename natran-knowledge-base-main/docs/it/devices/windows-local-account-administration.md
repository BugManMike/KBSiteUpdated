---
type: Runbook
title: Windows local account administration
description: Changing a local account's permission level, suspending and re-enabling it, deleting it with or without keeping data, and listing the accounts on a device.
tags: [manage-engine, devices, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

All of these run as Endpoint Central configurations against a **computer name**, and every
one of them requires the device to be connected to the internet. **None of them forcibly
logs the user out.**

# Find the local username first

The internal Windows username differs from what the employee sees. John Smith sees
"John Smith"; the computer sees `johnsmith_natran`. That name is assigned by GCPW when the
user first creates their account.

`endpointcentral.manageengine.com` → **Inventory** → **Computers** → find the device. The
name is in the *Logged On Users* or *Last Login User* column. Add that column via the icon
in the table's upper-right corner if it is not shown.

For a complete list of every account on a device, run the **List All Local User Accounts**
configuration against the computer name, wait for the Execution Summary to turn from yellow
to green, then **Execution Status** tab → *Remarks* column → **View Log**.

**Do not delete these.** They are system accounts, disabled by default:

- `Administrator`
- `DefaultAccount`
- `Guest`
- `WDAGUtilityAccount`

# Change permission level

**Configuration** tab → **All Configurations** → either **Change local account type to
Standard** or **Change local account type to Administrator**.

**Modify → Configuration**. In the *Command Line* field replace `username` with the local
username, e.g. `johnsmith_natran`. Set **Define Targets** to **Computer** and enter the
computer name. **Deploy Immediately.** If the user is online their permission level updates.

# Suspend and re-enable

There are two ways to stop a user signing in.

**Suspend their Google Workspace account.** Because sign-in goes through GCPW, suspending
the Workspace account prevents future sign-in. `admin.google.com` → search the user → click
their name → **Suspend**.

> This does **not** end their current Windows session, and there is a window in which a user
> who signs into Windows before the device syncs with Workspace can still reach their
> computer.

**Suspend the Windows account.** **Configuration** → **All Configurations** → **Suspend User
Account** → **Modify → Configuration**. Set the *Command Line* to:

```
net user username /active:no
```

Set **Define Target** to **Computer** and enter the computer name.

To re-enable, use the **Enable User Account** configuration with:

```
net user username /active:yes
```

# Delete

**Method 1 — delete and keep the data (recommended).** Backs up all of the user's data on
the device before deleting the local account. Data lands in `C:\Users` under a name like
`C:\johnsmith_natr_SAVED_2025-09-15`.

> The retained folder is readable by **anyone using that computer**. If the data is not
> needed, use Method 2.

**All Configurations** → **Safe Delete User Account** → **Modify → Configuration** → enter
the username in **Script Argument(s)** → **Define Target** = Computer + computer name.

**Method 2 — delete the user and the data. Cannot be undone.**

**All Configurations** → **Permanently Delete User** → **Modify → Configuration** → enter
the username in **Script Argument(s)** → **Define Target** = Computer + computer name.

# Lock, log off and disable in one step

A separate on-demand pair exists for the case where the user is still signed in:

1. **On-Demand: Lock, logoff and disable user account** — logs the user off if signed in and
   disables the account so they cannot sign back in.
2. **On-Demand: Safe delete user** — permanently deletes the account and retains a copy of
   the data in the `User` subfolder, accessible to admins.

> **Naming conflict in the source.** These two on-demand configurations are named
> *On-Demand: Safe delete user* here and **Safe Delete User Account** in the deletion section
> above, with slightly different descriptions of where retained data lands (`User` subfolder
> versus `C:\Users\<name>_SAVED_<date>`). It is unclear whether these are one configuration
> or two. IT to confirm the actual configuration names in Endpoint Central.

# Deleting a folder by command prompt

Endpoint Central can open a command prompt on a device:

1. Locate the computer in **Inventory**.
2. **Actions → System Manager → Command Prompt**.
3. Navigate to the folder under `C:\Users\` you want to remove.
4. `rmdir /s "foldername"` — e.g. `rmdir /s "JohnSmith"`, or with a full path
   `rmdir /s "C:\Users\JohnSmith"`.

# Related

- [Windows default administrator account](/it/devices/windows-default-administrator-account.md)
- [GCPW deployment](/it/devices/gcpw-deployment.md) — assigns the local username
- [Workspace account offboarding](/it/google-workspace/account-offboarding.md)
