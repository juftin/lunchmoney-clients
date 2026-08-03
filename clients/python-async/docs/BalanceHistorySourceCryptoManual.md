# BalanceHistorySourceCryptoManual

Source information for a manual cryptocurrency balance history entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies this entry as belonging to a manual crypto account. | 
**crypto_manual_id** | **int** | ID of the manual crypto account associated with this entry. | 
**symbol** | **str** | Crypto symbol associated with the manual crypto account, when available. | [optional] 

## Example

```python
from lunchmoney.models.balance_history_source_crypto_manual import BalanceHistorySourceCryptoManual

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceHistorySourceCryptoManual from a JSON string
balance_history_source_crypto_manual_instance = BalanceHistorySourceCryptoManual.from_json(json)
# print the JSON string representation of the object
print(BalanceHistorySourceCryptoManual.to_json())

# convert the object into a dict
balance_history_source_crypto_manual_dict = balance_history_source_crypto_manual_instance.to_dict()
# create an instance of BalanceHistorySourceCryptoManual from a dict
balance_history_source_crypto_manual_from_dict = BalanceHistorySourceCryptoManual.from_dict(balance_history_source_crypto_manual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


