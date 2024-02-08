# xero_python.payrollau.PayrollAuApi

All URIs are relative to *https://api.xero.com/payroll.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_leave_application**](PayrollAuApi.md#approve_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID}/approve | Approve a requested leave application by a unique leave application id
[**create_employee**](PayrollAuApi.md#create_employee) | **POST** /Employees | Creates a payroll employee
[**create_leave_application**](PayrollAuApi.md#create_leave_application) | **POST** /LeaveApplications | Creates a leave application
[**create_pay_item**](PayrollAuApi.md#create_pay_item) | **POST** /PayItems | Creates a pay item
[**create_pay_run**](PayrollAuApi.md#create_pay_run) | **POST** /PayRuns | Creates a pay run
[**create_payroll_calendar**](PayrollAuApi.md#create_payroll_calendar) | **POST** /PayrollCalendars | Creates a Payroll Calendar
[**create_superfund**](PayrollAuApi.md#create_superfund) | **POST** /Superfunds | Creates a superfund
[**create_timesheet**](PayrollAuApi.md#create_timesheet) | **POST** /Timesheets | Creates a timesheet
[**get_employee**](PayrollAuApi.md#get_employee) | **GET** /Employees/{EmployeeID} | Retrieves an employee&#39;s detail by unique employee id
[**get_employees**](PayrollAuApi.md#get_employees) | **GET** /Employees | Searches payroll employees
[**get_leave_application**](PayrollAuApi.md#get_leave_application) | **GET** /LeaveApplications/{LeaveApplicationID} | Retrieves a leave application by a unique leave application id
[**get_leave_applications**](PayrollAuApi.md#get_leave_applications) | **GET** /LeaveApplications | Retrieves leave applications
[**get_leave_applications_v2**](PayrollAuApi.md#get_leave_applications_v2) | **GET** /LeaveApplications/v2 | Retrieves leave applications including leave requests
[**get_pay_items**](PayrollAuApi.md#get_pay_items) | **GET** /PayItems | Retrieves pay items
[**get_pay_run**](PayrollAuApi.md#get_pay_run) | **GET** /PayRuns/{PayRunID} | Retrieves a pay run by using a unique pay run id
[**get_pay_runs**](PayrollAuApi.md#get_pay_runs) | **GET** /PayRuns | Retrieves pay runs
[**get_payroll_calendar**](PayrollAuApi.md#get_payroll_calendar) | **GET** /PayrollCalendars/{PayrollCalendarID} | Retrieves payroll calendar by using a unique payroll calendar ID
[**get_payroll_calendars**](PayrollAuApi.md#get_payroll_calendars) | **GET** /PayrollCalendars | Retrieves payroll calendars
[**get_payslip**](PayrollAuApi.md#get_payslip) | **GET** /Payslip/{PayslipID} | Retrieves for a payslip by a unique payslip id
[**get_settings**](PayrollAuApi.md#get_settings) | **GET** /Settings | Retrieves payroll settings
[**get_superfund**](PayrollAuApi.md#get_superfund) | **GET** /Superfunds/{SuperFundID} | Retrieves a superfund by using a unique superfund ID
[**get_superfund_products**](PayrollAuApi.md#get_superfund_products) | **GET** /SuperfundProducts | Retrieves superfund products
[**get_superfunds**](PayrollAuApi.md#get_superfunds) | **GET** /Superfunds | Retrieves superfunds
[**get_timesheet**](PayrollAuApi.md#get_timesheet) | **GET** /Timesheets/{TimesheetID} | Retrieves a timesheet by using a unique timesheet id
[**get_timesheets**](PayrollAuApi.md#get_timesheets) | **GET** /Timesheets | Retrieves timesheets
[**reject_leave_application**](PayrollAuApi.md#reject_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID}/reject | Reject a leave application by a unique leave application id
[**update_employee**](PayrollAuApi.md#update_employee) | **POST** /Employees/{EmployeeID} | Updates an employee&#39;s detail
[**update_leave_application**](PayrollAuApi.md#update_leave_application) | **POST** /LeaveApplications/{LeaveApplicationID} | Updates a specific leave application
[**update_pay_run**](PayrollAuApi.md#update_pay_run) | **POST** /PayRuns/{PayRunID} | Updates a pay run
[**update_payslip**](PayrollAuApi.md#update_payslip) | **POST** /Payslip/{PayslipID} | Updates a payslip
[**update_superfund**](PayrollAuApi.md#update_superfund) | **POST** /Superfunds/{SuperFundID} | Updates a superfund
[**update_timesheet**](PayrollAuApi.md#update_timesheet) | **POST** /Timesheets/{TimesheetID} | Updates a timesheet


# **approve_leave_application**
> LeaveApplications approve_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)

Approve a requested leave application by a unique leave application id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Approve a requested leave application by a unique leave application id
    api_response = api_instance.approve_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->approve_leave_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | [**str**](.md)| Leave Application id for single object | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee**
> Employees create_employee(xero_tenant_id, employee, idempotency_key=idempotency_key)

Creates a payroll employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee = [ { "FirstName": "Albus", "LastName": "Dumbledore", "DateOfBirth": "/Date(321523200000+0000)/", "HomeAddress": { "AddressLine1": "101 Green St", "City": "Island Bay", "Region": "NSW", "PostalCode": "6023", "Country": "AUSTRALIA" }, "StartDate": "/Date(321523200000+0000)/", "MiddleNames": "Percival", "Email": "albus39608@hogwarts.edu", "Gender": "M", "Phone": "444-2323", "Mobile": "555-1212", "IsAuthorisedToApproveLeave": true, "IsAuthorisedToApproveTimesheets": true, "JobTitle": "Regional Manager", "Classification": "corporate", "OrdinaryEarningsRateID": "ab874dfb-ab09-4c91-954e-43acf6fc23b4", "Status": "ACTIVE" } ] # list[Employee] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a payroll employee
    api_response = api_instance.create_employee(xero_tenant_id, employee, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee** | [**list[Employee]**](Employee.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_leave_application**
> LeaveApplications create_leave_application(xero_tenant_id, leave_application, idempotency_key=idempotency_key)

Creates a leave application

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_application = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "Title": "Hello World", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/" } ] # list[LeaveApplication] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a leave application
    api_response = api_instance.create_leave_application(xero_tenant_id, leave_application, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_leave_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application** | [**list[LeaveApplication]**](LeaveApplication.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pay_item**
> PayItems create_pay_item(xero_tenant_id, pay_item, idempotency_key=idempotency_key)

Creates a pay item

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_item = { "EarningsRates": [ { "Name": "MyRate", "AccountCode": "400", "TypeOfUnits": "4.00", "IsExemptFromTax": true, "IsExemptFromSuper": true, "IsReportableAsW1": false, "AllowanceContributesToAnnualLeaveRate": false, "AllowanceContributesToOvertimeRate": false, "EarningsType": "ORDINARYTIMEEARNINGS", "EarningsRateID": "1fa4e226-b711-46ba-a8a7-4344c9c5fb87", "RateType": "MULTIPLE", "RatePerUnit": "10.0", "Multiplier": 1.5, "Amount": 5, "EmploymentTerminationPaymentType": "O" } ] } # PayItem | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a pay item
    api_response = api_instance.create_pay_item(xero_tenant_id, pay_item, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_pay_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_item** | [**PayItem**](PayItem.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pay_run**
> PayRuns create_pay_run(xero_tenant_id, pay_run, idempotency_key=idempotency_key)

Creates a pay run

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run = [ { "PayrollCalendarID": "78bb86b9-e1ea-47ac-b75d-f087a81931de", "PayRunPeriodStartDate": "/Date(1572566400000+0000)/", "PayRunPeriodEndDate": "/Date(1573084800000+0000)/", "PayRunStatus": "DRAFT", "PaymentDate": "/Date(1573171200000+0000)/" } ] # list[PayRun] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a pay run
    api_response = api_instance.create_pay_run(xero_tenant_id, pay_run, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_pay_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run** | [**list[PayRun]**](PayRun.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payroll_calendar**
> PayrollCalendars create_payroll_calendar(xero_tenant_id, payroll_calendar, idempotency_key=idempotency_key)

Creates a Payroll Calendar

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
payroll_calendar = [ { "PayrollCalendarID":"78bb86b9-e1ea-47ac-b75d-f087a81931de", "PayRunPeriodStartDate":"/Date(1572566400000+0000)/", "PayRunPeriodEndDate":"/Date(1573084800000+0000)/", "PayRunStatus":"DRAFT", "PaymentDate":"/Date(1573171200000+0000)/" } ] # list[PayrollCalendar] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a Payroll Calendar
    api_response = api_instance.create_payroll_calendar(xero_tenant_id, payroll_calendar, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_payroll_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payroll_calendar** | [**list[PayrollCalendar]**](PayrollCalendar.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_superfund**
> SuperFunds create_superfund(xero_tenant_id, super_fund, idempotency_key=idempotency_key)

Creates a superfund

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
super_fund = [ { "usi":"PTC0133AU", "Type":"REGULATED", "Name":"Bar99359", "AccountNumber":"FB36350", "AccountName":"Foo38428", "USI":"PTC0133AU" } ] # list[SuperFund] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a superfund
    api_response = api_instance.create_superfund(xero_tenant_id, super_fund, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_superfund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund** | [**list[SuperFund]**](SuperFund.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet**
> Timesheets create_timesheet(xero_tenant_id, timesheet, idempotency_key=idempotency_key)

Creates a timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet = [ { "EmployeeID":"b34e89ff-770d-4099-b7e5-f968767118bc", "StartDate":"/Date(1573171200000+0000)/", "EndDate":"/Date(1573689600000+0000)/", "Status":"DRAFT", "TimesheetLines":[ { "EarningsRateID":"ab874dfb-ab09-4c91-954e-43acf6fc23b4", "TrackingItemID":"af5e9ce2-2349-4136-be99-3561b189f473", "NumberOfUnits":[ 2.0, 10.0, 0.0, 0.0, 5.0, 0.0, 5.0 ] } ] } ] # list[Timesheet] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a timesheet
    api_response = api_instance.create_timesheet(xero_tenant_id, timesheet, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->create_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet** | [**list[Timesheet]**](Timesheet.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> Employees get_employee(xero_tenant_id, employee_id)

Retrieves an employee's detail by unique employee id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
try:
    # Retrieves an employee's detail by unique employee id
    api_response = api_instance.get_employee(xero_tenant_id, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> Employees get_employees(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Searches payroll employees

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 employees will be returned in a single API call (optional)
try:
    # Searches payroll employees
    api_response = api_instance.get_employees(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 employees will be returned in a single API call | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_application**
> LeaveApplications get_leave_application(xero_tenant_id, leave_application_id)

Retrieves a leave application by a unique leave application id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
try:
    # Retrieves a leave application by a unique leave application id
    api_response = api_instance.get_leave_application(xero_tenant_id, leave_application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_leave_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | [**str**](.md)| Leave Application id for single object | 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_applications**
> LeaveApplications get_leave_applications(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves leave applications

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)
try:
    # Retrieves leave applications
    api_response = api_instance.get_leave_applications(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_leave_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leave_applications_v2**
> LeaveApplications get_leave_applications_v2(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves leave applications including leave requests

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)
try:
    # Retrieves leave applications including leave requests
    api_response = api_instance.get_leave_applications_v2(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_leave_applications_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_items**
> PayItems get_pay_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves pay items

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)
try:
    # Retrieves pay items
    api_response = api_instance.get_pay_items(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_pay_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_run**
> PayRuns get_pay_run(xero_tenant_id, pay_run_id)

Retrieves a pay run by using a unique pay run id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | PayRun id for single object
try:
    # Retrieves a pay run by using a unique pay run id
    api_response = api_instance.get_pay_run(xero_tenant_id, pay_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_pay_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | [**str**](.md)| PayRun id for single object | 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pay_runs**
> PayRuns get_pay_runs(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves pay runs

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 PayRuns will be returned in a single API call (optional)
try:
    # Retrieves pay runs
    api_response = api_instance.get_pay_runs(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_pay_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 PayRuns will be returned in a single API call | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_calendar**
> PayrollCalendars get_payroll_calendar(xero_tenant_id, payroll_calendar_id)

Retrieves payroll calendar by using a unique payroll calendar ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
payroll_calendar_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payroll Calendar id for single object
try:
    # Retrieves payroll calendar by using a unique payroll calendar ID
    api_response = api_instance.get_payroll_calendar(xero_tenant_id, payroll_calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_payroll_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payroll_calendar_id** | [**str**](.md)| Payroll Calendar id for single object | 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payroll_calendars**
> PayrollCalendars get_payroll_calendars(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves payroll calendars

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 objects will be returned in a single API call (optional)
try:
    # Retrieves payroll calendars
    api_response = api_instance.get_payroll_calendars(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_payroll_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payslip**
> PayslipObject get_payslip(xero_tenant_id, payslip_id)

Retrieves for a payslip by a unique payslip id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
payslip_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payslip id for single object
try:
    # Retrieves for a payslip by a unique payslip id
    api_response = api_instance.get_payslip(xero_tenant_id, payslip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_payslip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payslip_id** | [**str**](.md)| Payslip id for single object | 

### Return type

[**PayslipObject**](PayslipObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> SettingsObject get_settings(xero_tenant_id)

Retrieves payroll settings

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
try:
    # Retrieves payroll settings
    api_response = api_instance.get_settings(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**SettingsObject**](SettingsObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superfund**
> SuperFunds get_superfund(xero_tenant_id, super_fund_id)

Retrieves a superfund by using a unique superfund ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
super_fund_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Superfund id for single object
try:
    # Retrieves a superfund by using a unique superfund ID
    api_response = api_instance.get_superfund(xero_tenant_id, super_fund_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_superfund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund_id** | [**str**](.md)| Superfund id for single object | 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superfund_products**
> SuperFundProducts get_superfund_products(xero_tenant_id, abn=abn, usi=usi)

Retrieves superfund products

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
abn = '40022701955' # str | The ABN of the Regulated SuperFund (optional)
usi = 'OSF0001AU' # str | The USI of the Regulated SuperFund (optional)
try:
    # Retrieves superfund products
    api_response = api_instance.get_superfund_products(xero_tenant_id, abn=abn, usi=usi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_superfund_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **abn** | **str**| The ABN of the Regulated SuperFund | [optional] 
 **usi** | **str**| The USI of the Regulated SuperFund | [optional] 

### Return type

[**SuperFundProducts**](SuperFundProducts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_superfunds**
> SuperFunds get_superfunds(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves superfunds

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call (optional)
try:
    # Retrieves superfunds
    api_response = api_instance.get_superfunds(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_superfunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 SuperFunds will be returned in a single API call | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheet**
> TimesheetObject get_timesheet(xero_tenant_id, timesheet_id)

Retrieves a timesheet by using a unique timesheet id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Timesheet id for single object
try:
    # Retrieves a timesheet by using a unique timesheet id
    api_response = api_instance.get_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Timesheet id for single object | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheets**
> Timesheets get_timesheets(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)

Retrieves timesheets

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
if_modified_since = '2020-02-06T12:17:43.202-08:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'Status==\"ACTIVE\"' # str | Filter by an any element (optional)
order = 'EmailAddress%20DESC' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 timesheets will be returned in a single API call (optional)
try:
    # Retrieves timesheets
    api_response = api_instance.get_timesheets(xero_tenant_id, if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->get_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 timesheets will be returned in a single API call | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_leave_application**
> LeaveApplications reject_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)

Reject a leave application by a unique leave application id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Reject a leave application by a unique leave application id
    api_response = api_instance.reject_leave_application(xero_tenant_id, leave_application_id, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->reject_leave_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | [**str**](.md)| Leave Application id for single object | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> Employees update_employee(xero_tenant_id, employee_id, employee, idempotency_key=idempotency_key)

Updates an employee's detail

Update properties on a single employee

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
employee_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Employee id for single object
employee = [ { "MiddleNames": "Frank" } ] # list[Employee] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates an employee's detail
    api_response = api_instance.update_employee(xero_tenant_id, employee_id, employee, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **employee_id** | [**str**](.md)| Employee id for single object | 
 **employee** | [**list[Employee]**](Employee.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_leave_application**
> LeaveApplications update_leave_application(xero_tenant_id, leave_application_id, leave_application, idempotency_key=idempotency_key)

Updates a specific leave application

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
leave_application_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Leave Application id for single object
leave_application = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveApplicationID": "1d4cd583-0107-4386-936b-672eb3d1f624", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "LeavePeriods": [ { "PayPeriodStartDate": "/Date(1572566400000+0000)/", "PayPeriodEndDate": "/Date(1573084800000+0000)/", "LeavePeriodStatus": "SCHEDULED", "NumberOfUnits": 7.6 } ], "Title": "vacation", "Description": "My updated Description", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/", "PayOutType": "DEFAULT" } ] # list[LeaveApplication] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a specific leave application
    api_response = api_instance.update_leave_application(xero_tenant_id, leave_application_id, leave_application, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_leave_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **leave_application_id** | [**str**](.md)| Leave Application id for single object | 
 **leave_application** | [**list[LeaveApplication]**](LeaveApplication.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pay_run**
> PayRuns update_pay_run(xero_tenant_id, pay_run_id, pay_run, idempotency_key=idempotency_key)

Updates a pay run

Update properties on a single PayRun

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
pay_run_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | PayRun id for single object
pay_run = [xero_python.payrollau.PayRun()] # list[PayRun] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a pay run
    api_response = api_instance.update_pay_run(xero_tenant_id, pay_run_id, pay_run, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_pay_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **pay_run_id** | [**str**](.md)| PayRun id for single object | 
 **pay_run** | [**list[PayRun]**](PayRun.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payslip**
> Payslips update_payslip(xero_tenant_id, payslip_id, payslip_lines, idempotency_key=idempotency_key)

Updates a payslip

Update lines on a single payslips

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
payslip_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Payslip id for single object
payslip_lines = { "Payslip": { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "DeductionLines": [ { "DeductionTypeID": "727af5e8-b347-4ae7-85fc-9b82266d0aec", "CalculationType": "FIXEDAMOUNT", "NumberOfUnits": 10 } ] } } # list[PayslipLines] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a payslip
    api_response = api_instance.update_payslip(xero_tenant_id, payslip_id, payslip_lines, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_payslip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **payslip_id** | [**str**](.md)| Payslip id for single object | 
 **payslip_lines** | [**list[PayslipLines]**](PayslipLines.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Payslips**](Payslips.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_superfund**
> SuperFunds update_superfund(xero_tenant_id, super_fund_id, super_fund, idempotency_key=idempotency_key)

Updates a superfund

Update properties on a single Superfund

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
super_fund_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Superfund id for single object
super_fund =  [ { "Type":"REGULATED", "Name":"Nice23534" } ] # list[SuperFund] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a superfund
    api_response = api_instance.update_superfund(xero_tenant_id, super_fund_id, super_fund, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_superfund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **super_fund_id** | [**str**](.md)| Superfund id for single object | 
 **super_fund** | [**list[SuperFund]**](SuperFund.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timesheet**
> Timesheets update_timesheet(xero_tenant_id, timesheet_id, timesheet, idempotency_key=idempotency_key)

Updates a timesheet

Update properties on a single timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollau import PayrollAuApi
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
api_instance = PayrollAuApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = '4ff1e5cc-9835-40d5-bb18-09fdb118db9c' # str | Timesheet id for single object
timesheet = [ { "EmployeeID":"b34e89ff-770d-4099-b7e5-f968767118bc", "StartDate":"/Date(1573171200000+0000)/", "EndDate":"/Date(1573689600000+0000)/", "Status":"APPROVED", "Hours":22.0, "TimesheetID":"a7eb0a79-8511-4ee7-b473-3a25f28abcb9", "TimesheetLines":[ { "EarningsRateID":"ab874dfb-ab09-4c91-954e-43acf6fc23b4", "TrackingItemID":"af5e9ce2-2349-4136-be99-3561b189f473", "NumberOfUnits":[ 2.0, 10.0, 0.0, 0.0, 5.0, 0.0, 5.0 ], "UpdatedDateUTC":"/Date(1573516185127+0000)/" } ] } ] # list[Timesheet] | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a timesheet
    api_response = api_instance.update_timesheet(xero_tenant_id, timesheet_id, timesheet, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuApi->update_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Timesheet id for single object | 
 **timesheet** | [**list[Timesheet]**](Timesheet.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

