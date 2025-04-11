# InvoiceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Xero Identifier of invoice | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode | [optional] 
**line_items** | [**list[LineItemResponse]**](LineItemResponse.md) | Not included in summary mode | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


