# Natran Wiki — full inventory (enumerated 2026-07-28)

Source root: `1gfI4Z18Rmd6UnjTm0Xned1SvdiwQ0GZQ` ("Natran Wiki", YouNeedAWiki-fronted)

**Totals: 72 folders, ~438 files, 6 levels deep** (root + 5).
DECISIONS.md OQ-005 recorded "~322 files across three levels" — both figures were low.

## Classification

| Class | Count | Convert? |
|---|---|---|
| Real content | ~242 | yes |
| Link stub (~1024 B, title is a markdown link, empty body) | ~96 | no |
| Binary (pdf/video/audio/image/pptx/spreadsheet/form/json/shortcut) | ~95 | no |
| Navigation shell / link directory | ~5 | no (except 1, see below) |

### wiki.page files — all 6 opened individually

| Path | Size | Verdict |
|---|---|---|
| `/wiki.page` | 1266 | Nav shell. `{{files}}` placeholder. Not convertible. |
| `/Human Resources/wiki.page` | 3377 | **Hybrid.** Mostly links, but carries a real benefits open-enrollment calendar (MetLife May 15, health Aug 1, Guardian Sept 1, premiums collected a month ahead). Extract the calendar. |
| `/HR/Onboarding/wiki.page` | 5687 | **Hybrid.** Provisioning checklist grouped by role (everyone / office / technicians) + admin-vs-user split. Structure is real knowledge; targets are links. |
| `/HR/Offboarding/wiki.page` | 3633 | **Hybrid.** Offboarding checklist: suspend software, then freeze/wipe devices. Same shape. |
| `/Accounting/wiki.page` | 16895 | **GENUINE REFERENCE.** "Schedule of Events" — the bookkeeping close calendar: daily (Mon–Fri), bi-weekly payroll, monthly, and ad-hoc processes, each with an owner (Caryn Bangsoy; franchise tax = Michael Arndt). Convert. |
| `/Accounting/Earning Reports/wiki.page` | 2067 | Link directory of quarterly earnings reports. Not convertible. |

### Other link directories confirmed by opening
- `/Operations/Other Resources/Technician Resource` — pure link directory.
- `/Accounting/Roles /B&P Agent` — **NOT a link directory.** Real daily/weekly/monthly A/R + payroll-assistance duty list. Convert. (References **ServiceCEO**, a system that appears nowhere else — likely pre-PestRoutes legacy.)
- `/WIP/Untitled document` — 2-line fragment ("Past due collection" steps, "Decline credit card"). Too thin; unconvertible.

## Folder tree

```
Natran Wiki/                                    7 files
├── Human Resources/                            6
│   ├── Onboarding/                             6
│   │   └── Device Setup & Onboarding/          11
│   ├── Safety/                                 2
│   │   └── Safety Documents/                   4  (all pdf)
│   ├── Other Resources/                        9
│   ├── Offboarding/                            3
│   ├── HR Forms/                               7
│   │   └── Injury related HR forms/            4  (all pdf)
│   └── QualityPro Certifications/              4
├── Technology/                                 12
│   └── Resources/                              1  (json)
├── WIP/                                        5
├── Operations/                                 11
│   ├── Inventory/                              5
│   ├── Other Resources/                        1
│   ├── TDA Forms/                              6  (all pdf)
│   ├── Technicians/                            6
│   │   ├── Processes/                          29
│   │   └── How-To Videos/                      1  (mp4)
│   ├── Houston Branch/                         4
│   ├── Austin Branch/                          2  (both stubs)
│   ├── Operations Managers/                    4  (all stubs)
│   ├── Insurance Cards/                        1  (pdf)
│   ├── Apprentice Training Class/              0
│   │   ├── Customer Service Skills/            1
│   │   ├── Record Keeping and Reporting/       0  (EMPTY)
│   │   ├── Pest Control Fundamentals/          6
│   │   ├── Safety and Regulatory Compliance/   1  (stub)
│   │   ├── Green Pest Control Principles/      3  (all stubs)
│   │   └── Equipment and Tools/                1  (stub)
│   ├── Fleet Management/                       5
│   └── Training, Licensing, CEU/               3
│       ├── Monthly Technical Trainings/        14 (all pptx/pdf)
│       └── QualityPro Certifications/          4  (DUPLICATE of HR's)
├── Sales and Marketing/                        1
│   ├── Sales/                                  8
│   │   ├── Sales Documentation/                4
│   │   ├── Sales Bible/                        13
│   │   ├── Sales Support Rep Documents/        0
│   │   │   ├── Report Guides/                  2
│   │   │   │   └── Report Templates/           1  (spreadsheet)
│   │   │   ├── SMS Follow-Up Scripts/          3  (all stubs)
│   │   │   └── Call Scripts/                   1
│   │   ├── Specialty Tech Outside Sales/       6
│   │   └── 3 Point Leads Process/              5
│   └── Marketing/                              1
│       └── Customer Retention Journey/         4
├── Customer Care and Dispatch/                 13
│   ├── Process Documentation/                  12
│   │   └── Other Documents/                    1
│   ├── Customer Prep Sheets/                   6
│   ├── CC Training Material /                  24
│   ├── Team Lead Material /                    1
│   └── Scheduling/                             18
├── Shared Services (CCRs, ISRs, OpSRs, SSRs)/  1
│   ├── Training Call Files/                    18 (17 audio + 1 doc)
│   ├── PestRoutes Basics/                      3
│   │   ├── Scheduling/                         1  (mp4)
│   │   ├── Sales Reports & Commission Res./    3  (binary)
│   │   └── Route Grade Keys - Print Files/     3  (jpg)
│   ├── Reference Docs/                         2  (spreadsheets)
│   ├── SOPs by Service Type/                   3
│   └── SOPs by Category/                       8
└── Accounting/                                 1
    ├── Processes/                              63  ← largest single folder
    ├── Payroll/                                2
    ├── Budgeting/                              3
    ├── Earning Reports/                        2
    ├── Roles /                                 1
    ├── Collections/                            1
    └── Procurement/                            11
```

## The hub document

`Natran Core Processes` (`1eWWlf4kxO5reYoN1RExpNXhQ2WZkZPpZy_ET8UW5e1E`, **432 KB**, multi-tab,
modified 2026-05-29) is the single largest source. At least **20 link stubs** across the tree are
bookmark links into its tabs: HR, Leadership Team, IT, CCR, Dispatch/Scheduling, Accounts
Receivable, Accounts Payable, Bookkeeping, Financial Modeling, Scorecards, Technician Inventory,
Technician Service, Warehouse Manager, Operations Sales, Inside Sales, FSM, RCA, Fleet Manager.

This is the doc DECISIONS.md OQ-005 names as the Phase-3 divergence forcing point.

## Duplication / conflict candidates (verify at conversion)

- `Copy of Flea and Tick Prep Sheet` vs `Flea and Tick Prep Sheet`
- **`Account Receivable Process` exists twice in Accounting/Processes** — two distinct file IDs,
  identical title (`1mFcV0-7dxgczuCzcNSeSSFN6TQrZkYf9rz5v2mxM3BQ`, `1gnrmNiWb_iddmS_cJvn7e1K30lZCPsjzdcHv5nQ_AG0`)
- Three overlapping commission docs: `Sales Commission`, `Sales commission proces`,
  `How to calculate salesperson commissions`
- `QualityPro Certifications` folder duplicated (HR + Operations/Training)
- QualityPro & GreenPro Study Guide PDFs each appear 3×
- `Termite Graph Guide and Checklist.pdf` appears 3×
- `Public Health Study Materials`, `Exam Registrations` each appear 2×
- `Service Descriptions` stub appears 4×; `Pet Protocol` stub 3×; `Fleet Manager Core Process`
  stub 2×; `Technician Shirt Order Form` stub 2×
- `New Vehicle Procurement Process` split 4 ways by role (Procurement / Operations / Bookkeeping /
  Purchaser); `Vehicle Decommission Process` split 3 ways — check for threshold disagreements
- `CoastalMister_Repair_Form_Fillable_OLD_DO_NOT_USE.pdf` sits beside the current form

## Cross-company contamination (Natran vs Advantage Pro Services)

- `/Insurance` — Workers Comp policy 0002103695 "Coverage includes Natran, LLC **and Advantage Pro
  Services, Inc.**"
- `/Accounting/Processes/How to Journalize APS's Intercompany transactions into the Natran QB account`
- `/Accounting/Processes/Uploading KingRanch to Bill.com`
- `/Accounting/Processes/How to Prorate the Corporate branch transactions between ATX and HTX`

These are the "another company's details" class the ingestion brief warns about. Transcribe
faithfully, flag in-file, do not reconcile.

## Filing corrections needed (source folder is wrong)

| Source | Belongs in |
|---|---|
| `Accounting/Processes/How to calculate technician PTO rate` | people/ |
| `Accounting/Processes/How to calculate salesperson commissions`, `Sales Commission`, `Sales commission proces` | people/ (compensation) |
| `Accounting/Processes/How to add employees to overtime alerts` | people/ |
| `Accounting/Processes/Referral bonus` | people/ |
| `Accounting/Payroll/EMPLOYMENT WORK STATUS CHANGE FORM` | people/ |
| `Accounting/Procurement/Company Fleet Management Policies` | field-ops/fleet |
| `Accounting/Procurement/*vehicle*`, `Order a Fuel Card`, `Order Toll Tag` | field-ops/fleet |
| `Operations/After-Hours Emergency Line Protocol` | it/telephony/ |
| `Operations/Tech Voicemail Greeting Script` | it/telephony/ |
| `HR/Onboarding/Device Setup*/Voicemail Greeting Script for Office Personnel`, `How to setup voicemail greetings for office users` | it/telephony/ |
| `Technology/How to setup call monitoring in Ringcentral` | it/telephony/ |
| `HR/Other Resources/Which Access Control profile should I use in Pestroutes?` | it/ |
| `HR/Other Resources/Add user to Wex fuel card system` | field-ops/fleet |
| `WIP/Erase Chromebooks and other ChromeOS devices` | it/ |
| `Customer Care and Dispatch/Schedule of Events` | needs reading — likely field-ops or customer-care |
| `Sales/Service Descriptions` (1.4 MB) | referenced by 4 depts — cross-cutting |

## Screenshot loss (image-heavy — will convert thin)

Any doc over ~100 KB is mostly embedded screenshots. Worst offenders:
`SMS/Email Templates` (44.8 MB), `Instructions on how to activate the Windows Default
Administrator Account` (1.02 MB), `Tech Forms` (5.29 MB), `Service Descriptions` (1.46 MB),
`Pending Cancels` (1.12 MB), `Referral Coupon Process` (1.53 MB), `Adding sub-sources to marketing
sources` (1.14 MB), `End of Day Technciain Route Review` (1.13 MB), `Tech Referral Process`
(3.16 MB), `Sentricon and Ecozone Premium Set Up` (681 KB), `How to Book Depreciation` (524 KB).
Note the loss at the bottom of each affected file.
