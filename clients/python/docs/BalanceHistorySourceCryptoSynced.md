# BalanceHistorySourceCryptoSynced

Source information for a synced cryptocurrency balance history entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to a synced crypto connection. | 
**crypto_synced_id** | **int** | ID of the synced crypto connection associated with this entry. | 
**symbol** | **str** | Crypto symbol (e.g. &#x60;eth&#x60;, &#x60;btc&#x60;) identifying the specific currency within the synced account. | 

## Example

```python
from lunchmoney.models.balance_history_source_crypto_synced import BalanceHistorySourceCryptoSynced

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistorySourceCryptoSynced from a JSON string
balance_history_source_crypto_synced_instance = BalanceHistorySourceCryptoSynced.from_json(json)
# print the JSON string representation of the object
print(BalanceHistorySourceCryptoSynced.to_json())

# convert the object into a dict
balance_history_source_crypto_synced_dict = balance_history_source_crypto_synced_instance.to_dict()
# create an instance of BalanceHistorySourceCryptoSynced from a dict
balance_history_source_crypto_synced_from_dict = BalanceHistorySourceCryptoSynced.from_dict(balance_history_source_crypto_synced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


