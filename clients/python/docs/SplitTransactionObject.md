# SplitTransactionObject

The object representing a split transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**SplitTransactionObjectAmount**](SplitTransactionObjectAmount.md) |  | 
**payee** | **str** | The payee for the child transaction. Will inherit the original payee from the parent if not defined. | [optional] 
**var_date** | **date** | Must be in ISO 8601 format (YYYY-MM-DD). Will inherit from the parent if not defined. | [optional] 
**category_id** | **int** | Category ID for the child transaction. The category must already exist for the account. If omitted, the child inherits the parent category. If &#x60;null&#x60;, the child has no category. | [optional] 
**tag_ids** | **List[int]** | The IDs of any tags to apply to this split child transaction. Each ID must match an existing tag. | [optional] 
**notes** | **str** | Notes for the child transaction. If omitted, the child inherits the parent notes. If &#x60;null&#x60; or an empty string, the child has no notes. | [optional] 

## Example

```python
from lunchmoney.models.split_transaction_object import SplitTransactionObject

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionObject from a JSON string
split_transaction_object_instance = SplitTransactionObject.from_json(json)
# print the JSON string representation of the object
print(SplitTransactionObject.to_json())

# convert the object into a dict
split_transaction_object_dict = split_transaction_object_instance.to_dict()
# create an instance of SplitTransactionObject from a dict
split_transaction_object_from_dict = SplitTransactionObject.from_dict(split_transaction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


