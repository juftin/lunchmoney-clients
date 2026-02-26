# UpsertBudgetRequestObjectAmount

Budget amount. May be a string or a number in double format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.upsert_budget_request_object_amount import UpsertBudgetRequestObjectAmount

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBudgetRequestObjectAmount from a JSON string
upsert_budget_request_object_amount_instance = UpsertBudgetRequestObjectAmount.from_json(json)
# print the JSON string representation of the object
print(UpsertBudgetRequestObjectAmount.to_json())

# convert the object into a dict
upsert_budget_request_object_amount_dict = upsert_budget_request_object_amount_instance.to_dict()
# create an instance of UpsertBudgetRequestObjectAmount from a dict
upsert_budget_request_object_amount_from_dict = UpsertBudgetRequestObjectAmount.from_dict(upsert_budget_request_object_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


