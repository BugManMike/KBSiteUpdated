---
type: Runbook
title: Email signature deployment
description: Deploying a user's email signature with GAM, which pulls their details from their Workspace profile, plus the Gmail defaults the user must set afterwards.
tags: [google-workspace, signatures, onboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Signatures are deployed with **GAM** (Google Apps Manager), which fetches an HTML template
from Drive and find-and-replaces placeholders with data pulled from the user's Workspace
profile. For how the template and placeholders work, see
[email signature template structure](/it/google-workspace/email-signature-template-structure.md).

The user's profile must already carry their photo URL, phone number and extension. See
[profile photo](/it/google-workspace/profile-photo.md).

**Do not edit the template files.**

# Deploy

Open GAM. If you do not have access, speak with the system administrator.

There are two templates, one per company.

**Natran** — template file `1bmQSDtl2Kbx2aOz3m0QKafaSfb3dMZ7j`, owner `admin@natran.com`:

```
gam user <user email> signature ghtml admin@natran.com 1bmQSDtl2Kbx2aOz3m0QKafaSfb3dMZ7j replace FirstName field:name.givenname replace LastName field:name.familyname replace Email field:email.primaryemail replace Profile_Pic_URL schema:Email_Sig.Profile_Pic_URL5751 replace Job_Title schema:Email_Sig.Job_Title1411 replace License_No schema:Email_Sig.License_No replace Dept schema:Email_Sig.Dept replace Tel1_No schema:Email_Sig.Tel1_No replace Tel1_Ext schema:Email_Sig.Tel1_Ext replace Tel1_Label schema:Email_Sig.Tel1_Label replace Tel1_Icon_URL schema:Email_Sig.Tel1_Pic_URL replace Tel2_No schema:Email_Sig.Tel2_No replace Tel2_Ext schema:Email_Sig.Tel2_Ext replace Tel2_Label schema:Email_Sig.Tel2_Label replace Tel2_Icon_URL schema:Email_Sig.Tel2_Pic_URL replace Tel3_No schema:Email_Sig.Tel3_No replace Tel3_Ext schema:Email_Sig.Tel3_Ext replace Tel3_Label schema:Email_Sig.Tel3_Label replace Tel3_Icon_URL schema:Email_Sig.Tel3_Pic_URL replace Tel4_No schema:Email_Sig.Tel4_No replace Tel4_Ext schema:Email_Sig.Tel4_Ext replace Tel4_Label schema:Email_Sig.Tel4_Label replace Tel4_Icon_URL schema:Email_Sig.Tel4_Pic_URL
```

**Advantage Pro Services** — template file `1QuzUgM3UoN4nbzdePtlZp_dNoO83awDe`, owner
`admin@advantageproservices.com`:

```
gam user <user email> signature ghtml admin@advantageproservices.com 1QuzUgM3UoN4nbzdePtlZp_dNoO83awDe replace ProfilePhoto schema:Email_Signature.Profile_Photo_URL replace FirstName field:name.givenname replace LastName field:name.familyname replace Title field:organization.title replace Department field:organization.department replace Extension schema:Email_Signature.Phone_Extension replace DirectPhone schema:Email_Signature.Direct_Phone_Number replace DeptPhone schema:Email_Signature.Department_Phone replace Mobile schema:Email_Signature.Mobile_Phone replace Email field:email.primaryemail
```

> **Several defects in this section of the source, all needing IT to resolve:**
>
> 1. **The Natran command is hardcoded to a real person** — as written it reads
>    `gam user codyrodgers@natran.com`, not a `<user email>` placeholder. Substituted above,
>    but anyone copying from the source will re-signature that account.
> 2. **The two companies use different custom-schema names.** Natran uses `Email_Sig.*` with
>    numeric suffixes (`Profile_Pic_URL5751`, `Job_Title1411`); APS uses
>    `Email_Signature.*` without them. They are not interchangeable.
> 3. **The placeholder mapping table documents only the APS schema** — see
>    [template structure](/it/google-workspace/email-signature-template-structure.md). There
>    is no mapping table for the Natran schema, including the `License_No`, `Dept` and four
>    `Tel*` blocks that only Natran uses.
> 4. **The intro says "The template … is saved here. Do not edit it," linking only the APS
>    file**, while a later paragraph correctly states there are two files. A reader following
>    the intro would deploy the APS signature to a Natran user.
> 5. Two stray editorial artifacts — a bare name-and-email mention and an `@raegan` comment
>    handle — sit inside this procedure as leftovers from Google Docs commenting.

# Set the signature as the Gmail default

The GAM command installs the signature but does not select it. This step is done in the
user's mailbox, either by signing in as them or via Gmail delegation:

1. Click the gear icon in the upper right to open Quick Settings, then **See all settings**.
2. Scroll to **Signature**.
3. Under *Signature defaults*, select **My Signature** for both **New Emails Use** and
   **Reply/Forward Use**.
4. Scroll to the bottom and press **Save**.

# Related

- [Email signature template structure](/it/google-workspace/email-signature-template-structure.md)
- [Profile photo](/it/google-workspace/profile-photo.md)
- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
