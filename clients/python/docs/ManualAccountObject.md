# ManualAccountObject

An object containing information about a manual account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this account | 
**name** | **str** | Name of the account | 
**institution_name** | **str** | Name of institution holding the account | 
**display_name** | **str** | Optional display name for the account as set by the user or derived from the &#x60;institution_name&#x60; and &#x60;name&#x60; if not explicitly set. | 
**type** | [**AccountTypeEnum**](AccountTypeEnum.md) | Primary type of the account | 
**subtype** | **str** | Optional account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | 
**balance** | **str** | Current balance of the account in numeric format to 4 decimal places | 
**currency** | **str** | Three-letter lowercase currency code of the account balance | 
**to_base** | **float** | The balance converted to the user&#39;s primary currency | 
**balance_as_of** | **datetime** | Date balance was last updated in ISO 8601 extended format, can be in date or date-time format | 
**status** | **str** | The status of the account | 
**closed_on** | **date** | The date this account was closed in YYYY-MM-DD format. Will be null if the account has not been marked as closed. | 
**external_id** | **str** | An optional external_id that may be set or updated via the API | 
**custom_metadata** | **Dict[str, object]** | User defined JSON data that can be set or cleared via the API | [optional] 
**exclude_from_transactions** | **bool** | If true, this account will not show up as an option for assignment when creating transactions manually | [default to False]
**created_by_name** | **str** | The name of the user who created the account | 
**created_at** | **datetime** | Date/time the account was created in ISO 8601 extended format | 
**updated_at** | **datetime** | Date/time the account was created in ISO 8601 extended format | 

## Example

```python
from lunchmoney.models.manual_account_object import ManualAccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of ManualAccountObject from a JSON string
manual_account_object_instance = ManualAccountObject.from_json(json)
# print the JSON string representation of the object
print(ManualAccountObject.to_json())

# convert the object into a dict
manual_account_object_dict = manual_account_object_instance.to_dict()
# create an instance of ManualAccountObject from a dict
manual_account_object_from_dict = ManualAccountObject.from_dict(manual_account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


