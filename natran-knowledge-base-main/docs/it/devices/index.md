# Devices

Company device management. Windows devices run through ManageEngine Endpoint Central, Apple
devices through Jamf Now, and Chromebooks directly in the Google Workspace admin console.

## Windows

* [Windows device enrollment](endpoint-central-device-enrollment.md) - The three things installed on a new company Windows device before any other setup happens, and how to find a device's computer name.
* [Windows PC setup](windows-pc-setup.md) - Full build of a Windows device: OS setup, the GCPW enrollment script, registering the serial as company-owned, then per-user software, web apps, printer and scan folder.
* [Endpoint Central configuration catalogue](endpoint-central-configuration-catalogue.md) - The standing configurations applied to company Windows devices, the device groups they target, and how often each reapplies.
* [Windows default administrator account](windows-default-administrator-account.md) - How to temporarily activate and then deactivate the hidden passwordless Windows administrator account.
* [Windows local account administration](windows-local-account-administration.md) - Changing permission level, suspending, deleting with or without keeping data, and listing the accounts on a device.
* [Windows device user removal and return](windows-device-user-removal.md) - Removing a user's local account by hand, returning the device to storage, and the HR notification that closes the loop.

## Apple and Chrome

* [Apple device assignment](apple-device-assignment.md) - Assigning an iPhone or iPad in Jamf Now: naming, blueprint, user assignment, and the inventory records.
* [Apple device self-service setup](apple-device-self-service-setup.md) - The setup an employee performs themselves on a new iPhone or iPad, including the eight apps they must configure.
* [Apple device erase and unassign](apple-device-erase.md) - Wiping a returned device: retaining what is needed, resetting the blueprint, erasing, and updating inventory.
* [Chromebook assignment](chromebook-assignment.md) - Recording a Chromebook against an employee and moving it into their organizational unit.
* [AT&T SIM activation](att-sim-activation.md) - The four values AT&T needs to activate the SIM in an Apple-purchased iPhone.

## Software and peripherals

* [Software deployment packages](software-deployment-packages.md) - How to add a software package to Endpoint Central for deployment, and which software targets which device group.
* [Teramind agent deployment](teramind-agent-deployment.md) - How the Teramind monitoring agent is packaged, deployed to all Windows devices, and exempted from Windows Defender.
* [Teramind user monitoring](teramind-user-monitoring.md) - Turning monitoring on for an employee in the Teramind portal, buying licences, and removing a departing user.
* [Chrome managed browser enrollment](chrome-managed-browser-enrollment.md) - How Chrome on company devices is enrolled into cloud management, and how to confirm enrollment.
* [GCPW deployment](gcpw-deployment.md) - How Google Credential Provider for Windows is deployed so users sign into Windows with their Google account.
* [Busylight setup](busylight-setup.md) - What to buy, which software to install, and how to load the preset call-status light priorities.
* [Device QR code labels](device-qr-code-labels.md) - Generating and applying QR code stickers so a device can be identified without hunting for its serial number.
