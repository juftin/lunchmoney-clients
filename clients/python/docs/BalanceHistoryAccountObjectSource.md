# BalanceHistoryAccountObjectSource

Identifies the account these balance entries belong to. The shape varies by `source.type`. Each source type exposes a type-specific account id field (`manual_account_id`, `plaid_account_id`, `crypto_manual_id`, `crypto_synced_id`, or `deleted_account_id`). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to a manual account. | 
**manual_account_id** | **int** | ID of the manual account associated with this entry. | 
**plaid_account_id** | **int** | ID of the Plaid account associated with this entry. | 
**crypto_manual_id** | **int** | ID of the manual crypto account associated with this entry. | 
**symbol** | **str** | Archived &#x60;symbol&#x60; for a deleted crypto account source | 
**crypto_synced_id** | **int** | ID of the synced crypto connection associated with this entry. | 
**deleted_account_id** | **int** | Identifier for the deleted account history source | 
**name** | **str** | Archived account &#x60;name&#x60; for the deleted account source | 
**institution_name** | **str** | Archived &#x60;institution_name&#x60; for the deleted account source | 
**display_name** | **str** | Archived &#x60;display_name&#x60; of the deleted account | 
**account_type** | **str** | Archived &#x60;type&#x60; of the deleted account source | 
**subtype** | **str** | Archived &#x60;subtype&#x60; of the deleted account source | 
**mask** | **str** | Archived account &#x60;mask&#x60; for a deleted Plaid account source | 

## Example

```python
from lunchmoney.models.balance_history_account_object_source import BalanceHistoryAccountObjectSource

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryAccountObjectSource from a JSON string
balance_history_account_object_source_instance = BalanceHistoryAccountObjectSource.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryAccountObjectSource.to_json())

# convert the object into a dict
balance_history_account_object_source_dict = balance_history_account_object_source_instance.to_dict()
# create an instance of BalanceHistoryAccountObjectSource from a dict
balance_history_account_object_source_from_dict = BalanceHistoryAccountObjectSource.from_dict(balance_history_account_object_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


