# CreateCryptocurrencyRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coingecko_url** | **str** | CoinGecko coin-page URL in the form &#x60;https://www.coingecko.com/{locale}/coins/{id}&#x60; | 

## Example

```python
from lunchmoney.models.create_cryptocurrency_request_object import CreateCryptocurrencyRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCryptocurrencyRequestObject from a JSON string
create_cryptocurrency_request_object_instance = CreateCryptocurrencyRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateCryptocurrencyRequestObject.to_json())

# convert the object into a dict
create_cryptocurrency_request_object_dict = create_cryptocurrency_request_object_instance.to_dict()
# create an instance of CreateCryptocurrencyRequestObject from a dict
create_cryptocurrency_request_object_from_dict = CreateCryptocurrencyRequestObject.from_dict(create_cryptocurrency_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


