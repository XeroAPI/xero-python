# xero_python.appstore.AppStoreApi

All URIs are relative to *https://api.xero.com/appstore/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription**](AppStoreApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Retrieves a subscription for a given subscriptionId


# **get_subscription**
> Subscription get_subscription(subscription_id)

Retrieves a subscription for a given subscriptionId

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.appstore import AppStoreApi
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
api_instance = AppStoreApi(api_client)

subscription_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for Subscription object
try:
    # Retrieves a subscription for a given subscriptionId
    api_response = api_instance.get_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppStoreApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Unique identifier for Subscription object | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

