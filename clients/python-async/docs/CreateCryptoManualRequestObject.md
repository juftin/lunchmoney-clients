# CreateCryptoManualRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-defined name for the manual crypto asset | 
**display_name** | **str** | Display name for the manual crypto asset. If omitted or &#x60;null&#x60;, clients may derive one from &#x60;institution_name&#x60; + &#x60;name&#x60;. | [optional] 
**institution_name** | **str** | Institution or wallet provider display name. If omitted or &#x60;null&#x60;, no institution name is set. | [optional] 
**balance** | [**CreateCryptoManualRequestObjectBalance**](CreateCryptoManualRequestObjectBalance.md) |  | 
**symbol** | **str** | Cryptocurrency symbol to track. Must match the &#x60;symbol&#x60; of one of the supported cryptocurrencies returned by &#x60;GET /cryptocurrencies&#x60;. | 

## Example

```python
from lunchmoney.models.create_crypto_manual_request_object import CreateCryptoManualRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCryptoManualRequestObject from a JSON string
create_crypto_manual_request_object_instance = CreateCryptoManualRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateCryptoManualRequestObject.to_json())

# convert the object into a dict
create_crypto_manual_request_object_dict = create_crypto_manual_request_object_instance.to_dict()
# create an instance of CreateCryptoManualRequestObject from a dict
create_crypto_manual_request_object_from_dict = CreateCryptoManualRequestObject.from_dict(create_crypto_manual_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


