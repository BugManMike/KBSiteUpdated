---
type: Reference
title: Zoho software repository (Raspberry Pi)
description: The Raspberry Pi acting as the SMB software repository for ManageEngine deployments — its addresses and paths, how to reach it, monthly maintenance, and troubleshooting.
tags: [raspberry-pi, network, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

A Raspberry Pi is a lightweight Linux device that can act as a file server in a small office.
This one serves the software packages that ManageEngine Endpoint Central deploys — see
[software deployment packages](/it/devices/software-deployment-packages.md).

# The device

| | |
|---|---|
| Zoho identifier | `natran12460` |
| Device hostname | `zoho-repo` |
| Fixed office IP | `192.168.1.100` |
| Primary admin user | `natran` |
| Function | Local network share (SMB) for ManageEngine Endpoint Central software deployment |

# Remote management

| Method | How |
|---|---|
| Web portal, from anywhere | [Raspberry Pi Connect dashboard](https://connect.raspberrypi.com/devices/8b035f7a-0b09-4286-aa55-fe38cbce4c51) → **Screen Sharing** |
| Local terminal, in the office | From a Windows PC on the same network, in PowerShell or CMD: `ssh natran@192.168.1.100` |
| Hardware | Micro-HDMI and USB keyboard/mouse for direct troubleshooting |

# Repository configuration

The Pi shares a folder on its SD card to the office network via Samba.

| | |
|---|---|
| Internal Pi path | `/home/pi/swrepository` |
| Office network path (UNC) | `\\192.168.1.100\ZohoRepo` |
| Username | `natran` |
| Password | Manually set Samba password — not recorded here |

Ensure the Software Repository settings in Endpoint Central point at the UNC path above using
these credentials.

> **Path mismatch worth checking.** The internal path is `/home/pi/swrepository` but the admin
> user is `natran`, not `pi`. If the Samba share is owned by `natran`, a home directory under
> `/home/pi/` is unexpected. Recorded as found — IT to confirm the actual share path.

# Monthly maintenance

Run these in the terminal each month for security and performance:

```bash
# Update software and OS
sudo apt update && sudo apt full-upgrade -y

# Clean up system cache
sudo apt autoremove -y && sudo apt clean

# Restart to apply updates
sudo reboot
```

# Troubleshooting

| Symptom | Action |
|---|---|
| Zoho reports "Access Denied" | Verify the Samba user is active: `sudo smbpasswd -e natran` |
| Cannot find the Pi on the network | Check the assigned IP: `hostname -I` |
| Storage full | Check SD card space with `df -h`. Delete old installers from `/home/pi/swrepository`. |
| Remote share invisible | Restart the file service: `sudo systemctl restart smbd` |

# Hardware notes

- **Power:** always use the official 5V 3A Raspberry Pi power supply.
- **Shutting down:** always run `sudo shutdown now` before unplugging. Pulling power risks SD
  card corruption.
- **Static IP:** `192.168.1.100` is reserved in the UDM Pro by MAC address. **If the Pi is
  moved to a different VLAN, that reservation must be updated in the UniFi controller.**

# Related

- [Software deployment packages](/it/devices/software-deployment-packages.md)
- [Door access](/it/network/door-access-unifi.md) — same UniFi controller
