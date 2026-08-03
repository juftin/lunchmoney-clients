# HistoricalBalanceHistoryEntry

A stored monthly balance for a past month. The `id` may be used with balance history entry endpoints. The balance represents the account balance at or around the end of `month`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as a stored snapshot of a past month. | 
**id** | **int** | Unique identifier for this historical balance entry. | 
**month** | **str** | Calendar month for this entry in YYYY-MM format. | 
**balance** | **str** | Historical balance for this entry, as a numeric string with up to four decimal places. Trailing zeros and decimal places are not guaranteed in responses. For manual and Plaid accounts this is in the account currency. For crypto accounts this is in the user&#39;s primary currency. | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of &#x60;balance&#x60;. For crypto entries this is the user&#39;s primary currency. | 
**to_base** | **float** | Historical balance converted to the user&#39;s primary currency. When the entry currency is the user&#39;s primary currency, this is the numeric value of &#x60;balance&#x60;. | 
**crypto_balance** | **str** | Crypto quantity for this balance entry, when available. This may be present for crypto or deleted-account entries and is &#x60;null&#x60; otherwise. | 

## Example

```python
from lunchmoney.models.historical_balance_history_entry import HistoricalBalanceHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalBalanceHistoryEntry from a JSON string
historical_balance_history_entry_instance = HistoricalBalanceHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(HistoricalBalanceHistoryEntry.to_json())

# convert the object into a dict
historical_balance_history_entry_dict = historical_balance_history_entry_instance.to_dict()
# create an instance of HistoricalBalanceHistoryEntry from a dict
historical_balance_history_entry_from_dict = HistoricalBalanceHistoryEntry.from_dict(historical_balance_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


