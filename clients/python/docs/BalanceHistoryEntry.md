# BalanceHistoryEntry

A monthly balance history entry. Discriminated by `type`. `historical` entries are stored snapshots of past months with an `id`. `current` entries are ephemeral snapshots with no balance-entry `id`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as a stored snapshot of a past month. | 
**id** | **int** | Unique identifier for this historical balance entry. | 
**month** | **str** | Calendar month for this entry in YYYY-MM format. For current entries this is the current month. | 
**balance** | **str** | Calculated balance for the current month, as a numeric string with up to four decimal places. Trailing zeros and decimal places are not guaranteed in responses. For manual and Plaid accounts this is in the account currency. For crypto accounts this is in the user&#39;s primary currency. | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the calculated &#x60;balance&#x60;. For crypto entries this is the user&#39;s primary currency. | 
**to_base** | **float** | Calculated balance converted to the user&#39;s primary currency. When the entry currency is the user&#39;s primary currency, this is the numeric value of &#x60;balance&#x60;. | 
**crypto_balance** | **str** | Crypto quantity for this calculated entry, when available. This may be present for crypto entries and is &#x60;null&#x60; otherwise. | 

## Example

```python
from lunchmoney.models.balance_history_entry import BalanceHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistoryEntry from a JSON string
balance_history_entry_instance = BalanceHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(BalanceHistoryEntry.to_json())

# convert the object into a dict
balance_history_entry_dict = balance_history_entry_instance.to_dict()
# create an instance of BalanceHistoryEntry from a dict
balance_history_entry_from_dict = BalanceHistoryEntry.from_dict(balance_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


