# xero_python.assets.AssetApi

All URIs are relative to *https://api.xero.com/assets.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetApi.md#create_asset) | **POST** /Assets | adds a fixed asset
[**create_asset_type**](AssetApi.md#create_asset_type) | **POST** /AssetTypes | adds a fixed asset type
[**get_asset_by_id**](AssetApi.md#get_asset_by_id) | **GET** /Assets/{id} | Retrieves fixed asset by id
[**get_asset_settings**](AssetApi.md#get_asset_settings) | **GET** /Settings | searches fixed asset settings
[**get_asset_types**](AssetApi.md#get_asset_types) | **GET** /AssetTypes | searches fixed asset types
[**get_assets**](AssetApi.md#get_assets) | **GET** /Assets | searches fixed asset


# **create_asset**
> Asset create_asset(xero_tenant_id, asset, idempotency_key=idempotency_key)

adds a fixed asset

Adds an asset to the system

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
asset = { "assetName":"Computer74863", "assetNumber":"123477544", "purchaseDate":"2020-01-01", "purchasePrice":100.0, "disposalPrice":23.23, "assetStatus":"Draft", "bookDepreciationSetting":{ "depreciationMethod":"StraightLine", "averagingMethod":"ActualDays", "depreciationRate":0.5, "depreciationCalculationMethod":"None" }, "bookDepreciationDetail":{ "currentCapitalGain":5.32, "currentGainLoss":3.88, "depreciationStartDate":"2020-01-02", "costLimit":100.0, "currentAccumDepreciationAmount":2.25 }, "AccountingBookValue":99.5 } # Asset | Fixed asset you are creating
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # adds a fixed asset
    api_response = api_instance.create_asset(xero_tenant_id, asset, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **asset** | [**Asset**](Asset.md)| Fixed asset you are creating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_type**
> AssetType create_asset_type(xero_tenant_id, asset_type, idempotency_key=idempotency_key)

adds a fixed asset type

Adds an fixed asset type to the system

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
asset_type = { "assetTypeName":"Machinery11004", "fixedAssetAccountId":"3d8d063a-c148-4bb8-8b3c-a5e2ad3b1e82", "depreciationExpenseAccountId":"d1602f69-f900-4616-8d34-90af393fa368", "accumulatedDepreciationAccountId":"9195cadd-8645-41e6-9f67-7bcd421defe8", "bookDepreciationSetting":{ "depreciationMethod":"DiminishingValue100", "averagingMethod":"ActualDays", "depreciationRate":0.05, "depreciationCalculationMethod":"None" } } # AssetType | Asset type to add
idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)
try:
    # adds a fixed asset type
    api_response = api_instance.create_asset_type(xero_tenant_id, asset_type, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->create_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **asset_type** | [**AssetType**](AssetType.md)| Asset type to add | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> Asset get_asset_by_id(xero_tenant_id, id)

Retrieves fixed asset by id

By passing in the appropriate asset id, you can search for a specific fixed asset in the system 

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
id = '00000000-0000-0000-0000-000000000000' # str | fixed asset id for single object
try:
    # Retrieves fixed asset by id
    api_response = api_instance.get_asset_by_id(xero_tenant_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **id** | [**str**](.md)| fixed asset id for single object | 

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_settings**
> Setting get_asset_settings(xero_tenant_id)

searches fixed asset settings

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # searches fixed asset settings
    api_response = api_instance.get_asset_settings(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**Setting**](Setting.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> list[AssetType] get_asset_types(xero_tenant_id)

searches fixed asset types

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
try:
    # searches fixed asset types
    api_response = api_instance.get_asset_types(xero_tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 

### Return type

[**list[AssetType]**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> Assets get_assets(xero_tenant_id, status, page=page, page_size=page_size, order_by=order_by, sort_direction=sort_direction, filter_by=filter_by)

searches fixed asset

By passing in the appropriate options, you can search for available fixed asset in the system

### Example

* OAuth Authentication (OAuth2): 
```python
from xero_python.api_client import Configuration, ApiClient
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.exceptions import ApiException
from xero_python.assets import AssetApi
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
api_instance = AssetApi(api_client)

xero_tenant_id = 'YOUR_XERO_TENANT_ID' # str | Xero identifier for Tenant
status = xero_python.assets.AssetStatusQueryParam() # AssetStatusQueryParam | Required when retrieving a collection of assets. See Asset Status Codes
page = 1 # int | Results are paged. This specifies which page of the results to return. The default page is 1. (optional)
page_size = 5 # int | The number of records returned per page. By default the number of records returned is 10. (optional)
order_by = 'AssetName' # str | Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. (optional)
sort_direction = 'ASC' # str | ASC or DESC (optional)
filter_by = 'Company Car' # str | A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. (optional)
try:
    # searches fixed asset
    api_response = api_instance.get_assets(xero_tenant_id, status, page=page, page_size=page_size, order_by=order_by, sort_direction=sort_direction, filter_by=filter_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **status** | [**AssetStatusQueryParam**](.md)| Required when retrieving a collection of assets. See Asset Status Codes | 
 **page** | **int**| Results are paged. This specifies which page of the results to return. The default page is 1. | [optional] 
 **page_size** | **int**| The number of records returned per page. By default the number of records returned is 10. | [optional] 
 **order_by** | **str**| Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. | [optional] 
 **sort_direction** | **str**| ASC or DESC | [optional] 
 **filter_by** | **str**| A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. | [optional] 

### Return type

[**Assets**](Assets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

