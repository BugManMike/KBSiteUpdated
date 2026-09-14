---
type: Runbook
title: Teramind user monitoring
description: Turning monitoring on for an employee in the Teramind portal, buying licences when they run out, and removing a departing user.
tags: [teramind, devices, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1fOhlLX7wZFRXKCA3dMVCgIIF2GlHbXQO8PJC2hZ1BF0
    resource: https://docs.google.com/document/d/1fOhlLX7wZFRXKCA3dMVCgIIF2GlHbXQO8PJC2hZ1BF0/edit
    title: Teramind setup
status: draft
---

Installing the agent does not start monitoring. **Monitoring is turned on per user in the
Teramind portal**, which is what this covers. For the agent itself see
[Teramind agent deployment](/it/devices/teramind-agent-deployment.md).

**The user must sign into their Windows device before Teramind will detect their account.**
Nothing here can be done in advance of that.

# Turn monitoring on

1. Sign into `natran.teramind.co` with company credentials.
2. **Employees** in the left navigation.
3. Find the device the employee is using and click the name.
4. Set **Monitor this user** to **Yes**.
5. **Edit Info** → enter **first name and last name only**.
6. Select the **department** they are assigned to.
7. **Apply Changes**.

# Licences

**A licence is required for every monitored user.** An unlicensed user in the Employees list is
not being monitored, even if monitoring is switched on.

**Before buying more, delete any old employees.** Then, with the right permissions:

1. **My Account**
2. **Upgrade Package**
3. Increase the number of users to track → **Update Subscription**
4. Return to **Employees** and confirm no monitored user is flagged unlicensed

Contact the system administrator if you lack permission.

# Remove a departing user

1. Sign into `natran.teramind.co`.
2. **Employees**.
3. Click the employee name.
4. Click the **trash icon** to delete the user.

> Deleting frees the licence, which is why the licensing section above says to clear old
> employees first. Offboarding and licence management are the same task here.

# The per-device agent install in this source

The same source document also describes installing the agent by hand — sign into the portal,
click your name, **Download Teramind Agent**, select **No** on *"Do you want the user to know"*,
download the build matching the OS, and install it.

> **This manual install is superseded.** The agent is deployed automatically to all devices
> carrying the Endpoint Central agent — see
> [Teramind agent deployment](/it/devices/teramind-agent-deployment.md), which is from a 2026
> source against this document's 2024. The manual route is recorded only because it names the
> **"Do you want the user to know" → No** choice, which is a monitoring-visibility decision that
> appears nowhere else and is not obviously an IT call to make. IT and HR to confirm that
> setting is intended.

# Related

- [Teramind agent deployment](/it/devices/teramind-agent-deployment.md)
- [Configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md)
