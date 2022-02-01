# SubscriptionItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | Date when the subscription to this product will end | [optional] 
**id** | **str** | The unique identifier of the subscription item. | 
**price** | [**Price**](Price.md) |  | 
**product** | [**Product**](Product.md) |  | 
**start_date** | **datetime** | Date the subscription started, or will start. Note: this could be in the future for downgrades or reduced number of seats that haven&#39;t taken effect yet.  | 
**status** | **str** | Status of the subscription item. Available statuses are ACTIVE, CANCELED, and PENDING_ACTIVATION.  | 
**test_mode** | **bool** | If the subscription is a test subscription | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


