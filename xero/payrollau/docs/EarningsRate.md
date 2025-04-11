# EarningsRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the earnings rate (max length &#x3D; 100) | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**type_of_units** | **str** | Type of units used to record earnings (max length &#x3D; 50). Only When RateType is RATEPERUNIT | [optional] 
**is_exempt_from_tax** | **bool** | Most payments are subject to tax, so you should only set this value if you are sure that a payment is exempt from PAYG withholding | [optional] 
**is_exempt_from_super** | **bool** | See the ATO website for details of which payments are exempt from SGC | [optional] 
**is_reportable_as_w1** | **bool** | Boolean to determine if the earnings rate is reportable or exempt from W1 | [optional] 
**allowance_contributes_to_annual_leave_rate** | **bool** | Boolean to determine if the allowance earnings rate contributes towards annual leave rate. Only applicable if EarningsType is ALLOWANCE and RateType is RATEPERUNIT | [optional] 
**allowance_contributes_to_overtime_rate** | **bool** | Boolean to determine if the allowance earnings rate contributes towards overtime allowance rate. Only applicable if EarningsType is ALLOWANCE and RateType is RATEPERUNIT | [optional] 
**earnings_type** | [**EarningsType**](EarningsType.md) |  | [optional] 
**earnings_rate_id** | **str** | Xero identifier | [optional] 
**rate_type** | [**RateType**](RateType.md) |  | [optional] 
**rate_per_unit** | **str** | Default rate per unit (optional). Only applicable if RateType is RATEPERUNIT. | [optional] 
**multiplier** | **float** | This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MULTIPLE | [optional] 
**accrue_leave** | **bool** | Indicates that this earnings rate should accrue leave. Only applicable if RateType is MULTIPLE | [optional] 
**amount** | **float** | Optional Amount for FIXEDAMOUNT RateType EarningsRate | [optional] 
**employment_termination_payment_type** | [**EmploymentTerminationPaymentType**](EmploymentTerminationPaymentType.md) |  | [optional] 
**updated_date_utc** | **datetime** | Last modified timestamp | [optional] 
**current_record** | **bool** | Is the current record | [optional] 
**allowance_type** | [**AllowanceType**](AllowanceType.md) |  | [optional] 
**allowance_category** | [**AllowanceCategory**](AllowanceCategory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


