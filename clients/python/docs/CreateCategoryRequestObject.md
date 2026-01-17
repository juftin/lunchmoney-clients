# CreateCategoryRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new category. Must be between 1 and 100 characters. Must not match the name of any existing categories or category groups. | 
**description** | **str** | The description of the category. Must not exceed 200 characters. | [optional] 
**is_income** | **bool** | If &#x60;true&#x60;, the transactions in this category will be treated as income. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] [default to False]
**exclude_from_budget** | **bool** | If &#x60;true&#x60;, the transactions in this category will be excluded from the budget. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] [default to False]
**exclude_from_totals** | **bool** | If &#x60;true&#x60;, the transactions in this category will be excluded from totals. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] [default to False]
**is_group** | **bool** | If &#x60;true&#x60;, the category is created as a category group. | [optional] [default to False]
**group_id** | **int** | If set to the ID of an existing category group, this new category will be assigned to that group. Cannot be set if &#x60;is_group&#x60; is true. | [optional] 
**archived** | **bool** | If &#x60;true&#x60;, the category is archived and not displayed in relevant areas of the Lunch Money app. | [optional] [default to False]
**children** | [**List[CreateCategoryRequestObjectChildrenInner]**](CreateCategoryRequestObjectChildrenInner.md) | The list of existing category objects, or existing category IDs or names of new categories to add to the new category group. This attribute should only be set if &#x60;is_group&#x60; is also set to true.&lt;br&gt; The categories or IDs specified must already exist and may not be category groups themselves. Categories that already belong to another category group will be moved. If strings are specified, they will be used as the names of new categories that will be added to the new category group. The request will fail if any names are the same as the name of an existing category.&lt;br&gt; It is permissible to provide both full category objects and IDs as well as strings for names in the same request. | [optional] 
**order** | **int** | An index specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order is relative to the other categories within the group.&lt;br&gt;While this property can be set via the API it is generally set by the user in the Lunch Money GUI. API. | [optional] 
**collapsed** | **bool** | If &#x60;true&#x60;, the category is collapsed in the Lunch Money GUI.&lt;br&gt;While this property can be set via the API it is generally set by the user in the Lunch Money GUI. | [optional] 

## Example

```python
from lunchmoney-python.models.create_category_request_object import CreateCategoryRequestObject

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


