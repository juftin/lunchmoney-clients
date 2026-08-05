# UpdateCryptoManualRequestObject

Update a manual crypto balance. System-defined properties are accepted when resubmitting a `GET /crypto/manual/{id}` response body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique ID for the manual crypto asset. Ignored if set | [optional] 
**name** | **str** | If set, the new name of the manual crypto asset | [optional] 
**display_name** | **str** | If set, the new display name for the manual crypto asset | [optional] 
**institution_name** | **str** | If set, the new institution or wallet provider display name | [optional] 
**balance** | [**UpdateCryptoManualRequestObjectBalance**](UpdateCryptoManualRequestObjectBalance.md) |  | [optional] 
**symbol** | **str** | Existing cryptocurrency symbol. Ignored if set. | [optional] 
**coingecko_id** | **str** | System-defined CoinGecko identifier for this symbol. Ignored if set. | [optional] 
**to_base** | **float** | System defined balance converted to the user&#39;s primary currency. Ignored if set | [optional] 
**balance_as_of** | **datetime** | System defined date/time the manual balance record was last updated in ISO 8601 extended format. Ignored if set | [optional] 
**exchange_rate_as_of** | **datetime** | System defined date/time the exchange rate used to calculate to_base was observed in ISO 8601 extended format. Ignored if set | [optional] 
**created_by_name** | **str** | System defined name of the user who created the crypto asset. Ignored if set | [optional] 
**created_at** | **datetime** | System defined date/time the crypto asset was created in ISO 8601 extended format. Ignored if set | [optional] 
**updated_at** | **datetime** | System defined date/time the crypto asset was last updated in ISO 8601 extended format. Ignored if set | [optional] 

## Example

```python
from lunchmoney.models.update_crypto_manual_request_object import UpdateCryptoManualRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCryptoManualRequestObject from a JSON string
update_crypto_manual_request_object_instance = UpdateCryptoManualRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateCryptoManualRequestObject.to_json())

# convert the object into a dict
update_crypto_manual_request_object_dict = update_crypto_manual_request_object_instance.to_dict()
# create an instance of UpdateCryptoManualRequestObject from a dict
update_crypto_manual_request_object_from_dict = UpdateCryptoManualRequestObject.from_dict(update_crypto_manual_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


