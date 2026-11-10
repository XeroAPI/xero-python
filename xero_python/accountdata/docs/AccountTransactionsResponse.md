# AccountTransactionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Organisation&#39;s base currency code (ISO 4217). | 
**max_journal_number** | **int** | Maximum journal number included in this result set. Captured at the first request and held constant across all pages for consistency.  | 
**lines** | [**list[AccountTransactionLine]**](AccountTransactionLine.md) | Transaction lines for this page (max 200). | 
**pagination** | [**AccountTransactionsResponsePagination**](AccountTransactionsResponsePagination.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


