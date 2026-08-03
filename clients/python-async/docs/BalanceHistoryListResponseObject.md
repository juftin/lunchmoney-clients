# BalanceHistoryListResponseObject

List response for balance history GET endpoints. Entries are grouped by account source under `balance_history`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_history** | [**List[BalanceHistoryAccountObject]**](BalanceHistoryAccountObject.md) |  | 

## Example

```python
from lunchmoney.models.balance_history_list_response_object import BalanceHistoryListResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryListResponseObject from a JSON string
balance_history_list_response_object_instance = BalanceHistoryListResponseObject.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryListResponseObject.to_json())

# convert the object into a dict
balance_history_list_response_object_dict = balance_history_list_response_object_instance.to_dict()
# create an instance of BalanceHistoryListResponseObject from a dict
balance_history_list_response_object_from_dict = BalanceHistoryListResponseObject.from_dict(balance_history_list_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


