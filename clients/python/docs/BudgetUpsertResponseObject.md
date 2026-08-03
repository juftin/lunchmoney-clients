# BudgetUpsertResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | Category ID | [optional] 
**start_date** | **date** | Start date of the budget period | [optional] 
**amount** | **str** | Budget amount in the stored currency (string for consistency with other amount fields in the API). | [optional] 
**currency** | **str** | Currency code for the budget | [optional] 
**to_base** | **float** | Amount converted to the user&#39;s primary currency | [optional] 
**notes** | **str** | Notes for the budget period | [optional] 

## Example

```python
from lunchmoney.models.budget_upsert_response_object import BudgetUpsertResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpsertResponseObject from a JSON string
budget_upsert_response_object_instance = BudgetUpsertResponseObject.from_json(json)
# print the JSON string representation of the object
print(BudgetUpsertResponseObject.to_json())

# convert the object into a dict
budget_upsert_response_object_dict = budget_upsert_response_object_instance.to_dict()
# create an instance of BudgetUpsertResponseObject from a dict
budget_upsert_response_object_from_dict = BudgetUpsertResponseObject.from_dict(budget_upsert_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


