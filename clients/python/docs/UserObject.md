# UserObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user&#39;s name | 
**email** | **str** | The user&#39;s email | 
**id** | **int** | Unique ID for the user | 
**account_id** | **int** | Unique ID for the current budgeting account | 
**budget_name** | **str** | Name of the current budgeting account | 
**primary_currency** | [**CurrencyEnum**](CurrencyEnum.md) | Primary currency for the current budgeting account | 
**api_key_label** | **str** | Label assigned by the user to the API key being used. Returns null if no label is set | 

## Example

```python
from lunchmoney.models.user_object import UserObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserObject from a JSON string
user_object_instance = UserObject.from_json(json)
# print the JSON string representation of the object
print(UserObject.to_json())

# convert the object into a dict
user_object_dict = user_object_instance.to_dict()
# create an instance of UserObject from a dict
user_object_from_dict = UserObject.from_dict(user_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


