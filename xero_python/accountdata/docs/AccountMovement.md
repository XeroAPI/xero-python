# AccountMovement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account this movement is for. | 
**date_range** | [**AccountingDateRange**](AccountingDateRange.md) |  | 
**debits** | **float** | Total debits posted to this account within the date range. | 
**credits** | **float** | Total credits posted to this account within the date range. | 
**movement** | [**LedgerDecimal**](LedgerDecimal.md) |  | 
**signed_movement** | **float** | Movement as a signed number (positive for debit, negative for credit). | 
**tax_debits** | **float** | Total tax debits within the date range. Omitted from the response when tax values are not available. | [optional] 
**tax_credits** | **float** | Total tax credits within the date range. Omitted from the response when tax values are not available. | [optional] 
**signed_tax_movement** | **float** | Tax movement as a signed number (positive for debit, negative for credit). Omitted from the response when tax values are not available. | [optional] 
**account** | [**Account**](Account.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


