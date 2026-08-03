# BalanceHistorySourcePlaid

Source information for a Plaid-synced account balance history entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to a Plaid-synced account. | 
**plaid_account_id** | **int** | ID of the Plaid account associated with this entry. | 

## Example

```python
from lunchmoney.models.balance_history_source_plaid import BalanceHistorySourcePlaid

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistorySourcePlaid from a JSON string
balance_history_source_plaid_instance = BalanceHistorySourcePlaid.from_json(json)
# print the JSON string representation of the object
print(BalanceHistorySourcePlaid.to_json())

# convert the object into a dict
balance_history_source_plaid_dict = balance_history_source_plaid_instance.to_dict()
# create an instance of BalanceHistorySourcePlaid from a dict
balance_history_source_plaid_from_dict = BalanceHistorySourcePlaid.from_dict(balance_history_source_plaid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


