# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**credit_note** | [**CreditNote**](CreditNote.md) |  | [optional] 
**prepayment** | [**Prepayment**](Prepayment.md) |  | [optional] 
**overpayment** | [**Overpayment**](Overpayment.md) |  | [optional] 
**invoice_number** | **str** | Number of invoice or credit note you are applying payment to e.g.INV-4003 | [optional] 
**credit_note_number** | **str** | Number of invoice or credit note you are applying payment to e.g. INV-4003 | [optional] 
**batch_payment** | [**BatchPayment**](BatchPayment.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**code** | **str** | Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value) | [optional] 
**date** | **date** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 | [optional] 
**currency_rate** | **float** | Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500 | [optional] 
**amount** | **float** | The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00 | [optional] 
**bank_amount** | **float** | The amount of the payment in the currency of the bank account. | [optional] 
**reference** | **str** | An optional description for the payment e.g. Direct Debit | [optional] 
**is_reconciled** | **bool** | An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET | [optional] 
**status** | **str** | The status of the payment. | [optional] 
**payment_type** | **str** | See Payment Types. | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the payment | [optional] 
**payment_id** | **str** | The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**batch_payment_id** | **str** | Present if the payment was created as part of a batch. | [optional] 
**bank_account_number** | **str** | The suppliers bank account number the payment is being made to | [optional] 
**particulars** | **str** | The suppliers bank account number the payment is being made to | [optional] 
**details** | **str** | The information to appear on the supplier&#39;s bank account | [optional] 
**has_account** | **bool** | A boolean to indicate if a contact has an validation errors | [optional] [default to False]
**has_validation_errors** | **bool** | A boolean to indicate if a contact has an validation errors | [optional] [default to False]
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**list[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


