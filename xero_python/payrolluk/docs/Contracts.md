# Contracts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The contract start date of the employee. This will be locked once an employee has been paid and cannot be changed (YYYY-MM-DD) | 
**employment_status** | [**EmploymentStatus**](EmploymentStatus.md) |  | 
**contract_type** | [**ContractType**](ContractType.md) |  | 
**public_key** | **str** | The public key of the contract. Public key is required if the intention is to edit an existing contract. If no key is supplied a new contract will be created | [optional] 
**is_fixed_term** | **bool** | describes whether the contract is fixed term (required if trying to create Fixed term contract) | [optional] 
**fixed_term_end_date** | **date** | The fixed term end date of the employee. Not required if isFixedTerm is false or not provided (required if trying to create Fixed term contract) | [optional] 
**developmental_role_details** | [**DevelopmentalRoleDetails**](DevelopmentalRoleDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


