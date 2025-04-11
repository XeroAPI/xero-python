# PaymentService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_service_id** | **str** | Xero identifier | [optional] 
**payment_service_name** | **str** | Name of payment service | [optional] 
**payment_service_url** | **str** | The custom payment URL | [optional] 
**pay_now_text** | **str** | The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card | [optional] 
**payment_service_type** | **str** | This will always be CUSTOM for payment services created via the API. | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


