# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Identifier of the task. | [optional] 
**name** | **str** | Name of the task. | [optional] 
**rate** | [**Amount**](Amount.md) |  | [optional] 
**charge_type** | [**ChargeType**](ChargeType.md) |  | [optional] 
**estimate_minutes** | **float** | An estimated time to perform the task | [optional] 
**project_id** | **str** | Identifier of the project task belongs to. | [optional] 
**total_minutes** | **float** | Total minutes which have been logged against the task. Logged by assigning a time entry to a task | [optional] 
**total_amount** | [**Amount**](Amount.md) |  | [optional] 
**minutes_invoiced** | **float** | Minutes on this task which have been invoiced. | [optional] 
**minutes_to_be_invoiced** | **float** | Minutes on this task which have not been invoiced. | [optional] 
**fixed_minutes** | **float** | Minutes logged against this task if its charge type is &#x60;FIXED&#x60;. | [optional] 
**non_chargeable_minutes** | **float** | Minutes logged against this task if its charge type is &#x60;NON_CHARGEABLE&#x60;. | [optional] 
**amount_to_be_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**amount_invoiced** | [**Amount**](Amount.md) |  | [optional] 
**status** | **str** | Status of the task. When a task of ChargeType is &#x60;FIXED&#x60; and the rate amount is invoiced the status will be set to &#x60;INVOICED&#x60; and can&#39;t be modified. A task with ChargeType of &#x60;TIME&#x60; or &#x60;NON_CHARGEABLE&#x60; cannot have a status of &#x60;INVOICED&#x60;. A &#x60;LOCKED&#x60; state indicates that the task is currently changing state (for example being invoiced) and can&#39;t be modified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


