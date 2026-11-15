# BulkFeedConnectionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | On a create, Xero&#39;s identifier for the new Feed Connection; absent when the item was rejected, since nothing was created.  On a termination, the identifier supplied in the request, echoed back; absent only when the item did not include a usable identifier.  | [optional] 
**account_token** | **str** | The &#x60;accountToken&#x60; supplied in the request, echoed back, including on a rejected item. Not returned on a termination.  | [optional] 
**status** | **str** | &#x60;SUCCESS&#x60; means the item reached the state the request asked for — on a create the connection exists, on a termination it is gone, including the idempotent case where it was already gone. &#x60;REJECTED&#x60; means nothing was written, or Xero confirmed that nothing took effect. A &#x60;4xx&#x60; item needs correcting before it is sent again, and a &#x60;500&#x60; item can be resent as it is. &#x60;error&#x60; says why. &#x60;PARTIAL_FAILURE&#x60; means the item did not complete, and the state it left behind needs attention or could not be confirmed. &#x60;error.subtype&#x60; says which, &#x60;error.detail&#x60; describes it, and the item needs attention that neither of the other two values implies.  A client deserialising this into a closed set of &#x60;SUCCESS&#x60; and &#x60;REJECTED&#x60; will fail on &#x60;PARTIAL_FAILURE&#x60;. That is intended rather than an oversight: binding it silently to either of the other two would hide state that the partner has to act on.  | [optional] 
**status_code** | **int** | The numeric status of this item: &#x60;201&#x60; on a created connection, &#x60;204&#x60; on a terminated or already-absent one, a 4xx on a rejection, &#x60;500&#x60; on a partial failure or on a rejection whose error is &#x60;internal-error&#x60; or &#x60;too-many-requests&#x60;. The response envelope is computed from the items&#39; &#x60;statusCode&#x60; values: all 2xx is &#x60;200&#x60;, all 4xx is &#x60;400&#x60;, anything else is &#x60;207&#x60;. So a partner can size up one item without reading &#x60;status&#x60; and &#x60;error&#x60; together. Never &#x60;202&#x60; and never &#x60;207&#x60;: those are envelope-only, and an item-level &#x60;207&#x60; would be numerically inside 2xx, so a batch of partial failures could be reported as &#x60;200&#x60;.  | [optional] 
**error** | [**ItemError**](ItemError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


