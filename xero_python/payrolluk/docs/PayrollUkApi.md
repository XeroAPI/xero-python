# xero_python.payrolluk.PayrollUkApi

All URIs are relative to *https://api.xero.com/payroll.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_timesheet**](PayrollUkApi.md#approve_timesheet) | **POST** /Timesheets/{TimesheetID}/Approve | approve a timesheet
[**create_benefit**](PayrollUkApi.md#create_benefit) | **POST** /Benefits | create a new benefit
[**create_deduction**](PayrollUkApi.md#create_deduction) | **POST** /Deductions | create a new deduction
[**create_earnings_rate**](PayrollUkApi.md#create_earnings_rate) | **POST** /EarningsRates | create a new earnings rate
[**create_employee**](PayrollUkApi.md#create_employee) | **POST** /Employees | creates employees
[**create_employee_earnings_template**](PayrollUkApi.md#create_employee_earnings_template) | **POST** /Employees/{EmployeeId}/PayTemplates/earnings | creates employee earnings template records
[**create_employee_leave**](PayrollUkApi.md#create_employee_leave) | **POST** /Employees/{EmployeeId}/Leave | creates employee leave records
[**create_employee_leave_type**](PayrollUkApi.md#create_employee_leave_type) | **POST** /Employees/{EmployeeId}/LeaveTypes | creates employee leave type records
[**create_employee_opening_balances**](PayrollUkApi.md#create_employee_opening_balances) | **POST** /Employees/{EmployeeId}/ukopeningbalances | creates employee opening balances
[**create_employee_payment_method**](PayrollUkApi.md#create_employee_payment_method) | **POST** /Employees/{EmployeeId}/PaymentMethods | creates employee payment method
[**create_employee_salary_and_wage**](PayrollUkApi.md#create_employee_salary_and_wage) | **POST** /Employees/{EmployeeId}/SalaryAndWages | creates employee salary and wage record
[**create_employee_statutory_sick_leave**](PayrollUkApi.md#create_employee_statutory_sick_leave) | **POST** /StatutoryLeaves/Sick | creates employee statutory sick leave records
[**create_employment**](PayrollUkApi.md#create_employment) | **POST** /Employees/{EmployeeId}/Employment | creates employment
[**create_leave_type**](PayrollUkApi.md#create_leave_type) | **POST** /LeaveTypes | create a new leave type
[**create_multiple_employee_earnings_template**](PayrollUkApi.md#create_multiple_employee_earnings_template) | **POST** /Employees/{EmployeeId}/paytemplateearnings | creates multiple employee earnings template records
[**create_pay_run_calendar**](PayrollUkApi.md#create_pay_run_calendar) | **POST** /PayRunCalendars | create a new payrun calendar
[**create_reimbursement**](PayrollUkApi.md#create_reimbursement) | **POST** /Reimbursements | create a new reimbursement
[**create_timesheet**](PayrollUkApi.md#create_timesheet) | **POST** /Timesheets | create a new timesheet
[**create_timesheet_line**](PayrollUkApi.md#create_timesheet_line) | **POST** /Timesheets/{TimesheetID}/Lines | create a new timesheet line
[**delete_employee_earnings_template**](PayrollUkApi.md#delete_employee_earnings_template) | **DELETE** /Employees/{EmployeeId}/PayTemplates/earnings/{PayTemplateEarningID} | deletes an employee earnings template record
[**delete_employee_leave**](PayrollUkApi.md#delete_employee_leave) | **DELETE** /Employees/{EmployeeId}/Leave/{LeaveID} | deletes an employee leave record
[**delete_employee_salary_and_wage**](PayrollUkApi.md#delete_employee_salary_and_wage) | **DELETE** /Employees/{EmployeeId}/SalaryAndWages/{SalaryAndWagesID} | deletes an employee salary and wages record
[**delete_timesheet**](PayrollUkApi.md#delete_timesheet) | **DELETE** /Timesheets/{TimesheetID} | delete a timesheet
[**delete_timesheet_line**](PayrollUkApi.md#delete_timesheet_line) | **DELETE** /Timesheets/{TimesheetID}/Lines/{TimesheetLineID} | delete a timesheet line
[**get_benefit**](PayrollUkApi.md#get_benefit) | **GET** /Benefits/{id} | retrieve a single benefit by id
[**get_benefits**](PayrollUkApi.md#get_benefits) | **GET** /Benefits | searches benefits
[**get_deduction**](PayrollUkApi.md#get_deduction) | **GET** /Deductions/{deductionId} | retrieve a single deduction by id
[**get_deductions**](PayrollUkApi.md#get_deductions) | **GET** /Deductions | searches deductions
[**get_earnings_order**](PayrollUkApi.md#get_earnings_order) | **GET** /EarningsOrders/{id} | retrieve a single deduction by id
[**get_earnings_orders**](PayrollUkApi.md#get_earnings_orders) | **GET** /EarningsOrders | searches earnings orders
[**get_earnings_rate**](PayrollUkApi.md#get_earnings_rate) | **GET** /EarningsRates/{EarningsRateID} | retrieve a single earnings rates by id
[**get_earnings_rates**](PayrollUkApi.md#get_earnings_rates) | **GET** /EarningsRates | searches earnings rates
[**get_employee**](PayrollUkApi.md#get_employee) | **GET** /Employees/{EmployeeId} | searches employees
[**get_employee_leave**](PayrollUkApi.md#get_employee_leave) | **GET** /Employees/{EmployeeId}/Leave/{LeaveID} | retrieve a single employee leave record
[**get_employee_leave_balances**](PayrollUkApi.md#get_employee_leave_balances) | **GET** /Employees/{EmployeeId}/LeaveBalances | search employee leave balances
[**get_employee_leave_periods**](PayrollUkApi.md#get_employee_leave_periods) | **GET** /Employees/{EmployeeId}/LeavePeriods | searches employee leave periods
[**get_employee_leave_types**](PayrollUkApi.md#get_employee_leave_types) | **GET** /Employees/{EmployeeId}/LeaveTypes | searches employee leave types
[**get_employee_leaves**](PayrollUkApi.md#get_employee_leaves) | **GET** /Employees/{EmployeeId}/Leave | search employee leave records
[**get_employee_opening_balances**](PayrollUkApi.md#get_employee_opening_balances) | **GET** /Employees/{EmployeeId}/ukopeningbalances | retrieve employee openingbalances
[**get_employee_pay_template**](PayrollUkApi.md#get_employee_pay_template) | **GET** /Employees/{EmployeeId}/PayTemplates | searches employee pay templates
[**get_employee_payment_method**](PayrollUkApi.md#get_employee_payment_method) | **GET** /Employees/{EmployeeId}/PaymentMethods | retrieves an employee&#39;s payment method
[**get_employee_salary_and_wage**](PayrollUkApi.md#get_employee_salary_and_wage) | **GET** /Employees/{EmployeeId}/SalaryAndWages/{SalaryAndWagesID} | get employee salary and wages record by id
[**get_employee_salary_and_wages**](PayrollUkApi.md#get_employee_salary_and_wages) | **GET** /Employees/{EmployeeId}/SalaryAndWages | retrieves an employee&#39;s salary and wages
[**get_employee_statutory_leave_balances**](PayrollUkApi.md#get_employee_statutory_leave_balances) | **GET** /Employees/{EmployeeId}/StatutoryLeaveBalance | search employee leave balances
[**get_employee_statutory_sick_leave**](PayrollUkApi.md#get_employee_statutory_sick_leave) | **GET** /StatutoryLeaves/Sick/{StatutorySickLeaveID} | retrieve a statutory sick leave for an employee
[**get_employee_tax**](PayrollUkApi.md#get_employee_tax) | **GET** /Employees/{EmployeeId}/Tax | searches tax records for an employee
[**get_employees**](PayrollUkApi.md#get_employees) | **GET** /Employees | searches employees
[**get_leave_type**](PayrollUkApi.md#get_leave_type) | **GET** /LeaveTypes/{LeaveTypeID} | retrieve a single leave type by id
[**get_leave_types**](PayrollUkApi.md#get_leave_types) | **GET** /LeaveTypes | searches leave types
[**get_pay_run**](PayrollUkApi.md#get_pay_run) | **GET** /PayRuns/{PayRunID} | retrieve a single pay run by id
[**get_pay_run_calendar**](PayrollUkApi.md#get_pay_run_calendar) | **GET** /PayRunCalendars/{PayRunCalendarID} | retrieve a single payrun calendar by id
[**get_pay_run_calendars**](PayrollUkApi.md#get_pay_run_calendars) | **GET** /PayRunCalendars | searches payrun calendars
[**get_pay_runs**](PayrollUkApi.md#get_pay_runs) | **GET** /PayRuns | searches pay runs
[**get_pay_slip**](PayrollUkApi.md#get_pay_slip) | **GET** /Payslips/{PayslipID} | retrieve a single payslip by id
[**get_pay_slips**](PayrollUkApi.md#get_pay_slips) | **GET** /Payslips | searches payslips
[**get_reimbursement**](PayrollUkApi.md#get_reimbursement) | **GET** /Reimbursements/{ReimbursementID} | retrieve a single reimbursement by id
[**get_reimbursements**](PayrollUkApi.md#get_reimbursements) | **GET** /Reimbursements | searches reimbursements
[**get_settings**](PayrollUkApi.md#get_settings) | **GET** /Settings | searches settings
[**get_statutory_leave_summary**](PayrollUkApi.md#get_statutory_leave_summary) | **GET** /statutoryleaves/summary/{EmployeeId} | retrieve a summary of statutory leaves for an employee
[**get_timesheet**](PayrollUkApi.md#get_timesheet) | **GET** /Timesheets/{TimesheetID} | retrieve a single timesheet by id
[**get_timesheets**](PayrollUkApi.md#get_timesheets) | **GET** /Timesheets | searches timesheets
[**get_tracking_categories**](PayrollUkApi.md#get_tracking_categories) | **GET** /settings/trackingCategories | searches tracking categories
[**revert_timesheet**](PayrollUkApi.md#revert_timesheet) | **POST** /Timesheets/{TimesheetID}/RevertToDraft | revert a timesheet to draft
[**update_employee**](PayrollUkApi.md#update_employee) | **PUT** /Employees/{EmployeeId} | updates employee
[**update_employee_earnings_template**](PayrollUkApi.md#update_employee_earnings_template) | **PUT** /Employees/{EmployeeId}/PayTemplates/earnings/{PayTemplateEarningID} | updates employee earnings template records
[**update_employee_leave**](PayrollUkApi.md#update_employee_leave) | **PUT** /Employees/{EmployeeId}/Leave/{LeaveID} | updates employee leave records
[**update_employee_opening_balances**](PayrollUkApi.md#update_employee_opening_balances) | **PUT** /Employees/{EmployeeId}/ukopeningbalances | updates employee opening balances
[**update_employee_salary_and_wage**](PayrollUkApi.md#update_employee_salary_and_wage) | **PUT** /Employees/{EmployeeId}/SalaryAndWages/{SalaryAndWagesID} | updates employee salary and wages record
[**update_pay_run**](PayrollUkApi.md#update_pay_run) | **PUT** /PayRuns/{PayRunID} | update a pay run
[**update_timesheet_line**](PayrollUkApi.md#update_timesheet_line) | **PUT** /Timesheets/{TimesheetID}/Lines/{TimesheetLineID} | update a timesheet line


# **approve_timesheet**
> TimesheetObject approve_timesheet(xero_tenant_id, timesheet_id)

approve a timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # approve a timesheet
    api_response = api_instance.approve_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->approve_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_benefit**
> BenefitObject create_benefit(xero_tenant_id, benefit)

create a new benefit

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
benefit = { "name": "My Big Bennie", "category": "StakeholderPension", "liabilityAccountId": "e0faa299-ca0d-4b0a-9e32-0dfabdf9179a", "expenseAccountId": "4b03500d-32fd-4616-8d70-e1e56e0519c6", "standardAmount": 50, "percentage": 25, "calculationType": "PercentageOfGross" } # Benefit | 
try:
    # create a new benefit
    api_response = api_instance.create_benefit(xero_tenant_id, benefit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_benefit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **benefit** | [**Benefit**](Benefit.md)|  | 

### Return type

[**BenefitObject**](BenefitObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deduction**
> DeductionObject create_deduction(xero_tenant_id, deduction)

create a new deduction

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
deduction = { "deductionName": "My new deducation", "deductionCategory": "SalarySacrifice", "liabilityAccountId": "e0faa299-ca0d-4b0a-9e32-0dfabdf9179a", "calculationType": "FixedAmount" } # Deduction | 
try:
    # create a new deduction
    api_response = api_instance.create_deduction(xero_tenant_id, deduction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_deduction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **deduction** | [**Deduction**](Deduction.md)|  | 

### Return type

[**DeductionObject**](DeductionObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_earnings_rate**
> EarningsRateObject create_earnings_rate(xero_tenant_id, earnings_rate)

create a new earnings rate

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
earnings_rate = { "name": "My Earnings Rate", "earningsType": "RegularEarnings", "rateType": "RatePerUnit", "typeOfUnits": "hours", "expenseAccountID": "4b03500d-32fd-4616-8d70-e1e56e0519c6" } # EarningsRate | 
try:
    # create a new earnings rate
    api_response = api_instance.create_earnings_rate(xero_tenant_id, earnings_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_earnings_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **earnings_rate** | [**EarningsRate**](EarningsRate.md)|  | 

### Return type

[**EarningsRateObject**](EarningsRateObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee**
> EmployeeObject create_employee(xero_tenant_id, employee)

creates employees

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee = { "title":"Mr", "firstName":"Mike", "lastName":"Fancy", "dateOfBirth":"1999-01-01", "address":{ "addressLine1":"101 Green St", "city":"San Francisco", "postCode":"6TGR4F", "country":"UK" }, "email":"mike@starkindustries.com", "gender":"M" } # Employee | 
try:
    # creates employees
    api_response = api_instance.create_employee(xero_tenant_id, employee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee** | [**Employee**](Employee.md)|  | 

### Return type

[**EmployeeObject**](EmployeeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_earnings_template**
> EarningsTemplateObject create_employee_earnings_template(xero_tenant_id, employee_id, earnings_template)

creates employee earnings template records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
earnings_template = xero_python.payrolluk.EarningsTemplate() # EarningsTemplate | 
try:
    # creates employee earnings template records
    api_response = api_instance.create_employee_earnings_template(xero_tenant_id, employee_id, earnings_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_earnings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **earnings_template** | [**EarningsTemplate**](EarningsTemplate.md)|  | 

### Return type

[**EarningsTemplateObject**](EarningsTemplateObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_leave**
> EmployeeLeaveObject create_employee_leave(xero_tenant_id, employee_id, employee_leave)

creates employee leave records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee_leave = { "leaveTypeID": "1d2778ee-86ea-45c0-bbf8-1045485f6b3f", "description": "Creating a Desription", "startDate": "2020-03-24", "endDate": "2020-03-26" } # EmployeeLeave | 
try:
    # creates employee leave records
    api_response = api_instance.create_employee_leave(xero_tenant_id, employee_id, employee_leave)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee_leave** | [**EmployeeLeave**](EmployeeLeave.md)|  | 

### Return type

[**EmployeeLeaveObject**](EmployeeLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_leave_type**
> EmployeeLeaveTypeObject create_employee_leave_type(xero_tenant_id, employee_id, employee_leave_type)

creates employee leave type records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee_leave_type = { "leaveTypeID": "4918f233-bd31-43f9-9633-bcc6de1178f2", "scheduleOfAccrual": "BeginningOfCalendarYear", "hoursAccruedAnnually": 10 } # EmployeeLeaveType | 
try:
    # creates employee leave type records
    api_response = api_instance.create_employee_leave_type(xero_tenant_id, employee_id, employee_leave_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_leave_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee_leave_type** | [**EmployeeLeaveType**](EmployeeLeaveType.md)|  | 

### Return type

[**EmployeeLeaveTypeObject**](EmployeeLeaveTypeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_opening_balances**
> EmployeeOpeningBalancesObject create_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balances)

creates employee opening balances

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee_opening_balances = { "statutoryAdoptionPay": 10, "statutoryMaternityPay": 10, "statutoryPaternityPay": 10, "statutorySharedParentalPay": 10, "statutorySickPay": 10, "priorEmployeeNumber": 10 } # EmployeeOpeningBalances | 
try:
    # creates employee opening balances
    api_response = api_instance.create_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee_opening_balances** | [**EmployeeOpeningBalances**](EmployeeOpeningBalances.md)|  | 

### Return type

[**EmployeeOpeningBalancesObject**](EmployeeOpeningBalancesObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_payment_method**
> PaymentMethodObject create_employee_payment_method(xero_tenant_id, employee_id, payment_method)

creates employee payment method

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
payment_method = { "paymentMethod": "Electronically", "bankAccounts": [ { "accountName": "Sid BofA", "accountNumber": "24987654", "sortCode": "287654" } ] } # PaymentMethod | 
try:
    # creates employee payment method
    api_response = api_instance.create_employee_payment_method(xero_tenant_id, employee_id, payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **payment_method** | [**PaymentMethod**](PaymentMethod.md)|  | 

### Return type

[**PaymentMethodObject**](PaymentMethodObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_salary_and_wage**
> SalaryAndWageObject create_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wage)

creates employee salary and wage record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
salary_and_wage = { "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnitsPerWeek": 2, "ratePerUnit": 10, "numberOfUnitsPerDay": 2, "effectiveFrom": "2020-05-01", "annualSalary": 100, "status": "ACTIVE", "paymentType": "Salary" } # SalaryAndWage | 
try:
    # creates employee salary and wage record
    api_response = api_instance.create_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_salary_and_wage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **salary_and_wage** | [**SalaryAndWage**](SalaryAndWage.md)|  | 

### Return type

[**SalaryAndWageObject**](SalaryAndWageObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_statutory_sick_leave**
> EmployeeStatutorySickLeaveObject create_employee_statutory_sick_leave(xero_tenant_id, employee_statutory_sick_leave)

creates employee statutory sick leave records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_statutory_sick_leave = { "employeeID": "aad6b292-7b94-408b-93f6-e489867e3fb0", "leaveTypeID": "aab78802-e9d3-4bbd-bc87-df858054988f", "startDate": "2020-04-21", "endDate": "2020-04-24", "workPattern": [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ], "isPregnancyRelated": false, "sufficientNotice": true } # EmployeeStatutorySickLeave | 
try:
    # creates employee statutory sick leave records
    api_response = api_instance.create_employee_statutory_sick_leave(xero_tenant_id, employee_statutory_sick_leave)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employee_statutory_sick_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_statutory_sick_leave** | [**EmployeeStatutorySickLeave**](EmployeeStatutorySickLeave.md)|  | 

### Return type

[**EmployeeStatutorySickLeaveObject**](EmployeeStatutorySickLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employment**
> EmploymentObject create_employment(xero_tenant_id, employee_id, employment)

creates employment

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employment = { "PayrollCalendarID": "216d80e6-af55-47b1-b718-9457c3f5d2fe", "StartDate": "2020-04-01", "EmployeeNumber": "123ABC", "NICategory": "A" } # Employment | 
try:
    # creates employment
    api_response = api_instance.create_employment(xero_tenant_id, employee_id, employment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_employment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employment** | [**Employment**](Employment.md)|  | 

### Return type

[**EmploymentObject**](EmploymentObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leave_type**
> LeaveTypeObject create_leave_type(xero_tenant_id, leave_type)

create a new leave type

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_type = { "name": "My opebvwbfxf Leave", "isPaidLeave": false, "showOnPayslip": true } # LeaveType | 
try:
    # create a new leave type
    api_response = api_instance.create_leave_type(xero_tenant_id, leave_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_leave_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_type** | [**LeaveType**](LeaveType.md)|  | 

### Return type

[**LeaveTypeObject**](LeaveTypeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_employee_earnings_template**
> EmployeePayTemplates create_multiple_employee_earnings_template(xero_tenant_id, employee_id, earnings_template)

creates multiple employee earnings template records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
earnings_template = [ { "ratePerUnit":20.0, "numberOfUnits":8.0, "earningsRateID":"87f5b43a-cf51-4b74-92de-94c819e82d27" }, { "ratePerUnit":20.0, "numberOfUnits":8.0, "earningsRateID":"973365f3-66b2-4c33-8ae6-14b75f78f68b" } ] # list[EarningsTemplate] | 
try:
    # creates multiple employee earnings template records
    api_response = api_instance.create_multiple_employee_earnings_template(xero_tenant_id, employee_id, earnings_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_multiple_employee_earnings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **earnings_template** | [**list[EarningsTemplate]**](EarningsTemplate.md)|  | 

### Return type

[**EmployeePayTemplates**](EmployeePayTemplates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pay_run_calendar**
> PayRunCalendarObject create_pay_run_calendar(xero_tenant_id, pay_run_calendar)

create a new payrun calendar

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_calendar = { "name": "My Weekly Cal", "calendarType": "Weekly", "periodStartDate": "2020-05-01", "paymentDate": "2020-05-15" } # PayRunCalendar | 
try:
    # create a new payrun calendar
    api_response = api_instance.create_pay_run_calendar(xero_tenant_id, pay_run_calendar)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_pay_run_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_calendar** | [**PayRunCalendar**](PayRunCalendar.md)|  | 

### Return type

[**PayRunCalendarObject**](PayRunCalendarObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reimbursement**
> ReimbursementObject create_reimbursement(xero_tenant_id, reimbursement)

create a new reimbursement

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
reimbursement = { "name": "My new Reimburse", "accountID": "9ee28149-32a9-4661-8eab-a28738696983" } # Reimbursement | 
try:
    # create a new reimbursement
    api_response = api_instance.create_reimbursement(xero_tenant_id, reimbursement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_reimbursement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **reimbursement** | [**Reimbursement**](Reimbursement.md)|  | 

### Return type

[**ReimbursementObject**](ReimbursementObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet**
> TimesheetObject create_timesheet(xero_tenant_id, timesheet)

create a new timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet = { "payrollCalendarID": "216d80e6-af55-47b1-b718-9457c3f5d2fe", "employeeID": "aad6b292-7b94-408b-93f6-e489867e3fb0", "startDate": "2020-04-13", "endDate": "2020-04-19", "timesheetLines": [ { "date": "2020-04-13", "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnits": 8 }, { "date": "2020-04-15", "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnits": 6 } ] } # Timesheet | 
try:
    # create a new timesheet
    api_response = api_instance.create_timesheet(xero_tenant_id, timesheet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet** | [**Timesheet**](Timesheet.md)|  | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet_line**
> TimesheetLineObject create_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line)

create a new timesheet line

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line = { "date": "2020-04-14", "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnits": 1 } # TimesheetLine | 
try:
    # create a new timesheet line
    api_response = api_instance.create_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->create_timesheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **timesheet_line** | [**TimesheetLine**](TimesheetLine.md)|  | 

### Return type

[**TimesheetLineObject**](TimesheetLineObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_earnings_template**
> delete_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id)

deletes an employee earnings template record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
pay_template_earning_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object
try:
    # deletes an employee earnings template record
    api_instance.delete_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id)
except ApiException as e:
    print("Exception when calling PayrollUkApi->delete_employee_earnings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **pay_template_earning_id** | [**str**](.md)| Id for single pay template earnings object | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_leave**
> EmployeeLeaveObject delete_employee_leave(xero_tenant_id, employee_id, leave_id)

deletes an employee leave record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
leave_id = 'c4be24e5-e840-4c92-9eaa-2d86cd596314' # str | Leave id for single object
try:
    # deletes an employee leave record
    api_response = api_instance.delete_employee_leave(xero_tenant_id, employee_id, leave_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->delete_employee_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **leave_id** | [**str**](.md)| Leave id for single object | 

### Return type

[**EmployeeLeaveObject**](EmployeeLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_salary_and_wage**
> delete_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id)

deletes an employee salary and wages record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi


# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
salary_and_wages_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single salary and wages object
try:
    # deletes an employee salary and wages record
    api_instance.delete_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id)
except ApiException as e:
    print("Exception when calling PayrollUkApi->delete_employee_salary_and_wage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **salary_and_wages_id** | [**str**](.md)| Id for single salary and wages object | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet**
> TimesheetLine delete_timesheet(xero_tenant_id, timesheet_id)

delete a timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # delete a timesheet
    api_response = api_instance.delete_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->delete_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 

### Return type

[**TimesheetLine**](TimesheetLine.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_line**
> TimesheetLine delete_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id)

delete a timesheet line

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line_id = 'timesheet_line_id_example' # str | Identifier for the timesheet line
try:
    # delete a timesheet line
    api_response = api_instance.delete_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->delete_timesheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **timesheet_line_id** | [**str**](.md)| Identifier for the timesheet line | 

### Return type

[**TimesheetLine**](TimesheetLine.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benefit**
> BenefitObject get_benefit(xero_tenant_id, id)

retrieve a single benefit by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
id = 'id_example' # str | Identifier for the benefit
try:
    # retrieve a single benefit by id
    api_response = api_instance.get_benefit(xero_tenant_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_benefit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | [**str**](.md)| Identifier for the benefit | 

### Return type

[**BenefitObject**](BenefitObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benefits**
> Benefits get_benefits(xero_tenant_id, page=page)

searches benefits

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches benefits
    api_response = api_instance.get_benefits(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_benefits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Benefits**](Benefits.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deduction**
> DeductionObject get_deduction(xero_tenant_id, deduction_id)

retrieve a single deduction by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
deduction_id = 'deduction_id_example' # str | Identifier for the deduction
try:
    # retrieve a single deduction by id
    api_response = api_instance.get_deduction(xero_tenant_id, deduction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_deduction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **deduction_id** | [**str**](.md)| Identifier for the deduction | 

### Return type

[**DeductionObject**](DeductionObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deductions**
> Deductions get_deductions(xero_tenant_id, page=page)

searches deductions

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches deductions
    api_response = api_instance.get_deductions(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_deductions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Deductions**](Deductions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earnings_order**
> EarningsOrderObject get_earnings_order(xero_tenant_id, id)

retrieve a single deduction by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
id = 'id_example' # str | Identifier for the deduction
try:
    # retrieve a single deduction by id
    api_response = api_instance.get_earnings_order(xero_tenant_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_earnings_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | [**str**](.md)| Identifier for the deduction | 

### Return type

[**EarningsOrderObject**](EarningsOrderObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earnings_orders**
> EarningsOrders get_earnings_orders(xero_tenant_id, page=page)

searches earnings orders

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches earnings orders
    api_response = api_instance.get_earnings_orders(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_earnings_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**EarningsOrders**](EarningsOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earnings_rate**
> EarningsRateObject get_earnings_rate(xero_tenant_id, earnings_rate_id)

retrieve a single earnings rates by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
earnings_rate_id = 'earnings_rate_id_example' # str | Identifier for the earnings rate
try:
    # retrieve a single earnings rates by id
    api_response = api_instance.get_earnings_rate(xero_tenant_id, earnings_rate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_earnings_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **earnings_rate_id** | [**str**](.md)| Identifier for the earnings rate | 

### Return type

[**EarningsRateObject**](EarningsRateObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earnings_rates**
> EarningsRates get_earnings_rates(xero_tenant_id, page=page)

searches earnings rates

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches earnings rates
    api_response = api_instance.get_earnings_rates(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_earnings_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**EarningsRates**](EarningsRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> EmployeeObject get_employee(xero_tenant_id, employee_id)

searches employees

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # searches employees
    api_response = api_instance.get_employee(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeObject**](EmployeeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_leave**
> EmployeeLeaveObject get_employee_leave(xero_tenant_id, employee_id, leave_id)

retrieve a single employee leave record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
leave_id = 'c4be24e5-e840-4c92-9eaa-2d86cd596314' # str | Leave id for single object
try:
    # retrieve a single employee leave record
    api_response = api_instance.get_employee_leave(xero_tenant_id, employee_id, leave_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **leave_id** | [**str**](.md)| Leave id for single object | 

### Return type

[**EmployeeLeaveObject**](EmployeeLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_leave_balances**
> EmployeeLeaveBalances get_employee_leave_balances(xero_tenant_id, employee_id)

search employee leave balances

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # search employee leave balances
    api_response = api_instance.get_employee_leave_balances(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_leave_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeLeaveBalances**](EmployeeLeaveBalances.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_leave_periods**
> LeavePeriods get_employee_leave_periods(xero_tenant_id, employee_id, start_date=start_date, end_date=end_date)

searches employee leave periods

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
start_date = '2013-10-20' # date | Filter by start date (optional)
end_date = 'Johnson' # date | Filter by end date (optional)
try:
    # searches employee leave periods
    api_response = api_instance.get_employee_leave_periods(xero_tenant_id, employee_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_leave_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **start_date** | **date**| Filter by start date | [optional] 
 **end_date** | **date**| Filter by end date | [optional] 

### Return type

[**LeavePeriods**](LeavePeriods.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_leave_types**
> EmployeeLeaveTypes get_employee_leave_types(xero_tenant_id, employee_id)

searches employee leave types

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # searches employee leave types
    api_response = api_instance.get_employee_leave_types(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_leave_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeLeaveTypes**](EmployeeLeaveTypes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_leaves**
> EmployeeLeaves get_employee_leaves(xero_tenant_id, employee_id)

search employee leave records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # search employee leave records
    api_response = api_instance.get_employee_leaves(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_leaves: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeLeaves**](EmployeeLeaves.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_opening_balances**
> EmployeeOpeningBalancesObject get_employee_opening_balances(xero_tenant_id, employee_id)

retrieve employee openingbalances

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # retrieve employee openingbalances
    api_response = api_instance.get_employee_opening_balances(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeOpeningBalancesObject**](EmployeeOpeningBalancesObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_pay_template**
> EmployeePayTemplateObject get_employee_pay_template(xero_tenant_id, employee_id)

searches employee pay templates

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # searches employee pay templates
    api_response = api_instance.get_employee_pay_template(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_pay_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeePayTemplateObject**](EmployeePayTemplateObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_payment_method**
> PaymentMethodObject get_employee_payment_method(xero_tenant_id, employee_id)

retrieves an employee's payment method

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # retrieves an employee's payment method
    api_response = api_instance.get_employee_payment_method(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**PaymentMethodObject**](PaymentMethodObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_salary_and_wage**
> SalaryAndWages get_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id)

get employee salary and wages record by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
salary_and_wages_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object
try:
    # get employee salary and wages record by id
    api_response = api_instance.get_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_salary_and_wage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **salary_and_wages_id** | [**str**](.md)| Id for single pay template earnings object | 

### Return type

[**SalaryAndWages**](SalaryAndWages.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_salary_and_wages**
> SalaryAndWages get_employee_salary_and_wages(xero_tenant_id, employee_id, page=page)

retrieves an employee's salary and wages

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # retrieves an employee's salary and wages
    api_response = api_instance.get_employee_salary_and_wages(xero_tenant_id, employee_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_salary_and_wages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**SalaryAndWages**](SalaryAndWages.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_statutory_leave_balances**
> EmployeeStatutoryLeaveBalanceObject get_employee_statutory_leave_balances(xero_tenant_id, employee_id, leave_type=leave_type, as_of_date=as_of_date)

search employee leave balances

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
leave_type = 'sick' # str | Filter by the type of statutory leave (optional)
as_of_date = '2013-10-20' # date | The date from which to calculate balance remaining. If not specified, current date UTC is used. (optional)
try:
    # search employee leave balances
    api_response = api_instance.get_employee_statutory_leave_balances(xero_tenant_id, employee_id, leave_type=leave_type, as_of_date=as_of_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_statutory_leave_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **leave_type** | **str**| Filter by the type of statutory leave | [optional] 
 **as_of_date** | **date**| The date from which to calculate balance remaining. If not specified, current date UTC is used. | [optional] 

### Return type

[**EmployeeStatutoryLeaveBalanceObject**](EmployeeStatutoryLeaveBalanceObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_statutory_sick_leave**
> EmployeeStatutorySickLeaveObject get_employee_statutory_sick_leave(xero_tenant_id, statutory_sick_leave_id)

retrieve a statutory sick leave for an employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
statutory_sick_leave_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Statutory sick leave id for single object
try:
    # retrieve a statutory sick leave for an employee
    api_response = api_instance.get_employee_statutory_sick_leave(xero_tenant_id, statutory_sick_leave_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_statutory_sick_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **statutory_sick_leave_id** | [**str**](.md)| Statutory sick leave id for single object | 

### Return type

[**EmployeeStatutorySickLeaveObject**](EmployeeStatutorySickLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_tax**
> EmployeeTaxObject get_employee_tax(xero_tenant_id, employee_id)

searches tax records for an employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # searches tax records for an employee
    api_response = api_instance.get_employee_tax(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employee_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**EmployeeTaxObject**](EmployeeTaxObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> Employees get_employees(xero_tenant_id, first_name=first_name, last_name=last_name, page=page)

searches employees

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
first_name = 'John' # str | Filter by first name (optional)
last_name = 'Johnson' # str | Filter by last name (optional)
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches employees
    api_response = api_instance.get_employees(xero_tenant_id, first_name=first_name, last_name=last_name, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **first_name** | **str**| Filter by first name | [optional] 
 **last_name** | **str**| Filter by last name | [optional] 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_type**
> LeaveTypeObject get_leave_type(xero_tenant_id, leave_type_id)

retrieve a single leave type by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_type_id = 'leave_type_id_example' # str | Identifier for the leave type
try:
    # retrieve a single leave type by id
    api_response = api_instance.get_leave_type(xero_tenant_id, leave_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_leave_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_type_id** | [**str**](.md)| Identifier for the leave type | 

### Return type

[**LeaveTypeObject**](LeaveTypeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_types**
> LeaveTypes get_leave_types(xero_tenant_id, page=page, active_only=active_only)

searches leave types

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
active_only = True # bool | Filters leave types by active status. By default the API returns all leave types. (optional)
try:
    # searches leave types
    api_response = api_instance.get_leave_types(xero_tenant_id, page=page, active_only=active_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_leave_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 
 **active_only** | **bool**| Filters leave types by active status. By default the API returns all leave types. | [optional] 

### Return type

[**LeaveTypes**](LeaveTypes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_run**
> PayRunObject get_pay_run(xero_tenant_id, pay_run_id)

retrieve a single pay run by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_id = 'pay_run_id_example' # str | Identifier for the pay run
try:
    # retrieve a single pay run by id
    api_response = api_instance.get_pay_run(xero_tenant_id, pay_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | [**str**](.md)| Identifier for the pay run | 

### Return type

[**PayRunObject**](PayRunObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_run_calendar**
> PayRunCalendarObject get_pay_run_calendar(xero_tenant_id, pay_run_calendar_id)

retrieve a single payrun calendar by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_calendar_id = 'pay_run_calendar_id_example' # str | Identifier for the payrun calendars
try:
    # retrieve a single payrun calendar by id
    api_response = api_instance.get_pay_run_calendar(xero_tenant_id, pay_run_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_run_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_calendar_id** | [**str**](.md)| Identifier for the payrun calendars | 

### Return type

[**PayRunCalendarObject**](PayRunCalendarObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_run_calendars**
> PayRunCalendars get_pay_run_calendars(xero_tenant_id, page=page)

searches payrun calendars

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches payrun calendars
    api_response = api_instance.get_pay_run_calendars(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_run_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**PayRunCalendars**](PayRunCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_runs**
> PayRuns get_pay_runs(xero_tenant_id, page=page, status=status)

searches pay runs

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
status = 'status_example' # str | By default get payruns will return all the payruns for an organization. You can add GET https://api.xero.com/payroll.xro/2.0/payRuns?statu={PayRunStatus} to filter the payruns by status. (optional)
try:
    # searches pay runs
    api_response = api_instance.get_pay_runs(xero_tenant_id, page=page, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 
 **status** | **str**| By default get payruns will return all the payruns for an organization. You can add GET https://api.xero.com/payroll.xro/2.0/payRuns?statu&#x3D;{PayRunStatus} to filter the payruns by status. | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slip**
> PayslipObject get_pay_slip(xero_tenant_id, payslip_id)

retrieve a single payslip by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
payslip_id = 'payslip_id_example' # str | Identifier for the payslip
try:
    # retrieve a single payslip by id
    api_response = api_instance.get_pay_slip(xero_tenant_id, payslip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_slip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payslip_id** | [**str**](.md)| Identifier for the payslip | 

### Return type

[**PayslipObject**](PayslipObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_slips**
> Payslips get_pay_slips(xero_tenant_id, pay_run_id, page=page)

searches payslips

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_id = 'pay_run_id_example' # str | PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun.
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches payslips
    api_response = api_instance.get_pay_slips(xero_tenant_id, pay_run_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_pay_slips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | [**str**](.md)| PayrunID which specifies the containing payrun of payslips to retrieve. By default, the API does not group payslips by payrun. | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Payslips**](Payslips.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reimbursement**
> ReimbursementObject get_reimbursement(xero_tenant_id, reimbursement_id)

retrieve a single reimbursement by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
reimbursement_id = 'reimbursement_id_example' # str | Identifier for the reimbursement
try:
    # retrieve a single reimbursement by id
    api_response = api_instance.get_reimbursement(xero_tenant_id, reimbursement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_reimbursement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **reimbursement_id** | [**str**](.md)| Identifier for the reimbursement | 

### Return type

[**ReimbursementObject**](ReimbursementObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reimbursements**
> Reimbursements get_reimbursements(xero_tenant_id, page=page)

searches reimbursements

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
try:
    # searches reimbursements
    api_response = api_instance.get_reimbursements(xero_tenant_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_reimbursements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 

### Return type

[**Reimbursements**](Reimbursements.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> Settings get_settings(xero_tenant_id)

searches settings

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
try:
    # searches settings
    api_response = api_instance.get_settings(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**Settings**](Settings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statutory_leave_summary**
> EmployeeStatutoryLeavesSummaries get_statutory_leave_summary(xero_tenant_id, employee_id, active_only=active_only)

retrieve a summary of statutory leaves for an employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
active_only = True # bool | Filter response with leaves that are currently active or yet to be taken. If not specified, all leaves (past, current, and future scheduled) are returned (optional)
try:
    # retrieve a summary of statutory leaves for an employee
    api_response = api_instance.get_statutory_leave_summary(xero_tenant_id, employee_id, active_only=active_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_statutory_leave_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **active_only** | **bool**| Filter response with leaves that are currently active or yet to be taken. If not specified, all leaves (past, current, and future scheduled) are returned | [optional] 

### Return type

[**EmployeeStatutoryLeavesSummaries**](EmployeeStatutoryLeavesSummaries.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheet**
> TimesheetObject get_timesheet(xero_tenant_id, timesheet_id)

retrieve a single timesheet by id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # retrieve a single timesheet by id
    api_response = api_instance.get_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheets**
> Timesheets get_timesheets(xero_tenant_id, page=page, employee_id=employee_id, payroll_calendar_id=payroll_calendar_id)

searches timesheets

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 56 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
employee_id = 'employee_id_example' # str | By default get Timesheets will return the timesheets for all employees in an organization. You can add GET https://…/timesheets?filter=employeeId=={EmployeeId} to get only the timesheets of a particular employee. (optional)
payroll_calendar_id = 'payroll_calendar_id_example' # str | By default get Timesheets will return all the timesheets for an organization. You can add GET https://…/timesheets?filter=payrollCalendarId=={PayrollCalendarID} to filter the timesheets by payroll calendar id (optional)
try:
    # searches timesheets
    api_response = api_instance.get_timesheets(xero_tenant_id, page=page, employee_id=employee_id, payroll_calendar_id=payroll_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 
 **employee_id** | [**str**](.md)| By default get Timesheets will return the timesheets for all employees in an organization. You can add GET https://…/timesheets?filter&#x3D;employeeId&#x3D;&#x3D;{EmployeeId} to get only the timesheets of a particular employee. | [optional] 
 **payroll_calendar_id** | [**str**](.md)| By default get Timesheets will return all the timesheets for an organization. You can add GET https://…/timesheets?filter&#x3D;payrollCalendarId&#x3D;&#x3D;{PayrollCalendarID} to filter the timesheets by payroll calendar id | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_categories**
> TrackingCategories get_tracking_categories(xero_tenant_id)

searches tracking categories

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
try:
    # searches tracking categories
    api_response = api_instance.get_tracking_categories(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->get_tracking_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_timesheet**
> TimesheetObject revert_timesheet(xero_tenant_id, timesheet_id)

revert a timesheet to draft

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # revert a timesheet to draft
    api_response = api_instance.revert_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->revert_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> EmployeeObject update_employee(xero_tenant_id, employee_id, employee)

updates employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee = { "title":"Mr", "firstName":"Mike", "lastName":"Johnllsbkrhwopson", "dateOfBirth":"1999-01-01", "address":{ "addressLine1":"101 Green St", "city":"San Francisco", "postCode":"6TGR4F", "country":"UK" }, "email":"84044@starkindustries.com", "gender":"M" } # Employee | 
try:
    # updates employee
    api_response = api_instance.update_employee(xero_tenant_id, employee_id, employee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee** | [**Employee**](Employee.md)|  | 

### Return type

[**EmployeeObject**](EmployeeObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_earnings_template**
> EarningsTemplateObject update_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id, earnings_template)

updates employee earnings template records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
pay_template_earning_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object
earnings_template = { "ratePerUnit": 30, "numberOfUnits": 4, "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27" } # EarningsTemplate | 
try:
    # updates employee earnings template records
    api_response = api_instance.update_employee_earnings_template(xero_tenant_id, employee_id, pay_template_earning_id, earnings_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_employee_earnings_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **pay_template_earning_id** | [**str**](.md)| Id for single pay template earnings object | 
 **earnings_template** | [**EarningsTemplate**](EarningsTemplate.md)|  | 

### Return type

[**EarningsTemplateObject**](EarningsTemplateObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_leave**
> EmployeeLeaveObject update_employee_leave(xero_tenant_id, employee_id, leave_id, employee_leave)

updates employee leave records

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
leave_id = 'c4be24e5-e840-4c92-9eaa-2d86cd596314' # str | Leave id for single object
employee_leave = { "leaveTypeID": "ed08dffe-788e-4b24-9630-f0fa2f4d164c", "description": "Creating a Description", "startDate": "2020-04-24", "endDate": "2020-04-26", "periods": [ { "periodStartDate": "2020-04-20", "periodEndDate": "2020-04-26", "numberOfUnits": 1, "periodStatus": "Approved" } ] } # EmployeeLeave | 
try:
    # updates employee leave records
    api_response = api_instance.update_employee_leave(xero_tenant_id, employee_id, leave_id, employee_leave)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_employee_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **leave_id** | [**str**](.md)| Leave id for single object | 
 **employee_leave** | [**EmployeeLeave**](EmployeeLeave.md)|  | 

### Return type

[**EmployeeLeaveObject**](EmployeeLeaveObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_opening_balances**
> EmployeeOpeningBalancesObject update_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balances)

updates employee opening balances

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee_opening_balances = { "statutoryAdoptionPay": 20, "statutoryMaternityPay": 20, "statutoryPaternityPay": 20, "statutorySharedParentalPay": 20, "statutorySickPay": 20, "priorEmployeeNumber": 20 } # EmployeeOpeningBalances | 
try:
    # updates employee opening balances
    api_response = api_instance.update_employee_opening_balances(xero_tenant_id, employee_id, employee_opening_balances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_employee_opening_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee_opening_balances** | [**EmployeeOpeningBalances**](EmployeeOpeningBalances.md)|  | 

### Return type

[**EmployeeOpeningBalancesObject**](EmployeeOpeningBalancesObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_salary_and_wage**
> SalaryAndWageObject update_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id, salary_and_wage)

updates employee salary and wages record

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
salary_and_wages_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Id for single pay template earnings object
salary_and_wage = { "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnitsPerWeek": 3, "ratePerUnit": 11, "effectiveFrom": "2020-05-15", "annualSalary": 101, "status": "ACTIVE", "paymentType": "Salary" } # SalaryAndWage | 
try:
    # updates employee salary and wages record
    api_response = api_instance.update_employee_salary_and_wage(xero_tenant_id, employee_id, salary_and_wages_id, salary_and_wage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_employee_salary_and_wage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **salary_and_wages_id** | [**str**](.md)| Id for single pay template earnings object | 
 **salary_and_wage** | [**SalaryAndWage**](SalaryAndWage.md)|  | 

### Return type

[**SalaryAndWageObject**](SalaryAndWageObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pay_run**
> PayRunObject update_pay_run(xero_tenant_id, pay_run_id, pay_run)

update a pay run

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_id = 'pay_run_id_example' # str | Identifier for the pay run
pay_run = { "paymentDate": "2020-05-01" } # PayRun | 
try:
    # update a pay run
    api_response = api_instance.update_pay_run(xero_tenant_id, pay_run_id, pay_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_pay_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | [**str**](.md)| Identifier for the pay run | 
 **pay_run** | [**PayRun**](PayRun.md)|  | 

### Return type

[**PayRunObject**](PayRunObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timesheet_line**
> TimesheetLineObject update_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id, timesheet_line)

update a timesheet line

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrolluk import PayrollUkApi
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
# simplified version, `xero_oauth2_token` represents permanent global token storage
xero_oauth2_token = {} # set to valid xero oauth2 token dictionary
# create client configuration with client id and client secret for automatic token refresh
api_config = Configuration(oauth2_token=OAuth2Token(
    client_id="YOUR_API_CLIENT_ID", client_secret="YOUR_API_CLIENT_SECRET"
))
# configure xero-python sdk client
api_client = ApiClient(
    api_config,
    oauth2_token_saver=lambda x: xero_oauth2_token.update(x),
    oauth2_token_getter=lambda : xero_oauth2_token
)
# create an instance of the API class
api_instance = PayrollUkApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line_id = 'timesheet_line_id_example' # str | Identifier for the timesheet line
timesheet_line = { "date": "2020-04-14", "earningsRateID": "87f5b43a-cf51-4b74-92de-94c819e82d27", "numberOfUnits": 2 } # TimesheetLine | 
try:
    # update a timesheet line
    api_response = api_instance.update_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id, timesheet_line)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollUkApi->update_timesheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **timesheet_line_id** | [**str**](.md)| Identifier for the timesheet line | 
 **timesheet_line** | [**TimesheetLine**](TimesheetLine.md)|  | 

### Return type

[**TimesheetLineObject**](TimesheetLineObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

