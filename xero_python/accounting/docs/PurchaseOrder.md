# PurchaseOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | See LineItems | [optional] 
**date** | **date** | Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**delivery_date** | **date** | Date the goods are to be delivered – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**purchase_order_number** | **str** | Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**status** | **str** | See Purchase Order Status Codes | [optional] 
**sent_to_contact** | **bool** | Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed | [optional] 
**delivery_address** | **str** | The address the goods are to be delivered to | [optional] 
**attention_to** | **str** | The person that the delivery is going to | [optional] 
**telephone** | **str** | The phone number for the person accepting the delivery | [optional] 
**delivery_instructions** | **str** | A free text feild for instructions (500 characters max) | [optional] 
**expected_arrival_date** | **date** | The date the goods are expected to arrive. | [optional] 
**purchase_order_id** | **str** | Xero generated unique identifier for purchase order | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used. | [optional] 
**sub_total** | **float** | Total of purchase order excluding taxes | [optional] 
**total_tax** | **float** | Total tax on purchase order | [optional] 
**total** | **float** | Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**total_discount** | **float** | Total of discounts applied on the purchase order line items | [optional] 
**has_attachments** | **bool** | boolean to indicate if a purchase order has an attachment | [optional] [default to False]
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**list[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


