# UpsertBalanceHistoryRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[BalanceHistoryUpdateItemObject]**](BalanceHistoryUpdateItemObject.md) | One or more monthly balance history entries to upsert. Each entry uses &#x60;month&#x60; (YYYY-MM) and &#x60;balance&#x60;. Do not include response-only fields such as &#x60;type&#x60;. PUT responses return only the &#x60;type: historical&#x60; entries modified by the request.  | 

## Example

```python
from lunchmoney.models.upsert_balance_history_request_object import UpsertBalanceHistoryRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBalanceHistoryRequestObject from a JSON string
upsert_balance_history_request_object_instance = UpsertBalanceHistoryRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpsertBalanceHistoryRequestObject.to_json())

# convert the object into a dict
upsert_balance_history_request_object_dict = upsert_balance_history_request_object_instance.to_dict()
# create an instance of UpsertBalanceHistoryRequestObject from a dict
upsert_balance_history_request_object_from_dict = UpsertBalanceHistoryRequestObject.from_dict(upsert_balance_history_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


