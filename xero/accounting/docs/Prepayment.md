# Prepayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Prepayment Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**date** | **date** | The date the prepayment is created YYYY-MM-DD | [optional] 
**status** | **str** | See Prepayment Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | See Prepayment Line Items | [optional] 
**sub_total** | **float** | The subtotal of the prepayment excluding taxes | [optional] 
**total_tax** | **float** | The total tax on the prepayment | [optional] 
**total** | **float** | The total of the prepayment(subtotal + total tax) | [optional] 
**reference** | **str** | Returns Invoice number field. Reference field isn&#39;t available. | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the prepayment | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**prepayment_id** | **str** | Xero generated unique identifier | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used | [optional] 
**remaining_credit** | **float** | The remaining credit balance on the prepayment | [optional] 
**allocations** | [**list[Allocation]**](Allocation.md) | See Allocations | [optional] 
**payments** | [**list[Payment]**](Payment.md) | See Payments | [optional] 
**applied_amount** | **float** | The amount of applied to an invoice | [optional] 
**has_attachments** | **bool** | boolean to indicate if a prepayment has an attachment | [optional] [default to False]
**attachments** | [**list[Attachment]**](Attachment.md) | See Attachments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


