# xero_python.finance.FinanceApi

All URIs are relative to *https://api.xero.com/finance.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounting_activity_account_usage**](FinanceApi.md#get_accounting_activity_account_usage) | **GET** /AccountingActivities/AccountUsage | Get account usage
[**get_accounting_activity_lock_history**](FinanceApi.md#get_accounting_activity_lock_history) | **GET** /AccountingActivities/LockHistory | Get lock history
[**get_accounting_activity_report_history**](FinanceApi.md#get_accounting_activity_report_history) | **GET** /AccountingActivities/ReportHistory | Get report history
[**get_accounting_activity_user_activities**](FinanceApi.md#get_accounting_activity_user_activities) | **GET** /AccountingActivities/UserActivities | Get user activities
[**get_cash_validation**](FinanceApi.md#get_cash_validation) | **GET** /CashValidation | Get cash validation
[**get_financial_statement_balance_sheet**](FinanceApi.md#get_financial_statement_balance_sheet) | **GET** /FinancialStatements/BalanceSheet | Get Balance Sheet report
[**get_financial_statement_cashflow**](FinanceApi.md#get_financial_statement_cashflow) | **GET** /FinancialStatements/Cashflow | Get Cash flow report
[**get_financial_statement_contacts_expense**](FinanceApi.md#get_financial_statement_contacts_expense) | **GET** /FinancialStatements/contacts/expense | Get expense by contacts report
[**get_financial_statement_contacts_revenue**](FinanceApi.md#get_financial_statement_contacts_revenue) | **GET** /FinancialStatements/contacts/revenue | Get revenue by contacts report
[**get_financial_statement_profit_and_loss**](FinanceApi.md#get_financial_statement_profit_and_loss) | **GET** /FinancialStatements/ProfitAndLoss | Get Profit &amp; Loss report
[**get_financial_statement_trial_balance**](FinanceApi.md#get_financial_statement_trial_balance) | **GET** /FinancialStatements/TrialBalance | Get Trial Balance report


# **get_accounting_activity_account_usage**
> AccountUsageResponse get_accounting_activity_account_usage(xero_tenant_id, start_month=start_month, end_month=end_month)

Get account usage

A summary of how each account is being transacted on exposing the level of detail and amounts attributable to manual adjustments.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
start_month = '2020-09' # str | date, yyyy-MM                 If no parameter is provided, the month 12 months prior to the end month will be used.                Account usage for up to 12 months from this date will be returned. (optional)
end_month = '2021-09' # str | date, yyyy-MM                 If no parameter is provided, the current month will be used.                Account usage for up to 12 months prior to this date will be returned. (optional)
try:
    # Get account usage
    api_response = api_instance.get_accounting_activity_account_usage(xero_tenant_id, start_month=start_month, end_month=end_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_accounting_activity_account_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **start_month** | **str**| date, yyyy-MM                 If no parameter is provided, the month 12 months prior to the end month will be used.                Account usage for up to 12 months from this date will be returned. | [optional] 
 **end_month** | **str**| date, yyyy-MM                 If no parameter is provided, the current month will be used.                Account usage for up to 12 months prior to this date will be returned. | [optional] 

### Return type

[**AccountUsageResponse**](AccountUsageResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_activity_lock_history**
> LockHistoryResponse get_accounting_activity_lock_history(xero_tenant_id, end_date=end_date)

Get lock history

Provides a history of locking of accounting books. Locking may be an indicator of good accounting practices that could reduce the risk of changes to accounting records in prior periods.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
end_date = '2021-09-15' # str | date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any changes to hard or soft lock dates that were made within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a change is visible from this API. (optional)
try:
    # Get lock history
    api_response = api_instance.get_accounting_activity_lock_history(xero_tenant_id, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_accounting_activity_lock_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **end_date** | **str**| date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any changes to hard or soft lock dates that were made within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a change is visible from this API. | [optional] 

### Return type

[**LockHistoryResponse**](LockHistoryResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_activity_report_history**
> ReportHistoryResponse get_accounting_activity_report_history(xero_tenant_id, end_date=end_date)

Get report history

For a specified organisation, provides a summary of all the reports published within a given period, which may be an indicator for good business management and oversight.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
end_date = '2021-09-15' # str | date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any reports that were published within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a published report is visible from this API. (optional)
try:
    # Get report history
    api_response = api_instance.get_accounting_activity_report_history(xero_tenant_id, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_accounting_activity_report_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **end_date** | **str**| date, yyyy-MM-dd                 If no parameter is provided, the current date will be used.                Any reports that were published within the period up to 12 months before this date will be returned.                Please be aware that there may be a delay of up to 3 days before a published report is visible from this API. | [optional] 

### Return type

[**ReportHistoryResponse**](ReportHistoryResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_activity_user_activities**
> UserActivitiesResponse get_accounting_activity_user_activities(xero_tenant_id, data_month=data_month)

Get user activities

For a specified organisation, provides a list of all the users registered, and a history of their accounting transactions. Also identifies the existence of an external accounting advisor and the level of interaction.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
data_month = '2021-09' # str | date, yyyy-MM                 The specified month must be complete (in the past); The current month cannot be specified since it is not complete.                If no parameter is provided, the month immediately previous to the current month will be used.                Any user activities occurring within the specified month will be returned.                Please be aware that there may be a delay of up to 3 days before a user activity is visible from this API. (optional)
try:
    # Get user activities
    api_response = api_instance.get_accounting_activity_user_activities(xero_tenant_id, data_month=data_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_accounting_activity_user_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **data_month** | **str**| date, yyyy-MM                 The specified month must be complete (in the past); The current month cannot be specified since it is not complete.                If no parameter is provided, the month immediately previous to the current month will be used.                Any user activities occurring within the specified month will be returned.                Please be aware that there may be a delay of up to 3 days before a user activity is visible from this API. | [optional] 

### Return type

[**UserActivitiesResponse**](UserActivitiesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_validation**
> list[CashValidationResponse] get_cash_validation(xero_tenant_id, balance_date=balance_date, as_at_system_date=as_at_system_date, begin_date=begin_date)

Get cash validation

Summarizes the total cash position for each account for an org

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
balance_date = '2021-09-15' # str | date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘balance date’ will return transactions based on the accounting date entered by the user.  Transactions before the balanceDate will be included.  The user has discretion as to which accounting period the transaction relates to.    The ‘balance date’  will control the latest maximum date of transactions included in the aggregate numbers.  Balance date does not affect the CurrentStatement object, as this will always return the most recent statement before asAtSystemDate (if specified) (optional)
as_at_system_date = '2021-09-15' # str | date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘as at’ date will return transactions based on the  creation date.  It reflects the date the transactions were entered into Xero, not the accounting date.  The ‘as at’ date can not be overridden by the user.  This can be used to estimate a ‘historical frequency of reconciliation’.    The ‘as at’ date will affect the current statement in the response, as any candidate statements created after this date will be filtered out.  Thus the current statement returned will be the most recent statement prior to the specified ‘as at’ date.  Be aware that neither the begin date, nor the balance date, will affect the current statement.    Note;  information is only presented when system architecture allows, meaning historical cash validation information will be an estimate. In addition, delete events are not aware of the ‘as at’ functionality in this endpoint, meaning that transactions deleted at the time the API is accessed will be considered to always have been deleted. (optional)
begin_date = '2021-09-15' # str | date, yyyy-MM-dd     If no parameter is provided, the aggregate results will be drawn from the user’s total history.    The ‘begin date’ will return transactions based on the accounting date entered by the user. Transactions after the beginDate will be included.  The user has discretion as to which accounting period the transaction relates to. (optional)
try:
    # Get cash validation
    api_response = api_instance.get_cash_validation(xero_tenant_id, balance_date=balance_date, as_at_system_date=as_at_system_date, begin_date=begin_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_cash_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **balance_date** | **str**| date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘balance date’ will return transactions based on the accounting date entered by the user.  Transactions before the balanceDate will be included.  The user has discretion as to which accounting period the transaction relates to.    The ‘balance date’  will control the latest maximum date of transactions included in the aggregate numbers.  Balance date does not affect the CurrentStatement object, as this will always return the most recent statement before asAtSystemDate (if specified) | [optional] 
 **as_at_system_date** | **str**| date, yyyy-MM-dd     If no parameter is provided, the current date will be used.    The ‘as at’ date will return transactions based on the  creation date.  It reflects the date the transactions were entered into Xero, not the accounting date.  The ‘as at’ date can not be overridden by the user.  This can be used to estimate a ‘historical frequency of reconciliation’.    The ‘as at’ date will affect the current statement in the response, as any candidate statements created after this date will be filtered out.  Thus the current statement returned will be the most recent statement prior to the specified ‘as at’ date.  Be aware that neither the begin date, nor the balance date, will affect the current statement.    Note;  information is only presented when system architecture allows, meaning historical cash validation information will be an estimate. In addition, delete events are not aware of the ‘as at’ functionality in this endpoint, meaning that transactions deleted at the time the API is accessed will be considered to always have been deleted. | [optional] 
 **begin_date** | **str**| date, yyyy-MM-dd     If no parameter is provided, the aggregate results will be drawn from the user’s total history.    The ‘begin date’ will return transactions based on the accounting date entered by the user. Transactions after the beginDate will be included.  The user has discretion as to which accounting period the transaction relates to. | [optional] 

### Return type

[**list[CashValidationResponse]**](CashValidationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_balance_sheet**
> BalanceSheetResponse get_financial_statement_balance_sheet(xero_tenant_id, balance_date=balance_date)

Get Balance Sheet report

The balance sheet report is a standard financial report which describes the financial position of an organisation at a point in time.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
balance_date = '2020-06-30' # str | Specifies the date for balance sheet report.    Format yyyy-MM-dd. If no parameter is provided, the current date will be used. (optional)
try:
    # Get Balance Sheet report
    api_response = api_instance.get_financial_statement_balance_sheet(xero_tenant_id, balance_date=balance_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_balance_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **balance_date** | **str**| Specifies the date for balance sheet report.    Format yyyy-MM-dd. If no parameter is provided, the current date will be used. | [optional] 

### Return type

[**BalanceSheetResponse**](BalanceSheetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_cashflow**
> CashflowResponse get_financial_statement_cashflow(xero_tenant_id, start_date=start_date, end_date=end_date)

Get Cash flow report

The statement of cash flows - direct method, provides the year to date changes in operating, financing and investing cash flow activities for an organisation. Cashflow statement is not available in US region at this stage.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
start_date = '2020-09-15' # str | Date e.g. yyyy-MM-dd    Specifies the start date for cash flow report.    If no parameter is provided, the date of 12 months before the end date will be used. (optional)
end_date = '2021-09-15' # str | Date e.g. yyyy-MM-dd    Specifies the end date for cash flow report.    If no parameter is provided, the current date will be used. (optional)
try:
    # Get Cash flow report
    api_response = api_instance.get_financial_statement_cashflow(xero_tenant_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_cashflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **start_date** | **str**| Date e.g. yyyy-MM-dd    Specifies the start date for cash flow report.    If no parameter is provided, the date of 12 months before the end date will be used. | [optional] 
 **end_date** | **str**| Date e.g. yyyy-MM-dd    Specifies the end date for cash flow report.    If no parameter is provided, the current date will be used. | [optional] 

### Return type

[**CashflowResponse**](CashflowResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_contacts_expense**
> IncomeByContactResponse get_financial_statement_contacts_expense(xero_tenant_id, contact_ids=contact_ids, include_manual_journals=include_manual_journals, start_date=start_date, end_date=end_date)

Get expense by contacts report

The expense by contact report provides a year to date profit and loss for customers and suppliers for a given organisation, including detailed contact information.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_ids = ['[\"00000000-0000-0000-0000-000000000000\",\"00000000-0000-0000-0000-000000000000\"]'] # list[str] | Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included (optional)
include_manual_journals = true # bool | Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included. (optional)
start_date = '2020-09-15' # str | Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. (optional)
end_date = '2020-09-15' # str | Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. (optional)
try:
    # Get expense by contacts report
    api_response = api_instance.get_financial_statement_contacts_expense(xero_tenant_id, contact_ids=contact_ids, include_manual_journals=include_manual_journals, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_contacts_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_ids** | [**list[str]**](str.md)| Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included | [optional] 
 **include_manual_journals** | **bool**| Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included. | [optional] 
 **start_date** | **str**| Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. | [optional] 
 **end_date** | **str**| Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. | [optional] 

### Return type

[**IncomeByContactResponse**](IncomeByContactResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_contacts_revenue**
> IncomeByContactResponse get_financial_statement_contacts_revenue(xero_tenant_id, contact_ids=contact_ids, include_manual_journals=include_manual_journals, start_date=start_date, end_date=end_date)

Get revenue by contacts report

The revenue by contact report provides a year to date profit and loss for customers and suppliers for a given organisation, including detailed contact information.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
contact_ids = ['[\"00000000-0000-0000-0000-000000000000\",\"00000000-0000-0000-0000-000000000000\"]'] # list[str] | Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included (optional)
include_manual_journals = true # bool | Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included. (optional)
start_date = '2020-09-15' # str | Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. (optional)
end_date = '2020-09-15' # str | Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. (optional)
try:
    # Get revenue by contacts report
    api_response = api_instance.get_financial_statement_contacts_revenue(xero_tenant_id, contact_ids=contact_ids, include_manual_journals=include_manual_journals, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_contacts_revenue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **contact_ids** | [**list[str]**](str.md)| Specifies the customer contacts to be included in the report.    If no parameter is provided, all customer contacts will be included | [optional] 
 **include_manual_journals** | **bool**| Specifies whether to include the manual journals in the report.                If no parameter is provided, manual journals will not be included. | [optional] 
 **start_date** | **str**| Date yyyy-MM-dd    Specifies the start date for the report.                If no parameter is provided, the date of 12 months before the end date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. | [optional] 
 **end_date** | **str**| Date yyyy-MM-dd    Specifies the end date for the report.    If no parameter is provided, the current date will be used.                It is recommended to always specify both a start date and end date; While the initial range may be set to 12 months, this may need to be reduced for high volume organisations in order to improve latency. | [optional] 

### Return type

[**IncomeByContactResponse**](IncomeByContactResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_profit_and_loss**
> ProfitAndLossResponse get_financial_statement_profit_and_loss(xero_tenant_id, start_date=start_date, end_date=end_date)

Get Profit & Loss report

The profit and loss statement is a standard financial report providing detailed year to date income and expense detail for an organisation.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
start_date = '2020-09-15' # str | Date e.g. yyyy-MM-dd    Specifies the start date for profit and loss report    If no parameter is provided, the date of 12 months before the end date will be used. (optional)
end_date = '2021-09-15' # str | Date e.g. yyyy-MM-dd    Specifies the end date for profit and loss report     If no parameter is provided, the current date will be used. (optional)
try:
    # Get Profit & Loss report
    api_response = api_instance.get_financial_statement_profit_and_loss(xero_tenant_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_profit_and_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **start_date** | **str**| Date e.g. yyyy-MM-dd    Specifies the start date for profit and loss report    If no parameter is provided, the date of 12 months before the end date will be used. | [optional] 
 **end_date** | **str**| Date e.g. yyyy-MM-dd    Specifies the end date for profit and loss report     If no parameter is provided, the current date will be used. | [optional] 

### Return type

[**ProfitAndLossResponse**](ProfitAndLossResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_statement_trial_balance**
> TrialBalanceResponse get_financial_statement_trial_balance(xero_tenant_id, end_date=end_date)

Get Trial Balance report

The trial balance provides a detailed list of all accounts of an organisation at a point in time, with revenue and expense items being year to date.

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.finance import FinanceApi
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
api_instance = FinanceApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
end_date = '2021-09-15' # str | Date e.g. yyyy-MM-dd     Specifies the end date for trial balance report     If no parameter is provided, the current date will be used. (optional)
try:
    # Get Trial Balance report
    api_response = api_instance.get_financial_statement_trial_balance(xero_tenant_id, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceApi->get_financial_statement_trial_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **end_date** | **str**| Date e.g. yyyy-MM-dd     Specifies the end date for trial balance report     If no parameter is provided, the current date will be used. | [optional] 

### Return type

[**TrialBalanceResponse**](TrialBalanceResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

