# CreateCategoryRequestObjectChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique ID for the category | 
**name** | **str** | Name of the category | 
**description** | **str** | Category description, or &#x60;null&#x60; if none is set | 
**is_income** | **bool** | If &#x60;true&#x60;, transactions in this category are treated as income. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**exclude_from_budget** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from the budget. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**exclude_from_totals** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from totals. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**updated_at** | **datetime** | Date and time the category was last updated (in the ISO 8601 extended format). | 
**created_at** | **datetime** | Date and time of when the category was created (ISO 8601 extended format). | 
**group_id** | **int** | ID of the category group this category belongs to, or &#x60;null&#x60; if it does not belong to a group, or is itself a group. | 
**is_group** | **bool** | If &#x60;true&#x60;, this category is created as a category group | 
**children** | [**List[ChildCategoryObject]**](ChildCategoryObject.md) | For category groups, contains details about the categories in the group. These objects are similar to Category Objects but the &#x60;is_group&#x60; property will always be &#x60;false&#x60;, and there will be no &#x60;children&#x60; attribute. | [optional] 
**archived** | **bool** | If true, the category is archived and hidden in relevant areas of the Lunch Money app. | 
**archived_at** | **datetime** | Date and time the category was last archived ( ISO 8601 extended format). | 
**order** | **int** | Position of the category on the categories page in the Lunch Money app. For grouped categories, the order is relative to others in the same group.&lt;br&gt; Categories with &#x60;order: null&#x60; are shown alphabetically before ordered categories | 
**collapsed** | **bool** | If &#x60;true&#x60;, the category appears collapsed in the Lunch Money app | [default to False]

## Example

```python
from lunchmoney.models.create_category_request_object_children_inner import CreateCategoryRequestObjectChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCategoryRequestObjectChildrenInner from a JSON string
create_category_request_object_children_inner_instance = CreateCategoryRequestObjectChildrenInner.from_json(json)
# print the JSON string representation of the object
print(CreateCategoryRequestObjectChildrenInner.to_json())

# convert the object into a dict
create_category_request_object_children_inner_dict = create_category_request_object_children_inner_instance.to_dict()
# create an instance of CreateCategoryRequestObjectChildrenInner from a dict
create_category_request_object_children_inner_from_dict = CreateCategoryRequestObjectChildrenInner.from_dict(create_category_request_object_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


