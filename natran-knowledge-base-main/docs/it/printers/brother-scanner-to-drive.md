---
type: Runbook
title: Brother scanner to Google Drive
description: Registering a Brother printer with Brother Web Connect so scans upload to a chosen Google Drive account, and saving one-sided and two-sided shortcuts on the device.
tags: [brother, printers, scanning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Scanning to Drive is two stages: get a temporary Brother account ID in a browser, then enter
it on the printer within its validity window.

# 1. Get a temporary Brother account ID

1. Go to **Brother Web Connect** — `bwc.brother.com`.
   - **Do this from the computer and browser signed into the Google account the scans should go to.**
2. Select the **country, language, and printer model**.
3. Select **Google Drive**.
4. **Agree** to the terms and conditions.
5. Select the Google account the scans will go to.
6. You are shown a **temporary Brother ID**. **Record it — it is needed in the next stage.**

# 2. Register the printer

On the printer's screen:

1. Find and select **Web App**.
2. Select **Google Drive**.
3. **Register Account**.
4. **OK**.
5. Enter the **temporary ID** from stage 1.
6. Enter a **display name** — e.g. *Billing Drive*, *HR Drive*.
7. Select **No** when asked about a PIN code.
8. **Yes** to confirm the details on the next screen.
9. **OK**.

# 3. Save a scan shortcut

1. **Upload from Scanner**.
2. **PDF**.
3. Change **Create Shortcut** to **Yes**.
   - You can choose which folder scans go into. **If you do not select a folder, scans land in
     the general section of the registered Drive account.**
   - There is a **scan two sided** option. Unselecting it scans only the front of each page,
     which is useful for documents not printed on both sides.
4. Once the settings are right, **OK**. *You need a document in the feeder to scan as a test at
   this point.*
5. **OK**.
6. Select an open spot on the home screen to save the shortcut.
7. Name the shortcut — e.g. **Front** for one-sided, **Front & Back** for two-sided.

# Adding the second shortcut

Repeat stage 3 to save a shortcut for whichever sidedness you did not pick first. **You do not
need to register the account again** — it appears as an option when you reach the register
screen.

# Related

- [Brother printer setup](/it/printers/brother-printer-setup.md)
