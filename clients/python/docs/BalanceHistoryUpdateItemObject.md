# BalanceHistoryUpdateItemObject

A single monthly balance entry to upsert. Request bodies use this shape. Responses return `type: historical` entries instead. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System-defined balance history entry id. Ignored if set. | [optional] 
**month** | **str** | Calendar month to upsert, in YYYY-MM format. Must be a past month. The current month cannot be written through PUT endpoints.  | 
**balance** | [**BalanceHistoryUpdateItemObjectBalance**](BalanceHistoryUpdateItemObjectBalance.md) |  | 
**symbol** | **str** | Optional for crypto balances. If set, it must match the account&#39;s symbol. Tolerated for deleted-account balances. Do not provide this for manual or Plaid balances. On the synced crypto path endpoint, if provided it must match the &#x60;symbol&#x60; path parameter.  | [optional] 
**crypto_balance** | **str** | Optional crypto quantity for crypto_manual, crypto_synced, and deleted balances. Do not provide this for manual or Plaid balances. | [optional] 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Optional currency for this balance entry. If omitted, it defaults to the account currency for manual/Plaid accounts, or the user&#39;s primary currency for crypto/deleted accounts. | [optional] 
**to_base** | **float** | System-defined historical balance converted to the user&#39;s primary currency. Ignored if set. Use &#x60;balance&#x60; to update the historical balance. | [optional] 

## Example

```python
from lunchmoney.models.balance_history_update_item_object import BalanceHistoryUpdateItemObject

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryUpdateItemObject from a JSON string
balance_history_update_item_object_instance = BalanceHistoryUpdateItemObject.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryUpdateItemObject.to_json())

# convert the object into a dict
balance_history_update_item_object_dict = balance_history_update_item_object_instance.to_dict()
# create an instance of BalanceHistoryUpdateItemObject from a dict
balance_history_update_item_object_from_dict = BalanceHistoryUpdateItemObject.from_dict(balance_history_update_item_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


