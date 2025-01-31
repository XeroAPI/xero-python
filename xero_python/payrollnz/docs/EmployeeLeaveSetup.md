# EmployeeLeaveSetup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_holiday_pay** | **bool** | Identifier if holiday pay will be included in each payslip | [optional] 
**holiday_pay_opening_balance** | **float** | Initial holiday pay balance. A percentage — usually 8% — of gross earnings since their last work anniversary. | [optional] 
**annual_leave_opening_balance** | **float** | Initial annual leave balance. The balance at their last anniversary, less any leave taken since then and excluding accrued annual leave. | [optional] 
**negative_annual_leave_balance_paid_amount** | **float** | The dollar value of annual leave opening balance if negative. | [optional] 
**sick_leave_hours_to_accrue_annually** | **float** | Deprecated use SickLeaveToAccrueAnnually | [optional] 
**sick_leave_maximum_hours_to_accrue** | **float** | Deprecated use SickLeaveMaximumToAccrue | [optional] 
**sick_leave_to_accrue_annually** | **float** | Number of units accrued annually for sick leave. The type of units is determined by the property \&quot;TypeOfUnitsToAccrue\&quot; on the \&quot;Sick Leave\&quot; leave type | [optional] 
**sick_leave_maximum_to_accrue** | **float** | Maximum number of units accrued annually for sick leave. The type of units is determined by the property \&quot;TypeOfUnitsToAccrue\&quot; on the \&quot;Sick Leave\&quot; leave type | [optional] 
**sick_leave_opening_balance** | **float** | Initial sick leave balance. This will be positive unless they&#39;ve taken sick leave in advance | [optional] 
**sick_leave_schedule_of_accrual** | **str** | Set Schedule of Accrual Type for Sick Leave | [optional] 
**sick_leave_anniversary_date** | **date** | If Sick Leave Schedule of Accrual is \&quot;OnAnniversaryDate\&quot;, this is the date when entitled to Sick Leave. When null the Employee&#39;s start date is used as the anniversary date | [optional] 
**annual_leave_anniversary_date** | **date** | The first date the employee will accrue Annual Leave. When null the Employee&#39;s start date is used as the anniversary date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


