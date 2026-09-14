---
type: Runbook
title: Device QR code labels
description: Generating and applying QR code stickers to company devices so a device can be identified without hunting for its serial number.
tags: [devices, inventory]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 10ifT6nY1Hm7IW66S6tysR2l91NWvrWNZAFc6gmQFB_g
    resource: https://docs.google.com/document/d/10ifT6nY1Hm7IW66S6tysR2l91NWvrWNZAFc6gmQFB_g/edit
    title: How to generate QR Codes
status: draft
---

**Why:** identifying a device's serial number is not always easy — not all devices have it
printed on them.

> Only needed when a device is first provisioned, or if a QR code needs replacing.

# Prerequisites

1. Open the
   [Devices spreadsheet](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/)
   and find the **QRCodeGenerator** tab.
2. Install the
   [QR Code Generator](https://workspace.google.com/marketplace/app/qr_code_generator/771094986501)
   add-on by AnyMerge.
3. Get access to the
   [QR Code Natran Template](https://docs.google.com/document/d/1rxHgy4jVARasOh4qKLukfP2Pt2AtJN0r2twknfN69PY/edit)
   Google Doc.
4. From the Devices spreadsheet, load the add-on: **Extensions** → **QR Code Generator** →
   **Open**.

# Generate

**The device must already be entered on the Company Owned Devices tab** before you can generate
a code. Everything below happens in the Devices spreadsheet.

1. Select the serial numbers you want codes for in **column A**. The rest of the device
   information pulls in automatically.
2. In the add-on panel, select the **Template** tab.
3. **Load** → select the **QR Code Natran Template**.
4. **Mapping** → confirm the placeholders map to the correct columns. The QR Code should be set
   as the QR Code and use the **Extra Large** option.
5. **Generate** → then **Open Document** → print.

The template is built for a **100mm × 150mm label printer with adhesive backing**.

# Apply

6. Apply the sticker:
   - **Laptops** — one on the bottom of the device and one on top of the lid.
   - **Smartphones** — on the back, before the phone goes into its case.
7. On the **Company Owned Devices** tab, set the **QR Code** column to **Yes**.
8. **Clear column A** so it is ready next time.

> Step 8 matters more than it reads. Leaving serials in column A means the next person
> regenerates labels for devices that already have them.

> The source references a video walkthrough for the mapping step, which is where the fiddliest
> part of this process lives. The written steps are thinner than the original.

# Related

- [Apple device assignment](/it/devices/apple-device-assignment.md)
- [Windows PC setup](/it/devices/windows-pc-setup.md)
