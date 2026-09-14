---
type: Runbook
title: Teramind agent deployment
description: How the Teramind monitoring agent is packaged, deployed to all Windows devices, and exempted from Windows Defender.
tags: [teramind, devices, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Teramind (`natran.teramind.co`) is a computer productivity monitoring tool. The agent is
installed automatically on all workgroup computers via Endpoint Central, on every device
that has the Endpoint Central agent.

**Installing the agent does not start monitoring.** Monitoring is turned on separately in
the Teramind portal.

# Inspect the existing setup

`endpointcentral.manageengine.com` → **Configuration** → **All Configuration** → open
**Deploy Teramind Agent**.

# How the package was built

First get the agent and the service address:

1. Open the Teramind portal at `natran.teramind.co`.
2. Download the agent from `natran.teramind.co/#/download/agent`.
3. Find the service IP and port: **My Account** in the sidebar → **Server & Port** tab, or
   `natran.teramind.co/#/settings/server`. There are two IP/port combinations; either works.

Then create the package:

1. `endpointcentral.manageengine.com`, signed in as an administrator.
2. **Software Deployment** at the top.
3. **+Package** → **Windows**.
4. Name it **Teramind Agent**.
5. Type: **MSI/MSP**.
6. License type: **Commercial**.
7. **Locate installable** → **From Local Computer** → Browse → select the downloaded agent.
8. Enter the uploaded filename, including extension, in the **MSI/MSP File Name** field. It
   looks like
   `teramind_agent_x64_s-i(__9110f5c75a2671e9e9541b970e84619219bc8cb6).msi`.
9. In **MSI/MSP Properties for installation**, enter the router property using the IP and
   port from above: `TMROUTER=IPAddress:Port`.
10. **Add Package**.

# How the deployment was configured

1. **Configuration** tab.
2. **Configuration** → **Windows** in the left nav under *Add Configuration*.
3. Hover **Install/Uninstall Windows Software** → **Computer Configuration**.
4. Name it **Deploy Teramind Agent**.
5. Operation type: **Install**.
6. Package Name: **Teramind Agent**.
7. Deployment Policy: **Deploy any time at the earliest**.
8. Target: **Domain** → **WORKGROUP**.
9. Check **Retry this configuration on failed targets**.
10. **Deploy**.

# Windows Defender exclusions

Exclusions are deployed as a script from Endpoint Central so Windows Security does not
remove Teramind as a virus. They are applied to **all** Windows devices, whether or not the
Teramind agent is installed.

**Configuration** tab → **Script Repository** on the left under *Settings* → the script is
named `Set-Defender-Teramind-Exclusions.ps1`.

Its contents, per Teramind KB 8791033:

```powershell
# Teramind Agent Exclusions for Windows Defender based on Teramind KB 8791033

# --- PROCESS EXCLUSIONS ---
# Adds the executables to the process exclusion list.
Add-MpPreference -ExclusionProcess "C:\Windows\System32\drivers\tmfsdrv2.sys"
Add-MpPreference -ExclusionProcess "C:\Windows\System32\drivers\tm_filter.sys"

# --- FOLDER EXCLUSIONS ---
# Excludes the main program folders. This is the most important part.
Add-MpPreference -ExclusionPath "C:\ProgramData\{4CEC2908-5CE4-48F0-A717-8FC833D8017A}"

Write-Host "Teramind exclusions for Windows Defender have been successfully applied."
```

> **Source gap.** The document announces "4 primary components" — package, deployment,
> Defender exclusions, and *"when and how the agent package should be updated"*. The fourth
> is never written. There is no documented agent-update procedure.

> **Empty tab.** The source has a dedicated `Teramind` tab that is empty; all Teramind
> content lives under Device Management instead. Nothing is missing from this file, but
> anyone navigating the source by tab will find nothing.

# Related

- [Software deployment packages](/it/devices/software-deployment-packages.md)
- [Configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md)
