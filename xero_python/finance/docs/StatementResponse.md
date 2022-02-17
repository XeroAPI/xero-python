# StatementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | Xero Identifier of statement | [optional] 
**start_date** | **datetime** | Start date of statement | [optional] 
**end_date** | **datetime** | End date of statement | [optional] 
**imported_date_time_utc** | **datetime** | Utc date time of when the statement was imported in Xero | [optional] 
**import_source** | **str** | Import source of statement (STMTIMPORTSRC/MANUAL, STMTIMPORTSRC/CSV, STMTIMPORTSRC/QIF, STMTIMPORTSRC/OFX, XeroApi) | [optional] 
**statement_lines** | [**list[StatementLineResponse]**](StatementLineResponse.md) | List of statement lines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


