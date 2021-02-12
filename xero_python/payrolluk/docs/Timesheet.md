# Timesheet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timesheet_id** | **str** | The Xero identifier for a Timesheet | [optional] 
**payroll_calendar_id** | **str** | The Xero identifier for the Payroll Calendar that the Timesheet applies to | 
**employee_id** | **str** | The Xero identifier for the Employee that the Timesheet is for | 
**start_date** | **date** | The Start Date of the Timesheet period (YYYY-MM-DD) | 
**end_date** | **date** | The End Date of the Timesheet period (YYYY-MM-DD) | 
**status** | **str** | Status of the timesheet | [optional] 
**total_hours** | **float** | The Total Hours of the Timesheet | [optional] 
**updated_date_utc** | **datetime** | The UTC date time that the Timesheet was last updated | [optional] 
**timesheet_lines** | [**list[TimesheetLine]**](TimesheetLine.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


