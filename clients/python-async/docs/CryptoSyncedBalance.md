# CryptoSyncedBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The asset name for this balance, typically the uppercased currency symbol (e.g. ETH). | 
**display_name** | **str** | Optional display name for the synced crypto asset as set by the user. If &#x60;null&#x60;, clients may derive a display name from syncedCryptoAccount&#39;s &#x60;provider&#x60; + &#x60;name&#x60;. | 
**balance** | **str** | Current balance in numeric format to 18 decimal places | 
**symbol** | **str** | Symbol of the currency held in the synced account | 
**coingecko_id** | **str** | CoinGecko identifier associated with this balance | 
**to_base** | **float** | Balance converted to the user&#39;s primary currency. May be null if no conversion was available. | 
**balance_as_of** | **datetime** | Date/time the balance was last updated in ISO 8601 extended format. | 
**exchange_rate_as_of** | **datetime** | Date/time the exchange rate used to calculate to_base was last updated in ISO 8601 extended format. Null when no exchange rate was used or no conversion was available. | 
**updated_at** | **datetime** | Date/time the crypto asset was last updated in ISO 8601 extended format | 

## Example

```python
from lunchmoney.models.crypto_synced_balance import CryptoSyncedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSyncedBalance from a JSON string
crypto_synced_balance_instance = CryptoSyncedBalance.from_json(json)
# print the JSON string representation of the object
print(CryptoSyncedBalance.to_json())

# convert the object into a dict
crypto_synced_balance_dict = crypto_synced_balance_instance.to_dict()
# create an instance of CryptoSyncedBalance from a dict
crypto_synced_balance_from_dict = CryptoSyncedBalance.from_dict(crypto_synced_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


