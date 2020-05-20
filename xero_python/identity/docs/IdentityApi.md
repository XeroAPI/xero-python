# xero_python.identity.IdentityApi

All URIs are relative to *https://api.xero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection**](IdentityApi.md#delete_connection) | **DELETE** /connections/{id} | Allows you to delete a connection for this user (i.e. disconnect a tenant)
[**get_connections**](IdentityApi.md#get_connections) | **GET** /connections | Allows you to retrieve the connections for this user


# **delete_connection**
> delete_connection(id)

Allows you to delete a connection for this user (i.e. disconnect a tenant)

Override the base server url that include version

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.identity import IdentityApi


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
api_instance = IdentityApi(api_client)

id = 'id_example' # str | Unique identifier for retrieving single object
try:
    # Allows you to delete a connection for this user (i.e. disconnect a tenant)
    api_instance.delete_connection(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Unique identifier for retrieving single object | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> list[Connection] get_connections()

Allows you to retrieve the connections for this user

Override the base server url that include version

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.identity import IdentityApi
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
api_instance = IdentityApi(api_client)

try:
    # Allows you to retrieve the connections for this user
    api_response = api_instance.get_connections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Connection]**](Connection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

