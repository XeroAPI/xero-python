# ItemError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies the error. | [optional] 
**subtype** | **str** | Present only on a partial failure (a &#x60;partial-failure-*&#x60; &#x60;type&#x60;). Names the exact cause within the &#x60;type&#x60;. Reading it is optional: the &#x60;type&#x60; alone fixes the recovery action and which identifier fields are present, so branch on &#x60;type&#x60; and use &#x60;subtype&#x60; for diagnostics.  | [optional] 
**title** | **str** | A short human-readable summary of the error. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence. | [optional] 
**account_id** | **str** | Present only on a partial failure. The Xero Bank Account the item concerns. On &#x60;partial-failure-new-account-creation&#x60;, the account that was created: connect it through &#x60;POST /FeedConnections/ExistingAccount&#x60;. On &#x60;partial-failure-previous-connection-deletion&#x60; and &#x60;partial-failure-connection-creation&#x60;, the account being connected. Absent on &#x60;partial-failure-connection-deletion&#x60; and &#x60;partial-failure-new-account-existence-not-confirmed&#x60;, where the account may not exist.  | [optional] 
**account_name** | **str** | Present only on a partial failure of type &#x60;partial-failure-new-account-creation&#x60; or &#x60;partial-failure-new-account-existence-not-confirmed&#x60;. The name of the account that was created, which is now taken; on &#x60;partial-failure-new-account-existence-not-confirmed&#x60;, the name of the account that may have been created.  | [optional] 
**connection_id** | **str** | Present only on a partial failure. On &#x60;partial-failure-previous-connection-deletion&#x60;, the previous connection on the account (removed, or being removed). On &#x60;partial-failure-connection-creation&#x60;, the connection this request created or was creating: the id it was given before the create (the Feed Connection &#x60;id&#x60; if it was recorded). When the subtype is &#x60;connection-existence-not-confirmed&#x60;, the create&#39;s outcome is unknown and the connection may not exist in Xero. On &#x60;partial-failure-connection-deletion&#x60;, the connection being deleted (the item &#x60;id&#x60; also echoes it). Absent on &#x60;partial-failure-new-account-creation&#x60; and &#x60;partial-failure-new-account-existence-not-confirmed&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


