# TimesheetEarningsLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_line_id** | **str** | Xero identifier for payroll earnings line | [optional] 
**earnings_rate_id** | **str** | Xero identifier for payroll leave earnings rate | [optional] 
**display_name** | **str** | name of earnings rate for display in UI | [optional] 
**rate_per_unit** | **float** | Rate per unit for leave earnings line | [optional] 
**number_of_units** | **float** | Leave earnings number of units | [optional] 
**fixed_amount** | **float** | Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed | [optional] 
**amount** | **float** | The amount of the earnings line. | [optional] 
**is_linked_to_timesheet** | **bool** | Identifies if the leave earnings is taken from the timesheet. False for leave earnings line | [optional] 
**is_average_daily_pay_rate** | **bool** | Identifies if the earnings is using an average daily pay rate | [optional] 
**is_system_generated** | **bool** | Flag to identify whether the earnings line is system generated or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


