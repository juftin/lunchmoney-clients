# CryptoSyncedListResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_synced** | [**List[SyncedCryptoAccount]**](SyncedCryptoAccount.md) |  | 

## Example

```python
from lunchmoney.models.crypto_synced_list_response_object import CryptoSyncedListResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSyncedListResponseObject from a JSON string
crypto_synced_list_response_object_instance = CryptoSyncedListResponseObject.from_json(json)
# print the JSON string representation of the object
print(CryptoSyncedListResponseObject.to_json())

# convert the object into a dict
crypto_synced_list_response_object_dict = crypto_synced_list_response_object_instance.to_dict()
# create an instance of CryptoSyncedListResponseObject from a dict
crypto_synced_list_response_object_from_dict = CryptoSyncedListResponseObject.from_dict(crypto_synced_list_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


