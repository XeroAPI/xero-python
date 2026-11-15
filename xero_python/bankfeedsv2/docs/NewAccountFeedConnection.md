# NewAccountFeedConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_token** | **str** | The financial institute&#39;s identifier for the account. Must be unique within your financial institute.  | 
**account_type** | [**AccountType**](AccountType.md) |  | 
**account_number** | **str** | The account number for the Xero Bank Account being created. Up to 40 characters when &#x60;accountType&#x60; is &#x60;BANK&#x60;. When &#x60;accountType&#x60; is &#x60;CREDITCARD&#x60;, supply only the last four digits, and digits only.  | 
**account_name** | **str** | The name for the Xero Bank Account being created. Rejected if the Organisation already has an account with this name.  | 
**currency** | **str** | ISO-4217 currency code. Must be a currency the Organisation has. | 
**country** | **str** | ISO-3166 alpha-2 country code. Required only when the Application supports multiple regions.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


