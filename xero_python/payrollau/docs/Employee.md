# Employee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of employee | 
**last_name** | **str** | Last name of employee | 
**date_of_birth** | **date** | Date of birth of the employee (YYYY-MM-DD) | 
**home_address** | [**HomeAddress**](HomeAddress.md) |  | [optional] 
**start_date** | **date** | Start date for an employee (YYYY-MM-DD) | [optional] 
**title** | **str** | Title of the employee | [optional] 
**middle_names** | **str** | Middle name(s) of the employee | [optional] 
**email** | **str** | The email address for the employee | [optional] 
**gender** | **str** | The employee’s gender. See Employee Gender | [optional] 
**phone** | **str** | Employee phone number | [optional] 
**mobile** | **str** | Employee mobile number | [optional] 
**twitter_user_name** | **str** | Employee’s twitter name | [optional] 
**is_authorised_to_approve_leave** | **bool** | Authorised to approve other employees&#39; leave requests | [optional] 
**is_authorised_to_approve_timesheets** | **bool** | Authorised to approve timesheets | [optional] 
**job_title** | **str** | JobTitle of the employee | [optional] 
**classification** | **str** | Employees classification | [optional] 
**ordinary_earnings_rate_id** | **str** | Xero unique identifier for earnings rate | [optional] 
**payroll_calendar_id** | **str** | Xero unique identifier for payroll calendar for the employee | [optional] 
**employee_group_name** | **str** | The Employee Group allows you to report on payroll expenses and liabilities for each group of employees | [optional] 
**employee_id** | **str** | Xero unique identifier for an Employee | [optional] 
**termination_date** | **date** | Employee Termination Date (YYYY-MM-DD) | [optional] 
**termination_reason** | **str** | * &#x60;V&#x60; Voluntary cessation - An employee resignation, retirement, domestic or pressing necessity or abandonment of employment * &#x60;I&#x60; Ill health - An employee resignation due to medical condition that prevents the continuation of employment, such as for illness, ill-health, medical unfitness or total permanent disability * &#x60;D&#x60; Deceased - The death of an employee * &#x60;R&#x60; Redundancy - An employer-initiated termination of employment due to a genuine redundancy or approved early retirement scheme * &#x60;F&#x60; Dismissal - An employer-initiated termination of employment due to dismissal, inability to perform the required work, misconduct or inefficiency * &#x60;C&#x60; Contract cessation - The natural conclusion of a limited employment relationship due to contract/engagement duration or task completion, seasonal work completion, or to cease casuals that are no longer required * &#x60;T&#x60; Transfer - The administrative arrangements performed to transfer employees across payroll systems, move them temporarily to another employer (machinery of government for public servants), transfer of business, move them to outsourcing arrangements or other such technical activities.  | [optional] 
**bank_accounts** | [**list[BankAccount]**](BankAccount.md) |  | [optional] 
**pay_template** | [**PayTemplate**](PayTemplate.md) |  | [optional] 
**opening_balances** | [**OpeningBalances**](OpeningBalances.md) |  | [optional] 
**tax_declaration** | [**TaxDeclaration**](TaxDeclaration.md) |  | [optional] 
**leave_balances** | [**list[LeaveBalance]**](LeaveBalance.md) |  | [optional] 
**leave_lines** | [**list[LeaveLine]**](LeaveLine.md) |  | [optional] 
**super_memberships** | [**list[SuperMembership]**](SuperMembership.md) |  | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**updated_date_utc** | **datetime** | Last modified timestamp | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


