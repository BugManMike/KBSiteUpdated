---
type: Template
title: HR email templates
description: The email drafts HR sends across onboarding and offboarding — insurance, payroll notification, fuel PIN, uniforms, training logins and device setup.
tags: [recruiting, onboarding, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:19:05Z
sources:
  - id: 17-b_uMI6MtawuYT2AXYLZ-_-NinKaN1_xa_6y8fO_hI
    resource: https://docs.google.com/document/d/17-b_uMI6MtawuYT2AXYLZ-_-NinKaN1_xa_6y8fO_hI/edit
    title: Natran HR Email Templates
status: draft
---

Around twenty email drafts, grouped into onboarding, offboarding and IT onboarding. HR's signature
block throughout is **Natran Green Pest Control, Human Resource Department, (832) 404-2235**.

> ## Security issues in the source — read this first
>
> **Four things in this document are security problems, and none of their values are reproduced
> here.** They are described so they can be fixed.
>
> 1. **The fuel PIN is set to the last four digits of the employee's Social Security number.** One
>    template states this outright. The same template tells the employee not to share the PIN — but
>    the PIN *is* part of their SSN, it appears on a weekly fuel report that identifies them by name,
>    and an administrator necessarily knows it. See
>    [driver fuel policy](/operations/fleet/driver-fuel-policy.md). **This should be changed to a
>    random PIN.**
> 2. **A shared default password is emailed in plaintext**, and the same string is reused across
>    Fieldroutes, NPMA QualityPro and TPCA training. A second shared password covers KnowledgeVine,
>    and a fixed access code covers the respirator questionnaire. **These are per-system shared
>    secrets sent by email to personal addresses.**
> 3. **The Houston branch back door code is emailed in plaintext** to new hires, at both their company
>    and **personal** email addresses. It is a short numeric code. Anyone with an old welcome email
>    retains it after leaving — and nothing in the offboarding templates rotates it. Austin has no
>    door code.
> 4. **Two templates were saved with a real employee's details still in them** — name, username,
>    password, company phone number and email. They are working drafts, not blanks.
>
> The values are in the source document if IT or HR need them to remediate. **They are deliberately
> not copied into this repository.**

# Onboarding

**Add to auto insurance** — to `susan.mousseau@assuredpartners.com`. For **Natran drivers only:
technicians, outside sales, service managers, branch managers and anyone assigned a company
vehicle.** The driver's licence is attached to the email.

> AssuredPartners is the same agency named on the company's general liability, auto and umbrella
> policies in the root Insurance document.

**Job description** — to the candidate, with a job link and the company Core Value video.

**Notification for new hires** — to the bookkeeper, copying the owner. Carries employee name, date of
hire, position, company, **classification (Houston, Austin or Corporate)** and **GL code**.

> The classification and GL code are what put the new hire's cost in the right place in the books —
> the same branch split the accounting batch will cover.

**Fuel PIN** — to the new hire's company email. States the PIN, that it must not be shared, and that
a fuel card follows when the company vehicle is issued. **See the security note above.**

**Door code and supervisor contact information (Houston only)** — to both company and personal email.
Carries the back door code and the branch manager's and field service manager's names, mobile numbers
and emails.

**Supervisor contact information (Austin only)** — same, without a door code. **"No door codes in
Austin."**

**Welcome and what to bring on your first day:**

- **Arrive at 9:00 am** on the first day. **During training, be at the office by 8:00 AM.**
- Bring a **voided check or a bank letter** with routing and account number.
- Bring **I-9 items** per the attached list: one item from **column A**, or one from **column B** and
  one from **column C**.
- **Bring your pest control licence** if you hold one.
- Day one is **HR orientation on benefits, new employee paperwork, then safety and online driving
  videos**. Day two is on-the-job training and initial work goals.
- **Dress code is casual; training shirts are provided on the first day.**
- Gusto account setup information is attached.

**Respirator fit test — medical exam questionnaire** — via `rapidmeq.com`, using a company access
code. The employee enters their own details and is guided to specific answers:

- Respirator use for emergencies only: **No**
- Type of respirator: **B**
- Additional protective clothing: **PPE — long sleeve shirt, long pants, and leather shoes**
- Temperature and humidity extremes: **Over 100 degrees**

> The questionnaire is reviewed by a doctor to medically clear the employee for a respirator. It asks
> for the last four digits of their SSN — that is the vendor's form, not a company choice. It pairs
> with the handbook's **Respirator Protocol**, which is in the Operations technician folder.

**Welcome email — usernames and passwords.** Issues credentials for **Fieldroutes**, **NPMA
QualityPro / GreenPro**, **KnowledgeVine training** and **TPCA training**. **See the security note
above.**

Training enrolment detail worth keeping: new technicians are signed up for a **20-hour apprentice
course, an 8-hour pest course and an 8-hour termite course**, with **a 100% quiz score required
before moving to the next course**, and a **fixed course expiry date** by which all must be
completed.

**Team welcome** — an internal announcement to the branch team, with a photo.

**TPCA and NPMA enrolment links** — `tpcatraining.com` and the NPMA online learning centre. See
[QualityPro certification registration](/people/qualitypro-certification-registration.md).

# IT onboarding

**Technician iPhone and iPad setup instructions** — separate Houston and Austin versions, addressed to
the branch manager and copying IT and the branch manager. Both:

- Give the employee their **company phone number, company email and temporary password**.
- Warn that on receiving the iPhone they must **create a passcode** and **set up 2-Step Verification
  on the first day or risk being locked out**.
- Link the self-service setup guide — which is
  [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md).
- **Ask the employee to reply confirming completion.**

> **Accounts should be set up in advance of the employee's first day.** That is the operative note on
> both templates.

> The links point at the **YouNeedAWiki** rendering of the setup document rather than the Google Doc.
> If the wiki front end is ever retired, these emails break. Relevant to `DECISIONS.md` OQ-005.

# Offboarding

**Remove from auto insurance** — to the same AssuredPartners contact, giving the last day worked.

**Terminate benefits** — listed in the index but **the draft itself is missing from the document.**

**Remove PestRoutes tasks** — to two named staff. *"I have locked ___'s PestRoute account. Please make
sure all appointments and tasks are cleared out."*

> This is the email that
> [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md) refers to when it says to
> "email office managers and ask them to clear any appointments, borders, visual groupings and
> reassign pending tasks" before deactivating. **The template asks only for appointments and tasks** —
> it omits borders and visual groupings, which the deactivation procedure says will block
> deactivation. Worth adding.

**Order Natran tech shirts** — to the uniform vendor, copying a named staff member. Specifies **name
patch (first name), TPCA level (Technician or Certified Applicator), Green Pro, Quality Pro, size, and
a count of 6.**

> **This is filed under offboarding in the source index**, which must be wrong — ordering shirts for a
> departing employee makes no sense, and the shirt count and licence patches are clearly onboarding.
> There is also a `Technician Shirt Order Form` Google Form stubbed twice elsewhere in the wiki. HR to
> confirm whether the email or the form is current.

# Structural notes

The document is built for Gmail's "create draft" links — *"click on the blue envelope button and it
will automatically generate an email draft."* Those buttons do not survive conversion, so the
recipient and subject fields are transcribed as tables instead.

Several later templates have **`Person` placeholders in the To, Cc and Bcc fields** rather than named
recipients, and the index lists headings that the body does not contain.

# Related

- [Recruiting SMS templates](/people/recruiting-sms-templates.md)
- [Employee file worksheet](/people/employee-file-worksheet.md)
- [Driver fuel policy](/operations/fleet/driver-fuel-policy.md)
- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md)
