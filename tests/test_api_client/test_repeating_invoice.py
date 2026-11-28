from xero_python.accounting.models.repeating_invoice import RepeatingInvoice


def test_repeating_invoice_exposes_total_discount():
    invoice = RepeatingInvoice(total_discount=12.5)

    assert RepeatingInvoice.attribute_map["total_discount"] == "TotalDiscount"
    assert RepeatingInvoice.openapi_types["total_discount"] == "float"
    assert invoice.total_discount == 12.5
