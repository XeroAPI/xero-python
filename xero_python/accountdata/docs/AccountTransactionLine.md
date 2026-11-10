# AccountTransactionLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_number** | **int** | Unique journal number for this transaction. | 
**journal_date** | **date** | Accounting date of the transaction (YYYY-MM-DD). | 
**description** | **str** | Line description, falling back to the journal narration. Empty if neither is set. | 
**account** | [**TransactionAccount**](TransactionAccount.md) |  | 
**net_amount** | [**LedgerDecimal**](LedgerDecimal.md) |  | 
**signed_net_amount** | **float** | Net amount as a signed number (positive for debit, negative for credit). | [optional] 
**tax_amount** | [**LedgerDecimal**](LedgerDecimal.md) |  | [optional] 
**signed_tax_amount** | **float** | Tax amount as a signed number (positive for debit, negative for credit). | [optional] 
**source** | [**LineSource**](LineSource.md) |  | 
**tax_rate** | [**LineTaxRate**](LineTaxRate.md) |  | 
**tracking_categories** | [**dict(str, TrackingItemDetails)**](TrackingItemDetails.md) | Present only when &#x60;include&#x3D;trackingCategories&#x60; was requested, and omitted otherwise. Keys are tracking category IDs (UUIDs); values describe the selected tracking option. The object is empty when the line has no tracking.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


