# BalanceHistorySourceManual

Source information for a manual account balance history entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to a manual account. | 
**manual_account_id** | **int** | ID of the manual account associated with this entry. | 

## Example

```python
from lunchmoney.models.balance_history_source_manual import BalanceHistorySourceManual

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistorySourceManual from a JSON string
balance_history_source_manual_instance = BalanceHistorySourceManual.from_json(json)
# print the JSON string representation of the object
print(BalanceHistorySourceManual.to_json())

# convert the object into a dict
balance_history_source_manual_dict = balance_history_source_manual_instance.to_dict()
# create an instance of BalanceHistorySourceManual from a dict
balance_history_source_manual_from_dict = BalanceHistorySourceManual.from_dict(balance_history_source_manual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


