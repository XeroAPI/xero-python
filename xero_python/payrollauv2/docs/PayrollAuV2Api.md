# xero_python.payrollauv2.PayrollAuV2Api

All URIs are relative to *https://api.xero.com/payroll.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_timesheet**](PayrollAuV2Api.md#approve_timesheet) | **POST** /Timesheets/{TimesheetID}/Approve | Approves a specific timesheet
[**create_timesheet**](PayrollAuV2Api.md#create_timesheet) | **POST** /Timesheets | Creates a new timesheet
[**create_timesheet_line**](PayrollAuV2Api.md#create_timesheet_line) | **POST** /Timesheets/{TimesheetID}/Lines | Creates a new timesheet line for a specific timesheet using a unique timesheet ID
[**delete_timesheet**](PayrollAuV2Api.md#delete_timesheet) | **DELETE** /Timesheets/{TimesheetID} | Deletes a specific timesheet
[**delete_timesheet_line**](PayrollAuV2Api.md#delete_timesheet_line) | **DELETE** /Timesheets/{TimesheetID}/Lines/{TimesheetLineID} | Deletes a specific timesheet line
[**get_timesheet**](PayrollAuV2Api.md#get_timesheet) | **GET** /Timesheets/{TimesheetID} | Retrieve a specific timesheet by using a unique timesheet ID
[**get_timesheets**](PayrollAuV2Api.md#get_timesheets) | **GET** /Timesheets | Retrieves timesheets
[**revert_timesheet**](PayrollAuV2Api.md#revert_timesheet) | **POST** /Timesheets/{TimesheetID}/RevertToDraft | Reverts a specific timesheet to draft
[**update_timesheet_line**](PayrollAuV2Api.md#update_timesheet_line) | **PUT** /Timesheets/{TimesheetID}/Lines/{TimesheetLineID} | Updates a specific timesheet line for a specific timesheet


# **approve_timesheet**
> TimesheetObject approve_timesheet(xero_tenant_id, timesheet_id, idempotency_key=idempotency_key)

Approves a specific timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Approves a specific timesheet
    api_response = api_instance.approve_timesheet(xero_tenant_id, timesheet_id, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->approve_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet**
> TimesheetObject create_timesheet(xero_tenant_id, timesheet, idempotency_key=idempotency_key)

Creates a new timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet = {"payrollCalendarID":"216d80e6-af55-47b1-b718-9457c3f5d2fe","employeeID":"aad6b292-7b94-408b-93f6-e489867e3fb0","startDate":"2020-04-13","endDate":"2020-04-19","timesheetLines":[{"date":"2020-04-13","earningsRateID":"87f5b43a-cf51-4b74-92de-94c819e82d27","numberOfUnits":8},{"date":"2020-04-15","earningsRateID":"87f5b43a-cf51-4b74-92de-94c819e82d27","numberOfUnits":6}]} # Timesheet | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a new timesheet
    api_response = api_instance.create_timesheet(xero_tenant_id, timesheet, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->create_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet** | [**Timesheet**](Timesheet.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet_line**
> TimesheetLineObject create_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line, idempotency_key=idempotency_key)

Creates a new timesheet line for a specific timesheet using a unique timesheet ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line = {"date":"2020-04-14","earningsRateID":"87f5b43a-cf51-4b74-92de-94c819e82d27","numberOfUnits":1} # TimesheetLine | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Creates a new timesheet line for a specific timesheet using a unique timesheet ID
    api_response = api_instance.create_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->create_timesheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **timesheet_line** | [**TimesheetLine**](TimesheetLine.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimesheetLineObject**](TimesheetLineObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet**
> TimesheetLine delete_timesheet(xero_tenant_id, timesheet_id)

Deletes a specific timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # Deletes a specific timesheet
    api_response = api_instance.delete_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->delete_timesheet: %s\n" % e)
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

Deletes a specific timesheet line

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line_id = 'timesheet_line_id_example' # str | Identifier for the timesheet line
try:
    # Deletes a specific timesheet line
    api_response = api_instance.delete_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->delete_timesheet_line: %s\n" % e)
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

# **get_timesheet**
> TimesheetObject get_timesheet(xero_tenant_id, timesheet_id)

Retrieve a specific timesheet by using a unique timesheet ID

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
try:
    # Retrieve a specific timesheet by using a unique timesheet ID
    api_response = api_instance.get_timesheet(xero_tenant_id, timesheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->get_timesheet: %s\n" % e)
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
> Timesheets get_timesheets(xero_tenant_id, page=page, filter=filter, status=status, start_date=start_date, end_date=end_date, sort=sort)

Retrieves timesheets

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 5 # int | Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. (optional)
filter = 'employeeId==00000000-0000-0000-0000-000000000000,payrollCalendarId==00000000-0000-0000-0000-000000000000' # str | Filter by employeeId and/or payrollCalendarId (optional)
status = 'Draft' # str | filter results by any timesheets with a matching timesheet status (optional)
start_date = '2019-01-02' # str | filter results by any timesheets with a startDate on or after the provided date (optional)
end_date = '2020-01-02' # str | filter results by any timesheets with a endDate on or before the provided date (optional)
sort = 'startDate' # str | sort the order of timesheets returned. The default is based on the timesheets createdDate, sorted oldest to newest. Currently, the only other option is to reverse the order based on the timesheets startDate, sorted newest to oldest. (optional)
try:
    # Retrieves timesheets
    api_response = api_instance.get_timesheets(xero_tenant_id, page=page, filter=filter, status=status, start_date=start_date, end_date=end_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->get_timesheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| Page number which specifies the set of records to retrieve. By default the number of the records per set is 100. | [optional] 
 **filter** | **str**| Filter by employeeId and/or payrollCalendarId | [optional] 
 **status** | **str**| filter results by any timesheets with a matching timesheet status | [optional] 
 **start_date** | **str**| filter results by any timesheets with a startDate on or after the provided date | [optional] 
 **end_date** | **str**| filter results by any timesheets with a endDate on or before the provided date | [optional] 
 **sort** | **str**| sort the order of timesheets returned. The default is based on the timesheets createdDate, sorted oldest to newest. Currently, the only other option is to reverse the order based on the timesheets startDate, sorted newest to oldest. | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_timesheet**
> TimesheetObject revert_timesheet(xero_tenant_id, timesheet_id, idempotency_key=idempotency_key)

Reverts a specific timesheet to draft

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Reverts a specific timesheet to draft
    api_response = api_instance.revert_timesheet(xero_tenant_id, timesheet_id, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->revert_timesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timesheet_line**
> TimesheetLineObject update_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id, timesheet_line, idempotency_key=idempotency_key)

Updates a specific timesheet line for a specific timesheet

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.payrollauv2 import PayrollAuV2Api
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
api_instance = PayrollAuV2Api(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
timesheet_id = 'timesheet_id_example' # str | Identifier for the timesheet
timesheet_line_id = 'timesheet_line_id_example' # str | Identifier for the timesheet line
timesheet_line = {"date":"2020-04-14","earningsRateID":"87f5b43a-cf51-4b74-92de-94c819e82d27","numberOfUnits":2} # TimesheetLine | 
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Updates a specific timesheet line for a specific timesheet
    api_response = api_instance.update_timesheet_line(xero_tenant_id, timesheet_id, timesheet_line_id, timesheet_line, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayrollAuV2Api->update_timesheet_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **timesheet_id** | [**str**](.md)| Identifier for the timesheet | 
 **timesheet_line_id** | [**str**](.md)| Identifier for the timesheet line | 
 **timesheet_line** | [**TimesheetLine**](TimesheetLine.md)|  | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimesheetLineObject**](TimesheetLineObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

