# PayRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_calendar_id** | **str** | Xero identifier for pay run | 
**pay_run_id** | **str** | Xero identifier for pay run | [optional] 
**pay_run_period_start_date** | **date** | Period Start Date for the PayRun (YYYY-MM-DD) | [optional] 
**pay_run_period_end_date** | **date** | Period End Date for the PayRun (YYYY-MM-DD) | [optional] 
**pay_run_status** | [**PayRunStatus**](PayRunStatus.md) |  | [optional] 
**payment_date** | **date** | Payment Date for the PayRun (YYYY-MM-DD) | [optional] 
**payslip_message** | **str** | Payslip message for the PayRun | [optional] 
**updated_date_utc** | **datetime** | Last modified timestamp | [optional] 
**payslips** | [**list[PayslipSummary]**](PayslipSummary.md) | The payslips in the payrun | [optional] 
**wages** | **float** | The total Wages for the Payrun | [optional] 
**deductions** | **float** | The total Deductions for the Payrun | [optional] 
**tax** | **float** | The total Tax for the Payrun | [optional] 
**super** | **float** | The total Super for the Payrun | [optional] 
**reimbursement** | **float** | The total Reimbursements for the Payrun | [optional] 
**net_pay** | **float** | The total NetPay for the Payrun | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


