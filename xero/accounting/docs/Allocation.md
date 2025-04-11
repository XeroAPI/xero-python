# Allocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_id** | **str** | Xero generated unique identifier | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | 
**overpayment** | [**Overpayment**](Overpayment.md) |  | [optional] 
**prepayment** | [**Prepayment**](Prepayment.md) |  | [optional] 
**credit_note** | [**CreditNote**](CreditNote.md) |  | [optional] 
**amount** | **float** | the amount being applied to the invoice | 
**date** | **date** | the date the allocation is applied YYYY-MM-DD. | 
**is_deleted** | **bool** | A flag that returns true when the allocation is succesfully deleted | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


