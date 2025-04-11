# BankTransactionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transaction_id** | **str** | Xero Identifier of transaction | [optional] 
**batch_payment_id** | **str** | Xero Identifier of batch payment. Present if the transaction is part of a batch. | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**date** | **date** | Date of transaction - YYYY-MM-DD | [optional] 
**amount** | **float** | Amount of transaction | [optional] 
**line_items** | [**list[LineItemResponse]**](LineItemResponse.md) | The LineItems element can contain any number of individual LineItem sub-elements. Not included in summary mode | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


