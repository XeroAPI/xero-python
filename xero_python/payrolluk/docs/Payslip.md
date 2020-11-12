# Payslip

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_slip_id** | **str** | The Xero identifier for a Payslip | [optional] 
**employee_id** | **str** | The Xero identifier for payroll employee | [optional] 
**pay_run_id** | **str** | The Xero identifier for the associated payrun | [optional] 
**last_edited** | **date** | The date payslip was last updated | [optional] 
**first_name** | **str** | Employee first name | [optional] 
**last_name** | **str** | Employee last name | [optional] 
**total_earnings** | **float** | Total earnings before any deductions. Same as gross earnings for UK. | [optional] 
**gross_earnings** | **float** | Total earnings before any deductions. Same as total earnings for UK. | [optional] 
**total_pay** | **float** | The employee net pay | [optional] 
**total_employer_taxes** | **float** | The employer&#39;s tax obligation | [optional] 
**total_employee_taxes** | **float** | The part of an employee&#39;s earnings that is deducted for tax purposes | [optional] 
**total_deductions** | **float** | Total amount subtracted from an employee&#39;s earnings to reach total pay | [optional] 
**total_reimbursements** | **float** | Total reimbursements are nontaxable payments to an employee used to repay out-of-pocket expenses when the person incurs those expenses through employment | [optional] 
**total_court_orders** | **float** | Total amounts required by law to subtract from the employee&#39;s earnings | [optional] 
**total_benefits** | **float** | Benefits (also called fringe benefits, perquisites or perks) are various non-earnings compensations provided to employees in addition to their normal earnings or salaries | [optional] 
**bacs_hash** | **str** | BACS Service User Number | [optional] 
**payment_method** | **str** | The payment method code | [optional] 
**earnings_lines** | [**list[EarningsLine]**](EarningsLine.md) |  | [optional] 
**leave_earnings_lines** | [**list[LeaveEarningsLine]**](LeaveEarningsLine.md) |  | [optional] 
**timesheet_earnings_lines** | [**list[TimesheetEarningsLine]**](TimesheetEarningsLine.md) |  | [optional] 
**deduction_lines** | [**list[DeductionLine]**](DeductionLine.md) |  | [optional] 
**reimbursement_lines** | [**list[ReimbursementLine]**](ReimbursementLine.md) |  | [optional] 
**leave_accrual_lines** | [**list[LeaveAccrualLine]**](LeaveAccrualLine.md) |  | [optional] 
**benefit_lines** | [**list[BenefitLine]**](BenefitLine.md) |  | [optional] 
**payment_lines** | [**list[PaymentLine]**](PaymentLine.md) |  | [optional] 
**employee_tax_lines** | [**list[TaxLine]**](TaxLine.md) |  | [optional] 
**employer_tax_lines** | [**list[TaxLine]**](TaxLine.md) |  | [optional] 
**court_order_lines** | [**list[CourtOrderLine]**](CourtOrderLine.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


