# xero_python.accounting.AccountingApi

All URIs are relative to *https://api.xero.com/api.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_payment**](AccountingApi.md#get_batch_payment) | **GET** /BatchPayments/{BatchPaymentID} | Retrieves a specific batch payment using a unique batch payment Id


# **get_batch_payment**
> BatchPayments get_batch_payment(xero_tenant_id, batch_payment_id)

Retrieves a specific batch payment using a unique batch payment Id

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.accounting import AccountingApi
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
api_instance = AccountingApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
batch_payment_id = '00000000-0000-0000-0000-000000000000' # str | Unique identifier for BatchPayment
try:
    # Retrieves a specific batch payment using a unique batch payment Id
    api_response = api_instance.get_batch_payment(xero_tenant_id, batch_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_batch_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **batch_payment_id** | [**str**](.md)| Unique identifier for BatchPayment | 

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

