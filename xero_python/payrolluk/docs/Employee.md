# Employee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Xero unique identifier for the employee | [optional] 
**title** | **str** | Title of the employee | [optional] 
**first_name** | **str** | First name of employee | [optional] 
**last_name** | **str** | Last name of employee | [optional] 
**date_of_birth** | **date** | Date of birth of the employee (YYYY-MM-DD) | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**email** | **str** | The email address for the employee | [optional] 
**gender** | **str** | The employee’s gender | [optional] 
**phone_number** | **str** | Employee phone number | [optional] 
**start_date** | **date** | Employment start date of the employee at the time it was requested | [optional] 
**end_date** | **date** | Employment end date of the employee at the time it was requested | [optional] 
**payroll_calendar_id** | **str** | Xero unique identifier for the payroll calendar of the employee | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the employee | [optional] 
**created_date_utc** | **datetime** | UTC timestamp when the employee was created in Xero | [optional] 
**ni_category** | [**NICategoryLetter**](NICategoryLetter.md) |  | [optional] 
**ni_categories** | [**list[NICategory]**](NICategory.md) | The employee&#39;s NI categories | [optional] 
**national_insurance_number** | **str** | National insurance number of the employee | [optional] 
**is_off_payroll_worker** | **bool** | Whether the employee is an off payroll worker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


