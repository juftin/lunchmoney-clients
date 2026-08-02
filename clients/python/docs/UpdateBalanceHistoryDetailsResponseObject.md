# UpdateBalanceHistoryDetailsResponseObject

Updated archived metadata for a deleted balance history source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Archived account name for the deleted account source | 
**institution_name** | **str** | Archived institution name for the deleted account source | 
**display_name** | **str** | Archived display name for the deleted account source | 
**account_type** | **str** | Archived account type for the deleted account source | 
**subtype** | **str** | Archived subtype for the deleted account source | 
**mask** | **str** | Archived account mask for the deleted account source | 

## Example

```python
from lunchmoney.models.update_balance_history_details_response_object import UpdateBalanceHistoryDetailsResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBalanceHistoryDetailsResponseObject from a JSON string
update_balance_history_details_response_object_instance = UpdateBalanceHistoryDetailsResponseObject.from_json(json)
# print the JSON string representation of the object
print(UpdateBalanceHistoryDetailsResponseObject.to_json())

# convert the object into a dict
update_balance_history_details_response_object_dict = update_balance_history_details_response_object_instance.to_dict()
# create an instance of UpdateBalanceHistoryDetailsResponseObject from a dict
update_balance_history_details_response_object_from_dict = UpdateBalanceHistoryDetailsResponseObject.from_dict(update_balance_history_details_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


