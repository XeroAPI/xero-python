# Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The Xero-generated Id for the asset | [optional] 
**asset_name** | **str** | The name of the asset | 
**asset_type_id** | **str** | The Xero-generated Id for the asset type | [optional] 
**asset_number** | **str** | Must be unique. | [optional] 
**purchase_date** | **date** | The date the asset was purchased YYYY-MM-DD | [optional] 
**purchase_price** | **float** | The purchase price of the asset | [optional] 
**disposal_price** | **float** | The price the asset was disposed at | [optional] 
**asset_status** | [**AssetStatus**](AssetStatus.md) |  | [optional] 
**warranty_expiry_date** | **str** | The date the asset’s warranty expires (if needed) YYYY-MM-DD | [optional] 
**serial_number** | **str** | The asset&#39;s serial number | [optional] 
**book_depreciation_setting** | [**BookDepreciationSetting**](BookDepreciationSetting.md) |  | [optional] 
**book_depreciation_detail** | [**BookDepreciationDetail**](BookDepreciationDetail.md) |  | [optional] 
**can_rollback** | **bool** | Boolean to indicate whether depreciation can be rolled back for this asset individually. This is true if it doesn&#39;t have &#39;legacy&#39; journal entries and if there is no lock period that would prevent this asset from rolling back. | [optional] 
**accounting_book_value** | **float** | The accounting value of the asset | [optional] 
**is_delete_enabled_for_date** | **bool** | Boolean to indicate whether delete is enabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


