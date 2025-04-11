# BankTransfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_bank_account** | [**Account**](Account.md) |  | 
**to_bank_account** | [**Account**](Account.md) |  | 
**amount** | **float** | amount of the transaction | 
**date** | **date** | The date of the Transfer YYYY-MM-DD | [optional] 
**bank_transfer_id** | **str** | The identifier of the Bank Transfer | [optional] 
**currency_rate** | **float** | The currency rate | [optional] 
**from_bank_transaction_id** | **str** | The Bank Transaction ID for the source account | [optional] 
**to_bank_transaction_id** | **str** | The Bank Transaction ID for the destination account | [optional] 
**from_is_reconciled** | **bool** | The Bank Transaction boolean to show if it is reconciled for the source account | [optional] [default to False]
**to_is_reconciled** | **bool** | The Bank Transaction boolean to show if it is reconciled for the destination account | [optional] [default to False]
**reference** | **str** | Reference for the transactions. | [optional] 
**has_attachments** | **bool** | Boolean to indicate if a Bank Transfer has an attachment | [optional] [default to False]
**created_date_utc** | **datetime** | UTC timestamp of creation date of bank transfer | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


