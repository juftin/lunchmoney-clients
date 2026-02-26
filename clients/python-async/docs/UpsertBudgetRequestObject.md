# UpsertBudgetRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the budget period in ISO 8601 date format (YYYY-MM-DD). Must be a valid budget period start for the account. | 
**category_id** | **int** | Category ID for the budget | 
**amount** | [**UpsertBudgetRequestObjectAmount**](UpsertBudgetRequestObjectAmount.md) |  | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter currency code. If omitted, the primary currency for the user&#39;s account is used. | [optional] 
**notes** | **str** | Optional notes for the budget period | [optional] 

## Example

```python
from lunchmoney.models.upsert_budget_request_object import UpsertBudgetRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBudgetRequestObject from a JSON string
upsert_budget_request_object_instance = UpsertBudgetRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpsertBudgetRequestObject.to_json())

# convert the object into a dict
upsert_budget_request_object_dict = upsert_budget_request_object_instance.to_dict()
# create an instance of UpsertBudgetRequestObject from a dict
upsert_budget_request_object_from_dict = UpsertBudgetRequestObject.from_dict(upsert_budget_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


