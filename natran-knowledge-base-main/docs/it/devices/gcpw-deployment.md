---
type: Runbook
title: GCPW deployment
description: How Google Credential Provider for Windows is deployed in two parts — the agent and a registry token — so users sign into Windows with their Google account.
tags: [gcpw, devices, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Google Credential Provider for Windows lets users sign in and create Windows accounts using
their Google account. It is deployed in two parts, both automatic: the **agent**, then a
**registry token**.

After initial installation, allow roughly **10 minutes** before the agent syncs with Google's
servers.

GCPW is what assigns the local Windows username — `johnsmith_natran` rather than
`John Smith`. See
[Windows local account administration](/it/devices/windows-local-account-administration.md).

# Inspect the existing setup

`endpointcentral.manageengine.com` → **Configurations** → **All Configurations** → open
**Deploy GCPW**, then return to All Configurations and open **Deploy GCPW Registry Token**.

# Part 1 — the agent

1. **Configurations** at the top.
2. **Configuration → Windows** in the sidebar under *Add Configuration*.
3. Hover **Install/Uninstall Windows Software** → **Computer Configuration**.
4. Operation Type: **Install**.
5. Name it **Deploy GCPW**.
6. Package name: search for **Google Chrome (x64)**. The package name also carries a long
   version number.
7. Under **Configure Install/Uninstall options**, ensure **System User** is selected.
8. Under **Apply Deployment Policy**, select **Deploy at any time earliest**. It installs
   after reboot or at the next server sync.
9. Target: **Domain** → **WORKGROUP** to reach all computers.
10. **Deploy**.

> **Source defect.** Step 6 instructs you to select the **Google Chrome (x64)** package for a
> configuration named *Deploy GCPW*. GCPW and Chrome are different installers. Either the
> package name is wrong here or the configuration installs Chrome rather than GCPW. IT to
> verify against the actual package in Endpoint Central before relying on this step.

# Part 2 — the registry token

Get the token:

1. Open `admin.google.com/ac/devices/windows/gcpwsetup` with an admin account.
2. Click download GCPW — **but do not download the file**.
3. Copy the token. **Do not regenerate it.** It resembles
   `3XXXXXX97-b4a0-41b1-9e3c-736XXXXX415b`.

Deploy it:

1. **Configurations** at the top.
2. **Configuration → Windows** under *Add Configuration*.
3. Hover **Registry** → **Computer Configuration**.
4. Name it **Deploy GCPW Registry Token**.
5. Registry Configuration type: **Manually**.
6. Action: **Write Value**.
7. **Header Key:** `HKEY_LOCAL_MACHINE`
8. **Sub-Key:** `SOFTWARE\Policies\Google\CloudManagement`
9. **Data Type:** `REG_SZ`
10. **Value Name:** `EnrollmentToken`
11. **Value Data:** the token copied above.
12. Target: **Domains** and **WORKGROUPS** to apply to all.
13. **Deploy**.

> **Possible collision.** This writes `EnrollmentToken` under
> `SOFTWARE\Policies\Google\CloudManagement`, while
> [Chrome managed browser enrollment](/it/devices/chrome-managed-browser-enrollment.md)
> writes `CloudManagementEnrollmentToken` under `SOFTWARE\Policies\Google\Chrome` using a
> *different* token from a different admin console page. The two are documented as separate
> and both are described as organisation-wide. IT to confirm both are required and that the
> tokens are not being confused for one another.

# Related

- [Device enrollment](/it/devices/endpoint-central-device-enrollment.md)
- [Windows local account administration](/it/devices/windows-local-account-administration.md)
