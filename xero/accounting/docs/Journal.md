# Journal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_id** | **str** | Xero identifier | [optional] 
**journal_date** | **date** | Date the journal was posted | [optional] 
**journal_number** | **int** | Xero generated journal number | [optional] 
**created_date_utc** | **datetime** | Created date UTC format | [optional] 
**reference** | **str** | reference field for additional indetifying information | [optional] 
**source_id** | **str** | The identifier for the source transaction (e.g. InvoiceID) | [optional] 
**source_type** | **str** | The journal source type. The type of transaction that created the journal | [optional] 
**journal_lines** | [**list[JournalLine]**](JournalLine.md) | See JournalLines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


