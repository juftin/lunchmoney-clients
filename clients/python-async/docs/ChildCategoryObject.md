# ChildCategoryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique ID for the category | 
**name** | **str** | The name of the category | 
**description** | **str** | Category description, or &#x60;null&#x60; if none is set | 
**is_income** | **bool** | If true, transactions in this category are treated as income. (Inherited from the Category Group). | 
**exclude_from_budget** | **bool** | If true, transactions in this category are excluded from the budget. (Inherited from Category Group). | 
**exclude_from_totals** | **bool** | If true, transactions in this category are excluded from totals. (Inherited from Category Group). | 
**updated_at** | **datetime** | Date and time the category was last updated (ISO 8601 extended format). | 
**created_at** | **datetime** | Date and time the category was created (ISO 8601 extended format). | 
**group_id** | **int** | ID of the category group this category belongs to, or &#x60;null&#x60; if it does not belong to a group, or is itself a group. | 
**is_group** | **bool** | Always false for categories that belong to a category group | 
**archived** | **bool** | If true, the category is archived and hidden in relevant areas of the Lunch Money app. | 
**archived_at** | **datetime** | Date and time the category was last archived ( ISO 8601 extended format). | 
**order** | **int** | Position of the category on the categories page in the Lunch Money app. For grouped categories, the order is relative to the others in the same group. | 
**collapsed** | **bool** | Always &#x60;false&#x60; for a child category. Child categories cannot be collapsed. | 

## Example

```python
from lunchmoney.models.child_category_object import ChildCategoryObject

# TODO update the JSON string below
json = "{}"
# create an instance of ChildCategoryObject from a JSON string
child_category_object_instance = ChildCategoryObject.from_json(json)
# print the JSON string representation of the object
print(ChildCategoryObject.to_json())

# convert the object into a dict
child_category_object_dict = child_category_object_instance.to_dict()
# create an instance of ChildCategoryObject from a dict
child_category_object_from_dict = ChildCategoryObject.from_dict(child_category_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


