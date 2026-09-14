---
type: Reference
title: Email signature template structure
description: How the signature HTML template, its placeholders, the GAM command segments and the conditional-removal tags fit together.
tags: [google-workspace, signatures]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

The signature system has three parts:

1. A blank HTML template containing **placeholders** — a keyword in braces, like `{this}`.
2. A **GAM script** that deploys the template to user accounts.
3. The same GAM script **find-and-replaces** the placeholders with data pulled from the
   user's Google Workspace profile.

For the deployment commands themselves, see
[email signature deployment](/it/google-workspace/email-signature-deployment.md).

# Placeholder to Workspace field mapping

| Placeholder | Workspace field |
|---|---|
| `{Title}` | `field:organization.title` |
| `{FirstName}` | `field:name.givenname` |
| `{LasName}` | `field:name.familyname` |
| `{Email}` | `field:email.primaryemail` |
| `{Mobile}` | `field:phone.value.type.mobile` |
| `{PhoneWork}` | `field:phone.value.type.work` |
| `{Extension}` | `schema:Email_Signature.Phone_Extension` |
| `{ProfilePhoto}` | `schema:Email_Signature.Profile_Photo_URL` |
| `{HoustonPhone}` | `schema:Email_Signature.Houston_Phone_Number` |
| `{AustinPhone}` | `schema:Email_Signature.Austin_Phone_Number` |

> **`{LasName}` is spelled that way in the source** — a missing `t`. Because the GAM command
> and the template must agree character-for-character, a typo like this works fine as long as
> both sides carry it. Do not "fix" it in one place only. IT to confirm which spelling is
> actually in the template file.

> **This table maps the APS schema only** (`Email_Signature.*`). The Natran template uses
> `Email_Sig.*` names with numeric suffixes and additional fields — `License_No`, `Dept`, and
> four numbered `Tel*` blocks. No mapping table exists for those.

# GAM command segments

| Command segment | What it does |
|---|---|
| `gam user <user email>` | Specifies whose signature to replace. Substitute the real email and remove the brackets. |
| `signature` | The GAM command indicating you are replacing the user's email signature. |
| `ghtml <html drive-file-owner-email> <html-drive-file-ID>` | Where to fetch the signature template. The owner address is static and required in order to fetch the file by Google file ID. |
| `replace FirstName field:name.givenname` | Replaces any `{FirstName}` in the template with data from the referenced profile field. |
| `replace ProfilePhoto schema:Email_Signature.Profile_Photo_URL` | Same, but `schema:` rather than `field:` because it references a custom attribute. |
| `replace ProfilePhoto schema:Email_Signature.Houston_Phone_Number` | Used for Natran office workers who may have branch-specific numbers. APS does not use this field. |

> **The last row is wrong as written.** It maps the placeholder `ProfilePhoto` to
> `Houston_Phone_Number` — copy-pasted from the row above without changing the placeholder
> name. The intended placeholder is presumably `{HoustonPhone}`, per the mapping table. IT to
> confirm.

# signature.html structure

The template uses simple tables and inline CSS. **No `<HTML>` or `<BODY>` tags are needed** —
Google processes and sanitises the file, stripping unnecessary code.

The files are structured in blocks so information stacks on a small mobile screen.

# Conditional removal: {RT} and {RTL}

Some data in the HTML is wrapped in `{RT}{/RT}` or `{RTL}{/RTL}`. These tell GAM that **if
the corresponding Workspace field is blank, the entire enclosed segment can be removed.**

For example, the template contains `{RT} Ext. {Extension} {/RT}`. If the user's
`schema:Email_Signature.Phone_Extension` field has data, the extension renders along with the
word *Ext.*. If the extension field is blank, everything between the tags is dropped — so the
signature does not read "Ext." followed by nothing.

# Template files

| Company | Drive file ID |
|---|---|
| Natran | `1bmQSDtl2Kbx2aOz3m0QKafaSfb3dMZ7j` |
| Advantage Pro Services | `1QuzUgM3UoN4nbzdePtlZp_dNoO83awDe` |

> Advantage Pro Services is a separate company from Natran, LLC. Its signature template and
> GAM command live in the Natran IT documentation. Recorded as found — whether APS material
> belongs in the Natran knowledge base is a scoping question for you, not something to
> resolve here.

# Related

- [Email signature deployment](/it/google-workspace/email-signature-deployment.md)
