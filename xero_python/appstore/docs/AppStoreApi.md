# xero_python.appstore.AppStoreApi

All URIs are relative to *https://api.xero.com/appstore/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription**](AppStoreApi.md#get_subscription) | **GET** /subscriptions/{subscriptionId} | Retrieves a subscription for a given subscriptionId
[**get_usage_records**](AppStoreApi.md#get_usage_records) | **GET** /subscriptions/{subscriptionId}/usage-records | Gets all usage records related to the subscription
[**post_usage_records**](AppStoreApi.md#post_usage_records) | **POST** /subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records | Send metered usage belonging to this subscription and subscription item
[**put_usage_records**](AppStoreApi.md#put_usage_records) | **PUT** /subscriptions/{subscriptionId}/items/{subscriptionItemId}/usage-records/{usageRecordId} | Update and existing metered usage belonging to this subscription and subscription item


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

# **get_usage_records**
> UsageRecordsList get_usage_records(subscription_id)

Gets all usage records related to the subscription

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
    # Gets all usage records related to the subscription
    api_response = api_instance.get_usage_records(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppStoreApi->get_usage_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Unique identifier for Subscription object | 

### Return type

[**UsageRecordsList**](UsageRecordsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_usage_records**
> UsageRecord post_usage_records(subscription_id, subscription_item_id, create_usage_record, idempotency_key=idempotency_key)

Send metered usage belonging to this subscription and subscription item

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
subscription_item_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the subscriptionItem
create_usage_record = { "timestamp": "2022-01-21T13:01:00", "quantity": 10 } # CreateUsageRecord | Contains the quantity for the usage record to create
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Send metered usage belonging to this subscription and subscription item
    api_response = api_instance.post_usage_records(subscription_id, subscription_item_id, create_usage_record, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppStoreApi->post_usage_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Unique identifier for Subscription object | 
 **subscription_item_id** | [**str**](.md)| The unique identifier of the subscriptionItem | 
 **create_usage_record** | [**CreateUsageRecord**](CreateUsageRecord.md)| Contains the quantity for the usage record to create | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**UsageRecord**](UsageRecord.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_usage_records**
> UsageRecord put_usage_records(subscription_id, subscription_item_id, usage_record_id, update_usage_record, idempotency_key=idempotency_key)

Update and existing metered usage belonging to this subscription and subscription item

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
subscription_item_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the subscriptionItem
usage_record_id = '00000000-0000-0000-0000-000000000000' # str | The unique identifier of the usage record
update_usage_record = { "quantity": 10 } # UpdateUsageRecord | Contains the quantity for the usage record to update
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # Update and existing metered usage belonging to this subscription and subscription item
    api_response = api_instance.put_usage_records(subscription_id, subscription_item_id, usage_record_id, update_usage_record, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppStoreApi->put_usage_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Unique identifier for Subscription object | 
 **subscription_item_id** | [**str**](.md)| The unique identifier of the subscriptionItem | 
 **usage_record_id** | [**str**](.md)| The unique identifier of the usage record | 
 **update_usage_record** | [**UpdateUsageRecord**](UpdateUsageRecord.md)| Contains the quantity for the usage record to update | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**UsageRecord**](UsageRecord.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

