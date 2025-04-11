# StatementLineResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_line_id** | **str** | Xero Identifier of statement line | [optional] 
**posted_date** | **date** | Date of when statement line was posted | [optional] 
**payee** | **str** | Payee description of statement line | [optional] 
**reference** | **str** | Reference description of statement line | [optional] 
**notes** | **str** | Notes description of statement line | [optional] 
**cheque_no** | **str** | Cheque number of statement line | [optional] 
**amount** | **float** | Amount of statement line | [optional] 
**transaction_date** | **date** | Transaction date of statement line | [optional] 
**type** | **str** | Type of statement line | [optional] 
**is_reconciled** | **bool** | Boolean to show if statement line is reconciled | [optional] 
**is_duplicate** | **bool** | Boolean to show if statement line is duplicate | [optional] 
**is_deleted** | **bool** | Boolean to show if statement line is deleted | [optional] 
**payments** | [**list[PaymentResponse]**](PaymentResponse.md) | List of payments associated with reconciled statement lines | [optional] 
**bank_transactions** | [**list[BankTransactionResponse]**](BankTransactionResponse.md) | List of bank transactions associated with reconciled statement lines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


