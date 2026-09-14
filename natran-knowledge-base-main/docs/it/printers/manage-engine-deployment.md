---
type: Runbook
title: ManageEngine printer deployment
description: Creating an IP Printer configuration in Endpoint Central so a fixed-IP printer deploys to work devices, including which driver INF file to pick.
tags: [manage-engine, printers, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

The printer must already have a fixed IP — see
[fixed IP assignment](/it/printers/fixed-ip-assignment.md).

> **Shortcut for a duplicate model.** If the new printer is the same make and model as one
> already set up, do not repeat this whole process. Copy the existing configuration and change
> the IP address and printer name.

# Create the configuration

1. Open `endpointcentral.manageengine.com`.
2. **Configurations** at the top.
3. **Configuration** from the left under *Add Configuration* → choose **Windows**.
4. Hover **IP Printer** in the configuration type list → **Computer Configuration**.
5. Name the configuration — use the same alias you gave the device in UniFi.
6. Enter the **IP address** you set previously.
7. **Printer Display Name** — again use the same alias. This becomes the printer's name to
   users.
8. Add the driver package:
   1. Open `support.brother.com` → **Downloads**. Search the printer's make and model.
   2. Select **Windows 11** as the OS and click the light blue **OK** button.
   3. Under *Full Software Package*, click **Full Driver & Software Package**.
   4. **Agree to the EULA and Download**.
   5. Return to the ManageEngine configuration.
   6. In **Add Package**, browse to and upload the downloaded file.
   7. Select **Advanced** settings. When asked to choose an INF file, **choose the one with
      PRC in the filename**.
9. Scroll down, **Save As** → **Template**. You can now deploy it to specific computers or
   groups.

# Choosing the INF file

Printer packages contain several INF files. For general-purpose printers choose the one
containing **PRC** in the filename.

| Suffix | Meaning |
|---|---|
| PRC | Printer — this is the one you want |
| PSC | PostScript |
| OFX | PC-FAX |

Others are for non-printer functions and can be ignored.

> **PRC is glossed as "PRC stands for Printer" in the source.** That expansion is not
> obviously right, but the instruction — pick the PRC file — is consistent in both places it
> appears, so the guidance stands even if the etymology does not.

# Screenshots

Written against screenshots of the Endpoint Central and Brother download interfaces that did
not survive conversion.

# Related

- [Fixed IP assignment](/it/printers/fixed-ip-assignment.md)
- [Brother printer setup](/it/printers/brother-printer-setup.md)
- [Software deployment packages](/it/devices/software-deployment-packages.md)
