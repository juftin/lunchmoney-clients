# CryptoManualObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique ID for the manual crypto balance | 
**name** | **str** | User-defined name for the crypto asset | 
**display_name** | **str** | Optional display name for the crypto asset. If &#x60;null&#x60;, clients may derive a display name from &#x60;institution_name&#x60; + &#x60;name&#x60;. | 
**institution_name** | **str** | Institution or wallet provider display name | 
**balance** | **str** | Current balance in numeric format to 18 decimal places | 
**symbol** | **str** | Cryptocurrency symbol | 
**coingecko_id** | **str** | CoinGecko identifier associated with this balance | 
**to_base** | **float** | Balance converted to the user&#39;s primary currency. May be null if no conversion was available. | 
**balance_as_of** | **datetime** | Date/time the manual balance record was last updated in ISO 8601 extended format. This is currently based on the manual crypto record&#39;s updated_at timestamp. | 
**exchange_rate_as_of** | **datetime** | Date/time the exchange rate used to calculate to_base was last updated in ISO 8601 extended format. Null when no exchange rate was used or no conversion was available. | 
**created_by_name** | **str** | Name of the user who created the crypto asset | 
**created_at** | **datetime** | Date/time the crypto asset was created in ISO 8601 extended format | 
**updated_at** | **datetime** | Date/time the crypto asset was last updated in ISO 8601 extended format | 

## Example

```python
from lunchmoney.models.crypto_manual_object import CryptoManualObject

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManualObject from a JSON string
crypto_manual_object_instance = CryptoManualObject.from_json(json)
# print the JSON string representation of the object
print(CryptoManualObject.to_json())

# convert the object into a dict
crypto_manual_object_dict = crypto_manual_object_instance.to_dict()
# create an instance of CryptoManualObject from a dict
crypto_manual_object_from_dict = CryptoManualObject.from_dict(crypto_manual_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


