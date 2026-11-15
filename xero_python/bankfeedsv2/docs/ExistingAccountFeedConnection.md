# ExistingAccountFeedConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Xero Bank Account to connect the feed to. Required. An all-zeros GUID is treated as though the field were absent.  | 
**account_token** | **str** | The financial institute&#39;s identifier for the account. Must be unique within your financial institute. Some financial institutes additionally constrain its format.  | 
**account_type** | [**AccountType**](AccountType.md) |  | 
**currency** | **str** | ISO-4217 currency code. Must match the currency of the Xero Bank Account named by &#x60;accountId&#x60;, and must be a currency the Organisation has.  | 
**country** | **str** | ISO-3166 alpha-2 country code. Required only when the Application supports multiple regions. Talk to your Partner Manager to confirm whether this applies to you.  | [optional] 
**account_number** | **str** | Ignored. Taken from the Xero Bank Account named by &#x60;accountId&#x60;. | [optional] 
**account_name** | **str** | Ignored. Taken from the Xero Bank Account named by &#x60;accountId&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


