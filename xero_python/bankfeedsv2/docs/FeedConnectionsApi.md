# xero_python.bankfeedsv2.FeedConnectionsApi

All URIs are relative to *https://api.xero.com/bankfeeds.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feed_connections_for_existing_accounts**](FeedConnectionsApi.md#create_feed_connections_for_existing_accounts) | **POST** /FeedConnections/ExistingAccount | Connect feeds to Xero Bank Accounts that already exist
[**create_feed_connections_for_new_accounts**](FeedConnectionsApi.md#create_feed_connections_for_new_accounts) | **POST** /FeedConnections/NewAccount | Create Xero Bank Accounts and connect feeds to them
[**delete_feed_connections**](FeedConnectionsApi.md#delete_feed_connections) | **POST** /FeedConnections/DeleteRequests | Terminate Feed Connections
[**get_feed_connection**](FeedConnectionsApi.md#get_feed_connection) | **GET** /FeedConnections/{id} | Retrieve a single Feed Connection
[**get_feed_connections**](FeedConnectionsApi.md#get_feed_connections) | **GET** /FeedConnections | Retrieve the Feed Connections for an Organisation


# **create_feed_connections_for_existing_accounts**
> BulkFeedConnectionResponse create_feed_connections_for_existing_accounts(xero_tenant_id, existing_account_feed_connections_request)

Connect feeds to Xero Bank Accounts that already exist

Creates Feed Connections against Xero Bank Accounts the Organisation already has. Each item must include the `accountId` of the account it connects to. Xero performs no matching of its own, and `accountNumber` and `accountName` are ignored if supplied.  Use this endpoint whenever the customer has chosen an account, including when they are reconnecting a feed that was previously terminated.  Each item is processed independently, and the response has one result per request item in request order. 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.bankfeedsv2 import FeedConnectionsApi
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
api_instance = FeedConnectionsApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
existing_account_feed_connections_request = {"items":[{"accountId":"87d7b3b9-af8e-4f7e-a7e1-294e6e50b19a","accountToken":"10000123","accountType":"BANK","currency":"AUD"},{"accountId":"2c1f0a7e-0c41-4a5e-9f6c-1f7b2b9a5d33","accountToken":"10000124","accountType":"CREDITCARD","currency":"GBP","country":"GB"}]} # ExistingAccountFeedConnectionsRequest | 
try:
    # Connect feeds to Xero Bank Accounts that already exist
    api_response = api_instance.create_feed_connections_for_existing_accounts(xero_tenant_id, existing_account_feed_connections_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedConnectionsApi->create_feed_connections_for_existing_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **existing_account_feed_connections_request** | [**ExistingAccountFeedConnectionsRequest**](ExistingAccountFeedConnectionsRequest.md)|  | 

### Return type

[**BulkFeedConnectionResponse**](BulkFeedConnectionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feed_connections_for_new_accounts**
> BulkFeedConnectionResponse create_feed_connections_for_new_accounts(xero_tenant_id, new_account_feed_connections_request)

Create Xero Bank Accounts and connect feeds to them

Creates a new Xero Bank Account for each item and connects a feed to it.  `accountId` must not be supplied. An item that includes one — including an all-zeros GUID, or a value that is not a GUID at all — is rejected, because supplying an account identifier means the Application intends to connect an account that already exists, which is what `/FeedConnections/ExistingAccount` is for.  `accountNumber` and `accountName` are required here, since they describe the account being created. If the Organisation already has an account with the requested name, the item is rejected with `account-name-already-exists` naming that account, and no account is created. The same applies to a second item in the same request that uses a name an earlier item has just taken. 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.bankfeedsv2 import FeedConnectionsApi
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
api_instance = FeedConnectionsApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
new_account_feed_connections_request = {"items":[{"accountToken":"10000123","accountNumber":"3809087654321500","accountName":"Joe's Savings Account","accountType":"BANK","currency":"AUD"},{"accountToken":"10000124","accountNumber":"1234","accountName":"Sam's Credit Card","accountType":"CREDITCARD","currency":"AUD"}]} # NewAccountFeedConnectionsRequest | 
try:
    # Create Xero Bank Accounts and connect feeds to them
    api_response = api_instance.create_feed_connections_for_new_accounts(xero_tenant_id, new_account_feed_connections_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedConnectionsApi->create_feed_connections_for_new_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **new_account_feed_connections_request** | [**NewAccountFeedConnectionsRequest**](NewAccountFeedConnectionsRequest.md)|  | 

### Return type

[**BulkFeedConnectionResponse**](BulkFeedConnectionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feed_connections**
> BulkFeedConnectionResponse delete_feed_connections(xero_tenant_id, delete_feed_connections_request)

Terminate Feed Connections

Terminates the Feed Connections named in the request. Terminating a Feed Connection discontinues the bank feed, and does not otherwise affect the customer's data in Xero.  Each item is identified by the Feed Connection `id` alone. An item naming a Feed Connection that does not exist, has already been terminated, or belongs to a different Application is reported as `feed-not-found-or-already-deleted` with `status` `SUCCESS` and `statusCode` `204` — there was nothing to terminate, which is not a failure, and is reported the same way a real termination is.  The same identifier may not appear twice in one request.  Re-sending a completed delete is idempotent. If an item reports `PARTIAL_FAILURE`, or the original response was lost, resend the same DeleteRequests item. The retry checks whether the connection remains and terminates it if needed. A `SUCCESS` item on the resend means the deletion is complete, including `feed-not-found-or-already-deleted` at `statusCode` `204`. If a retry keeps reporting `PARTIAL_FAILURE`, contact Xero support with the connection id in `error.connectionId`. 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.bankfeedsv2 import FeedConnectionsApi
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
api_instance = FeedConnectionsApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
delete_feed_connections_request = {"items":[{"id":"ac231d36-e7bc-4eb2-ad0f-2ecf328305f1"},{"id":"880600c2-d302-4b9c-a88a-e0253c926ab2"}]} # DeleteFeedConnectionsRequest | 
try:
    # Terminate Feed Connections
    api_response = api_instance.delete_feed_connections(xero_tenant_id, delete_feed_connections_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedConnectionsApi->delete_feed_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **delete_feed_connections_request** | [**DeleteFeedConnectionsRequest**](DeleteFeedConnectionsRequest.md)|  | 

### Return type

[**BulkFeedConnectionResponse**](BulkFeedConnectionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_connection**
> FeedConnection get_feed_connection(id, xero_tenant_id)

Retrieve a single Feed Connection

Returns one Feed Connection, as a bare object rather than inside an envelope.  The response is `404 bank-feed-not-found` when the identifier names no Feed Connection, when it names one belonging to a different Application, when it is an all-zeros GUID, and when it is not a GUID at all. These cases are deliberately indistinguishable from one another, so an Application cannot use this endpoint to discover what another Application has. 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.bankfeedsv2 import FeedConnectionsApi
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
api_instance = FeedConnectionsApi(api_client)

id = 'id_example' # str | The Feed Connection identifier.
xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
try:
    # Retrieve a single Feed Connection
    api_response = api_instance.get_feed_connection(id, xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedConnectionsApi->get_feed_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The Feed Connection identifier. | 
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**FeedConnection**](FeedConnection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_connections**
> PagedFeedConnections get_feed_connections(xero_tenant_id, page=page, page_size=page_size)

Retrieve the Feed Connections for an Organisation

Returns the Feed Connections belonging to both the Organisation in `Xero-Tenant-Id` and the Application associated with the OAuth client. Connections belonging to another Application are not returned, and there is no way to observe that they exist.  A `page` beyond the end of the collection returns an empty `items` array rather than an error. 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.bankfeedsv2 import FeedConnectionsApi
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
api_instance = FeedConnectionsApi(api_client)

xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
page = 1 # int | The page to return, counting from 1. (optional) (default to 1)
page_size = 10 # int | How many Feed Connections to return per page. No maximum is enforced. (optional) (default to 10)
try:
    # Retrieve the Feed Connections for an Organisation
    api_response = api_instance.get_feed_connections(xero_tenant_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedConnectionsApi->get_feed_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| The page to return, counting from 1. | [optional] [default to 1]
 **page_size** | **int**| How many Feed Connections to return per page. No maximum is enforced. | [optional] [default to 10]

### Return type

[**PagedFeedConnections**](PagedFeedConnections.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

