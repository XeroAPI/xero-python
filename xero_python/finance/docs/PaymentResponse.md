# PaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | Xero Identifier of payment | [optional] 
**batch_payment_id** | **str** | Xero Identifier of batch payment. Present if the payment was created as part of a batch. | [optional] 
**date** | **datetime** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 | [optional] 
**amount** | **float** | The amount of the payment | [optional] 
**bank_amount** | **float** | The bank amount of the payment | [optional] 
**currency_rate** | **float** | Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500 | [optional] 
**invoice** | [**InvoiceResponse**](InvoiceResponse.md) |  | [optional] 
**credit_note** | [**CreditNoteResponse**](CreditNoteResponse.md) |  | [optional] 
**prepayment** | [**PrepaymentResponse**](PrepaymentResponse.md) |  | [optional] 
**overpayment** | [**OverpaymentResponse**](OverpaymentResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


