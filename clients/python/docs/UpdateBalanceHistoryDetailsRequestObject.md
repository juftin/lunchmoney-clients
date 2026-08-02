# UpdateBalanceHistoryDetailsRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New archived account name for the deleted account source | [optional] 
**institution_name** | **str** | New archived institution name for the deleted account source | [optional] 
**display_name** | **str** | New display name for the deleted account source | [optional] 
**account_type** | **str** | New archived account type for the deleted account source | [optional] 
**subtype** | **str** | New archived subtype for the deleted account source | [optional] 
**mask** | **str** | New archived account mask for the deleted account source | [optional] 

## Example

```python
from lunchmoney.models.update_balance_history_details_request_object import UpdateBalanceHistoryDetailsRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBalanceHistoryDetailsRequestObject from a JSON string
update_balance_history_details_request_object_instance = UpdateBalanceHistoryDetailsRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateBalanceHistoryDetailsRequestObject.to_json())

# convert the object into a dict
update_balance_history_details_request_object_dict = update_balance_history_details_request_object_instance.to_dict()
# create an instance of UpdateBalanceHistoryDetailsRequestObject from a dict
update_balance_history_details_request_object_from_dict = UpdateBalanceHistoryDetailsRequestObject.from_dict(update_balance_history_details_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


