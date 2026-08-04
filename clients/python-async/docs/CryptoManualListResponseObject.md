# CryptoManualListResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_manual** | [**List[CryptoManualObject]**](CryptoManualObject.md) |  | 

## Example

```python
from lunchmoney.models.crypto_manual_list_response_object import CryptoManualListResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManualListResponseObject from a JSON string
crypto_manual_list_response_object_instance = CryptoManualListResponseObject.from_json(json)
# print the JSON string representation of the object
print(CryptoManualListResponseObject.to_json())

# convert the object into a dict
crypto_manual_list_response_object_dict = crypto_manual_list_response_object_instance.to_dict()
# create an instance of CryptoManualListResponseObject from a dict
crypto_manual_list_response_object_from_dict = CryptoManualListResponseObject.from_dict(crypto_manual_list_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


