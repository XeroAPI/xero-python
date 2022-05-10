# StatementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | Xero Identifier of statement | [optional] 
**start_date** | **date** | Start date of statement | [optional] 
**end_date** | **date** | End date of statement | [optional] 
**imported_date_time_utc** | **datetime** | Utc date time of when the statement was imported in Xero | [optional] 
**import_source** | **str** | Indicates the source of the statement data. Either imported from 1) direct bank feed OR 2) manual customer entry or upload. Manual import sources are STMTIMPORTSRC/MANUAL, STMTIMPORTSRC/CSV, STMTIMPORTSRC/OFX, Ofx or STMTIMPORTSRC/QIF. All other import sources are direct and, depending on the direct solution, may contain the name of the financial institution. | [optional] 
**start_balance** | **float** | Opening balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. | [optional] 
**end_balance** | **float** | Closing balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. | [optional] 
**statement_lines** | [**list[StatementLineResponse]**](StatementLineResponse.md) | List of statement lines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


