# UpdateCategoryRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | If set, updates the category name. Must be between 1 and 100 characters. | [optional] 
**description** | **str** | If set, updates the category description. Must not exceed 200 characters. | [optional] 
**is_income** | **bool** | If set, determines whether transactions in this category are treated as income. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] 
**exclude_from_budget** | **bool** | If set, determines whether transactions in this category are excluded from budgets. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] 
**exclude_from_totals** | **bool** | If set, determines whether transactions in this category are excluded from totals. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] 
**archived** | **bool** | If set, determines whether this category is archived. | [optional] 
**group_id** | **int** | If set to the ID of an existing category group, and this category is not itself a category group, this category will be assigned to that group. | [optional] 
**is_group** | **bool** | This property is tolerated but cannot be changed. This API cannot be used to convert a category into a category group or vice versa. | [optional] [default to False]
**children** | [**List[CreateCategoryRequestObjectChildrenInner]**](CreateCategoryRequestObjectChildrenInner.md) | List of existing category objects, existing category IDs, or names of new categories to add to the category group. This attribute should only be set when modifying an existing category group.&lt;br&gt; Categories or IDs must already exist and must not already belong to a category group. Categories that already belong to another category group will be moved. If strings are specified, they will be used as names for new categories added to the group. The request will fail if any provided name matches an existing category name.&lt;br&gt; You may mix full category objects, IDs, and new category names in the same request. | [optional] 
**order** | **int** | Position of the category on the categories page in the Lunch Money app. For categories within a category group, the order is relative to the other categories in the group.&lt;br&gt;While this property can be set via the API, it is generally managed by the user in the Lunch Money app. | [optional] 
**collapsed** | **bool** | If &#x60;true&#x60;, the category is collapsed in the Lunch Money app.&lt;br&gt;While this property can be set via the API it is generally set by the user in the Lunch Money app. | [optional] 
**id** | **int** | System defined unique identifier for the category. Ignored if set. | [optional] 
**archived_at** | **datetime** | System set date and time of when the category was last archived (in the ISO 8601 extended format). Provide an ISO 8601 extended datetime or &#x60;null&#x60; to clear it. | [optional] 
**updated_at** | **datetime** | System set date and time of when the category was last updated (in the ISO 8601 extended format). Ignored if set. | [optional] 
**created_at** | **datetime** | System set date and time of when the category was created (in the ISO 8601 extended format). Ignored if set. | [optional] 

## Example

```python
from lunchmoney.models.update_category_request_object import UpdateCategoryRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCategoryRequestObject from a JSON string
update_category_request_object_instance = UpdateCategoryRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateCategoryRequestObject.to_json())

# convert the object into a dict
update_category_request_object_dict = update_category_request_object_instance.to_dict()
# create an instance of UpdateCategoryRequestObject from a dict
update_category_request_object_from_dict = UpdateCategoryRequestObject.from_dict(update_category_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


