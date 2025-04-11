# TaxDeclaration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Address line 1 for employee home address | [optional] 
**employment_basis** | [**EmploymentBasis**](EmploymentBasis.md) |  | [optional] 
**tfn_exemption_type** | [**TFNExemptionType**](TFNExemptionType.md) |  | [optional] 
**tax_file_number** | **str** | The tax file number e.g 123123123. | [optional] 
**abn** | **str** | 11-digit Australian Business Number e.g 21006819692 or an empty string (\&quot;\&quot;) to unset a previously set value. Only applicable, and mandatory if income type is NONEMPLOYEE. | [optional] 
**australian_resident_for_tax_purposes** | **bool** | If the employee is Australian resident for tax purposes. e.g true or false | [optional] 
**residency_status** | [**ResidencyStatus**](ResidencyStatus.md) |  | [optional] 
**tax_scale_type** | [**TaxScaleType**](TaxScaleType.md) |  | [optional] 
**work_condition** | [**WorkCondition**](WorkCondition.md) |  | [optional] 
**senior_marital_status** | [**SeniorMaritalStatus**](SeniorMaritalStatus.md) |  | [optional] 
**tax_free_threshold_claimed** | **bool** | If tax free threshold claimed. e.g true or false | [optional] 
**tax_offset_estimated_amount** | **float** | If has tax offset estimated then the tax offset estimated amount. e.g 100 | [optional] 
**has_help_debt** | **bool** | If employee has HECS or HELP debt. e.g true or false | [optional] 
**has_sfss_debt** | **bool** | If employee has financial supplement debt. e.g true or false | [optional] 
**has_trade_support_loan_debt** | **bool** | If employee has trade support loan. e.g true or false | [optional] 
**upward_variation_tax_withholding_amount** | **float** | If the employee has requested that additional tax be withheld each pay run. e.g 50 | [optional] 
**eligible_to_receive_leave_loading** | **bool** | If the employee is eligible to receive an additional percentage on top of ordinary earnings when they take leave (typically 17.5%). e.g true or false | [optional] 
**approved_withholding_variation_percentage** | **float** | If the employee has approved withholding variation. e.g (0 - 100) | [optional] 
**has_student_startup_loan** | **bool** | If the employee is eligible for student startup loan rules | [optional] 
**has_loan_or_student_debt** | **bool** | If the employee has any of the following loans or debts: Higher Education Loan Program (HELP/HECS), VET Student Loan (VSL), Financial Supplement (FS), Student Start-up Loan (SSL), or Trade Support Loan (TSL) | [optional] 
**updated_date_utc** | **datetime** | Last modified timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


