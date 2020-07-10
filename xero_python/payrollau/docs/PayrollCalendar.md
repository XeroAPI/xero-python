# PayrollCalendar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Payroll Calendar | [optional] 
**calendar_type** | [**CalendarType**](CalendarType.md) |  | [optional] 
**start_date** | **date** | The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD) | [optional] 
**payment_date** | **date** | The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD) | [optional] 
**payroll_calendar_id** | **str** | Xero identifier | [optional] 
**updated_date_utc** | **datetime** | Last modified timestamp | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


