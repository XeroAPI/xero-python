# xero_python.accounting.AccountingApi

All URIs are relative to *https://api.xero.com/api.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountingApi.md#create_account) | **PUT** /Accounts | Allows you to create a new chart of accounts
[**create_account_attachment_by_file_name**](AccountingApi.md#create_account_attachment_by_file_name) | **PUT** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to create Attachment on Account
[**create_bank_transaction_attachment_by_file_name**](AccountingApi.md#create_bank_transaction_attachment_by_file_name) | **PUT** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to createa an Attachment on BankTransaction by Filename
[**create_bank_transaction_history_record**](AccountingApi.md#create_bank_transaction_history_record) | **PUT** /BankTransactions/{BankTransactionID}/History | Allows you to create history record for a bank transactions
[**create_bank_transactions**](AccountingApi.md#create_bank_transactions) | **PUT** /BankTransactions | Allows you to create one or more spend or receive money transaction
[**create_bank_transfer**](AccountingApi.md#create_bank_transfer) | **PUT** /BankTransfers | Allows you to create a bank transfers
[**create_bank_transfer_attachment_by_file_name**](AccountingApi.md#create_bank_transfer_attachment_by_file_name) | **PUT** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**create_bank_transfer_history_record**](AccountingApi.md#create_bank_transfer_history_record) | **PUT** /BankTransfers/{BankTransferID}/History | 
[**create_batch_payment**](AccountingApi.md#create_batch_payment) | **PUT** /BatchPayments | Create one or many BatchPayments for invoices
[**create_batch_payment_history_record**](AccountingApi.md#create_batch_payment_history_record) | **PUT** /BatchPayments/{BatchPaymentID}/History | Allows you to create a history record for a Batch Payment
[**create_branding_theme_payment_services**](AccountingApi.md#create_branding_theme_payment_services) | **POST** /BrandingThemes/{BrandingThemeID}/PaymentServices | Allow for the creation of new custom payment service for specified Branding Theme
[**create_contact_attachment_by_file_name**](AccountingApi.md#create_contact_attachment_by_file_name) | **PUT** /Contacts/{ContactID}/Attachments/{FileName} | 
[**create_contact_group**](AccountingApi.md#create_contact_group) | **PUT** /ContactGroups | Allows you to create a contact group
[**create_contact_group_contacts**](AccountingApi.md#create_contact_group_contacts) | **PUT** /ContactGroups/{ContactGroupID}/Contacts | Allows you to add Contacts to a Contact Group
[**create_contact_history**](AccountingApi.md#create_contact_history) | **PUT** /Contacts/{ContactID}/History | Allows you to retrieve a history records of an Contact
[**create_contacts**](AccountingApi.md#create_contacts) | **PUT** /Contacts | Allows you to create a multiple contacts (bulk) in a Xero organisation
[**create_credit_note_allocation**](AccountingApi.md#create_credit_note_allocation) | **PUT** /CreditNotes/{CreditNoteID}/Allocations | Allows you to create Allocation on CreditNote
[**create_credit_note_attachment_by_file_name**](AccountingApi.md#create_credit_note_attachment_by_file_name) | **PUT** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to create Attachments on CreditNote by file name
[**create_credit_note_history**](AccountingApi.md#create_credit_note_history) | **PUT** /CreditNotes/{CreditNoteID}/History | Allows you to retrieve a history records of an CreditNote
[**create_credit_notes**](AccountingApi.md#create_credit_notes) | **PUT** /CreditNotes | Allows you to create a credit note
[**create_currency**](AccountingApi.md#create_currency) | **PUT** /Currencies | 
[**create_employees**](AccountingApi.md#create_employees) | **PUT** /Employees | Allows you to create new employees used in Xero payrun
[**create_expense_claim_history**](AccountingApi.md#create_expense_claim_history) | **PUT** /ExpenseClaims/{ExpenseClaimID}/History | Allows you to create a history records of an ExpenseClaim
[**create_expense_claims**](AccountingApi.md#create_expense_claims) | **PUT** /ExpenseClaims | Allows you to retrieve expense claims
[**create_invoice_attachment_by_file_name**](AccountingApi.md#create_invoice_attachment_by_file_name) | **PUT** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to create an Attachment on invoices or purchase bills by it&#39;s filename
[**create_invoice_history**](AccountingApi.md#create_invoice_history) | **PUT** /Invoices/{InvoiceID}/History | Allows you to retrieve a history records of an invoice
[**create_invoices**](AccountingApi.md#create_invoices) | **PUT** /Invoices | Allows you to create one or more sales invoices or purchase bills
[**create_item_history**](AccountingApi.md#create_item_history) | **PUT** /Items/{ItemID}/History | Allows you to create a history record for items
[**create_items**](AccountingApi.md#create_items) | **PUT** /Items | Allows you to create one or more items
[**create_linked_transaction**](AccountingApi.md#create_linked_transaction) | **PUT** /LinkedTransactions | Allows you to create linked transactions (billable expenses)
[**create_manual_journal_attachment_by_file_name**](AccountingApi.md#create_manual_journal_attachment_by_file_name) | **PUT** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to create a specified Attachment on ManualJournal by file name
[**create_manual_journals**](AccountingApi.md#create_manual_journals) | **PUT** /ManualJournals | Allows you to create one or more manual journals
[**create_overpayment_allocations**](AccountingApi.md#create_overpayment_allocations) | **PUT** /Overpayments/{OverpaymentID}/Allocations | Allows you to create a single allocation for an overpayment
[**create_overpayment_history**](AccountingApi.md#create_overpayment_history) | **PUT** /Overpayments/{OverpaymentID}/History | Allows you to create history records of an Overpayment
[**create_payment**](AccountingApi.md#create_payment) | **POST** /Payments | Allows you to create a single payment for invoices or credit notes
[**create_payment_history**](AccountingApi.md#create_payment_history) | **PUT** /Payments/{PaymentID}/History | Allows you to create a history record for a payment
[**create_payment_service**](AccountingApi.md#create_payment_service) | **PUT** /PaymentServices | Allows you to create payment services
[**create_payments**](AccountingApi.md#create_payments) | **PUT** /Payments | Allows you to create multiple payments for invoices or credit notes
[**create_prepayment_allocations**](AccountingApi.md#create_prepayment_allocations) | **PUT** /Prepayments/{PrepaymentID}/Allocations | Allows you to create an Allocation for prepayments
[**create_prepayment_history**](AccountingApi.md#create_prepayment_history) | **PUT** /Prepayments/{PrepaymentID}/History | Allows you to create a history record for an Prepayment
[**create_purchase_order_history**](AccountingApi.md#create_purchase_order_history) | **PUT** /PurchaseOrders/{PurchaseOrderID}/History | Allows you to create HistoryRecord for purchase orders
[**create_purchase_orders**](AccountingApi.md#create_purchase_orders) | **PUT** /PurchaseOrders | Allows you to create one or more purchase orders
[**create_quote_attachment_by_file_name**](AccountingApi.md#create_quote_attachment_by_file_name) | **PUT** /Quotes/{QuoteID}/Attachments/{FileName} | Allows you to create Attachment on Quote
[**create_quote_history**](AccountingApi.md#create_quote_history) | **PUT** /Quotes/{QuoteID}/History | Allows you to retrieve a history records of an quote
[**create_quotes**](AccountingApi.md#create_quotes) | **PUT** /Quotes | Allows you to create one or more quotes
[**create_receipt**](AccountingApi.md#create_receipt) | **PUT** /Receipts | Allows you to create draft expense claim receipts for any user
[**create_receipt_attachment_by_file_name**](AccountingApi.md#create_receipt_attachment_by_file_name) | **PUT** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to create Attachment on expense claim receipts by file name
[**create_receipt_history**](AccountingApi.md#create_receipt_history) | **PUT** /Receipts/{ReceiptID}/History | Allows you to retrieve a history records of an Receipt
[**create_repeating_invoice_attachment_by_file_name**](AccountingApi.md#create_repeating_invoice_attachment_by_file_name) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to create attachment on repeating invoices by file name
[**create_repeating_invoice_history**](AccountingApi.md#create_repeating_invoice_history) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/History | Allows you to create history for a repeating invoice
[**create_tax_rates**](AccountingApi.md#create_tax_rates) | **PUT** /TaxRates | Allows you to create one or more Tax Rates
[**create_tracking_category**](AccountingApi.md#create_tracking_category) | **PUT** /TrackingCategories | Allows you to create tracking categories
[**create_tracking_options**](AccountingApi.md#create_tracking_options) | **PUT** /TrackingCategories/{TrackingCategoryID}/Options | Allows you to create options for a specified tracking category
[**delete_account**](AccountingApi.md#delete_account) | **DELETE** /Accounts/{AccountID} | Allows you to delete a chart of accounts
[**delete_contact_group_contact**](AccountingApi.md#delete_contact_group_contact) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts/{ContactID} | Allows you to delete a specific Contact from a Contact Group
[**delete_contact_group_contacts**](AccountingApi.md#delete_contact_group_contacts) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts | Allows you to delete  all Contacts from a Contact Group
[**delete_item**](AccountingApi.md#delete_item) | **DELETE** /Items/{ItemID} | Allows you to delete a specified item
[**delete_linked_transaction**](AccountingApi.md#delete_linked_transaction) | **DELETE** /LinkedTransactions/{LinkedTransactionID} | Allows you to delete a specified linked transactions (billable expenses)
[**delete_payment**](AccountingApi.md#delete_payment) | **POST** /Payments/{PaymentID} | Allows you to update a specified payment for invoices and credit notes
[**delete_tracking_category**](AccountingApi.md#delete_tracking_category) | **DELETE** /TrackingCategories/{TrackingCategoryID} | Allows you to delete tracking categories
[**delete_tracking_options**](AccountingApi.md#delete_tracking_options) | **DELETE** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Allows you to delete a specified option for a specified tracking category
[**email_invoice**](AccountingApi.md#email_invoice) | **POST** /Invoices/{InvoiceID}/Email | Allows you to email a copy of invoice to related Contact
[**get_account**](AccountingApi.md#get_account) | **GET** /Accounts/{AccountID} | Allows you to retrieve a single chart of accounts
[**get_account_attachment_by_file_name**](AccountingApi.md#get_account_attachment_by_file_name) | **GET** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to retrieve Attachment on Account by Filename
[**get_account_attachment_by_id**](AccountingApi.md#get_account_attachment_by_id) | **GET** /Accounts/{AccountID}/Attachments/{AttachmentID} | Allows you to retrieve specific Attachment on Account
[**get_account_attachments**](AccountingApi.md#get_account_attachments) | **GET** /Accounts/{AccountID}/Attachments | Allows you to retrieve Attachments for accounts
[**get_accounts**](AccountingApi.md#get_accounts) | **GET** /Accounts | Allows you to retrieve the full chart of accounts
[**get_bank_transaction**](AccountingApi.md#get_bank_transaction) | **GET** /BankTransactions/{BankTransactionID} | Allows you to retrieve a single spend or receive money transaction
[**get_bank_transaction_attachment_by_file_name**](AccountingApi.md#get_bank_transaction_attachment_by_file_name) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to retrieve Attachments on BankTransaction by Filename
[**get_bank_transaction_attachment_by_id**](AccountingApi.md#get_bank_transaction_attachment_by_id) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on a specific BankTransaction
[**get_bank_transaction_attachments**](AccountingApi.md#get_bank_transaction_attachments) | **GET** /BankTransactions/{BankTransactionID}/Attachments | Allows you to retrieve any attachments to bank transactions
[**get_bank_transactions**](AccountingApi.md#get_bank_transactions) | **GET** /BankTransactions | Allows you to retrieve any spend or receive money transactions
[**get_bank_transactions_history**](AccountingApi.md#get_bank_transactions_history) | **GET** /BankTransactions/{BankTransactionID}/History | Allows you to retrieve history from a bank transactions
[**get_bank_transfer**](AccountingApi.md#get_bank_transfer) | **GET** /BankTransfers/{BankTransferID} | Allows you to retrieve any bank transfers
[**get_bank_transfer_attachment_by_file_name**](AccountingApi.md#get_bank_transfer_attachment_by_file_name) | **GET** /BankTransfers/{BankTransferID}/Attachments/{FileName} | Allows you to retrieve Attachments on BankTransfer by file name
[**get_bank_transfer_attachment_by_id**](AccountingApi.md#get_bank_transfer_attachment_by_id) | **GET** /BankTransfers/{BankTransferID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on BankTransfer
[**get_bank_transfer_attachments**](AccountingApi.md#get_bank_transfer_attachments) | **GET** /BankTransfers/{BankTransferID}/Attachments | Allows you to retrieve Attachments from  bank transfers
[**get_bank_transfer_history**](AccountingApi.md#get_bank_transfer_history) | **GET** /BankTransfers/{BankTransferID}/History | Allows you to retrieve history from a bank transfers
[**get_bank_transfers**](AccountingApi.md#get_bank_transfers) | **GET** /BankTransfers | Allows you to retrieve all bank transfers
[**get_batch_payment_history**](AccountingApi.md#get_batch_payment_history) | **GET** /BatchPayments/{BatchPaymentID}/History | Allows you to retrieve history from a Batch Payment
[**get_batch_payments**](AccountingApi.md#get_batch_payments) | **GET** /BatchPayments | Retrieve either one or many BatchPayments for invoices
[**get_branding_theme**](AccountingApi.md#get_branding_theme) | **GET** /BrandingThemes/{BrandingThemeID} | Allows you to retrieve a specific BrandingThemes
[**get_branding_theme_payment_services**](AccountingApi.md#get_branding_theme_payment_services) | **GET** /BrandingThemes/{BrandingThemeID}/PaymentServices | Allows you to retrieve the Payment services for a Branding Theme
[**get_branding_themes**](AccountingApi.md#get_branding_themes) | **GET** /BrandingThemes | Allows you to retrieve all the BrandingThemes
[**get_contact**](AccountingApi.md#get_contact) | **GET** /Contacts/{ContactID} | Allows you to retrieve a single contacts in a Xero organisation
[**get_contact_attachment_by_file_name**](AccountingApi.md#get_contact_attachment_by_file_name) | **GET** /Contacts/{ContactID}/Attachments/{FileName} | Allows you to retrieve Attachments on Contacts by file name
[**get_contact_attachment_by_id**](AccountingApi.md#get_contact_attachment_by_id) | **GET** /Contacts/{ContactID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on Contacts
[**get_contact_attachments**](AccountingApi.md#get_contact_attachments) | **GET** /Contacts/{ContactID}/Attachments | Allows you to retrieve, add and update contacts in a Xero organisation
[**get_contact_by_contact_number**](AccountingApi.md#get_contact_by_contact_number) | **GET** /Contacts/{ContactNumber} | Allows you to retrieve a single contact by Contact Number in a Xero organisation
[**get_contact_cis_settings**](AccountingApi.md#get_contact_cis_settings) | **GET** /Contacts/{ContactID}/CISSettings | Allows you to retrieve CISSettings for a contact in a Xero organisation
[**get_contact_group**](AccountingApi.md#get_contact_group) | **GET** /ContactGroups/{ContactGroupID} | Allows you to retrieve a unique Contact Group by ID
[**get_contact_groups**](AccountingApi.md#get_contact_groups) | **GET** /ContactGroups | Allows you to retrieve the ContactID and Name of all the contacts in a contact group
[**get_contact_history**](AccountingApi.md#get_contact_history) | **GET** /Contacts/{ContactID}/History | Allows you to retrieve a history records of an Contact
[**get_contacts**](AccountingApi.md#get_contacts) | **GET** /Contacts | Allows you to retrieve all contacts in a Xero organisation
[**get_credit_note**](AccountingApi.md#get_credit_note) | **GET** /CreditNotes/{CreditNoteID} | Allows you to retrieve a specific credit note
[**get_credit_note_as_pdf**](AccountingApi.md#get_credit_note_as_pdf) | **GET** /CreditNotes/{CreditNoteID}/pdf | Allows you to retrieve Credit Note as PDF files
[**get_credit_note_attachment_by_file_name**](AccountingApi.md#get_credit_note_attachment_by_file_name) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to retrieve Attachments on CreditNote by file name
[**get_credit_note_attachment_by_id**](AccountingApi.md#get_credit_note_attachment_by_id) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on CreditNote
[**get_credit_note_attachments**](AccountingApi.md#get_credit_note_attachments) | **GET** /CreditNotes/{CreditNoteID}/Attachments | Allows you to retrieve Attachments for credit notes
[**get_credit_note_history**](AccountingApi.md#get_credit_note_history) | **GET** /CreditNotes/{CreditNoteID}/History | Allows you to retrieve a history records of an CreditNote
[**get_credit_notes**](AccountingApi.md#get_credit_notes) | **GET** /CreditNotes | Allows you to retrieve any credit notes
[**get_currencies**](AccountingApi.md#get_currencies) | **GET** /Currencies | Allows you to retrieve currencies for your organisation
[**get_employee**](AccountingApi.md#get_employee) | **GET** /Employees/{EmployeeID} | Allows you to retrieve a specific employee used in Xero payrun
[**get_employees**](AccountingApi.md#get_employees) | **GET** /Employees | Allows you to retrieve employees used in Xero payrun
[**get_expense_claim**](AccountingApi.md#get_expense_claim) | **GET** /ExpenseClaims/{ExpenseClaimID} | Allows you to retrieve a specified expense claim
[**get_expense_claim_history**](AccountingApi.md#get_expense_claim_history) | **GET** /ExpenseClaims/{ExpenseClaimID}/History | Allows you to retrieve a history records of an ExpenseClaim
[**get_expense_claims**](AccountingApi.md#get_expense_claims) | **GET** /ExpenseClaims | Allows you to retrieve expense claims
[**get_invoice**](AccountingApi.md#get_invoice) | **GET** /Invoices/{InvoiceID} | Allows you to retrieve a specified sales invoice or purchase bill
[**get_invoice_as_pdf**](AccountingApi.md#get_invoice_as_pdf) | **GET** /Invoices/{InvoiceID}/pdf | Allows you to retrieve invoices or purchase bills as PDF files
[**get_invoice_attachment_by_file_name**](AccountingApi.md#get_invoice_attachment_by_file_name) | **GET** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to retrieve Attachment on invoices or purchase bills by it&#39;s filename
[**get_invoice_attachment_by_id**](AccountingApi.md#get_invoice_attachment_by_id) | **GET** /Invoices/{InvoiceID}/Attachments/{AttachmentID} | Allows you to retrieve a specified Attachment on invoices or purchase bills by it&#39;s ID
[**get_invoice_attachments**](AccountingApi.md#get_invoice_attachments) | **GET** /Invoices/{InvoiceID}/Attachments | Allows you to retrieve Attachments on invoices or purchase bills
[**get_invoice_history**](AccountingApi.md#get_invoice_history) | **GET** /Invoices/{InvoiceID}/History | Allows you to retrieve a history records of an invoice
[**get_invoice_reminders**](AccountingApi.md#get_invoice_reminders) | **GET** /InvoiceReminders/Settings | Allows you to retrieve invoice reminder settings
[**get_invoices**](AccountingApi.md#get_invoices) | **GET** /Invoices | Allows you to retrieve any sales invoices or purchase bills
[**get_item**](AccountingApi.md#get_item) | **GET** /Items/{ItemID} | Allows you to retrieve a specified item
[**get_item_history**](AccountingApi.md#get_item_history) | **GET** /Items/{ItemID}/History | Allows you to retrieve history for items
[**get_items**](AccountingApi.md#get_items) | **GET** /Items | Allows you to retrieve any items
[**get_journal**](AccountingApi.md#get_journal) | **GET** /Journals/{JournalID} | Allows you to retrieve a specified journals.
[**get_journals**](AccountingApi.md#get_journals) | **GET** /Journals | Allows you to retrieve any journals.
[**get_linked_transaction**](AccountingApi.md#get_linked_transaction) | **GET** /LinkedTransactions/{LinkedTransactionID} | Allows you to retrieve a specified linked transactions (billable expenses)
[**get_linked_transactions**](AccountingApi.md#get_linked_transactions) | **GET** /LinkedTransactions | Retrieve linked transactions (billable expenses)
[**get_manual_journal**](AccountingApi.md#get_manual_journal) | **GET** /ManualJournals/{ManualJournalID} | Allows you to retrieve a specified manual journals
[**get_manual_journal_attachment_by_file_name**](AccountingApi.md#get_manual_journal_attachment_by_file_name) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to retrieve specified Attachment on ManualJournal by file name
[**get_manual_journal_attachment_by_id**](AccountingApi.md#get_manual_journal_attachment_by_id) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{AttachmentID} | Allows you to retrieve specified Attachment on ManualJournals
[**get_manual_journal_attachments**](AccountingApi.md#get_manual_journal_attachments) | **GET** /ManualJournals/{ManualJournalID}/Attachments | Allows you to retrieve Attachment for manual journals
[**get_manual_journals**](AccountingApi.md#get_manual_journals) | **GET** /ManualJournals | Allows you to retrieve any manual journals
[**get_online_invoice**](AccountingApi.md#get_online_invoice) | **GET** /Invoices/{InvoiceID}/OnlineInvoice | Allows you to retrieve a URL to an online invoice
[**get_organisation_cis_settings**](AccountingApi.md#get_organisation_cis_settings) | **GET** /Organisation/{OrganisationID}/CISSettings | Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.
[**get_organisations**](AccountingApi.md#get_organisations) | **GET** /Organisation | Allows you to retrieve Organisation details
[**get_overpayment**](AccountingApi.md#get_overpayment) | **GET** /Overpayments/{OverpaymentID} | Allows you to retrieve a specified overpayments
[**get_overpayment_history**](AccountingApi.md#get_overpayment_history) | **GET** /Overpayments/{OverpaymentID}/History | Allows you to retrieve a history records of an Overpayment
[**get_overpayments**](AccountingApi.md#get_overpayments) | **GET** /Overpayments | Allows you to retrieve overpayments
[**get_payment**](AccountingApi.md#get_payment) | **GET** /Payments/{PaymentID} | Allows you to retrieve a specified payment for invoices and credit notes
[**get_payment_history**](AccountingApi.md#get_payment_history) | **GET** /Payments/{PaymentID}/History | Allows you to retrieve history records of a payment
[**get_payment_services**](AccountingApi.md#get_payment_services) | **GET** /PaymentServices | Allows you to retrieve payment services
[**get_payments**](AccountingApi.md#get_payments) | **GET** /Payments | Allows you to retrieve payments for invoices and credit notes
[**get_prepayment**](AccountingApi.md#get_prepayment) | **GET** /Prepayments/{PrepaymentID} | Allows you to retrieve a specified prepayments
[**get_prepayment_history**](AccountingApi.md#get_prepayment_history) | **GET** /Prepayments/{PrepaymentID}/History | Allows you to retrieve a history records of an Prepayment
[**get_prepayments**](AccountingApi.md#get_prepayments) | **GET** /Prepayments | Allows you to retrieve prepayments
[**get_purchase_order**](AccountingApi.md#get_purchase_order) | **GET** /PurchaseOrders/{PurchaseOrderID} | Allows you to retrieve a specified purchase orders
[**get_purchase_order_as_pdf**](AccountingApi.md#get_purchase_order_as_pdf) | **GET** /PurchaseOrders/{PurchaseOrderID}/pdf | Allows you to retrieve purchase orders as PDF files
[**get_purchase_order_by_number**](AccountingApi.md#get_purchase_order_by_number) | **GET** /PurchaseOrders/{PurchaseOrderNumber} | Allows you to retrieve a specified purchase orders
[**get_purchase_order_history**](AccountingApi.md#get_purchase_order_history) | **GET** /PurchaseOrders/{PurchaseOrderID}/History | Allows you to retrieve history for PurchaseOrder
[**get_purchase_orders**](AccountingApi.md#get_purchase_orders) | **GET** /PurchaseOrders | Allows you to retrieve purchase orders
[**get_quote**](AccountingApi.md#get_quote) | **GET** /Quotes/{QuoteID} | Allows you to retrieve a specified quote
[**get_quote_as_pdf**](AccountingApi.md#get_quote_as_pdf) | **GET** /Quotes/{QuotesID}/pdf | Allows you to retrieve quotes as PDF files
[**get_quote_attachment_by_file_name**](AccountingApi.md#get_quote_attachment_by_file_name) | **GET** /Quotes/{QuoteID}/Attachments/{FileName} | Allows you to retrieve Attachment on Quote by Filename
[**get_quote_attachment_by_id**](AccountingApi.md#get_quote_attachment_by_id) | **GET** /Quotes/{QuoteID}/Attachments/{AttachmentID} | Allows you to retrieve specific Attachment on Quote
[**get_quote_attachments**](AccountingApi.md#get_quote_attachments) | **GET** /Quotes/{QuoteID}/Attachments | Allows you to retrieve Attachments for Quotes
[**get_quote_history**](AccountingApi.md#get_quote_history) | **GET** /Quotes/{QuoteID}/History | Allows you to retrieve a history records of an quote
[**get_quotes**](AccountingApi.md#get_quotes) | **GET** /Quotes | Allows you to retrieve any sales quotes
[**get_receipt**](AccountingApi.md#get_receipt) | **GET** /Receipts/{ReceiptID} | Allows you to retrieve a specified draft expense claim receipts
[**get_receipt_attachment_by_file_name**](AccountingApi.md#get_receipt_attachment_by_file_name) | **GET** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to retrieve Attachments on expense claim receipts by file name
[**get_receipt_attachment_by_id**](AccountingApi.md#get_receipt_attachment_by_id) | **GET** /Receipts/{ReceiptID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on expense claim receipts by ID
[**get_receipt_attachments**](AccountingApi.md#get_receipt_attachments) | **GET** /Receipts/{ReceiptID}/Attachments | Allows you to retrieve Attachments for expense claim receipts
[**get_receipt_history**](AccountingApi.md#get_receipt_history) | **GET** /Receipts/{ReceiptID}/History | Allows you to retrieve a history records of an Receipt
[**get_receipts**](AccountingApi.md#get_receipts) | **GET** /Receipts | Allows you to retrieve draft expense claim receipts for any user
[**get_repeating_invoice**](AccountingApi.md#get_repeating_invoice) | **GET** /RepeatingInvoices/{RepeatingInvoiceID} | Allows you to retrieve a specified repeating invoice
[**get_repeating_invoice_attachment_by_file_name**](AccountingApi.md#get_repeating_invoice_attachment_by_file_name) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to retrieve specified attachment on repeating invoices by file name
[**get_repeating_invoice_attachment_by_id**](AccountingApi.md#get_repeating_invoice_attachment_by_id) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{AttachmentID} | Allows you to retrieve a specified Attachments on repeating invoices
[**get_repeating_invoice_attachments**](AccountingApi.md#get_repeating_invoice_attachments) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments | Allows you to retrieve Attachments on repeating invoice
[**get_repeating_invoice_history**](AccountingApi.md#get_repeating_invoice_history) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/History | Allows you to retrieve history for a repeating invoice
[**get_repeating_invoices**](AccountingApi.md#get_repeating_invoices) | **GET** /RepeatingInvoices | Allows you to retrieve any repeating invoices
[**get_report_aged_payables_by_contact**](AccountingApi.md#get_report_aged_payables_by_contact) | **GET** /Reports/AgedPayablesByContact | Allows you to retrieve report for AgedPayablesByContact
[**get_report_aged_receivables_by_contact**](AccountingApi.md#get_report_aged_receivables_by_contact) | **GET** /Reports/AgedReceivablesByContact | Allows you to retrieve report for AgedReceivablesByContact
[**get_report_ba_sor_gst**](AccountingApi.md#get_report_ba_sor_gst) | **GET** /Reports/{ReportID} | Allows you to retrieve report for BAS only valid for AU orgs
[**get_report_ba_sor_gst_list**](AccountingApi.md#get_report_ba_sor_gst_list) | **GET** /Reports | Allows you to retrieve report for BAS only valid for AU orgs
[**get_report_balance_sheet**](AccountingApi.md#get_report_balance_sheet) | **GET** /Reports/BalanceSheet | Allows you to retrieve report for BalanceSheet
[**get_report_bank_summary**](AccountingApi.md#get_report_bank_summary) | **GET** /Reports/BankSummary | Allows you to retrieve report for BankSummary
[**get_report_budget_summary**](AccountingApi.md#get_report_budget_summary) | **GET** /Reports/BudgetSummary | Allows you to retrieve report for Budget Summary
[**get_report_executive_summary**](AccountingApi.md#get_report_executive_summary) | **GET** /Reports/ExecutiveSummary | Allows you to retrieve report for ExecutiveSummary
[**get_report_profit_and_loss**](AccountingApi.md#get_report_profit_and_loss) | **GET** /Reports/ProfitAndLoss | Allows you to retrieve report for ProfitAndLoss
[**get_report_ten_ninety_nine**](AccountingApi.md#get_report_ten_ninety_nine) | **GET** /Reports/TenNinetyNine | Allows you to retrieve report for TenNinetyNine
[**get_report_trial_balance**](AccountingApi.md#get_report_trial_balance) | **GET** /Reports/TrialBalance | Allows you to retrieve report for TrialBalance
[**get_tax_rates**](AccountingApi.md#get_tax_rates) | **GET** /TaxRates | Allows you to retrieve Tax Rates
[**get_tracking_categories**](AccountingApi.md#get_tracking_categories) | **GET** /TrackingCategories | Allows you to retrieve tracking categories and options
[**get_tracking_category**](AccountingApi.md#get_tracking_category) | **GET** /TrackingCategories/{TrackingCategoryID} | Allows you to retrieve tracking categories and options for specified category
[**get_user**](AccountingApi.md#get_user) | **GET** /Users/{UserID} | Allows you to retrieve a specified user
[**get_users**](AccountingApi.md#get_users) | **GET** /Users | Allows you to retrieve users
[**update_account**](AccountingApi.md#update_account) | **POST** /Accounts/{AccountID} | Allows you to update a chart of accounts
[**update_account_attachment_by_file_name**](AccountingApi.md#update_account_attachment_by_file_name) | **POST** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to update Attachment on Account by Filename
[**update_bank_transaction**](AccountingApi.md#update_bank_transaction) | **POST** /BankTransactions/{BankTransactionID} | Allows you to update a single spend or receive money transaction
[**update_bank_transaction_attachment_by_file_name**](AccountingApi.md#update_bank_transaction_attachment_by_file_name) | **POST** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to update an Attachment on BankTransaction by Filename
[**update_bank_transfer_attachment_by_file_name**](AccountingApi.md#update_bank_transfer_attachment_by_file_name) | **POST** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**update_contact**](AccountingApi.md#update_contact) | **POST** /Contacts/{ContactID} | 
[**update_contact_attachment_by_file_name**](AccountingApi.md#update_contact_attachment_by_file_name) | **POST** /Contacts/{ContactID}/Attachments/{FileName} | 
[**update_contact_group**](AccountingApi.md#update_contact_group) | **POST** /ContactGroups/{ContactGroupID} | Allows you to update a Contact Group
[**update_credit_note**](AccountingApi.md#update_credit_note) | **POST** /CreditNotes/{CreditNoteID} | Allows you to update a specific credit note
[**update_credit_note_attachment_by_file_name**](AccountingApi.md#update_credit_note_attachment_by_file_name) | **POST** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to update Attachments on CreditNote by file name
[**update_expense_claim**](AccountingApi.md#update_expense_claim) | **POST** /ExpenseClaims/{ExpenseClaimID} | Allows you to update specified expense claims
[**update_invoice**](AccountingApi.md#update_invoice) | **POST** /Invoices/{InvoiceID} | Allows you to update a specified sales invoices or purchase bills
[**update_invoice_attachment_by_file_name**](AccountingApi.md#update_invoice_attachment_by_file_name) | **POST** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to update Attachment on invoices or purchase bills by it&#39;s filename
[**update_item**](AccountingApi.md#update_item) | **POST** /Items/{ItemID} | Allows you to update a specified item
[**update_linked_transaction**](AccountingApi.md#update_linked_transaction) | **POST** /LinkedTransactions/{LinkedTransactionID} | Allows you to update a specified linked transactions (billable expenses)
[**update_manual_journal**](AccountingApi.md#update_manual_journal) | **POST** /ManualJournals/{ManualJournalID} | Allows you to update a specified manual journal
[**update_manual_journal_attachment_by_file_name**](AccountingApi.md#update_manual_journal_attachment_by_file_name) | **POST** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to update a specified Attachment on ManualJournal by file name
[**update_or_create_bank_transactions**](AccountingApi.md#update_or_create_bank_transactions) | **POST** /BankTransactions | Allows you to update or create one or more spend or receive money transaction
[**update_or_create_contacts**](AccountingApi.md#update_or_create_contacts) | **POST** /Contacts | Allows you to update OR create one or more contacts in a Xero organisation
[**update_or_create_credit_notes**](AccountingApi.md#update_or_create_credit_notes) | **POST** /CreditNotes | Allows you to update OR create one or more credit notes
[**update_or_create_employees**](AccountingApi.md#update_or_create_employees) | **POST** /Employees | Allows you to create a single new employees used in Xero payrun
[**update_or_create_invoices**](AccountingApi.md#update_or_create_invoices) | **POST** /Invoices | Allows you to update OR create one or more sales invoices or purchase bills
[**update_or_create_items**](AccountingApi.md#update_or_create_items) | **POST** /Items | Allows you to update or create one or more items
[**update_or_create_manual_journals**](AccountingApi.md#update_or_create_manual_journals) | **POST** /ManualJournals | Allows you to create a single manual journal
[**update_or_create_purchase_orders**](AccountingApi.md#update_or_create_purchase_orders) | **POST** /PurchaseOrders | Allows you to update or create one or more purchase orders
[**update_or_create_quotes**](AccountingApi.md#update_or_create_quotes) | **POST** /Quotes | Allows you to update OR create one or more quotes
[**update_purchase_order**](AccountingApi.md#update_purchase_order) | **POST** /PurchaseOrders/{PurchaseOrderID} | Allows you to update a specified purchase order
[**update_quote**](AccountingApi.md#update_quote) | **POST** /Quotes/{QuoteID} | Allows you to update a specified quote
[**update_quote_attachment_by_file_name**](AccountingApi.md#update_quote_attachment_by_file_name) | **POST** /Quotes/{QuoteID}/Attachments/{FileName} | Allows you to update Attachment on Quote by Filename
[**update_receipt**](AccountingApi.md#update_receipt) | **POST** /Receipts/{ReceiptID} | Allows you to retrieve a specified draft expense claim receipts
[**update_receipt_attachment_by_file_name**](AccountingApi.md#update_receipt_attachment_by_file_name) | **POST** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to update Attachment on expense claim receipts by file name
[**update_repeating_invoice_attachment_by_file_name**](AccountingApi.md#update_repeating_invoice_attachment_by_file_name) | **POST** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to update specified attachment on repeating invoices by file name
[**update_tax_rate**](AccountingApi.md#update_tax_rate) | **POST** /TaxRates | Allows you to update Tax Rates
[**update_tracking_category**](AccountingApi.md#update_tracking_category) | **POST** /TrackingCategories/{TrackingCategoryID} | Allows you to update tracking categories
[**update_tracking_options**](AccountingApi.md#update_tracking_options) | **POST** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Allows you to update options for a specified tracking category


# **create_account**
> Accounts create_account(xero_tenant_id, account)

Allows you to create a new chart of accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account = { code: "123456", name: "Foobar", type: AccountType.EXPENSE, description: "Hello World" } # Account | Account object in body of request
try:
    # Allows you to create a new chart of accounts
    api_response = api_instance.create_account(xero_tenant_id, account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account** | [**Account**](Account.md)| Account object in body of request | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_attachment_by_file_name**
> Attachments create_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, body)

Allows you to create Attachment on Account

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Account object
file_name = 'xero-dev.jpg' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to create Attachment on Account
    api_response = api_instance.create_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transaction_attachment_by_file_name**
> Attachments create_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, body)

Allows you to createa an Attachment on BankTransaction by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
file_name = 'xero-dev.jpg' # str | The name of the file being attached
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to createa an Attachment on BankTransaction by Filename
    api_response = api_instance.create_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transaction_history_record**
> HistoryRecords create_bank_transaction_history_record(xero_tenant_id, bank_transaction_id, history_records)

Allows you to create history record for a bank transactions

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create history record for a bank transactions
    api_response = api_instance.create_bank_transaction_history_record(xero_tenant_id, bank_transaction_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transaction_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transactions**
> BankTransactions create_bank_transactions(xero_tenant_id, bank_transactions, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to create one or more spend or receive money transaction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transactions = { bankTransactions:[ { type: BankTransaction.TypeEnum.SPEND, contact: { contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity: 1.0, unitAmount:20.0, accountCode:"000" } ], bankAccount:{ code:"000" } } ] } # BankTransactions | BankTransactions with an array of BankTransaction objects in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to create one or more spend or receive money transaction
    api_response = api_instance.create_bank_transactions(xero_tenant_id, bank_transactions, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transactions** | [**BankTransactions**](BankTransactions.md)| BankTransactions with an array of BankTransaction objects in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer**
> BankTransfers create_bank_transfer(xero_tenant_id, bank_transfers)

Allows you to create a bank transfers

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfers = { bankTransfers:[ { fromBankAccount: { code:"000", accountID:"00000000-0000-0000-000-000000000000"}, toBankAccount:{ code:"001", accountID:"00000000-0000-0000-000-000000000000"}, amount:"50.00" } ] } # BankTransfers | BankTransfers with array of BankTransfer objects in request body
try:
    # Allows you to create a bank transfers
    api_response = api_instance.create_bank_transfer(xero_tenant_id, bank_transfers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfers** | [**BankTransfers**](BankTransfers.md)| BankTransfers with array of BankTransfer objects in request body | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer_attachment_by_file_name**
> Attachments create_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, body)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Bank Transfer
body = 'body_example' # str | Byte array of file in body of request
try:
    api_response = api_instance.create_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer_history_record**
> HistoryRecords create_bank_transfer_history_record(xero_tenant_id, bank_transfer_id, history_records)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    api_response = api_instance.create_bank_transfer_history_record(xero_tenant_id, bank_transfer_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_payment**
> BatchPayments create_batch_payment(xero_tenant_id, batch_payments, summarize_errors=summarize_errors)

Create one or many BatchPayments for invoices

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
batch_payments = { batchPayments: [ { account: { accountID: "00000000-0000-0000-000-000000000000" }, reference: "ref", date: "2018-08-01", payments: [ { account: { code: "001" }, date: "2019-12-31", amount: 500, invoice: { invoiceID: "00000000-0000-0000-000-000000000000", lineItems: [], contact: {}, type: Invoice.TypeEnum.ACCPAY } } ] } ] } # BatchPayments | BatchPayments with an array of Payments in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Create one or many BatchPayments for invoices
    api_response = api_instance.create_batch_payment(xero_tenant_id, batch_payments, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_batch_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **batch_payments** | [**BatchPayments**](BatchPayments.md)| BatchPayments with an array of Payments in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_payment_history_record**
> HistoryRecords create_batch_payment_history_record(xero_tenant_id, batch_payment_id, history_records)

Allows you to create a history record for a Batch Payment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
batch_payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for BatchPayment
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create a history record for a Batch Payment
    api_response = api_instance.create_batch_payment_history_record(xero_tenant_id, batch_payment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_batch_payment_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **batch_payment_id** | [**str**](.md)| Unique identifier for BatchPayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_branding_theme_payment_services**
> PaymentServices create_branding_theme_payment_services(xero_tenant_id, branding_theme_id, payment_service)

Allow for the creation of new custom payment service for specified Branding Theme

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
branding_theme_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Branding Theme
payment_service = { paymentServiceID:"dede7858-14e3-4a46-bf95-4d4cc491e645", paymentServiceName:"ACME Payments", paymentServiceUrl:"https://www.payupnow.com/", payNowText:"Pay Now" } # PaymentService | PaymentService object in body of request
try:
    # Allow for the creation of new custom payment service for specified Branding Theme
    api_response = api_instance.create_branding_theme_payment_services(xero_tenant_id, branding_theme_id, payment_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_branding_theme_payment_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 
 **payment_service** | [**PaymentService**](PaymentService.md)| PaymentService object in body of request | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_attachment_by_file_name**
> Attachments create_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, body)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
file_name = 'xero-dev.jpg' # str | Name for the file you are attaching
body = 'body_example' # str | Byte array of file in body of request
try:
    api_response = api_instance.create_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_group**
> ContactGroups create_contact_group(xero_tenant_id, contact_groups)

Allows you to create a contact group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_groups = { contactGroups:[ { name:"VIPs" } ] } # ContactGroups | ContactGroups with an array of names in request body
try:
    # Allows you to create a contact group
    api_response = api_instance.create_contact_group(xero_tenant_id, contact_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_groups** | [**ContactGroups**](ContactGroups.md)| ContactGroups with an array of names in request body | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_group_contacts**
> Contacts create_contact_group_contacts(xero_tenant_id, contact_group_id, contacts)

Allows you to add Contacts to a Contact Group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_group_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact Group
contacts = { contacts:[ { contactID:"a3675fc4-f8dd-4f03-ba5b-f1870566bcd7" }, { contactID:"4e1753b9-018a-4775-b6aa-1bc7871cfee3" } ] } # Contacts | Contacts with array of contacts specifiying the ContactID to be added to ContactGroup in body of request
try:
    # Allows you to add Contacts to a Contact Group
    api_response = api_instance.create_contact_group_contacts(xero_tenant_id, contact_group_id, contacts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_group_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contacts** | [**Contacts**](Contacts.md)| Contacts with array of contacts specifiying the ContactID to be added to ContactGroup in body of request | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_history**
> HistoryRecords create_contact_history(xero_tenant_id, contact_id, history_records)

Allows you to retrieve a history records of an Contact

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to retrieve a history records of an Contact
    api_response = api_instance.create_contact_history(xero_tenant_id, contact_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contacts**
> Contacts create_contacts(xero_tenant_id, contacts, summarize_errors=summarize_errors)

Allows you to create a multiple contacts (bulk) in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contacts = {contacts: [{ name:"Bruce Banner", emailAddress:"hulk@avengers.com", phones:[ { phoneType: Phone.PhoneTypeEnum.MOBILE, phoneNumber:"555-1212", phoneAreaCode:"415" } ], paymentTerms:{ bills:{ day:15, type: PaymentTermType.OFCURRENTMONTH }, sales:{ day:10, type: PaymentTermType.DAYSAFTERBILLMONTH } } } ] } # Contacts | Contacts with an array of Contact objects to create in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create a multiple contacts (bulk) in a Xero organisation
    api_response = api_instance.create_contacts(xero_tenant_id, contacts, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contacts** | [**Contacts**](Contacts.md)| Contacts with an array of Contact objects to create in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_allocation**
> Allocations create_credit_note_allocation(xero_tenant_id, credit_note_id, allocations)

Allows you to create Allocation on CreditNote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
allocations = { allocations:[ { amount:1.0, date:"2019-03-05", invoice:{ invoiceID:"c45720a1-ade3-4a38-a064-d15489be6841", lineItems:[], type: Invoice.TypeEnum.ACCPAY, contact:{} } } ] } # Allocations | Allocations with array of Allocation object in body of request.
try:
    # Allows you to create Allocation on CreditNote
    api_response = api_instance.create_credit_note_allocation(xero_tenant_id, credit_note_id, allocations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations with array of Allocation object in body of request. | 

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_attachment_by_file_name**
> Attachments create_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, body, include_online=include_online)

Allows you to create Attachments on CreditNote by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching to Credit Note
body = 'body_example' # str | Byte array of file in body of request
include_online = False # bool | Allows an attachment to be seen by the end customer within their online invoice (optional) (default to False)
try:
    # Allows you to create Attachments on CreditNote by file name
    api_response = api_instance.create_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, body, include_online=include_online)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **body** | **str**| Byte array of file in body of request | 
 **include_online** | **bool**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to False]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_history**
> HistoryRecords create_credit_note_history(xero_tenant_id, credit_note_id, history_records)

Allows you to retrieve a history records of an CreditNote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to retrieve a history records of an CreditNote
    api_response = api_instance.create_credit_note_history(xero_tenant_id, credit_note_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_notes**
> CreditNotes create_credit_notes(xero_tenant_id, credit_notes, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to create a credit note

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_notes = { creditNotes:[ { type: CreditNote.TypeEnum.ACCPAYCREDIT, contact:{ contactID:"430fa14a-f945-44d3-9f97-5df5e28441b8" }, date:"2019-01-05", lineItems:[ { description:"Foobar", quantity:2.0, unitAmount:20.0, accountCode:"400" } ] } ] } # CreditNotes | Credit Notes with array of CreditNote object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to create a credit note
    api_response = api_instance.create_credit_notes(xero_tenant_id, credit_notes, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_notes** | [**CreditNotes**](CreditNotes.md)| Credit Notes with array of CreditNote object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_currency**
> Currencies create_currency(xero_tenant_id, currency)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
currency = { code: CurrencyCode.USD, description:"United States Dollar" } # Currency | Currency obejct in the body of request
try:
    api_response = api_instance.create_currency(xero_tenant_id, currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **currency** | [**Currency**](Currency.md)| Currency obejct in the body of request | 

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employees**
> Employees create_employees(xero_tenant_id, employees, summarize_errors=summarize_errors)

Allows you to create new employees used in Xero payrun

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
employees = { employees:[ { firstName:"Nick", lastName:"Fury", externalLink:{ url:"http://twitter.com/#!/search/Nick+Fury" } } ] } # Employees | Employees with array of Employee object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create new employees used in Xero payrun
    api_response = api_instance.create_employees(xero_tenant_id, employees, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_expense_claim_history**
> HistoryRecords create_expense_claim_history(xero_tenant_id, expense_claim_id, history_records)

Allows you to create a history records of an ExpenseClaim

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
expense_claim_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ExpenseClaim
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create a history records of an ExpenseClaim
    api_response = api_instance.create_expense_claim_history(xero_tenant_id, expense_claim_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_expense_claim_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_expense_claims**
> ExpenseClaims create_expense_claims(xero_tenant_id, expense_claims)

Allows you to retrieve expense claims

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
expense_claims = { expenseClaims:[ { status: ExpenseClaim.StatusEnum.SUBMITTED, user:{ userID:"d1164823-0ac1-41ad-987b-b4e30fe0b273" }, receipts:[ { receiptID:"dc1c7f6d-0a4c-402f-acac-551d62ce5816", lineItems:[], contact: {}, user: {}, date: "2018-01-01" } ] } ] } # ExpenseClaims | ExpenseClaims with array of ExpenseClaim object in body of request
try:
    # Allows you to retrieve expense claims
    api_response = api_instance.create_expense_claims(xero_tenant_id, expense_claims)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_expense_claims: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **expense_claims** | [**ExpenseClaims**](ExpenseClaims.md)| ExpenseClaims with array of ExpenseClaim object in body of request | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_attachment_by_file_name**
> Attachments create_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, body, include_online=include_online)

Allows you to create an Attachment on invoices or purchase bills by it's filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching
body = 'body_example' # str | Byte array of file in body of request
include_online = False # bool | Allows an attachment to be seen by the end customer within their online invoice (optional) (default to False)
try:
    # Allows you to create an Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.create_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, body, include_online=include_online)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 
 **include_online** | **bool**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to False]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_history**
> HistoryRecords create_invoice_history(xero_tenant_id, invoice_id, history_records)

Allows you to retrieve a history records of an invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to retrieve a history records of an invoice
    api_response = api_instance.create_invoice_history(xero_tenant_id, invoice_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoices**
> Invoices create_invoices(xero_tenant_id, invoices, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to create one or more sales invoices or purchase bills

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoices = { invoices:[ { type: Invoice.TypeEnum.ACCREC, contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Acme Tires", quantity:2.0, unitAmount:20.0, accountCode:"000", taxType:"NONE", lineAmount:40.0 } ], date:"2019-03-11", dueDate:"2018-12-10", reference:"Website Design", status: Invoice.StatusEnum.DRAFT } ] } # Invoices | Invoices with an array of invoice objects in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to create one or more sales invoices or purchase bills
    api_response = api_instance.create_invoices(xero_tenant_id, invoices, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoices** | [**Invoices**](Invoices.md)| Invoices with an array of invoice objects in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_history**
> HistoryRecords create_item_history(xero_tenant_id, item_id, history_records)

Allows you to create a history record for items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
item_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Item
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create a history record for items
    api_response = api_instance.create_item_history(xero_tenant_id, item_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_item_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **item_id** | [**str**](.md)| Unique identifier for an Item | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_items**
> Items create_items(xero_tenant_id, items, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to create one or more items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
items = { items:[ { code:"abcXYZ123", name:"HelloWorld11", description:"Foobar", inventoryAssetAccountCode:"140", purchaseDetails: {cOGSAccountCode:"500"} } ] } # Items | Items with an array of Item objects in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to create one or more items
    api_response = api_instance.create_items(xero_tenant_id, items, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **items** | [**Items**](Items.md)| Items with an array of Item objects in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_linked_transaction**
> LinkedTransactions create_linked_transaction(xero_tenant_id, linked_transaction)

Allows you to create linked transactions (billable expenses)

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
linked_transaction = { sourceTransactionID:"00000000-0000-0000-000-000000000000", sourceLineItemID:"00000000-0000-0000-000-000000000000"} # LinkedTransaction | LinkedTransaction object in body of request
try:
    # Allows you to create linked transactions (billable expenses)
    api_response = api_instance.create_linked_transaction(xero_tenant_id, linked_transaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **linked_transaction** | [**LinkedTransaction**](LinkedTransaction.md)| LinkedTransaction object in body of request | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_journal_attachment_by_file_name**
> Attachments create_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, body)

Allows you to create a specified Attachment on ManualJournal by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a ManualJournal
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to create a specified Attachment on ManualJournal by file name
    api_response = api_instance.create_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_journals**
> ManualJournals create_manual_journals(xero_tenant_id, manual_journals, summarize_errors=summarize_errors)

Allows you to create one or more manual journals

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journals = { manualJournals:[ { narration:"Foo bar", journalLines:[ { lineAmount:100.0, accountCode:"400", description:"Hello there" }, { lineAmount:-100.0, accountCode:"400", description:"Goodbye", tracking:[ { name:"Simpsons", option:"Bart" } ] } ], date:"2019-03-14" } ] } # ManualJournals | ManualJournals array with ManualJournal object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create one or more manual journals
    api_response = api_instance.create_manual_journals(xero_tenant_id, manual_journals, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_manual_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_overpayment_allocations**
> Allocations create_overpayment_allocations(xero_tenant_id, overpayment_id, allocations, summarize_errors=summarize_errors)

Allows you to create a single allocation for an overpayment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
overpayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Overpayment
allocations = { allocations:[ { invoice:{ invoiceID:"00000000-0000-0000-000-000000000000", lineItems:[], contact: {}, type: Invoice.TypeEnum.ACCPAY }, amount:1.0, date:"2019-03-12" } ] } # Allocations | Allocations array with Allocation object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create a single allocation for an overpayment
    api_response = api_instance.create_overpayment_allocations(xero_tenant_id, overpayment_id, allocations, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_overpayment_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations array with Allocation object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_overpayment_history**
> HistoryRecords create_overpayment_history(xero_tenant_id, overpayment_id, history_records)

Allows you to create history records of an Overpayment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
overpayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Overpayment
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create history records of an Overpayment
    api_response = api_instance.create_overpayment_history(xero_tenant_id, overpayment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_overpayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment**
> Payments create_payment(xero_tenant_id, payment)

Allows you to create a single payment for invoices or credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment = { invoice:{ invoiceID:"00000000-0000-0000-000-000000000000", lineItems:[], contact: {}, type: Invoice.TypeEnum.ACCPAY }, account:{ code:"970" }, date:"2019-03-12", amount:1.0 } # Payment | Request body with a single Payment object
try:
    # Allows you to create a single payment for invoices or credit notes
    api_response = api_instance.create_payment(xero_tenant_id, payment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment** | [**Payment**](Payment.md)| Request body with a single Payment object | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_history**
> HistoryRecords create_payment_history(xero_tenant_id, payment_id, history_records)

Allows you to create a history record for a payment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Payment
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create a history record for a payment
    api_response = api_instance.create_payment_history(xero_tenant_id, payment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_service**
> PaymentServices create_payment_service(xero_tenant_id, payment_services)

Allows you to create payment services

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment_services = { paymentServices:[ { paymentServiceName:"PayUpNow", paymentServiceUrl:"https://www.payupnow.com/", payNowText:"Time To Pay" } ] } # PaymentServices | PaymentServices array with PaymentService object in body of request
try:
    # Allows you to create payment services
    api_response = api_instance.create_payment_service(xero_tenant_id, payment_services)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment_services** | [**PaymentServices**](PaymentServices.md)| PaymentServices array with PaymentService object in body of request | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payments**
> Payments create_payments(xero_tenant_id, payments, summarize_errors=summarize_errors)

Allows you to create multiple payments for invoices or credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payments = { payments:[ { invoice:{ invoiceID:"00000000-0000-0000-000-000000000000", lineItems:[], contact: {}, type: Invoice.TypeEnum.ACCPAY }, account:{ code:"970" }, date:"2019-03-12", amount:1.0 } ] } # Payments | Payments array with Payment object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create multiple payments for invoices or credit notes
    api_response = api_instance.create_payments(xero_tenant_id, payments, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payments** | [**Payments**](Payments.md)| Payments array with Payment object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prepayment_allocations**
> Allocations create_prepayment_allocations(xero_tenant_id, prepayment_id, allocations, summarize_errors=summarize_errors)

Allows you to create an Allocation for prepayments

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
prepayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Prepayment
allocations = { allocations:[ { invoice:{ invoiceID:"00000000-0000-0000-000-000000000000", lineItems:[], contact: {}, type: null }, amount:1.0, date:"2019-03-13" } ] } # Allocations | Allocations with an array of Allocation object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create an Allocation for prepayments
    api_response = api_instance.create_prepayment_allocations(xero_tenant_id, prepayment_id, allocations, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_prepayment_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **prepayment_id** | [**str**](.md)| Unique identifier for Prepayment | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations with an array of Allocation object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prepayment_history**
> HistoryRecords create_prepayment_history(xero_tenant_id, prepayment_id, history_records)

Allows you to create a history record for an Prepayment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
prepayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PrePayment
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create a history record for an Prepayment
    api_response = api_instance.create_prepayment_history(xero_tenant_id, prepayment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_prepayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_purchase_order_history**
> HistoryRecords create_purchase_order_history(xero_tenant_id, purchase_order_id, history_records)

Allows you to create HistoryRecord for purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PurchaseOrder
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create HistoryRecord for purchase orders
    api_response = api_instance.create_purchase_order_history(xero_tenant_id, purchase_order_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_purchase_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_purchase_orders**
> PurchaseOrders create_purchase_orders(xero_tenant_id, purchase_orders, summarize_errors=summarize_errors)

Allows you to create one or more purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_orders = { purchaseOrders:[ { contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity:1.0, unitAmount:20.0, accountCode:"710" } ], date:"2019-03-13" } ] } # PurchaseOrders | PurchaseOrders with an array of PurchaseOrder object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create one or more purchase orders
    api_response = api_instance.create_purchase_orders(xero_tenant_id, purchase_orders, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_orders** | [**PurchaseOrders**](PurchaseOrders.md)| PurchaseOrders with an array of PurchaseOrder object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote_attachment_by_file_name**
> Attachments create_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, body)

Allows you to create Attachment on Quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Quote object
file_name = 'xero-dev.jpg' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to create Attachment on Quote
    api_response = api_instance.create_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_quote_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for Quote object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote_history**
> HistoryRecords create_quote_history(xero_tenant_id, quote_id, history_records)

Allows you to retrieve a history records of an quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Quote
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to retrieve a history records of an quote
    api_response = api_instance.create_quote_history(xero_tenant_id, quote_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_quote_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for an Quote | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quotes**
> Quotes create_quotes(xero_tenant_id, quotes, summarize_errors=summarize_errors)

Allows you to create one or more quotes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quotes = { quotes:[ { contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity:1.0, unitAmount:20.0, accountCode:"12775" } ], date:"2020-02-01" } ] } # Quotes | Quotes with an array of Quote object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create one or more quotes
    api_response = api_instance.create_quotes(xero_tenant_id, quotes, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quotes** | [**Quotes**](Quotes.md)| Quotes with an array of Quote object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt**
> Receipts create_receipt(xero_tenant_id, receipts, unitdp=unitdp)

Allows you to create draft expense claim receipts for any user

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipts = { receipts:[ { contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity:2.0, unitAmount:20.0, accountCode:"400", taxType:"NONE", lineAmount:40.0 } ], user:{ userID:"00000000-0000-0000-000-000000000000" }, lineAmountTypes: LineAmountTypes.Inclusive, status: Receipt.StatusEnum.DRAFT , date: null} ] } # Receipts | Receipts with an array of Receipt object in body of request
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to create draft expense claim receipts for any user
    api_response = api_instance.create_receipt(xero_tenant_id, receipts, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipts** | [**Receipts**](Receipts.md)| Receipts with an array of Receipt object in body of request | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt_attachment_by_file_name**
> Attachments create_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, body)

Allows you to create Attachment on expense claim receipts by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
file_name = 'xero-dev.jpg' # str | The name of the file being attached to the Receipt
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to create Attachment on expense claim receipts by file name
    api_response = api_instance.create_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt_history**
> HistoryRecords create_receipt_history(xero_tenant_id, receipt_id, history_records)

Allows you to retrieve a history records of an Receipt

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to retrieve a history records of an Receipt
    api_response = api_instance.create_receipt_history(xero_tenant_id, receipt_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repeating_invoice_attachment_by_file_name**
> Attachments create_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, body)

Allows you to create attachment on repeating invoices by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Repeating Invoice
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to create attachment on repeating invoices by file name
    api_response = api_instance.create_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repeating_invoice_history**
> HistoryRecords create_repeating_invoice_history(xero_tenant_id, repeating_invoice_id, history_records)

Allows you to create history for a repeating invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
history_records = { historyRecords:[ { details :"Hello World" } ] } # HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
try:
    # Allows you to create history for a repeating invoice
    api_response = api_instance.create_repeating_invoice_history(xero_tenant_id, repeating_invoice_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_repeating_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tax_rates**
> TaxRates create_tax_rates(xero_tenant_id, tax_rates)

Allows you to create one or more Tax Rates

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tax_rates = { taxRates:[ { name:"CA State Tax", taxComponents:[ { name:"State Tax", rate:2.25 } ] } ] } # TaxRates | TaxRates array with TaxRate object in body of request
try:
    # Allows you to create one or more Tax Rates
    api_response = api_instance.create_tax_rates(xero_tenant_id, tax_rates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tax_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tax_rates** | [**TaxRates**](TaxRates.md)| TaxRates array with TaxRate object in body of request | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracking_category**
> TrackingCategories create_tracking_category(xero_tenant_id, tracking_category)

Allows you to create tracking categories

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category = { name:"FooBar" } # TrackingCategory | TrackingCategory object in body of request
try:
    # Allows you to create tracking categories
    api_response = api_instance.create_tracking_category(xero_tenant_id, tracking_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category** | [**TrackingCategory**](TrackingCategory.md)| TrackingCategory object in body of request | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracking_options**
> TrackingOptions create_tracking_options(xero_tenant_id, tracking_category_id, tracking_option)

Allows you to create options for a specified tracking category

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
tracking_option = { name:"Bar" } # TrackingOption | TrackingOption object in body of request
try:
    # Allows you to create options for a specified tracking category
    api_response = api_instance.create_tracking_options(xero_tenant_id, tracking_category_id, tracking_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tracking_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_option** | [**TrackingOption**](TrackingOption.md)| TrackingOption object in body of request | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> Accounts delete_account(xero_tenant_id, account_id)

Allows you to delete a chart of accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for retrieving single object
try:
    # Allows you to delete a chart of accounts
    api_response = api_instance.delete_account(xero_tenant_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_group_contact**
> delete_contact_group_contact(xero_tenant_id, contact_group_id, contact_id)

Allows you to delete a specific Contact from a Contact Group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_group_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact Group
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
try:
    # Allows you to delete a specific Contact from a Contact Group
    api_instance.delete_contact_group_contact(xero_tenant_id, contact_group_id, contact_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_contact_group_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_group_contacts**
> delete_contact_group_contacts(xero_tenant_id, contact_group_id)

Allows you to delete  all Contacts from a Contact Group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_group_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact Group
try:
    # Allows you to delete  all Contacts from a Contact Group
    api_instance.delete_contact_group_contacts(xero_tenant_id, contact_group_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_contact_group_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(xero_tenant_id, item_id)

Allows you to delete a specified item

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
item_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Item
try:
    # Allows you to delete a specified item
    api_instance.delete_item(xero_tenant_id, item_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **item_id** | [**str**](.md)| Unique identifier for an Item | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_transaction**
> delete_linked_transaction(xero_tenant_id, linked_transaction_id)

Allows you to delete a specified linked transactions (billable expenses)

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
linked_transaction_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a LinkedTransaction
try:
    # Allows you to delete a specified linked transactions (billable expenses)
    api_instance.delete_linked_transaction(xero_tenant_id, linked_transaction_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment**
> Payments delete_payment(xero_tenant_id, payment_id, payment_delete)

Allows you to update a specified payment for invoices and credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Payment
payment_delete = { status:"DELETED" } # PaymentDelete | 
try:
    # Allows you to update a specified payment for invoices and credit notes
    api_response = api_instance.delete_payment(xero_tenant_id, payment_id, payment_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 
 **payment_delete** | [**PaymentDelete**](PaymentDelete.md)|  | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracking_category**
> TrackingCategories delete_tracking_category(xero_tenant_id, tracking_category_id)

Allows you to delete tracking categories

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
try:
    # Allows you to delete tracking categories
    api_response = api_instance.delete_tracking_category(xero_tenant_id, tracking_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracking_options**
> TrackingOptions delete_tracking_options(xero_tenant_id, tracking_category_id, tracking_option_id)

Allows you to delete a specified option for a specified tracking category

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
tracking_option_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Tracking Option
try:
    # Allows you to delete a specified option for a specified tracking category
    api_response = api_instance.delete_tracking_options(xero_tenant_id, tracking_category_id, tracking_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_tracking_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_option_id** | [**str**](.md)| Unique identifier for a Tracking Option | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_invoice**
> email_invoice(xero_tenant_id, invoice_id, request_empty)

Allows you to email a copy of invoice to related Contact

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
request_empty = {} # RequestEmpty | 
try:
    # Allows you to email a copy of invoice to related Contact
    api_instance.email_invoice(xero_tenant_id, invoice_id, request_empty)
except ApiException as e:
    print("Exception when calling AccountingApi->email_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **request_empty** | [**RequestEmpty**](RequestEmpty.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Accounts get_account(xero_tenant_id, account_id)

Allows you to retrieve a single chart of accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for retrieving single object
try:
    # Allows you to retrieve a single chart of accounts
    api_response = api_instance.get_account(xero_tenant_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachment_by_file_name**
> file get_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, content_type)

Allows you to retrieve Attachment on Account by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Account object
file_name = 'xero-dev.jpg' # str | Name of the attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachment on Account by Filename
    api_response = api_instance.get_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachment_by_id**
> file get_account_attachment_by_id(xero_tenant_id, account_id, attachment_id, content_type)

Allows you to retrieve specific Attachment on Account

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Account object
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Attachment object
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve specific Attachment on Account
    api_response = api_instance.get_account_attachment_by_id(xero_tenant_id, account_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **attachment_id** | [**str**](.md)| Unique identifier for Attachment object | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachments**
> Attachments get_account_attachments(xero_tenant_id, account_id)

Allows you to retrieve Attachments for accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Account object
try:
    # Allows you to retrieve Attachments for accounts
    api_response = api_instance.get_account_attachments(xero_tenant_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for Account object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> Accounts get_accounts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve the full chart of accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Account.StatusEnum.ACTIVE + '\" AND Type==\"' + Account.BankAccountTypeEnum.BANK + '\"' # str | Filter by an any element (optional)
order = 'Name ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve the full chart of accounts
    api_response = api_instance.get_accounts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction**
> BankTransactions get_bank_transaction(xero_tenant_id, bank_transaction_id, unitdp=unitdp)

Allows you to retrieve a single spend or receive money transaction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a single spend or receive money transaction
    api_response = api_instance.get_bank_transaction(xero_tenant_id, bank_transaction_id, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachment_by_file_name**
> file get_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, content_type)

Allows you to retrieve Attachments on BankTransaction by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
file_name = 'xero-dev.jpg' # str | The name of the file being attached
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on BankTransaction by Filename
    api_response = api_instance.get_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachment_by_id**
> file get_bank_transaction_attachment_by_id(xero_tenant_id, bank_transaction_id, attachment_id, content_type)

Allows you to retrieve Attachments on a specific BankTransaction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
attachment_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for an attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on a specific BankTransaction
    api_response = api_instance.get_bank_transaction_attachment_by_id(xero_tenant_id, bank_transaction_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **attachment_id** | [**str**](.md)| Xero generated unique identifier for an attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachments**
> Attachments get_bank_transaction_attachments(xero_tenant_id, bank_transaction_id)

Allows you to retrieve any attachments to bank transactions

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
try:
    # Allows you to retrieve any attachments to bank transactions
    api_response = api_instance.get_bank_transaction_attachments(xero_tenant_id, bank_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transactions**
> BankTransactions get_bank_transactions(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve any spend or receive money transactions

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + BankTransaction.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Type ASC' # str | Order by an any element (optional)
page = 1 # int | Up to 100 bank transactions will be returned in a single API call with line items details (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve any spend or receive money transactions
    api_response = api_instance.get_bank_transactions(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| Up to 100 bank transactions will be returned in a single API call with line items details | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transactions_history**
> HistoryRecords get_bank_transactions_history(xero_tenant_id, bank_transaction_id)

Allows you to retrieve history from a bank transactions

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
try:
    # Allows you to retrieve history from a bank transactions
    api_response = api_instance.get_bank_transactions_history(xero_tenant_id, bank_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transactions_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer**
> BankTransfers get_bank_transfer(xero_tenant_id, bank_transfer_id)

Allows you to retrieve any bank transfers

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
try:
    # Allows you to retrieve any bank transfers
    api_response = api_instance.get_bank_transfer(xero_tenant_id, bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachment_by_file_name**
> file get_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, content_type)

Allows you to retrieve Attachments on BankTransfer by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Bank Transfer
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on BankTransfer by file name
    api_response = api_instance.get_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachment_by_id**
> file get_bank_transfer_attachment_by_id(xero_tenant_id, bank_transfer_id, attachment_id, content_type)

Allows you to retrieve Attachments on BankTransfer

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
attachment_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for an Attachment to a bank transfer
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on BankTransfer
    api_response = api_instance.get_bank_transfer_attachment_by_id(xero_tenant_id, bank_transfer_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **attachment_id** | [**str**](.md)| Xero generated unique identifier for an Attachment to a bank transfer | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachments**
> Attachments get_bank_transfer_attachments(xero_tenant_id, bank_transfer_id)

Allows you to retrieve Attachments from  bank transfers

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
try:
    # Allows you to retrieve Attachments from  bank transfers
    api_response = api_instance.get_bank_transfer_attachments(xero_tenant_id, bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_history**
> HistoryRecords get_bank_transfer_history(xero_tenant_id, bank_transfer_id)

Allows you to retrieve history from a bank transfers

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
try:
    # Allows you to retrieve history from a bank transfers
    api_response = api_instance.get_bank_transfer_history(xero_tenant_id, bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfers**
> BankTransfers get_bank_transfers(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve all bank transfers

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + BankTransfer.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Amount ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve all bank transfers
    api_response = api_instance.get_bank_transfers(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_payment_history**
> HistoryRecords get_batch_payment_history(xero_tenant_id, batch_payment_id)

Allows you to retrieve history from a Batch Payment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
batch_payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for BatchPayment
try:
    # Allows you to retrieve history from a Batch Payment
    api_response = api_instance.get_batch_payment_history(xero_tenant_id, batch_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_batch_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **batch_payment_id** | [**str**](.md)| Unique identifier for BatchPayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_payments**
> BatchPayments get_batch_payments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Retrieve either one or many BatchPayments for invoices

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + BatchPayment.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Date ASC' # str | Order by an any element (optional)
try:
    # Retrieve either one or many BatchPayments for invoices
    api_response = api_instance.get_batch_payments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_batch_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_theme**
> BrandingThemes get_branding_theme(xero_tenant_id, branding_theme_id)

Allows you to retrieve a specific BrandingThemes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
branding_theme_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Branding Theme
try:
    # Allows you to retrieve a specific BrandingThemes
    api_response = api_instance.get_branding_theme(xero_tenant_id, branding_theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_theme_payment_services**
> PaymentServices get_branding_theme_payment_services(xero_tenant_id, branding_theme_id)

Allows you to retrieve the Payment services for a Branding Theme

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
branding_theme_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Branding Theme
try:
    # Allows you to retrieve the Payment services for a Branding Theme
    api_response = api_instance.get_branding_theme_payment_services(xero_tenant_id, branding_theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_theme_payment_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_themes**
> BrandingThemes get_branding_themes(xero_tenant_id)

Allows you to retrieve all the BrandingThemes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # Allows you to retrieve all the BrandingThemes
    api_response = api_instance.get_branding_themes(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_themes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contacts get_contact(xero_tenant_id, contact_id)

Allows you to retrieve a single contacts in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
try:
    # Allows you to retrieve a single contacts in a Xero organisation
    api_response = api_instance.get_contact(xero_tenant_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachment_by_file_name**
> file get_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, content_type)

Allows you to retrieve Attachments on Contacts by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
file_name = 'xero-dev.jpg' # str | Name for the file you are attaching
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on Contacts by file name
    api_response = api_instance.get_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachment_by_id**
> file get_contact_attachment_by_id(xero_tenant_id, contact_id, attachment_id, content_type)

Allows you to retrieve Attachments on Contacts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on Contacts
    api_response = api_instance.get_contact_attachment_by_id(xero_tenant_id, contact_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachments**
> Attachments get_contact_attachments(xero_tenant_id, contact_id)

Allows you to retrieve, add and update contacts in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
try:
    # Allows you to retrieve, add and update contacts in a Xero organisation
    api_response = api_instance.get_contact_attachments(xero_tenant_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_contact_number**
> Contacts get_contact_by_contact_number(xero_tenant_id, contact_number)

Allows you to retrieve a single contact by Contact Number in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_number = 'SB2' # str | This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50).
try:
    # Allows you to retrieve a single contact by Contact Number in a Xero organisation
    api_response = api_instance.get_contact_by_contact_number(xero_tenant_id, contact_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_by_contact_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_number** | **str**| This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_cis_settings**
> CISSettings get_contact_cis_settings(xero_tenant_id, contact_id)

Allows you to retrieve CISSettings for a contact in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
try:
    # Allows you to retrieve CISSettings for a contact in a Xero organisation
    api_response = api_instance.get_contact_cis_settings(xero_tenant_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_cis_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**CISSettings**](CISSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_group**
> ContactGroups get_contact_group(xero_tenant_id, contact_group_id)

Allows you to retrieve a unique Contact Group by ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_group_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact Group
try:
    # Allows you to retrieve a unique Contact Group by ID
    api_response = api_instance.get_contact_group(xero_tenant_id, contact_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_groups**
> ContactGroups get_contact_groups(xero_tenant_id, where=where, order=order)

Allows you to retrieve the ContactID and Name of all the contacts in a contact group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
where = 'Status==\"' + ContactGroup.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Name ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve the ContactID and Name of all the contacts in a contact group
    api_response = api_instance.get_contact_groups(xero_tenant_id, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_history**
> HistoryRecords get_contact_history(xero_tenant_id, contact_id)

Allows you to retrieve a history records of an Contact

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
try:
    # Allows you to retrieve a history records of an Contact
    api_response = api_instance.get_contact_history(xero_tenant_id, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> Contacts get_contacts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, page=page, include_archived=include_archived)

Allows you to retrieve all contacts in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Contact.ContactStatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Name ASC' # str | Order by an any element (optional)
i_ds = ['00000000-0000-0000-000-000000000000,00000000-0000-0000-000-000000000000'] # list[str] | Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. (optional)
page = 1 # int | e.g. page=1 - Up to 100 contacts will be returned in a single API call. (optional)
include_archived = True # bool | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response (optional)
try:
    # Allows you to retrieve all contacts in a Xero organisation
    api_response = api_instance.get_contacts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, page=page, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **i_ds** | [**list[str]**](str.md)| Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. | [optional] 
 **page** | **int**| e.g. page&#x3D;1 - Up to 100 contacts will be returned in a single API call. | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note**
> CreditNotes get_credit_note(xero_tenant_id, credit_note_id, unitdp=unitdp)

Allows you to retrieve a specific credit note

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a specific credit note
    api_response = api_instance.get_credit_note(xero_tenant_id, credit_note_id, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_as_pdf**
> file get_credit_note_as_pdf(xero_tenant_id, credit_note_id)

Allows you to retrieve Credit Note as PDF files

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
try:
    # Allows you to retrieve Credit Note as PDF files
    api_response = api_instance.get_credit_note_as_pdf(xero_tenant_id, credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachment_by_file_name**
> file get_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, content_type)

Allows you to retrieve Attachments on CreditNote by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching to Credit Note
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on CreditNote by file name
    api_response = api_instance.get_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachment_by_id**
> file get_credit_note_attachment_by_id(xero_tenant_id, credit_note_id, attachment_id, content_type)

Allows you to retrieve Attachments on CreditNote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on CreditNote
    api_response = api_instance.get_credit_note_attachment_by_id(xero_tenant_id, credit_note_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachments**
> Attachments get_credit_note_attachments(xero_tenant_id, credit_note_id)

Allows you to retrieve Attachments for credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
try:
    # Allows you to retrieve Attachments for credit notes
    api_response = api_instance.get_credit_note_attachments(xero_tenant_id, credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_history**
> HistoryRecords get_credit_note_history(xero_tenant_id, credit_note_id)

Allows you to retrieve a history records of an CreditNote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
try:
    # Allows you to retrieve a history records of an CreditNote
    api_response = api_instance.get_credit_note_history(xero_tenant_id, credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_notes**
> CreditNotes get_credit_notes(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve any credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + CreditNote.StatusEnum.DRAFT + '\"' # str | Filter by an any element (optional)
order = 'CreditNoteNumber ASC' # str | Order by an any element (optional)
page = 1 # int | e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve any credit notes
    api_response = api_instance.get_credit_notes(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> Currencies get_currencies(xero_tenant_id, where=where, order=order)

Allows you to retrieve currencies for your organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
where = 'Status==\"' + Currency.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Code ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve currencies for your organisation
    api_response = api_instance.get_currencies(xero_tenant_id, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> Employees get_employee(xero_tenant_id, employee_id)

Allows you to retrieve a specific employee used in Xero payrun

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
employee_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Employee
try:
    # Allows you to retrieve a specific employee used in Xero payrun
    api_response = api_instance.get_employee(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Unique identifier for a Employee | 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> Employees get_employees(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve employees used in Xero payrun

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Employee.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve employees used in Xero payrun
    api_response = api_instance.get_employees(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claim**
> ExpenseClaims get_expense_claim(xero_tenant_id, expense_claim_id)

Allows you to retrieve a specified expense claim

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
expense_claim_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ExpenseClaim
try:
    # Allows you to retrieve a specified expense claim
    api_response = api_instance.get_expense_claim(xero_tenant_id, expense_claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claim_history**
> HistoryRecords get_expense_claim_history(xero_tenant_id, expense_claim_id)

Allows you to retrieve a history records of an ExpenseClaim

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
expense_claim_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ExpenseClaim
try:
    # Allows you to retrieve a history records of an ExpenseClaim
    api_response = api_instance.get_expense_claim_history(xero_tenant_id, expense_claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claim_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claims**
> ExpenseClaims get_expense_claims(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve expense claims

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + ExpenseClaim.StatusEnum.SUBMITTED + '\"' # str | Filter by an any element (optional)
order = 'Status ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve expense claims
    api_response = api_instance.get_expense_claims(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claims: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> Invoices get_invoice(xero_tenant_id, invoice_id, unitdp=unitdp)

Allows you to retrieve a specified sales invoice or purchase bill

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a specified sales invoice or purchase bill
    api_response = api_instance.get_invoice(xero_tenant_id, invoice_id, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_pdf**
> file get_invoice_as_pdf(xero_tenant_id, invoice_id)

Allows you to retrieve invoices or purchase bills as PDF files

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
try:
    # Allows you to retrieve invoices or purchase bills as PDF files
    api_response = api_instance.get_invoice_as_pdf(xero_tenant_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachment_by_file_name**
> file get_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, content_type)

Allows you to retrieve Attachment on invoices or purchase bills by it's filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.get_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachment_by_id**
> file get_invoice_attachment_by_id(xero_tenant_id, invoice_id, attachment_id, content_type)

Allows you to retrieve a specified Attachment on invoices or purchase bills by it's ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve a specified Attachment on invoices or purchase bills by it's ID
    api_response = api_instance.get_invoice_attachment_by_id(xero_tenant_id, invoice_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **attachment_id** | [**str**](.md)| Unique identifier for an Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachments**
> Attachments get_invoice_attachments(xero_tenant_id, invoice_id)

Allows you to retrieve Attachments on invoices or purchase bills

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
try:
    # Allows you to retrieve Attachments on invoices or purchase bills
    api_response = api_instance.get_invoice_attachments(xero_tenant_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_history**
> HistoryRecords get_invoice_history(xero_tenant_id, invoice_id)

Allows you to retrieve a history records of an invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
try:
    # Allows you to retrieve a history records of an invoice
    api_response = api_instance.get_invoice_history(xero_tenant_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_reminders**
> InvoiceReminders get_invoice_reminders(xero_tenant_id)

Allows you to retrieve invoice reminder settings

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # Allows you to retrieve invoice reminder settings
    api_response = api_instance.get_invoice_reminders(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_reminders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**InvoiceReminders**](InvoiceReminders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> Invoices get_invoices(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, invoice_numbers=invoice_numbers, contact_i_ds=contact_i_ds, statuses=statuses, page=page, include_archived=include_archived, created_by_my_app=created_by_my_app, unitdp=unitdp)

Allows you to retrieve any sales invoices or purchase bills

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Invoice.StatusEnum.DRAFT + '\"' # str | Filter by an any element (optional)
order = 'InvoiceNumber ASC' # str | Order by an any element (optional)
i_ds = ['00000000-0000-0000-000-000000000000,00000000-0000-0000-000-000000000000'] # list[str] | Filter by a comma-separated list of InvoicesIDs. (optional)
invoice_numbers = ['null'] # list[str] | Filter by a comma-separated list of InvoiceNumbers. (optional)
contact_i_ds = ['00000000-0000-0000-000-000000000000,00000000-0000-0000-000-000000000000'] # list[str] | Filter by a comma-separated list of ContactIDs. (optional)
statuses = ['null'] # list[str] | Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. (optional)
page = 1 # int | e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice (optional)
include_archived = True # bool | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response (optional)
created_by_my_app = false # bool | When set to true you'll only retrieve Invoices created by your app (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve any sales invoices or purchase bills
    api_response = api_instance.get_invoices(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, invoice_numbers=invoice_numbers, contact_i_ds=contact_i_ds, statuses=statuses, page=page, include_archived=include_archived, created_by_my_app=created_by_my_app, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **i_ds** | [**list[str]**](str.md)| Filter by a comma-separated list of InvoicesIDs. | [optional] 
 **invoice_numbers** | [**list[str]**](str.md)| Filter by a comma-separated list of InvoiceNumbers. | [optional] 
 **contact_i_ds** | [**list[str]**](str.md)| Filter by a comma-separated list of ContactIDs. | [optional] 
 **statuses** | [**list[str]**](str.md)| Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 
 **created_by_my_app** | **bool**| When set to true you&#39;ll only retrieve Invoices created by your app | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Items get_item(xero_tenant_id, item_id, unitdp=unitdp)

Allows you to retrieve a specified item

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
item_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Item
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a specified item
    api_response = api_instance.get_item(xero_tenant_id, item_id, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **item_id** | [**str**](.md)| Unique identifier for an Item | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_history**
> HistoryRecords get_item_history(xero_tenant_id, item_id)

Allows you to retrieve history for items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
item_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Item
try:
    # Allows you to retrieve history for items
    api_response = api_instance.get_item_history(xero_tenant_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_item_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **item_id** | [**str**](.md)| Unique identifier for an Item | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items**
> Items get_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)

Allows you to retrieve any items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'IsSold==true' # str | Filter by an any element (optional)
order = 'Code ASC' # str | Order by an any element (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve any items
    api_response = api_instance.get_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal**
> Journals get_journal(xero_tenant_id, journal_id)

Allows you to retrieve a specified journals.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Journal
try:
    # Allows you to retrieve a specified journals.
    api_response = api_instance.get_journal(xero_tenant_id, journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **journal_id** | [**str**](.md)| Unique identifier for a Journal | 

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journals**
> Journals get_journals(xero_tenant_id, if_modified_since=if_modified_since, offset=offset, payments_only=payments_only)

Allows you to retrieve any journals.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
offset = 10 # int | Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned (optional)
payments_only = True # bool | Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. (optional)
try:
    # Allows you to retrieve any journals.
    api_response = api_instance.get_journals(xero_tenant_id, if_modified_since=if_modified_since, offset=offset, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **offset** | **int**| Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned | [optional] 
 **payments_only** | **bool**| Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. | [optional] 

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_transaction**
> LinkedTransactions get_linked_transaction(xero_tenant_id, linked_transaction_id)

Allows you to retrieve a specified linked transactions (billable expenses)

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
linked_transaction_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a LinkedTransaction
try:
    # Allows you to retrieve a specified linked transactions (billable expenses)
    api_response = api_instance.get_linked_transaction(xero_tenant_id, linked_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_transactions**
> LinkedTransactions get_linked_transactions(xero_tenant_id, page=page, linked_transaction_id=linked_transaction_id, source_transaction_id=source_transaction_id, contact_id=contact_id, status=status, target_transaction_id=target_transaction_id)

Retrieve linked transactions (billable expenses)

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
page = 1 # int | Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1. (optional)
linked_transaction_id = '00000000-0000-0000-000-000000000000' # str | The Xero identifier for an Linked Transaction (optional)
source_transaction_id = '00000000-0000-0000-000-000000000000' # str | Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice (optional)
contact_id = '00000000-0000-0000-000-000000000000' # str | Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. (optional)
status = 'APPROVED' # str | Filter by the combination of ContactID and Status. Get  the linked transactions associaed to a  customer and with a status (optional)
target_transaction_id = '00000000-0000-0000-000-000000000000' # str | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice (optional)
try:
    # Retrieve linked transactions (billable expenses)
    api_response = api_instance.get_linked_transactions(xero_tenant_id, page=page, linked_transaction_id=linked_transaction_id, source_transaction_id=source_transaction_id, contact_id=contact_id, status=status, target_transaction_id=target_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_linked_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page&#x3D;1. | [optional] 
 **linked_transaction_id** | **str**| The Xero identifier for an Linked Transaction | [optional] 
 **source_transaction_id** | **str**| Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice | [optional] 
 **contact_id** | **str**| Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. | [optional] 
 **status** | **str**| Filter by the combination of ContactID and Status. Get  the linked transactions associaed to a  customer and with a status | [optional] 
 **target_transaction_id** | **str**| Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice | [optional] 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal**
> ManualJournals get_manual_journal(xero_tenant_id, manual_journal_id)

Allows you to retrieve a specified manual journals

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
try:
    # Allows you to retrieve a specified manual journals
    api_response = api_instance.get_manual_journal(xero_tenant_id, manual_journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachment_by_file_name**
> file get_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, content_type)

Allows you to retrieve specified Attachment on ManualJournal by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a ManualJournal
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve specified Attachment on ManualJournal by file name
    api_response = api_instance.get_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachment_by_id**
> file get_manual_journal_attachment_by_id(xero_tenant_id, manual_journal_id, attachment_id, content_type)

Allows you to retrieve specified Attachment on ManualJournals

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve specified Attachment on ManualJournals
    api_response = api_instance.get_manual_journal_attachment_by_id(xero_tenant_id, manual_journal_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachments**
> Attachments get_manual_journal_attachments(xero_tenant_id, manual_journal_id)

Allows you to retrieve Attachment for manual journals

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
try:
    # Allows you to retrieve Attachment for manual journals
    api_response = api_instance.get_manual_journal_attachments(xero_tenant_id, manual_journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journals**
> ManualJournals get_manual_journals(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Allows you to retrieve any manual journals

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + ManualJournal.StatusEnum.DRAFT + '\"' # str | Filter by an any element (optional)
order = 'Date ASC' # str | Order by an any element (optional)
page = 1 # int | e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment (optional)
try:
    # Allows you to retrieve any manual journals
    api_response = api_instance.get_manual_journals(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment | [optional] 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_invoice**
> OnlineInvoices get_online_invoice(xero_tenant_id, invoice_id)

Allows you to retrieve a URL to an online invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
try:
    # Allows you to retrieve a URL to an online invoice
    api_response = api_instance.get_online_invoice(xero_tenant_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_online_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**OnlineInvoices**](OnlineInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisation_cis_settings**
> CISOrgSetting get_organisation_cis_settings(xero_tenant_id, organisation_id)

Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
organisation_id = '00000000-0000-0000-000-000000000000' # str | The unique Xero identifier for an organisation
try:
    # Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.
    api_response = api_instance.get_organisation_cis_settings(xero_tenant_id, organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_organisation_cis_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **organisation_id** | [**str**](.md)| The unique Xero identifier for an organisation | 

### Return type

[**CISOrgSetting**](CISOrgSetting.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisations**
> Organisations get_organisations(xero_tenant_id)

Allows you to retrieve Organisation details

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # Allows you to retrieve Organisation details
    api_response = api_instance.get_organisations(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**Organisations**](Organisations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayment**
> Overpayments get_overpayment(xero_tenant_id, overpayment_id)

Allows you to retrieve a specified overpayments

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
overpayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Overpayment
try:
    # Allows you to retrieve a specified overpayments
    api_response = api_instance.get_overpayment(xero_tenant_id, overpayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayment_history**
> HistoryRecords get_overpayment_history(xero_tenant_id, overpayment_id)

Allows you to retrieve a history records of an Overpayment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
overpayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Overpayment
try:
    # Allows you to retrieve a history records of an Overpayment
    api_response = api_instance.get_overpayment_history(xero_tenant_id, overpayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayments**
> Overpayments get_overpayments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve overpayments

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Overpayment.StatusEnum.AUTHORISED + '\"' # str | Filter by an any element (optional)
order = 'RemainingCredit ASC' # str | Order by an any element (optional)
page = 1 # int | e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve overpayments
    api_response = api_instance.get_overpayments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> Payments get_payment(xero_tenant_id, payment_id)

Allows you to retrieve a specified payment for invoices and credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Payment
try:
    # Allows you to retrieve a specified payment for invoices and credit notes
    api_response = api_instance.get_payment(xero_tenant_id, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_history**
> HistoryRecords get_payment_history(xero_tenant_id, payment_id)

Allows you to retrieve history records of a payment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
payment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Payment
try:
    # Allows you to retrieve history records of a payment
    api_response = api_instance.get_payment_history(xero_tenant_id, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_services**
> PaymentServices get_payment_services(xero_tenant_id)

Allows you to retrieve payment services

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # Allows you to retrieve payment services
    api_response = api_instance.get_payment_services(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> Payments get_payments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve payments for invoices and credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Payment.StatusEnum.AUTHORISED + '\"' # str | Filter by an any element (optional)
order = 'Amount ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve payments for invoices and credit notes
    api_response = api_instance.get_payments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayment**
> Prepayments get_prepayment(xero_tenant_id, prepayment_id)

Allows you to retrieve a specified prepayments

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
prepayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PrePayment
try:
    # Allows you to retrieve a specified prepayments
    api_response = api_instance.get_prepayment(xero_tenant_id, prepayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayment_history**
> HistoryRecords get_prepayment_history(xero_tenant_id, prepayment_id)

Allows you to retrieve a history records of an Prepayment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
prepayment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PrePayment
try:
    # Allows you to retrieve a history records of an Prepayment
    api_response = api_instance.get_prepayment_history(xero_tenant_id, prepayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayments**
> Prepayments get_prepayments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve prepayments

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Prepayment.StatusEnum.AUTHORISED + '\"' # str | Filter by an any element (optional)
order = 'Reference ASC' # str | Order by an any element (optional)
page = 1 # int | e.g. page=1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve prepayments
    api_response = api_instance.get_prepayments(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order**
> PurchaseOrders get_purchase_order(xero_tenant_id, purchase_order_id)

Allows you to retrieve a specified purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PurchaseOrder
try:
    # Allows you to retrieve a specified purchase orders
    api_response = api_instance.get_purchase_order(xero_tenant_id, purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order_as_pdf**
> file get_purchase_order_as_pdf(xero_tenant_id, purchase_order_id)

Allows you to retrieve purchase orders as PDF files

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Purchase Order
try:
    # Allows you to retrieve purchase orders as PDF files
    api_response = api_instance.get_purchase_order_as_pdf(xero_tenant_id, purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_id** | [**str**](.md)| Unique identifier for an Purchase Order | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order_by_number**
> PurchaseOrders get_purchase_order_by_number(xero_tenant_id, purchase_order_number)

Allows you to retrieve a specified purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_number = 'PO1234' # str | Unique identifier for a PurchaseOrder
try:
    # Allows you to retrieve a specified purchase orders
    api_response = api_instance.get_purchase_order_by_number(xero_tenant_id, purchase_order_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order_by_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_number** | **str**| Unique identifier for a PurchaseOrder | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order_history**
> HistoryRecords get_purchase_order_history(xero_tenant_id, purchase_order_id)

Allows you to retrieve history for PurchaseOrder

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PurchaseOrder
try:
    # Allows you to retrieve history for PurchaseOrder
    api_response = api_instance.get_purchase_order_history(xero_tenant_id, purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_orders**
> PurchaseOrders get_purchase_orders(xero_tenant_id, if_modified_since=if_modified_since, status=status, date_from=date_from, date_to=date_to, order=order, page=page)

Allows you to retrieve purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
status = 'SUBMITTED' # str | Filter by purchase order status (optional)
date_from = '2019-12-01' # str | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31 (optional)
date_to = '2019-12-31' # str | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31 (optional)
order = 'PurchaseOrderNumber ASC' # str | Order by an any element (optional)
page = 1 # int | To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned. (optional)
try:
    # Allows you to retrieve purchase orders
    api_response = api_instance.get_purchase_orders(xero_tenant_id, if_modified_since=if_modified_since, status=status, date_from=date_from, date_to=date_to, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **status** | **str**| Filter by purchase order status | [optional] 
 **date_from** | **str**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **date_to** | **str**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| To specify a page, append the page parameter to the URL e.g. ?page&#x3D;1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page&#x3D;2 and continuing this process until no more results are returned. | [optional] 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote**
> Quotes get_quote(xero_tenant_id, quote_id)

Allows you to retrieve a specified quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Quote
try:
    # Allows you to retrieve a specified quote
    api_response = api_instance.get_quote(xero_tenant_id, quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for an Quote | 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_as_pdf**
> file get_quote_as_pdf(xero_tenant_id, quote_id)

Allows you to retrieve quotes as PDF files

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Quote
try:
    # Allows you to retrieve quotes as PDF files
    api_response = api_instance.get_quote_as_pdf(xero_tenant_id, quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for an Quote | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_attachment_by_file_name**
> file get_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, content_type)

Allows you to retrieve Attachment on Quote by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Quote object
file_name = 'xero-dev.jpg' # str | Name of the attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachment on Quote by Filename
    api_response = api_instance.get_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for Quote object | 
 **file_name** | **str**| Name of the attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_attachment_by_id**
> file get_quote_attachment_by_id(xero_tenant_id, quote_id, attachment_id, content_type)

Allows you to retrieve specific Attachment on Quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Quote object
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Attachment object
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve specific Attachment on Quote
    api_response = api_instance.get_quote_attachment_by_id(xero_tenant_id, quote_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for Quote object | 
 **attachment_id** | [**str**](.md)| Unique identifier for Attachment object | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_attachments**
> Attachments get_quote_attachments(xero_tenant_id, quote_id)

Allows you to retrieve Attachments for Quotes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Quote object
try:
    # Allows you to retrieve Attachments for Quotes
    api_response = api_instance.get_quote_attachments(xero_tenant_id, quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for Quote object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_history**
> HistoryRecords get_quote_history(xero_tenant_id, quote_id)

Allows you to retrieve a history records of an quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Quote
try:
    # Allows you to retrieve a history records of an quote
    api_response = api_instance.get_quote_history(xero_tenant_id, quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quote_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for an Quote | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes**
> Quotes get_quotes(xero_tenant_id, if_modified_since=if_modified_since, date_from=date_from, date_to=date_to, expiry_date_from=expiry_date_from, expiry_date_to=expiry_date_to, contact_id=contact_id, status=status, page=page, order=order)

Allows you to retrieve any sales quotes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
date_from = '2013-10-20' # date | Filter for quotes after a particular date (optional)
date_to = '2013-10-20' # date | Filter for quotes before a particular date (optional)
expiry_date_from = '2013-10-20' # date | Filter for quotes expiring after a particular date (optional)
expiry_date_to = '2013-10-20' # date | Filter for quotes before a particular date (optional)
contact_id = '00000000-0000-0000-000-000000000000' # str | Filter for quotes belonging to a particular contact (optional)
status = 'status_example' # str | Filter for quotes of a particular Status (optional)
page = 1 # int | e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote (optional)
order = 'ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve any sales quotes
    api_response = api_instance.get_quotes(xero_tenant_id, if_modified_since=if_modified_since, date_from=date_from, date_to=date_to, expiry_date_from=expiry_date_from, expiry_date_to=expiry_date_to, contact_id=contact_id, status=status, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **date_from** | **date**| Filter for quotes after a particular date | [optional] 
 **date_to** | **date**| Filter for quotes before a particular date | [optional] 
 **expiry_date_from** | **date**| Filter for quotes expiring after a particular date | [optional] 
 **expiry_date_to** | **date**| Filter for quotes before a particular date | [optional] 
 **contact_id** | [**str**](.md)| Filter for quotes belonging to a particular contact | [optional] 
 **status** | **str**| Filter for quotes of a particular Status | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt**
> Receipts get_receipt(xero_tenant_id, receipt_id, unitdp=unitdp)

Allows you to retrieve a specified draft expense claim receipts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a specified draft expense claim receipts
    api_response = api_instance.get_receipt(xero_tenant_id, receipt_id, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachment_by_file_name**
> file get_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, content_type)

Allows you to retrieve Attachments on expense claim receipts by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
file_name = 'xero-dev.jpg' # str | The name of the file being attached to the Receipt
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on expense claim receipts by file name
    api_response = api_instance.get_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachment_by_id**
> file get_receipt_attachment_by_id(xero_tenant_id, receipt_id, attachment_id, content_type)

Allows you to retrieve Attachments on expense claim receipts by ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve Attachments on expense claim receipts by ID
    api_response = api_instance.get_receipt_attachment_by_id(xero_tenant_id, receipt_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachments**
> Attachments get_receipt_attachments(xero_tenant_id, receipt_id)

Allows you to retrieve Attachments for expense claim receipts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
try:
    # Allows you to retrieve Attachments for expense claim receipts
    api_response = api_instance.get_receipt_attachments(xero_tenant_id, receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_history**
> HistoryRecords get_receipt_history(xero_tenant_id, receipt_id)

Allows you to retrieve a history records of an Receipt

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
try:
    # Allows you to retrieve a history records of an Receipt
    api_response = api_instance.get_receipt_history(xero_tenant_id, receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts**
> Receipts get_receipts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)

Allows you to retrieve draft expense claim receipts for any user

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"' + Receipt.StatusEnum.DRAFT + '\"' # str | Filter by an any element (optional)
order = 'ReceiptNumber ASC' # str | Order by an any element (optional)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve draft expense claim receipts for any user
    api_response = api_instance.get_receipts(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice**
> RepeatingInvoices get_repeating_invoice(xero_tenant_id, repeating_invoice_id)

Allows you to retrieve a specified repeating invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
try:
    # Allows you to retrieve a specified repeating invoice
    api_response = api_instance.get_repeating_invoice(xero_tenant_id, repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachment_by_file_name**
> file get_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, content_type)

Allows you to retrieve specified attachment on repeating invoices by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Repeating Invoice
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve specified attachment on repeating invoices by file name
    api_response = api_instance.get_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachment_by_id**
> file get_repeating_invoice_attachment_by_id(xero_tenant_id, repeating_invoice_id, attachment_id, content_type)

Allows you to retrieve a specified Attachments on repeating invoices

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
attachment_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Attachment
content_type = 'image/jpg' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
try:
    # Allows you to retrieve a specified Attachments on repeating invoices
    api_response = api_instance.get_repeating_invoice_attachment_by_id(xero_tenant_id, repeating_invoice_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachments**
> Attachments get_repeating_invoice_attachments(xero_tenant_id, repeating_invoice_id)

Allows you to retrieve Attachments on repeating invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
try:
    # Allows you to retrieve Attachments on repeating invoice
    api_response = api_instance.get_repeating_invoice_attachments(xero_tenant_id, repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_history**
> HistoryRecords get_repeating_invoice_history(xero_tenant_id, repeating_invoice_id)

Allows you to retrieve history for a repeating invoice

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
try:
    # Allows you to retrieve history for a repeating invoice
    api_response = api_instance.get_repeating_invoice_history(xero_tenant_id, repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoices**
> RepeatingInvoices get_repeating_invoices(xero_tenant_id, where=where, order=order)

Allows you to retrieve any repeating invoices

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
where = 'Status==\"' + RepeatingInvoice.StatusEnum.DRAFT + '\"' # str | Filter by an any element (optional)
order = 'Total ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve any repeating invoices
    api_response = api_instance.get_repeating_invoices(xero_tenant_id, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_aged_payables_by_contact**
> ReportWithRows get_report_aged_payables_by_contact(xero_tenant_id, contact_id, date=date, from_date=from_date, to_date=to_date)

Allows you to retrieve report for AgedPayablesByContact

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
date = '2013-10-20' # date | The date of the Aged Payables By Contact report (optional)
from_date = '2013-10-20' # date | The from date of the Aged Payables By Contact report (optional)
to_date = '2013-10-20' # date | The to date of the Aged Payables By Contact report (optional)
try:
    # Allows you to retrieve report for AgedPayablesByContact
    api_response = api_instance.get_report_aged_payables_by_contact(xero_tenant_id, contact_id, date=date, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_aged_payables_by_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **date** | **date**| The date of the Aged Payables By Contact report | [optional] 
 **from_date** | **date**| The from date of the Aged Payables By Contact report | [optional] 
 **to_date** | **date**| The to date of the Aged Payables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_aged_receivables_by_contact**
> ReportWithRows get_report_aged_receivables_by_contact(xero_tenant_id, contact_id, date=date, from_date=from_date, to_date=to_date)

Allows you to retrieve report for AgedReceivablesByContact

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
date = '2013-10-20' # date | The date of the Aged Receivables By Contact report (optional)
from_date = '2013-10-20' # date | The from date of the Aged Receivables By Contact report (optional)
to_date = '2013-10-20' # date | The to date of the Aged Receivables By Contact report (optional)
try:
    # Allows you to retrieve report for AgedReceivablesByContact
    api_response = api_instance.get_report_aged_receivables_by_contact(xero_tenant_id, contact_id, date=date, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_aged_receivables_by_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **date** | **date**| The date of the Aged Receivables By Contact report | [optional] 
 **from_date** | **date**| The from date of the Aged Receivables By Contact report | [optional] 
 **to_date** | **date**| The to date of the Aged Receivables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ba_sor_gst**
> ReportWithRows get_report_ba_sor_gst(xero_tenant_id, report_id)

Allows you to retrieve report for BAS only valid for AU orgs

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
report_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Report
try:
    # Allows you to retrieve report for BAS only valid for AU orgs
    api_response = api_instance.get_report_ba_sor_gst(xero_tenant_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ba_sor_gst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **report_id** | **str**| Unique identifier for a Report | 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ba_sor_gst_list**
> ReportWithRows get_report_ba_sor_gst_list(xero_tenant_id)

Allows you to retrieve report for BAS only valid for AU orgs

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # Allows you to retrieve report for BAS only valid for AU orgs
    api_response = api_instance.get_report_ba_sor_gst_list(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ba_sor_gst_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_balance_sheet**
> ReportWithRows get_report_balance_sheet(xero_tenant_id, date=date, periods=periods, timeframe=timeframe, tracking_option_id1=tracking_option_id1, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)

Allows you to retrieve report for BalanceSheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
date = '2019-11-01' # str | The date of the Balance Sheet report (optional)
periods = 3 # int | The number of periods for the Balance Sheet report (optional)
timeframe = 'MONTH' # str | The period size to compare to (MONTH, QUARTER, YEAR) (optional)
tracking_option_id1 = '00000000-0000-0000-000-000000000000' # str | The tracking option 1 for the Balance Sheet report (optional)
tracking_option_id2 = '00000000-0000-0000-000-000000000000' # str | The tracking option 2 for the Balance Sheet report (optional)
standard_layout = true # bool | The standard layout boolean for the Balance Sheet report (optional)
payments_only = false # bool | return a cash basis for the Balance Sheet report (optional)
try:
    # Allows you to retrieve report for BalanceSheet
    api_response = api_instance.get_report_balance_sheet(xero_tenant_id, date=date, periods=periods, timeframe=timeframe, tracking_option_id1=tracking_option_id1, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_balance_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **date** | **str**| The date of the Balance Sheet report | [optional] 
 **periods** | **int**| The number of periods for the Balance Sheet report | [optional] 
 **timeframe** | **str**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **tracking_option_id1** | **str**| The tracking option 1 for the Balance Sheet report | [optional] 
 **tracking_option_id2** | **str**| The tracking option 2 for the Balance Sheet report | [optional] 
 **standard_layout** | **bool**| The standard layout boolean for the Balance Sheet report | [optional] 
 **payments_only** | **bool**| return a cash basis for the Balance Sheet report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_bank_summary**
> ReportWithRows get_report_bank_summary(xero_tenant_id, from_date=from_date, to_date=to_date)

Allows you to retrieve report for BankSummary

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
from_date = '2019-11-01' # date | The from date for the Bank Summary report e.g. 2018-03-31 (optional)
to_date = '2019-11-30' # date | The to date for the Bank Summary report e.g. 2018-03-31 (optional)
try:
    # Allows you to retrieve report for BankSummary
    api_response = api_instance.get_report_bank_summary(xero_tenant_id, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_bank_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **from_date** | **date**| The from date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **to_date** | **date**| The to date for the Bank Summary report e.g. 2018-03-31 | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_budget_summary**
> ReportWithRows get_report_budget_summary(xero_tenant_id, date=date, period=period, timeframe=timeframe)

Allows you to retrieve report for Budget Summary

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
date = '2019-03-31' # date | The date for the Bank Summary report e.g. 2018-03-31 (optional)
period = 2 # int | The number of periods to compare (integer between 1 and 12) (optional)
timeframe = 3 # int | The period size to compare to (1=month, 3=quarter, 12=year) (optional)
try:
    # Allows you to retrieve report for Budget Summary
    api_response = api_instance.get_report_budget_summary(xero_tenant_id, date=date, period=period, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_budget_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **date** | **date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **period** | **int**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **int**| The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year) | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_executive_summary**
> ReportWithRows get_report_executive_summary(xero_tenant_id, date=date)

Allows you to retrieve report for ExecutiveSummary

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
date = '2019-03-31' # date | The date for the Bank Summary report e.g. 2018-03-31 (optional)
try:
    # Allows you to retrieve report for ExecutiveSummary
    api_response = api_instance.get_report_executive_summary(xero_tenant_id, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_executive_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **date** | **date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_profit_and_loss**
> ReportWithRows get_report_profit_and_loss(xero_tenant_id, from_date=from_date, to_date=to_date, periods=periods, timeframe=timeframe, tracking_category_id=tracking_category_id, tracking_category_id2=tracking_category_id2, tracking_option_id=tracking_option_id, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)

Allows you to retrieve report for ProfitAndLoss

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
from_date = '2019-03-01' # date | The from date for the ProfitAndLoss report e.g. 2018-03-31 (optional)
to_date = '2019-03-31' # date | The to date for the ProfitAndLoss report e.g. 2018-03-31 (optional)
periods = 3 # int | The number of periods to compare (integer between 1 and 12) (optional)
timeframe = 'MONTH' # str | The period size to compare to (MONTH, QUARTER, YEAR) (optional)
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | The trackingCategory 1 for the ProfitAndLoss report (optional)
tracking_category_id2 = '00000000-0000-0000-000-000000000000' # str | The trackingCategory 2 for the ProfitAndLoss report (optional)
tracking_option_id = '00000000-0000-0000-000-000000000000' # str | The tracking option 1 for the ProfitAndLoss report (optional)
tracking_option_id2 = '00000000-0000-0000-000-000000000000' # str | The tracking option 2 for the ProfitAndLoss report (optional)
standard_layout = true # bool | Return the standard layout for the ProfitAndLoss report (optional)
payments_only = false # bool | Return cash only basis for the ProfitAndLoss report (optional)
try:
    # Allows you to retrieve report for ProfitAndLoss
    api_response = api_instance.get_report_profit_and_loss(xero_tenant_id, from_date=from_date, to_date=to_date, periods=periods, timeframe=timeframe, tracking_category_id=tracking_category_id, tracking_category_id2=tracking_category_id2, tracking_option_id=tracking_option_id, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_profit_and_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **from_date** | **date**| The from date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **to_date** | **date**| The to date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **periods** | **int**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **str**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **tracking_category_id** | **str**| The trackingCategory 1 for the ProfitAndLoss report | [optional] 
 **tracking_category_id2** | **str**| The trackingCategory 2 for the ProfitAndLoss report | [optional] 
 **tracking_option_id** | **str**| The tracking option 1 for the ProfitAndLoss report | [optional] 
 **tracking_option_id2** | **str**| The tracking option 2 for the ProfitAndLoss report | [optional] 
 **standard_layout** | **bool**| Return the standard layout for the ProfitAndLoss report | [optional] 
 **payments_only** | **bool**| Return cash only basis for the ProfitAndLoss report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ten_ninety_nine**
> Reports get_report_ten_ninety_nine(xero_tenant_id, report_year=report_year)

Allows you to retrieve report for TenNinetyNine

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
report_year = '2019' # str | The year of the 1099 report (optional)
try:
    # Allows you to retrieve report for TenNinetyNine
    api_response = api_instance.get_report_ten_ninety_nine(xero_tenant_id, report_year=report_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ten_ninety_nine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **report_year** | **str**| The year of the 1099 report | [optional] 

### Return type

[**Reports**](Reports.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_trial_balance**
> ReportWithRows get_report_trial_balance(xero_tenant_id, date=date, payments_only=payments_only)

Allows you to retrieve report for TrialBalance

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
date = '2019-10-31' # date | The date for the Trial Balance report e.g. 2018-03-31 (optional)
payments_only = true # bool | Return cash only basis for the Trial Balance report (optional)
try:
    # Allows you to retrieve report for TrialBalance
    api_response = api_instance.get_report_trial_balance(xero_tenant_id, date=date, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_trial_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **date** | **date**| The date for the Trial Balance report e.g. 2018-03-31 | [optional] 
 **payments_only** | **bool**| Return cash only basis for the Trial Balance report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rates**
> TaxRates get_tax_rates(xero_tenant_id, where=where, order=order, tax_type=tax_type)

Allows you to retrieve Tax Rates

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
where = 'Status==\"' + TaxRate.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Name ASC' # str | Order by an any element (optional)
tax_type = 'INPUT' # str | Filter by tax type (optional)
try:
    # Allows you to retrieve Tax Rates
    api_response = api_instance.get_tax_rates(xero_tenant_id, where=where, order=order, tax_type=tax_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tax_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **tax_type** | **str**| Filter by tax type | [optional] 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_categories**
> TrackingCategories get_tracking_categories(xero_tenant_id, where=where, order=order, include_archived=include_archived)

Allows you to retrieve tracking categories and options

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
where = 'Status==\"' + TrackingCategory.StatusEnum.ACTIVE + '\"' # str | Filter by an any element (optional)
order = 'Name ASC' # str | Order by an any element (optional)
include_archived = True # bool | e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response (optional)
try:
    # Allows you to retrieve tracking categories and options
    api_response = api_instance.get_tracking_categories(xero_tenant_id, where=where, order=order, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tracking_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Categories and options with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_category**
> TrackingCategories get_tracking_category(xero_tenant_id, tracking_category_id)

Allows you to retrieve tracking categories and options for specified category

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
try:
    # Allows you to retrieve tracking categories and options for specified category
    api_response = api_instance.get_tracking_category(xero_tenant_id, tracking_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> Users get_user(xero_tenant_id, user_id)

Allows you to retrieve a specified user

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
user_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a User
try:
    # Allows you to retrieve a specified user
    api_response = api_instance.get_user(xero_tenant_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **user_id** | [**str**](.md)| Unique identifier for a User | 

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> Users get_users(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve users

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'IsSubscriber==true' # str | Filter by an any element (optional)
order = 'LastName ASC' # str | Order by an any element (optional)
try:
    # Allows you to retrieve users
    api_response = api_instance.get_users(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Accounts update_account(xero_tenant_id, account_id, accounts)

Allows you to update a chart of accounts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for retrieving single object
accounts = { accounts:[ { code:"123456", name:"BarFoo", accountID:"00000000-0000-0000-000-000000000000", type:AccountType.EXPENSE, description:"GoodBye World", taxType:"INPUT" } ] } # Accounts | Request of type Accounts array with one Account
try:
    # Allows you to update a chart of accounts
    api_response = api_instance.update_account(xero_tenant_id, account_id, accounts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 
 **accounts** | [**Accounts**](Accounts.md)| Request of type Accounts array with one Account | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_attachment_by_file_name**
> Attachments update_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, body)

Allows you to update Attachment on Account by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
account_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Account object
file_name = 'xero-dev.jpg' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update Attachment on Account by Filename
    api_response = api_instance.update_account_attachment_by_file_name(xero_tenant_id, account_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transaction**
> BankTransactions update_bank_transaction(xero_tenant_id, bank_transaction_id, bank_transactions, unitdp=unitdp)

Allows you to update a single spend or receive money transaction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
bank_transactions = { bankTransactions:[ { type: BankTransaction.TypeEnum.SPEND, date:"2019-02-25", reference:"You just updated", status:BankTransaction.StatusEnum.AUTHORISED, bankTransactionID:"00000000-0000-0000-000-000000000000", lineItems: [],contact: {}, bankAccount: {accountID: "00000000-0000-0000-000-000000000000"} } ] } # BankTransactions | 
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update a single spend or receive money transaction
    api_response = api_instance.update_bank_transaction(xero_tenant_id, bank_transaction_id, bank_transactions, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **bank_transactions** | [**BankTransactions**](BankTransactions.md)|  | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transaction_attachment_by_file_name**
> Attachments update_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, body)

Allows you to update an Attachment on BankTransaction by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transaction_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transaction
file_name = 'xero-dev.jpg' # str | The name of the file being attached
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update an Attachment on BankTransaction by Filename
    api_response = api_instance.update_bank_transaction_attachment_by_file_name(xero_tenant_id, bank_transaction_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transfer_attachment_by_file_name**
> Attachments update_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, body)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transfer_id = '00000000-0000-0000-000-000000000000' # str | Xero generated unique identifier for a bank transfer
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Bank Transfer
body = 'body_example' # str | Byte array of file in body of request
try:
    api_response = api_instance.update_bank_transfer_attachment_by_file_name(xero_tenant_id, bank_transfer_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contacts update_contact(xero_tenant_id, contact_id, contacts)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
contacts = { contacts:[ { contactID:"00000000-0000-0000-000-000000000000", name:"Thanos" } ] } # Contacts | an array of Contacts containing single Contact object with properties to update
try:
    api_response = api_instance.update_contact(xero_tenant_id, contact_id, contacts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **contacts** | [**Contacts**](Contacts.md)| an array of Contacts containing single Contact object with properties to update | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_attachment_by_file_name**
> Attachments update_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, body)



### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact
file_name = 'xero-dev.jpg' # str | Name for the file you are attaching
body = 'body_example' # str | Byte array of file in body of request
try:
    api_response = api_instance.update_contact_attachment_by_file_name(xero_tenant_id, contact_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_group**
> ContactGroups update_contact_group(xero_tenant_id, contact_group_id, contact_groups)

Allows you to update a Contact Group

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_group_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Contact Group
contact_groups = { contactGroups:[ { name:"Vendor" } ] } # ContactGroups | an array of Contact groups with Name of specific group to update
try:
    # Allows you to update a Contact Group
    api_response = api_instance.update_contact_group(xero_tenant_id, contact_group_id, contact_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contact_groups** | [**ContactGroups**](ContactGroups.md)| an array of Contact groups with Name of specific group to update | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note**
> CreditNotes update_credit_note(xero_tenant_id, credit_note_id, credit_notes, unitdp=unitdp)

Allows you to update a specific credit note

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
credit_notes = { creditNotes:[ { type:CreditNote.TypeEnum.ACCPAYCREDIT, contact:{ contactID:"00000000-0000-0000-000-000000000000" }, date:"2019-01-05", status: CreditNote.StatusEnum.AUTHORISED, reference: "Mind stone", lineItems:[ { description:"Infinity Stones", quantity:1.0, unitAmount:100.0, accountCode:"400" } ] } ] } # CreditNotes | an array of Credit Notes containing credit note details to update
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update a specific credit note
    api_response = api_instance.update_credit_note(xero_tenant_id, credit_note_id, credit_notes, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **credit_notes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes containing credit note details to update | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note_attachment_by_file_name**
> Attachments update_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, body)

Allows you to update Attachments on CreditNote by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_note_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Credit Note
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching to Credit Note
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update Attachments on CreditNote by file name
    api_response = api_instance.update_credit_note_attachment_by_file_name(xero_tenant_id, credit_note_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_claim**
> ExpenseClaims update_expense_claim(xero_tenant_id, expense_claim_id, expense_claims)

Allows you to update specified expense claims

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
expense_claim_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ExpenseClaim
expense_claims = { expenseClaims:[ { status:ExpenseClaim.StatusEnum.AUTHORISED, user:{ userID:"00000000-0000-0000-000-000000000000" }, receipts:[ { receiptID:"00000000-0000-0000-000-000000000000", lineItems: [], contact: {}, date:"2020-01-01", user:{} } ] } ] } # ExpenseClaims | 
try:
    # Allows you to update specified expense claims
    api_response = api_instance.update_expense_claim(xero_tenant_id, expense_claim_id, expense_claims)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_expense_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 
 **expense_claims** | [**ExpenseClaims**](ExpenseClaims.md)|  | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> Invoices update_invoice(xero_tenant_id, invoice_id, invoices, unitdp=unitdp)

Allows you to update a specified sales invoices or purchase bills

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
invoices = { invoices:[ { reference:"I am Iron Man", invoiceID:"00000000-0000-0000-000-000000000000", lineItems: [],contact: {},type: Invoice.TypeEnum.ACCPAY } ] } # Invoices | 
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update a specified sales invoices or purchase bills
    api_response = api_instance.update_invoice(xero_tenant_id, invoice_id, invoices, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **invoices** | [**Invoices**](Invoices.md)|  | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_attachment_by_file_name**
> Attachments update_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, body)

Allows you to update Attachment on invoices or purchase bills by it's filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Invoice
file_name = 'xero-dev.jpg' # str | Name of the file you are attaching
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.update_invoice_attachment_by_file_name(xero_tenant_id, invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> Items update_item(xero_tenant_id, item_id, items, unitdp=unitdp)

Allows you to update a specified item

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
item_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Item
items = { items:[ { code:"abc123", description:"Hello Xero" } ] } # Items | 
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update a specified item
    api_response = api_instance.update_item(xero_tenant_id, item_id, items, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **item_id** | [**str**](.md)| Unique identifier for an Item | 
 **items** | [**Items**](Items.md)|  | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_linked_transaction**
> LinkedTransactions update_linked_transaction(xero_tenant_id, linked_transaction_id, linked_transactions)

Allows you to update a specified linked transactions (billable expenses)

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
linked_transaction_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a LinkedTransaction
linked_transactions = { linkedTransactions:[ {sourceLineItemID:"00000000-0000-0000-000-000000000000", contactID:"00000000-0000-0000-000-000000000000" } ] } # LinkedTransactions | 
try:
    # Allows you to update a specified linked transactions (billable expenses)
    api_response = api_instance.update_linked_transaction(xero_tenant_id, linked_transaction_id, linked_transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 
 **linked_transactions** | [**LinkedTransactions**](LinkedTransactions.md)|  | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manual_journal**
> ManualJournals update_manual_journal(xero_tenant_id, manual_journal_id, manual_journals)

Allows you to update a specified manual journal

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
manual_journals = { manualJournals:[ { narration:"Hello Xero", manualJournalID:"00000000-0000-0000-000-000000000000",journalLines:[] } ] } # ManualJournals | 
try:
    # Allows you to update a specified manual journal
    api_response = api_instance.update_manual_journal(xero_tenant_id, manual_journal_id, manual_journals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_manual_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **manual_journals** | [**ManualJournals**](ManualJournals.md)|  | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manual_journal_attachment_by_file_name**
> Attachments update_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, body)

Allows you to update a specified Attachment on ManualJournal by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journal_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a ManualJournal
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a ManualJournal
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update a specified Attachment on ManualJournal by file name
    api_response = api_instance.update_manual_journal_attachment_by_file_name(xero_tenant_id, manual_journal_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_bank_transactions**
> BankTransactions update_or_create_bank_transactions(xero_tenant_id, bank_transactions, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to update or create one or more spend or receive money transaction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
bank_transactions = { bankTransactions:[ { type: BankTransaction.TypeEnum.SPEND, contact: { contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity: 1.0, unitAmount:20.0, accountCode:"000" } ], bankAccount:{ code:"000" } } ] } # BankTransactions | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update or create one or more spend or receive money transaction
    api_response = api_instance.update_or_create_bank_transactions(xero_tenant_id, bank_transactions, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **bank_transactions** | [**BankTransactions**](BankTransactions.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_contacts**
> Contacts update_or_create_contacts(xero_tenant_id, contacts, summarize_errors=summarize_errors)

Allows you to update OR create one or more contacts in a Xero organisation

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contacts = {contacts: [{ name:"Bruce Banner", emailAddress:"hulk@avengers.com", phones:[ { phoneType: Phone.PhoneTypeEnum.MOBILE, phoneNumber:"555-1212", phoneAreaCode:"415" } ], paymentTerms:{ bills:{ day:15, type: PaymentTermType.OFCURRENTMONTH }, sales:{ day:10, type: PaymentTermType.DAYSAFTERBILLMONTH } } } ] } # Contacts | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to update OR create one or more contacts in a Xero organisation
    api_response = api_instance.update_or_create_contacts(xero_tenant_id, contacts, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contacts** | [**Contacts**](Contacts.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_credit_notes**
> CreditNotes update_or_create_credit_notes(xero_tenant_id, credit_notes, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to update OR create one or more credit notes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
credit_notes = { creditNotes:[ { type: CreditNote.TypeEnum.ACCPAYCREDIT, contact:{ contactID:"00000000-0000-0000-000-000000000000" }, date:"2019-01-05", lineItems:[ { description:"Foobar", quantity:2.0, unitAmount:20.0, accountCode:"400" } ] } ] } # CreditNotes | an array of Credit Notes with a single CreditNote object.
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update OR create one or more credit notes
    api_response = api_instance.update_or_create_credit_notes(xero_tenant_id, credit_notes, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **credit_notes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes with a single CreditNote object. | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_employees**
> Employees update_or_create_employees(xero_tenant_id, employees, summarize_errors=summarize_errors)

Allows you to create a single new employees used in Xero payrun

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
employees = { employees:[ { firstName:"Nick", lastName:"Fury", externalLink:{ url:"http://twitter.com/#!/search/Nick+Fury" } } ] } # Employees | Employees with array of Employee object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create a single new employees used in Xero payrun
    api_response = api_instance.update_or_create_employees(xero_tenant_id, employees, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_invoices**
> Invoices update_or_create_invoices(xero_tenant_id, invoices, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to update OR create one or more sales invoices or purchase bills

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
invoices = { invoices:[ { type: Invoice.TypeEnum.ACCREC, contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Acme Tires", quantity:2.0, unitAmount:20.0, accountCode:"200", taxType:"NONE", lineAmount:40.0 } ], date:"2019-03-11", dueDate:"2018-12-10", reference:"Website Design", status: Invoice.StatusEnum.AUTHORISED } ] } # Invoices | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update OR create one or more sales invoices or purchase bills
    api_response = api_instance.update_or_create_invoices(xero_tenant_id, invoices, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **invoices** | [**Invoices**](Invoices.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_items**
> Items update_or_create_items(xero_tenant_id, items, summarize_errors=summarize_errors, unitdp=unitdp)

Allows you to update or create one or more items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
items = { items:[ { code:"abcXYZ", name:"HelloWorld", description:"Foobar" } ] } # Items | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to update or create one or more items
    api_response = api_instance.update_or_create_items(xero_tenant_id, items, summarize_errors=summarize_errors, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **items** | [**Items**](Items.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_manual_journals**
> ManualJournals update_or_create_manual_journals(xero_tenant_id, manual_journals, summarize_errors=summarize_errors)

Allows you to create a single manual journal

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
manual_journals = { manualJournals:[ { narration:"Foo bar", journalLines:[ { lineAmount:100.0, accountCode:"400", description:"Hello there" }, { lineAmount:-100.0, accountCode:"400", description:"Goodbye", tracking:[ { name:"Simpsons", option:"Bart" } ] } ], date:"2019-03-14" } ] } # ManualJournals | ManualJournals array with ManualJournal object in body of request
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to create a single manual journal
    api_response = api_instance.update_or_create_manual_journals(xero_tenant_id, manual_journals, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_manual_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **manual_journals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_purchase_orders**
> PurchaseOrders update_or_create_purchase_orders(xero_tenant_id, purchase_orders, summarize_errors=summarize_errors)

Allows you to update or create one or more purchase orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_orders = { purchaseOrders:[ { contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity:1.0, unitAmount:20.0, accountCode:"710" } ], date:"2019-03-13" } ] } # PurchaseOrders | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to update or create one or more purchase orders
    api_response = api_instance.update_or_create_purchase_orders(xero_tenant_id, purchase_orders, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_orders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_quotes**
> Quotes update_or_create_quotes(xero_tenant_id, quotes, summarize_errors=summarize_errors)

Allows you to update OR create one or more quotes

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quotes = { quotes:[ { contact:{ contactID:"00000000-0000-0000-000-000000000000" }, lineItems:[ { description:"Foobar", quantity:1.0, unitAmount:20.0, accountCode:"12775" } ], date:"2020-02-01" } ] } # Quotes | 
summarize_errors = False # bool | If false return 200 OK and mix of successfully created obejcts and any with validation errors (optional) (default to False)
try:
    # Allows you to update OR create one or more quotes
    api_response = api_instance.update_or_create_quotes(xero_tenant_id, quotes, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_or_create_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quotes** | [**Quotes**](Quotes.md)|  | 
 **summarize_errors** | **bool**| If false return 200 OK and mix of successfully created obejcts and any with validation errors | [optional] [default to False]

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_purchase_order**
> PurchaseOrders update_purchase_order(xero_tenant_id, purchase_order_id, purchase_orders)

Allows you to update a specified purchase order

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
purchase_order_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a PurchaseOrder
purchase_orders = { purchaseOrders:[ { attentionTo:"Peter Parker",lineItems: [],contact: {} } ] } # PurchaseOrders | 
try:
    # Allows you to update a specified purchase order
    api_response = api_instance.update_purchase_order(xero_tenant_id, purchase_order_id, purchase_orders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 
 **purchase_orders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quote**
> Quotes update_quote(xero_tenant_id, quote_id, quotes)

Allows you to update a specified quote

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for an Quote
quotes = {quotes:[{reference:"I am an update",contact:{contactID:"00000000-0000-0000-000-000000000000"},date:"2020-02-01"}]} # Quotes | 
try:
    # Allows you to update a specified quote
    api_response = api_instance.update_quote(xero_tenant_id, quote_id, quotes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for an Quote | 
 **quotes** | [**Quotes**](Quotes.md)|  | 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quote_attachment_by_file_name**
> Attachments update_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, body)

Allows you to update Attachment on Quote by Filename

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
quote_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for Quote object
file_name = 'xero-dev.jpg' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update Attachment on Quote by Filename
    api_response = api_instance.update_quote_attachment_by_file_name(xero_tenant_id, quote_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_quote_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **quote_id** | [**str**](.md)| Unique identifier for Quote object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt**
> Receipts update_receipt(xero_tenant_id, receipt_id, receipts, unitdp=unitdp)

Allows you to retrieve a specified draft expense claim receipts

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
receipts = { receipts:[ { user:{ userID:"00000000-0000-0000-000-000000000000" }, reference:"Foobar", date: "2020-01-01",contact: {},lineItems: []} ] } # Receipts | 
unitdp = 4 # int | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts (optional)
try:
    # Allows you to retrieve a specified draft expense claim receipts
    api_response = api_instance.update_receipt(xero_tenant_id, receipt_id, receipts, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **receipts** | [**Receipts**](Receipts.md)|  | 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt_attachment_by_file_name**
> Attachments update_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, body)

Allows you to update Attachment on expense claim receipts by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
receipt_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Receipt
file_name = 'xero-dev.jpg' # str | The name of the file being attached to the Receipt
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update Attachment on expense claim receipts by file name
    api_response = api_instance.update_receipt_attachment_by_file_name(xero_tenant_id, receipt_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repeating_invoice_attachment_by_file_name**
> Attachments update_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, body)

Allows you to update specified attachment on repeating invoices by file name

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
repeating_invoice_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Repeating Invoice
file_name = 'xero-dev.jpg' # str | The name of the file being attached to a Repeating Invoice
body = 'body_example' # str | Byte array of file in body of request
try:
    # Allows you to update specified attachment on repeating invoices by file name
    api_response = api_instance.update_repeating_invoice_attachment_by_file_name(xero_tenant_id, repeating_invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_rate**
> TaxRates update_tax_rate(xero_tenant_id, tax_rates)

Allows you to update Tax Rates

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tax_rates = { taxRates:[ { name:"State Tax NY", taxComponents:[ { name:"State Tax", rate:2.25 } ], status:"DELETED", reportTaxType:"INPUT" } ] } # TaxRates | 
try:
    # Allows you to update Tax Rates
    api_response = api_instance.update_tax_rate(xero_tenant_id, tax_rates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_tax_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tax_rates** | [**TaxRates**](TaxRates.md)|  | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracking_category**
> TrackingCategories update_tracking_category(xero_tenant_id, tracking_category_id, tracking_category)

Allows you to update tracking categories

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
tracking_category = { name:"Avengers" } # TrackingCategory | 
try:
    # Allows you to update tracking categories
    api_response = api_instance.update_tracking_category(xero_tenant_id, tracking_category_id, tracking_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_category** | [**TrackingCategory**](TrackingCategory.md)|  | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracking_options**
> TrackingOptions update_tracking_options(xero_tenant_id, tracking_category_id, tracking_option_id, tracking_option)

Allows you to update options for a specified tracking category

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
tracking_category_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a TrackingCategory
tracking_option_id = '00000000-0000-0000-000-000000000000' # str | Unique identifier for a Tracking Option
tracking_option = { name:"Vision" } # TrackingOption | 
try:
    # Allows you to update options for a specified tracking category
    api_response = api_instance.update_tracking_options(xero_tenant_id, tracking_category_id, tracking_option_id, tracking_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_tracking_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_option_id** | [**str**](.md)| Unique identifier for a Tracking Option | 
 **tracking_option** | [**TrackingOption**](TrackingOption.md)|  | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

