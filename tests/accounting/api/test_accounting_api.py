# -*- coding: utf-8 -*-
import datetime
import filecmp
from decimal import Decimal
from pathlib import Path

import pytest
from dateutil import tz

from xero_python.accounting import (
    AccountingApi,
    models,
    Account,
    Accounts,
    AccountType,
    CurrencyCode,
    LineAmountTypes,
    Invoices,
    Invoice,
    Contact,
    Payment,
    HistoryRecords,
    RequestEmpty,
    HistoryRecord,
    Address,
    ContactGroup,
    ContactPerson,
    Phone,
    LineItem,
    Attachments,
    Attachment,
)
from xero_python.api_client import ApiClient
from xero_python.rest import RESTClientObject


@pytest.fixture
def accounting_api(api_client):
    return AccountingApi(api_client=api_client)


@pytest.fixture
def sandbox_accounting_api(api_client):
    return AccountingApi(
        api_client=api_client,
        base_url="https://xero-accounting.getsandbox.com/api.xro/2.0",
    )


@pytest.fixture
def invoice_pdf():
    return Path(__file__).resolve().parent.joinpath("fixtures/inv-0032.pdf")


def test_accounting_api_instance_configuration(accounting_api):
    """
    Test AccountingApi() configured correctly
    """
    assert isinstance(accounting_api, AccountingApi)
    assert isinstance(accounting_api.api_client, ApiClient)
    assert isinstance(accounting_api.api_client.rest_client, RESTClientObject)


@pytest.mark.vcr()
def test_get_organisations(accounting_api: AccountingApi, xero_tenant_id):
    """
    Test AccountingApi.get_organisations()
    """
    # Given correct api client and xero tenant id
    # When fetching organisations
    response = accounting_api.get_organisations(xero_tenant_id=xero_tenant_id)
    # Then expect correct response with organisations tenant has access to
    assert isinstance(response, models.Organisations)
    organisations = response.organisations
    assert isinstance(organisations, list)
    assert len(organisations) == 1
    org = organisations[0]
    assert isinstance(org, models.Organisation)
    assert org.organisation_id
    assert org.is_demo_company


@pytest.mark.vcr()
def test_invoice_attachment_upload_and_download(
    accounting_api, xero_tenant_id, invoice_pdf
):
    """This is a full integration test, tested steps are:

       1. get first page of invoices
       2. choose first invoice
       3. upload test pdf file as invoice attachment
       4. confirm the invoice has new attachment
       5. download uploaded pdf file
    """

    # 1. get first page of invoices
    invoices = accounting_api.get_invoices(xero_tenant_id, page=1)
    assert isinstance(invoices, Invoices)
    assert len(invoices.invoices)
    # 2. choose first invoice
    invoice = invoices.invoices[0]
    assert isinstance(invoice, Invoice)
    # 3. upload test pdf file as invoice attachment
    include_online = True
    with invoice_pdf.open("rb") as pdf:
        response = accounting_api.create_invoice_attachment_by_file_name(
            xero_tenant_id,
            invoice.invoice_id,
            file_name=invoice_pdf.name,
            include_online=include_online,
            body=pdf.read(),
        )
    assert isinstance(response, Attachments)
    assert len(response.attachments) == 1
    attachment = response.attachments[0]
    assert isinstance(attachment, Attachment)
    assert attachment.file_name == invoice_pdf.name
    assert attachment.include_online == include_online
    assert attachment.content_length == invoice_pdf.stat().st_size
    # 4. confirm the invoice has new attachment
    attachments = accounting_api.get_invoice_attachments(
        xero_tenant_id, invoice.invoice_id
    )
    assert isinstance(attachments, Attachments)
    assert len(attachments.attachments)
    for invoice_attachment in attachments.attachments:
        if invoice_attachment.attachment_id == attachment.attachment_id:
            assert invoice_attachment == attachment
            break
    else:
        raise AssertionError("uploaded invoice attachment not found")
    # 5. download uploaded pdf file
    temp_pdf_path = accounting_api.get_invoice_attachment_by_id(
        xero_tenant_id,
        invoice.invoice_id,
        attachment.attachment_id,
        content_type=attachment.mime_type,
    )
    assert isinstance(temp_pdf_path, str)
    assert temp_pdf_path
    temp_pdf = Path(temp_pdf_path)
    assert temp_pdf.exists()
    assert filecmp.cmp(str(invoice_pdf), temp_pdf_path, shallow=False)
    # test cleanup
    temp_pdf.unlink()


@pytest.mark.sandbox
def test_get_accounts(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    expected = Accounts(
        accounts=[
            Account(
                account_id="ebd06280-af70-4bed-97c6-7451a454ad85",
                bank_account_number="0209087654321050",
                bank_account_type="BANK",
                code="091",
                currency_code=CurrencyCode.NZD,
                enable_payments_to_account=False,
                has_attachments=False,
                name="Business Savings Account",
                tax_type="NONE",
                type=AccountType.BANK,
            ),
            Account(
                account_id="7d05a53d-613d-4eb2-a2fc-dcb6adb80b80",
                code="200",
                description="Income from any normal business activity",
                enable_payments_to_account=False,
                has_attachments=False,
                name="Sales",
                tax_type="OUTPUT2",
                type=AccountType.REVENUE,
            ),
        ]
    )
    # When getting all accounts
    result = sandbox_accounting_api.get_accounts(xero_tenant_id)
    # Then expect all accounts to be received
    assert result == expected


@pytest.mark.sandbox
def test_get_account(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    account_id = "99ce6032-0678-4aa0-8148-240c75fee33a"
    expected = Accounts(
        accounts=[
            Account(
                _class="EXPENSE",
                account_id=account_id,
                code="123456",
                description="Hello World",
                enable_payments_to_account=False,
                has_attachments=False,
                name="FooBar",
                reporting_code="EXP",
                reporting_code_name="Expense",
                show_in_expense_claims=False,
                status="ACTIVE",
                tax_type="INPUT",
                type=AccountType.EXPENSE,
                updated_date_utc=datetime.datetime(
                    2019, 2, 22, 1, 2, 39, 120000, tzinfo=tz.UTC
                ),
            )
        ]
    )
    # When getting account
    result = sandbox_accounting_api.get_account(xero_tenant_id, account_id)
    # Then expect one account to be received
    assert result == expected


@pytest.mark.sandbox
def test_create_account(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test account data
    expected = Account(
        _class="EXPENSE",
        account_id="66b262e2-561e-423e-8937-47d558f13442",
        code="123456",
        description="Hello World",
        enable_payments_to_account=False,
        has_attachments=False,
        name="Foobar",
        reporting_code="EXP",
        reporting_code_name="Expense",
        show_in_expense_claims=False,
        status="ACTIVE",
        tax_type="INPUT",
        type=AccountType.EXPENSE,
        updated_date_utc=datetime.datetime(
            2019, 2, 21, 23, 59, 9, 320000, tzinfo=tz.UTC
        ),
    )
    account = Account(
        code=expected.code,
        name=expected.name,
        type=expected.type,
        bank_account_number=None,  # required but not set in sandbox version
    )
    # When creating account
    result = sandbox_accounting_api.create_account(xero_tenant_id, account)
    # Then expect new account to be created
    assert isinstance(result, Accounts)
    assert len(result.accounts) == 1
    result_account = result.accounts[0]
    assert result_account == expected


@pytest.mark.sandbox
def test_update_account(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    account_id = "99ce6032-0678-4aa0-8148-240c75fee33a"
    expected = accounts = Accounts(
        accounts=[
            Account(
                _class="EXPENSE",
                account_id=account_id,
                code="654321",
                description="Good Bye World",
                enable_payments_to_account=False,
                has_attachments=False,
                name="BarFoo",
                reporting_code="EXP",
                reporting_code_name="Expense",
                show_in_expense_claims=False,
                status="ACTIVE",
                tax_type="INPUT",
                type=AccountType.EXPENSE,
                updated_date_utc=datetime.datetime(
                    2019, 2, 22, 0, 29, 49, 333000, tzinfo=tz.UTC
                ),
            )
        ]
    )
    # When updating account
    result = sandbox_accounting_api.update_account(xero_tenant_id, account_id, accounts)
    # Then expect the account to be updated
    assert result == expected


@pytest.mark.sandbox
def test_delete_account(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    account_id = "7f3c0bec-f3e7-4073-b4d6-cc56dd027ef1"
    expected = Accounts(
        accounts=[
            Account(
                _class="EXPENSE",
                account_id=account_id,
                code="123456",
                description="Hello World",
                enable_payments_to_account=False,
                has_attachments=False,
                name="FooBar",
                reporting_code="EXP",
                reporting_code_name="Expense",
                show_in_expense_claims=False,
                status="DELETED",
                tax_type="INPUT",
                type=AccountType.EXPENSE,
                updated_date_utc=datetime.datetime(
                    2019, 2, 22, 1, 16, 57, 210000, tzinfo=tz.UTC
                ),
            )
        ]
    )
    # When deleting account
    result = sandbox_accounting_api.delete_account(xero_tenant_id, account_id)
    # Then expect the account to be deleted
    assert result == expected


@pytest.mark.sandbox
def test_get_account_attachments(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    account_id = "7f3c0bec-f3e7-4073-b4d6-cc56dd027ef1"
    expected = Attachments(
        attachments=[
            Attachment(
                attachment_id="52a643be-cd5c-489f-9778-53a9fd337756",
                content_length=Decimal("2878711"),
                file_name="sample5.jpg",
                include_online=None,
                mime_type="image/jpg",
                url="https://api.xero.com/api.xro/2.0/Accounts/"
                "da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
            )
        ]
    )
    # When getting account attachments
    result = sandbox_accounting_api.get_account_attachments(xero_tenant_id, account_id)
    # Then expect the account attachments to be received
    assert result == expected


@pytest.mark.sandbox
def test_get_invoices(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test invoices data
    # When getting all invoices
    result = sandbox_accounting_api.get_invoices(xero_tenant_id)
    # Then expect correct invoices received
    expected = Invoices(
        invoices=[
            Invoice(
                amount_credited=Decimal("0.00"),
                amount_due=Decimal("0.00"),
                amount_paid=Decimal("0.00"),
                contact=Contact(
                    contact_id="a3675fc4-f8dd-4f03-ba5b-f1870566bcd7",
                    has_attachments=False,
                    has_validation_errors=False,
                    name="Barney Rubble-83203",
                    addresses=[],
                    contact_groups=[],
                    contact_persons=[],
                    phones=[],
                ),
                credit_notes=[],
                line_items=[],
                overpayments=[],
                payments=[],
                prepayments=[],
                currency_code=CurrencyCode.NZD,
                currency_rate=Decimal("1.000000"),
                date=datetime.date(2018, 10, 20),
                due_date=datetime.date(2018, 12, 30),
                has_attachments=False,
                has_errors=False,
                invoice_id="d4956132-ed94-4dd7-9eaa-aa22dfdf06f2",
                invoice_number="INV-0001",
                is_discounted=False,
                line_amount_types=LineAmountTypes.EXCLUSIVE,
                reference="Red Fish, Blue Fish",
                sent_to_contact=True,
                status="VOIDED",
                sub_total=Decimal("40.00"),
                total=Decimal("40.00"),
                total_tax=Decimal("0.00"),
                type="ACCREC",
                updated_date_utc=datetime.datetime(
                    2018, 11, 2, 16, 31, 30, 160000, tzinfo=tz.UTC
                ),
            ),
            Invoice(
                amount_credited=Decimal("0.00"),
                amount_due=Decimal("0.00"),
                amount_paid=Decimal("46.00"),
                contact=Contact(
                    contact_id="a3675fc4-f8dd-4f03-ba5b-f1870566bcd7",
                    has_attachments=False,
                    has_validation_errors=False,
                    name="Barney Rubble-83203",
                    addresses=[],
                    contact_groups=[],
                    contact_persons=[],
                    phones=[],
                ),
                credit_notes=[],
                line_items=[],
                overpayments=[],
                prepayments=[],
                currency_code=CurrencyCode.NZD,
                currency_rate=Decimal("1.000000"),
                date=datetime.date(2018, 10, 20),
                due_date=datetime.date(2018, 12, 30),
                fully_paid_on_date=datetime.date(2018, 11, 29),
                has_attachments=False,
                has_errors=False,
                invoice_id="046d8a6d-1ae1-4b4d-9340-5601bdf41b87",
                invoice_number="INV-0002",
                is_discounted=False,
                line_amount_types=LineAmountTypes.EXCLUSIVE,
                payments=[
                    Payment(
                        amount=Decimal("46.00"),
                        currency_rate=Decimal("1.000000"),
                        date=datetime.date(2018, 11, 29),
                        has_account=False,
                        has_validation_errors=False,
                        payment_id="99ea7f6b-c513-4066-bc27-b7c65dcd76c2",
                    )
                ],
                reference="Red Fish, Blue Fish",
                sent_to_contact=True,
                status="PAID",
                sub_total=Decimal("40.00"),
                total=Decimal("46.00"),
                total_tax=Decimal("6.00"),
                type="ACCREC",
                updated_date_utc=datetime.datetime(
                    2018, 11, 2, 16, 36, 32, 690000, tzinfo=tz.UTC
                ),
            ),
            Invoice(
                amount_credited=Decimal("0.00"),
                amount_due=Decimal("115.00"),
                amount_paid=Decimal("0.00"),
                contact=Contact(
                    contact_id="a3675fc4-f8dd-4f03-ba5b-f1870566bcd7",
                    has_attachments=False,
                    has_validation_errors=False,
                    name="Barney Rubble-83203",
                    addresses=[],
                    contact_groups=[],
                    contact_persons=[],
                    phones=[],
                ),
                credit_notes=[],
                line_items=[],
                overpayments=[],
                payments=[],
                prepayments=[],
                currency_code=CurrencyCode.NZD,
                currency_rate=Decimal("1.000000"),
                date=datetime.date(2018, 11, 2),
                due_date=datetime.date(2018, 11, 7),
                has_attachments=False,
                has_errors=False,
                invoice_id="7ef31b20-de17-4312-8382-412f869b1510",
                invoice_number="INV-0003",
                is_discounted=False,
                line_amount_types=LineAmountTypes.EXCLUSIVE,
                reference="",
                status="AUTHORISED",
                sub_total=Decimal("100.00"),
                total=Decimal("115.00"),
                total_tax=Decimal("15.00"),
                type="ACCREC",
                updated_date_utc=datetime.datetime(
                    2018, 11, 2, 16, 37, 28, 927000, tzinfo=tz.UTC
                ),
            ),
        ]
    )
    assert result == expected


@pytest.mark.sandbox
def test_get_invoice_history(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test invoice data
    invoice_id = "d4956132-ed94-4dd7-9eaa-aa22dfdf06f2"
    # When getting invoice history
    result = sandbox_accounting_api.get_invoice_history(xero_tenant_id, invoice_id)
    # Then expect invoice history to be received
    expected = HistoryRecords()  # todo confirm empty response from sandbox is correct
    assert result == expected


@pytest.mark.sandbox
def test_update_or_create_invoices(
    sandbox_accounting_api: AccountingApi, xero_tenant_id
):
    # Given sandbox API, tenant id, and hardcoded test invoices data
    expected = invoices = Invoices(
        invoices=[
            Invoice(
                amount_due=Decimal("40.00"),
                amount_paid=Decimal("0.00"),
                contact=Contact(
                    addresses=[
                        Address(
                            address_type="STREET",
                            attention_to="",
                            city="",
                            country="",
                            postal_code="",
                            region="",
                        ),
                        Address(
                            address_type="POBOX",
                            attention_to="",
                            city="Anytown",
                            country="USA",
                            postal_code="10101",
                            region="NY",
                        ),
                    ],
                    bank_account_details="",
                    contact_groups=[
                        ContactGroup(
                            contact_group_id="17b44ed7-4389-4162-91cb-3dd5766e4e22",
                            contacts=[],
                            name="Oasis",
                            status="ACTIVE",
                        )
                    ],
                    contact_id="430fa14a-f945-44d3-9f97-5df5e28441b8",
                    contact_persons=[
                        ContactPerson(
                            email_address="debbie@rockstar.com",
                            first_name="Debbie",
                            include_in_emails=False,
                            last_name="Gwyther",
                        )
                    ],
                    contact_status="ACTIVE",
                    email_address="liam@rockstar.com",
                    first_name="Liam",
                    has_attachments=False,
                    has_validation_errors=False,
                    is_customer=True,
                    is_supplier=True,
                    last_name="Gallagher",
                    name="Liam Gallagher",
                    phones=[
                        Phone(
                            phone_area_code="212",
                            phone_country_code="",
                            phone_number="222-2222",
                            phone_type="DEFAULT",
                        ),
                        Phone(
                            phone_area_code="",
                            phone_country_code="",
                            phone_number="",
                            phone_type="DDI",
                        ),
                        Phone(
                            phone_area_code="212",
                            phone_country_code="",
                            phone_number="333-2233",
                            phone_type="FAX",
                        ),
                        Phone(
                            phone_area_code="212",
                            phone_country_code="",
                            phone_number="444-3433",
                            phone_type="MOBILE",
                        ),
                    ],
                    purchases_tracking_categories=[],
                    sales_tracking_categories=[],
                    updated_date_utc=datetime.datetime(
                        2019, 3, 5, 0, 54, 41, 53000, tzinfo=tz.UTC
                    ),
                ),
                currency_code=CurrencyCode.NZD,
                currency_rate=Decimal("1.000000"),
                date=datetime.date(2019, 3, 11),
                due_date=datetime.date(2018, 12, 10),
                has_attachments=False,
                has_errors=False,
                invoice_id="ed255415-e141-4150-aab7-89c3bbbb851c",
                invoice_number="INV-0007",
                is_discounted=False,
                line_amount_types=LineAmountTypes.EXCLUSIVE,
                line_items=[
                    LineItem(
                        account_code="200",
                        description="Acme Tires",
                        line_amount=Decimal("40.00"),
                        line_item_id="5f7a612b-fdcc-4d33-90fa-a9f6bc6db32f",
                        quantity=Decimal("2.0000"),
                        tax_amount=Decimal("0.00"),
                        tax_type="NONE",
                        tracking=[],
                        unit_amount=Decimal("20.00"),
                    )
                ],
                overpayments=[],
                prepayments=[],
                reference="Website Design",
                sent_to_contact=False,
                status="AUTHORISED",
                status_attribute_string="OK",
                sub_total=Decimal("40.00"),
                total=Decimal("40.00"),
                total_tax=Decimal("0.00"),
                type="ACCREC",
                updated_date_utc=datetime.datetime(
                    2019, 3, 11, 17, 58, 46, 117000, tzinfo=tz.UTC
                ),
            )
        ]
    )
    # When updating or creating invoices
    result = sandbox_accounting_api.update_or_create_invoices(xero_tenant_id, invoices)
    # Then expect invoices to be created or updated
    assert result == expected


@pytest.mark.sandbox
def test_create_invoice_history(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    invoice_id = "d4956132-ed94-4dd7-9eaa-aa22dfdf06f2"
    history_records = HistoryRecords(
        [
            HistoryRecord(
                details="Received through the Xero API from ABC Org",
                changes="Approved",
                user="System Generated",
                date_utc=datetime.datetime(2018, 2, 28, 21, 2, 11, tzinfo=tz.UTC),
            ),
            HistoryRecord(
                details="INV-0041 to ABC Furniture for 100.00.",
                changes="Edited",
                user="Mac Haag",
                date_utc=datetime.datetime(2018, 2, 28, 21, 1, 29, tzinfo=tz.UTC),
            ),
        ]
    )
    # When creating invoice history
    result = sandbox_accounting_api.create_invoice_history(
        xero_tenant_id, invoice_id, history_records
    )
    # Then expect created invoice history records
    expected = HistoryRecords()  # todo confirm empty response from sandbox is correct
    assert result == expected


@pytest.mark.sandbox
def test_email_invoice(sandbox_accounting_api: AccountingApi, xero_tenant_id):
    # Given sandbox API, tenant id, and hardcoded test data
    invoice_id = "d4956132-ed94-4dd7-9eaa-aa22dfdf06f2"
    request_empty = RequestEmpty()
    # When email invoice
    result = sandbox_accounting_api.email_invoice(
        xero_tenant_id, invoice_id, request_empty
    )
    # Then expect email invoiced
    assert result is None, "email_invoice doesn't return any data"
