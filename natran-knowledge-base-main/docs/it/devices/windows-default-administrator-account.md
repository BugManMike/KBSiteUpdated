---
type: Runbook
title: Windows default administrator account
description: How to temporarily activate and then deactivate the hidden passwordless Windows administrator account on a company device.
tags: [manage-engine, devices, security]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
  - id: 1ceGvPiJLXssBkvH-gweh3xdLI88pTXpn-8VPIZKk5Xs
    resource: https://docs.google.com/document/d/1ceGvPiJLXssBkvH-gweh3xdLI88pTXpn-8VPIZKk5Xs/edit
    title: Instructions on how to activate the Windows Default Administrator Account
status: draft
---

Every Windows device has a hidden administrator account named **`Administrator`**. If no
active account on a device has admin rights, this one can be enabled remotely to make
changes.

> **It is passwordless.** Activating it exposes full administrator privileges to anyone at
> the keyboard. Activate temporarily only.

# Activate

1. Open `endpointcentral.manageengine.com` and sign in with an administrator account.
2. **Configurations** tab.
3. **All Configurations** under the *Views* section on the left.
4. Find **Manually Activate Windows Default Administrator Account**.
5. In the *Action* column, click the icon to open its menu.
6. **Modify → Modify Configuration**.
7. Scroll to **Define Targets**.
8. Set Target 1 to **Computer**, then enter the computer name. Clear any existing name.
9. Scroll down, **Deploy Immediately**. If the device is online it receives the change
   immediately. You are forwarded to the configuration summary, where **Refresh** confirms
   success.
10. Confirm from the device with `WINDOWS+L` — `Administrator` appears among the users.

> **A second source gives this procedure differently in three places.** The wiki document
> *"Instructions on how to activate the Windows Default Administrator Account"* (2025-05):
>
> - names the configuration **"Activate Windows Default Administrator Account"** — without
>   *Manually*, which is how you find it in a long list;
> - ends with **"Click Save. Now reboot the computer"** rather than **Deploy Immediately**, so the
>   change lands on reboot instead of at once;
> - frames the trigger as losing administrator access to a laptop, and points at the
>   [Device Inventory](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit)
>   spreadsheet to find which computer belongs to whom — a useful step this document omits.
>
> Its step numbering also jumps from 7 to 9, so a step is missing from the original. IT to confirm
> the configuration's actual name and whether Save-plus-reboot or Deploy Immediately is current.

# Deactivate

The account **disables itself** the next time the device checks in with Endpoint Central.

> **Conflicting intervals in the source.** This section states the automatic disable happens
> "approximately every 90 minutes". The configuration catalogue states the refresh cycle is
> "approximately every 2 hours or when the device is rebooted". Both describe the same
> check-in. IT to reconcile — see
> [configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md).

To disable it manually, follow the steps above but select **Manually Deactivate Windows
Default Administrator Account**. Confirm with `WINDOWS+L` — `Administrator` is gone.

# Related

- [Configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md)
- [Windows local account administration](/it/devices/windows-local-account-administration.md)
