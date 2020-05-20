# Receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **date** | Date of receipt – YYYY-MM-DD | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**sub_total** | **float** | Total of receipt excluding taxes | [optional] 
**total_tax** | **float** | Total tax on receipt | [optional] 
**total** | **float** | Total of receipt tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**receipt_id** | **str** | Xero generated unique identifier for receipt | [optional] 
**status** | **str** | Current status of receipt – see status types | [optional] 
**receipt_number** | **str** | Xero generated sequence number for receipt in current claim for a given user | [optional] 
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**has_attachments** | **bool** | boolean to indicate if a receipt has an attachment | [optional] [default to False]
**url** | **str** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**list[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


