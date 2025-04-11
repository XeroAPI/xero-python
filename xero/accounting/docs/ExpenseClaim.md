# ExpenseClaim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_claim_id** | **str** | Xero generated unique identifier for an expense claim | [optional] 
**status** | **str** | Current status of an expense claim – see status types | [optional] 
**payments** | [**list[Payment]**](Payment.md) | See Payments | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**receipts** | [**list[Receipt]**](Receipt.md) |  | [optional] 
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**total** | **float** | The total of an expense claim being paid | [optional] 
**amount_due** | **float** | The amount due to be paid for an expense claim | [optional] 
**amount_paid** | **float** | The amount still to pay for an expense claim | [optional] 
**payment_due_date** | **date** | The date when the expense claim is due to be paid YYYY-MM-DD | [optional] 
**reporting_date** | **date** | The date the expense claim will be reported in Xero YYYY-MM-DD | [optional] 
**receipt_id** | **str** | The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


