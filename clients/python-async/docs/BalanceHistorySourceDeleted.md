# BalanceHistorySourceDeleted

Source information for balance history whose account has since been deleted. Historical balances are preserved when a user chooses to keep history on account deletion. This object contains details that can be used to display the deleted account in the UI. The `deleted_account_id` can be passed to [PUT /balance_history/deleted/{account_id}/details](#tag/balance-history/PUT/balance_history/deleted/{account_id}/details) to update the archived source metadata. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to an account that has since been deleted. | 
**deleted_account_id** | **int** | Identifier for the deleted account history source | 
**name** | **str** | Archived account &#x60;name&#x60; for the deleted account source | 
**institution_name** | **str** | Archived &#x60;institution_name&#x60; for the deleted account source | 
**display_name** | **str** | Archived &#x60;display_name&#x60; of the deleted account | 
**account_type** | **str** | Archived &#x60;type&#x60; of the deleted account source | 
**subtype** | **str** | Archived &#x60;subtype&#x60; of the deleted account source | 
**mask** | **str** | Archived account &#x60;mask&#x60; for a deleted Plaid account source | 
**symbol** | **str** | Archived &#x60;symbol&#x60; for a deleted crypto account source | 

## Example

```python
from lunchmoney.models.balance_history_source_deleted import BalanceHistorySourceDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistorySourceDeleted from a JSON string
balance_history_source_deleted_instance = BalanceHistorySourceDeleted.from_json(json)
# print the JSON string representation of the object
print(BalanceHistorySourceDeleted.to_json())

# convert the object into a dict
balance_history_source_deleted_dict = balance_history_source_deleted_instance.to_dict()
# create an instance of BalanceHistorySourceDeleted from a dict
balance_history_source_deleted_from_dict = BalanceHistorySourceDeleted.from_dict(balance_history_source_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


