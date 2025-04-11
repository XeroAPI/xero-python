# CashAccountResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreconciled_amount_pos** | **float** | Total value of transactions in the journals which are not reconciled to bank statement lines, and have a positive (debit) value. | [optional] 
**unreconciled_amount_neg** | **float** | Total value of transactions in the journals which are not reconciled to bank statement lines, and have a negative (credit) value. | [optional] 
**starting_balance** | **float** | Starting (or historic) balance from the journals (manually keyed in by users on account creation - unverified). | [optional] 
**account_balance** | **float** | Current cash at bank accounting value from the journals. | [optional] 
**balance_currency** | **str** | Currency which the cashAccount transactions relate to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


