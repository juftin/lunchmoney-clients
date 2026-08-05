# BalanceHistoryUpdateItemObjectBalance

Numeric value of the historical balance, up to four decimal places, as a number or string. For manual and Plaid accounts this is in the account currency. For crypto and deleted accounts this is in the user's primary currency. Do not include any special characters aside from a decimal point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.balance_history_update_item_object_balance import BalanceHistoryUpdateItemObjectBalance

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryUpdateItemObjectBalance from a JSON string
balance_history_update_item_object_balance_instance = BalanceHistoryUpdateItemObjectBalance.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryUpdateItemObjectBalance.to_json())

# convert the object into a dict
balance_history_update_item_object_balance_dict = balance_history_update_item_object_balance_instance.to_dict()
# create an instance of BalanceHistoryUpdateItemObjectBalance from a dict
balance_history_update_item_object_balance_from_dict = BalanceHistoryUpdateItemObjectBalance.from_dict(balance_history_update_item_object_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


