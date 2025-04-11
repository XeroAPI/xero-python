# ManualJournalLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_amount** | **float** | total for line. Debits are positive, credits are negative value | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**account_id** | **str** | See Accounts | [optional] 
**description** | **str** | Description for journal line | [optional] 
**tax_type** | **str** | The tax type from TaxRates | [optional] 
**tracking** | [**list[TrackingCategory]**](TrackingCategory.md) | Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 
**tax_amount** | **float** | The calculated tax amount based on the TaxType and LineAmount | [optional] 
**is_blank** | **bool** | is the line blank | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


