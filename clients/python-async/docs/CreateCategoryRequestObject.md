# CreateCategoryRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new category. Must be between 1 and 100 characters. The name must not match the name of any existing categories or category groups. | 
**description** | **str** | Description of the category. Maximum length is 200 characters. | [optional] 
**is_income** | **bool** | If &#x60;true&#x60;, transactions in this category are treated as income. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to False]
**exclude_from_budget** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from the budget. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to False]
**exclude_from_totals** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from totals. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to False]
**is_group** | **bool** | If &#x60;true&#x60;, this category will be created as a category group. | [optional] [default to False]
**group_id** | **int** | If set to the ID of an existing category group, the new category will be added to that group. Cannot be used if &#x60;is_group&#x60; is true. | [optional] 
**archived** | **bool** | If &#x60;true&#x60;, the category is archived and in relevant areas of the Lunch Money app. | [optional] [default to False]
**children** | [**List[CreateCategoryRequestObjectChildrenInner]**](CreateCategoryRequestObjectChildrenInner.md) | List of categories to include in the new category group. This field should only be set if &#x60;is_group&#x60; is also set to true.&lt;br&gt; You may provide existing category objects, existing category IDs, or names for new categories to add to the group. Categories or IDs must already exist and cannot be category groups. Categories that already belong to another group will be moved. If strings are provided, they will be used as names for new categories added to the group. The request will fail if any provided name already exists.&lt;br&gt; You may mix category objects, IDs, and new category names in the same request. | [optional] 
**order** | **int** | Position of the category on the categories page in the Lunch Money app. For grouped categories, the order is relative to other categories in the same group.&lt;br&gt;While this property can be set via the API, it is usually managed by the user in the Lunch Money app. | [optional] 
**collapsed** | **bool** | If &#x60;true&#x60;, the category group appears collapsed in the Lunch Money app. Can only be set to &#x60;true&#x60; for category groups.&lt;br&gt;While this property can be set via the API, it is usually managed by the user in the Lunch Money app. | [optional] 

## Example

```python
from lunchmoney.models.create_category_request_object import CreateCategoryRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCategoryRequestObject from a JSON string
create_category_request_object_instance = CreateCategoryRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateCategoryRequestObject.to_json())

# convert the object into a dict
create_category_request_object_dict = create_category_request_object_instance.to_dict()
# create an instance of CreateCategoryRequestObject from a dict
create_category_request_object_from_dict = CreateCategoryRequestObject.from_dict(create_category_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


