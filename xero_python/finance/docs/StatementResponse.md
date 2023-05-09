# StatementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | Xero Identifier of statement | [optional] 
**start_date** | **date** | Start date of statement | [optional] 
**end_date** | **date** | End date of statement | [optional] 
**imported_date_time_utc** | **datetime** | Utc date time of when the statement was imported in Xero | [optional] 
**import_source** | **str** | Identifies where the statement data in Xero was sourced, 1) direct bank feed, automatically loaded from the bank (eg STMTIMPORTSRC/CBAFEED); 2) indirect bank feed, automatically loaded from a 3rd party provider (eg STMTIMPORTSRC/YODLEE); 3) manually uploaded bank feed (eg STMTIMPORTSRC/CSV) or 4) manually entered statement data (STMTIMPORTSRC/MANUAL). | [optional] 
**start_balance** | **float** | Opening balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0. | [optional] 
**end_balance** | **float** | Closing balance sourced from imported bank statements (if supplied). Note, for manually uploaded statements, this balance is also manual and usually not supplied. Where not supplied, the value will be 0. | [optional] 
**indicative_start_balance** | **float** | Opening statement balance calculated in Xero (&#x3D; bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn&#39;t match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there&#39;s an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion&#x3D;true  | [optional] 
**indicative_end_balance** | **float** | Closing statement balance calculated in Xero (&#x3D; bank account conversion balance plus sum of imported bank statement lines). Note: If indicative statement balance doesn&#39;t match imported statement balance for the same date, either the conversion (opening at inception) balance in Xero is wrong or there&#39;s an error in the bank statement lines in Xero. Ref: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance?userregion&#x3D;true   | [optional] 
**statement_lines** | [**list[StatementLineResponse]**](StatementLineResponse.md) | List of statement lines | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


