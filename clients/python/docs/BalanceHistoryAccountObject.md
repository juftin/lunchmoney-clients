# BalanceHistoryAccountObject

Monthly balance entries grouped under a single account source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**BalanceHistoryAccountObjectSource**](BalanceHistoryAccountObjectSource.md) |  | 
**balances** | [**List[BalanceHistoryEntry]**](BalanceHistoryEntry.md) | Monthly balance entries for this account source. A &#x60;historical&#x60; entry is a stored snapshot of a past month and includes an &#x60;id&#x60;. A &#x60;current&#x60; entry is an ephemeral snapshot based on the account&#39;s current balances and has no balance-entry &#x60;id&#x60;. On PUT upsert responses, this array includes only the &#x60;type: historical&#x60; entries modified by that request.  | 

## Example

```python
from lunchmoney.models.balance_history_account_object import BalanceHistoryAccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryAccountObject from a JSON string
balance_history_account_object_instance = BalanceHistoryAccountObject.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryAccountObject.to_json())

# convert the object into a dict
balance_history_account_object_dict = balance_history_account_object_instance.to_dict()
# create an instance of BalanceHistoryAccountObject from a dict
balance_history_account_object_from_dict = BalanceHistoryAccountObject.from_dict(balance_history_account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


