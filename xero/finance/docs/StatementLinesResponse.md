# StatementLinesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreconciled_amount_pos** | **float** | Sum of the amounts of all statement lines where both the reconciled flag is set to FALSE, and the amount is positive. | [optional] 
**unreconciled_amount_neg** | **float** | Sum of the amounts of all statement lines where both the reconciled flag is set to FALSE, and the amount is negative. | [optional] 
**unreconciled_lines** | **int** | Count of all statement lines where the reconciled flag is set to FALSE. | [optional] 
**avg_days_unreconciled_pos** | **float** | Sum-product of age of statement line in days multiplied by transaction amount, divided by the sum of transaction amount - in for those statement lines in which the reconciled flag is set to FALSE, and the amount is positive. Provides an indication of the age of unreconciled transactions. | [optional] 
**avg_days_unreconciled_neg** | **float** | Sum-product of age of statement line in days multiplied by transaction amount, divided by the sum of transaction amount - in for those statement lines in which the reconciled flag is set to FALSE, and the amount is negative. Provides an indication of the age of unreconciled transactions. | [optional] 
**earliest_unreconciled_transaction** | **date** | UTC Date which is the earliest transaction date of a statement line for which the reconciled flag is set to FALSE.  This date is represented in ISO 8601 format. | [optional] 
**latest_unreconciled_transaction** | **date** | UTC Date which is the latest transaction date of a statement line for which the reconciled flag is set to FALSE.  This date is represented in ISO 8601 format. | [optional] 
**deleted_amount** | **float** | Sum of the amounts of all deleted statement lines.  Transactions may be deleted due to duplication or otherwise. | [optional] 
**total_amount** | **float** | Sum of the amounts of all statement lines.  This is used as a metric of comparison to the unreconciled figures above. | [optional] 
**data_source** | [**DataSourceResponse**](DataSourceResponse.md) |  | [optional] 
**earliest_reconciled_transaction** | **date** | UTC Date which is the earliest transaction date of a statement line for which the reconciled flag is set to TRUE.  This date is represented in ISO 8601 format. | [optional] 
**latest_reconciled_transaction** | **date** | UTC Date which is the latest transaction date of a statement line for which the reconciled flag is set to TRUE.  This date is represented in ISO 8601 format. | [optional] 
**reconciled_amount_pos** | **float** | Sum of the amounts of all statement lines where both the reconciled flag is set to TRUE, and the amount is positive. | [optional] 
**reconciled_amount_neg** | **float** | Sum of the amounts of all statement lines where both the reconciled flag is set to TRUE, and the amount is negative. | [optional] 
**reconciled_lines** | **int** | Count of all statement lines where the reconciled flag is set to TRUE | [optional] 
**total_amount_pos** | **float** | Sum of the amounts of all statement lines where the amount is positive | [optional] 
**total_amount_neg** | **float** | Sum of the amounts of all statement lines where the amount is negative. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


