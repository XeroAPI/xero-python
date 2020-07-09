# Timesheet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | The Xero identifier for an employee | 
**start_date** | **str** | Period start date (YYYY-MM-DD) | 
**end_date** | **str** | Period end date (YYYY-MM-DD) | 
**status** | [**TimesheetStatus**](TimesheetStatus.md) |  | [optional] 
**hours** | **float** | Timesheet total hours | [optional] 
**timesheet_id** | **str** | The Xero identifier for a Payroll Timesheet | [optional] 
**timesheet_lines** | [**list[TimesheetLine]**](TimesheetLine.md) |  | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


