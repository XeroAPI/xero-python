# ManualJournal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**narration** | **str** | Description of journal being posted | 
**journal_lines** | [**list[ManualJournalLine]**](ManualJournalLine.md) | See JournalLines | [optional] 
**date** | **date** | Date journal was posted – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**status** | **str** | See Manual Journal Status Codes | [optional] 
**url** | **str** | Url link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**show_on_cash_basis_reports** | **bool** | Boolean – default is true if not specified | [optional] 
**has_attachments** | **bool** | Boolean to indicate if a manual journal has an attachment | [optional] [default to False]
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**manual_journal_id** | **str** | The Xero identifier for a Manual Journal | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**warnings** | [**list[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


