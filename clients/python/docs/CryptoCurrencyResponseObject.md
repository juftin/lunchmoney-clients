# CryptoCurrencyResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptocurrencies** | [**List[CryptoCurrencyObject]**](CryptoCurrencyObject.md) | List of cryptocurrencies currently supported for manual tracking. | 

## Example

```python
from lunchmoney.models.crypto_currency_response_object import CryptoCurrencyResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoCurrencyResponseObject from a JSON string
crypto_currency_response_object_instance = CryptoCurrencyResponseObject.from_json(json)
# print the JSON string representation of the object
print(CryptoCurrencyResponseObject.to_json())

# convert the object into a dict
crypto_currency_response_object_dict = crypto_currency_response_object_instance.to_dict()
# create an instance of CryptoCurrencyResponseObject from a dict
crypto_currency_response_object_from_dict = CryptoCurrencyResponseObject.from_dict(crypto_currency_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


