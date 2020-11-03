# BankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Bank account name (max length &#x3D; 32) | 
**account_number** | **str** | Bank account number (digits only; max length &#x3D; 8) | 
**sort_code** | **str** | Bank account sort code (6 digits) | 
**particulars** | **str** | Particulars that appear on the statement. | [optional] 
**code** | **str** | Code of a transaction that appear on the statement. | [optional] 
**dollar_amount** | **float** | Dollar amount of a transaction. | [optional] 
**reference** | **str** | Statement Text/reference for a transaction that appear on the statement. | [optional] 
**calculation_type** | **str** | Calculation type for the transaction can be &#39;Fixed Amount&#39; or &#39;Balance&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


