# EmployeeLeaveSetup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_holiday_pay** | **bool** | Identifier if holiday pay will be included in each payslip | [optional] 
**holiday_pay_opening_balance** | **float** | Initial holiday pay balance. A percentage — usually 8% — of gross earnings since their last work anniversary. | [optional] 
**annual_leave_opening_balance** | **float** | Initial annual leave balance. The balance at their last anniversary, less any leave taken since then and excluding accrued annual leave. | [optional] 
**negative_annual_leave_balance_paid_amount** | **float** | The dollar value of annual leave opening balance if negative. | [optional] 
**sick_leave_hours_to_accrue_annually** | **float** | Number of hours accrued annually for sick leave. Multiply the number of days they&#39;re entitled to by the hours worked per day | [optional] 
**sick_leave_maximum_hours_to_accrue** | **float** | Maximum number of hours accrued annually for sick leave. Multiply the maximum days they can accrue by the hours worked per day | [optional] 
**sick_leave_opening_balance** | **float** | Initial sick leave balance. This will be positive unless they&#39;ve taken sick leave in advance | [optional] 
**sick_leave_schedule_of_accrual** | **str** | Set Schedule of Accrual Type for Sick Leave | [optional] 
**sick_leave_anniversary_date** | **date** | If Sick Leave Schedule of Accrual is \&quot;OnAnniversaryDate\&quot;, this is the date when entitled to Sick Leave | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


