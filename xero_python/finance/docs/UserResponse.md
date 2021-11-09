# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The Xero identifier for the user | [optional] 
**user_created_date_utc** | **datetime** | Timestamp of user creation. | [optional] 
**last_login_date_utc** | **datetime** | Timestamp of user last login | [optional] 
**is_external_partner** | **bool** | User is external partner. | [optional] 
**has_accountant_role** | **bool** | User has Accountant role. | [optional] 
**month_period** | **str** | Month period in format  yyyy-MM. | [optional] 
**number_of_logins** | **int** | Number of times the user has logged in. | [optional] 
**number_of_documents_created** | **int** | Number of documents created. | [optional] 
**net_value_documents_created** | **float** | Net value of documents created. | [optional] 
**absolute_value_documents_created** | **float** | Absolute value of documents created. | [optional] 
**attached_practices** | [**list[PracticeResponse]**](PracticeResponse.md) |  | [optional] 
**history_records** | [**list[HistoryRecordResponse]**](HistoryRecordResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


