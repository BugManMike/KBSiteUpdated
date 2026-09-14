---
type: Runbook
title: Entering a bill from the Bill.com inbox
description: Turning a document sitting in the Bill.com inbox into a bill — page selection, header details, and expense or item lines.
tags: [bill-com, payables]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1fEiKslb085tGVUhaP-SUfEb73C_kn54UP860fzo4vA4
    resource: https://docs.google.com/document/d/1fEiKslb085tGVUhaP-SUfEb73C_kn54UP860fzo4vA4/edit
    title: How to process bill documents from the Bill.com inbox
status: draft
---

BILL automates accounts payable, receivable and expense management on one platform, with accounting
integration. Documents that arrive in its inbox — including everything
[forwarded from email](/finance/bill-com-invoice-intake.md) — become bills here.

# 1. Select the pages

Next to *Attach page*, choose **All** or **None**, or tick the box per page to pick individual pages.
**Pages left out stay available to use later**, so a multi-invoice PDF can be split across several
bills.

# 2. Choose the action

Select **Enter Bill** to create a new bill.

# 3. Complete the bill details

Bill.com's AI pre-populates some fields from the document. **Review every one of them** rather than
trusting the extraction.

| Field | What goes in it |
|---|---|
| **Vendor Name** | The company or person to be paid. |
| **Invoice Number** | Whatever identifies the bill to the vendor. Entering a duplicate number for the same vendor raises a warning before saving. |
| **Purchase Order Number** | Only appears if Purchase Orders are enabled on the account. |
| **Payment term** | How soon the vendor expects payment. Defaults to the vendor's terms if set. Change it from the dropdown, tick **Apply as default for the vendor** to make the change stick, or **+ New Payment Term** to add one. |
| **Invoice Date** | The day the vendor created the invoice. |
| **Due Date** | Filled automatically once Payment Terms are selected. |
| **Amount** | The bill total. Leave blank when splitting into line items and the system totals them. |

## Expense lines

- **Account** — the expense or other account for what was purchased. **Add new account** if it does
  not exist.
- **Amount** — the amount allocated to that account.
- **Class** — the class for the bill, generally used on billable line items.

## Item lines

Select **Items** next to *Expenses* for the item grid.

1. Enter items and details.
2. Switch **Billable** on to mark a line billable to a customer or job.
3. **Add new item** if the item does not exist.
4. Amount and quantity fields accept `+ - * /` and do the arithmetic themselves.

# 4. Finish

- **Create Bill** — no more bills to enter.
- **Create & New** — go straight to the next bill.
- **Save as Draft** — from the caret next to *Create Bill*, if enabled on the account.

# Related

- [Forwarding vendor invoices into Bill.com](/finance/bill-com-invoice-intake.md)
- [Processing bill payments in Bill.com](/finance/bill-com-bill-payments.md)
- [Uploading King Ranch bills](/finance/king-ranch-bills.md)
