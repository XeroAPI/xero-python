# Quote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | QuoteID GUID is automatically generated and is returned after create or GET. | [optional] 
**quote_number** | **str** | Unique alpha numeric code identifying a quote (Max Length &#x3D; 255) | [optional] 
**reference** | **str** | Additional reference number | [optional] 
**terms** | **str** | Terms of the quote | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | See LineItems | [optional] 
**date** | **date** | Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation | [optional] 
**date_string** | **str** | Date the quote was issued (YYYY-MM-DD) | [optional] 
**expiry_date** | **date** | Date the quote expires – YYYY-MM-DD. | [optional] 
**expiry_date_string** | **str** | Date the quote expires – YYYY-MM-DD. | [optional] 
**status** | [**QuoteStatusCodes**](QuoteStatusCodes.md) |  | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency quote | [optional] 
**sub_total** | **float** | Total of quote excluding taxes. | [optional] 
**total_tax** | **float** | Total tax on quote | [optional] 
**total** | **float** | Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts | [optional] 
**total_discount** | **float** | Total of discounts applied on the quote line items | [optional] 
**title** | **str** | Title text for the quote | [optional] 
**summary** | **str** | Summary text for the quote | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 
**line_amount_types** | [**QuoteLineAmountTypes**](QuoteLineAmountTypes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


