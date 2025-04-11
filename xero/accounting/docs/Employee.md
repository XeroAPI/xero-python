# Employee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | The Xero identifier for an employee e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**status** | **str** | Current status of an employee – see contact status types | [optional] 
**first_name** | **str** | First name of an employee (max length &#x3D; 255) | [optional] 
**last_name** | **str** | Last name of an employee (max length &#x3D; 255) | [optional] 
**external_link** | [**ExternalLink**](ExternalLink.md) |  | [optional] 
**updated_date_utc** | **datetime** |  | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


