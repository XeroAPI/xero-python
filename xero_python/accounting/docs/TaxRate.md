# TaxRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tax rate | [optional] 
**tax_type** | **str** | The tax type | [optional] 
**tax_components** | [**list[TaxComponent]**](TaxComponent.md) | See TaxComponents | [optional] 
**status** | **str** | See Status Codes | [optional] 
**report_tax_type** | **str** | See ReportTaxTypes | [optional] 
**can_apply_to_assets** | **bool** | Boolean to describe if tax rate can be used for asset accounts i.e.  true,false | [optional] 
**can_apply_to_equity** | **bool** | Boolean to describe if tax rate can be used for equity accounts i.e true,false | [optional] 
**can_apply_to_expenses** | **bool** | Boolean to describe if tax rate can be used for expense accounts  i.e. true,false | [optional] 
**can_apply_to_liabilities** | **bool** | Boolean to describe if tax rate can be used for liability accounts  i.e. true,false | [optional] 
**can_apply_to_revenue** | **bool** | Boolean to describe if tax rate can be used for revenue accounts i.e. true,false | [optional] 
**display_tax_rate** | **float** | Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] 
**effective_rate** | **float** | Effective Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


