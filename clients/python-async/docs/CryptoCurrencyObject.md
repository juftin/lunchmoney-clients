# CryptoCurrencyObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System-defined unique identifier for this cryptocurrency in Lunch Money. | 
**coingecko_id** | **str** | System-defined CoinGecko identifier used to fetch the USD-based prices for this cryptocurrency. | 
**symbol** | **str** | Lowercase currency symbol that must be used as &#x60;symbol&#x60; when creating a manual crypto balance. | 
**full_name** | **str** | Human-readable name of the cryptocurrency. | 

## Example

```python
from lunchmoney.models.crypto_currency_object import CryptoCurrencyObject

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoCurrencyObject from a JSON string
crypto_currency_object_instance = CryptoCurrencyObject.from_json(json)
# print the JSON string representation of the object
print(CryptoCurrencyObject.to_json())

# convert the object into a dict
crypto_currency_object_dict = crypto_currency_object_instance.to_dict()
# create an instance of CryptoCurrencyObject from a dict
crypto_currency_object_from_dict = CryptoCurrencyObject.from_dict(crypto_currency_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


