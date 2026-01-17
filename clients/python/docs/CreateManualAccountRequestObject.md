# CreateManualAccountRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the manual account | 
**type** | [**AccountTypeEnum**](AccountTypeEnum.md) | The type of manual account. | 
**subtype** | **str** | An optional manual account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | [optional] 
**display_name** | **str** | Display name of the manual account as set by user.&lt;br&gt; This must be unique for the budgeting account.  If not set, it will be derived from the &#x60;institution_name&#x60; (if any) plus &#x60;name&#x60;. | [optional] 
**balance** | [**CreateManualAccountRequestObjectBalance**](CreateManualAccountRequestObjectBalance.md) |  | 
**balance_as_of** | **str** | Date/time the balance of the manual account was last updated in ISO 8601 extended format | [optional] 
**closed_on** | **date** | The date this manual account was closed in YYYY-MM-DD format. | [optional] 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format | [optional] 
**institution_name** | **str** | Name of institution holding the manual account | [optional] 
**external_id** | **str** | An optional user-defined ID for the manual account | [optional] 
**custom_metadata** | **Dict[str, object]** | An optional JSON object that includes additional data related to this account. This must be a valid JSON object and, when stringified, must not exceed 4096 characters. | [optional] 
**exclude_from_transactions** | **bool** | If &#x60;true&#x60;, transactions may not be assigned to this manual account. | [optional] [default to False]

## Example

```python
from lunchmoney-python.models.create_manual_account_request_object import CreateManualAccountRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManualAccountRequestObject from a JSON string
create_manual_account_request_object_instance = CreateManualAccountRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateManualAccountRequestObject.to_json())

# convert the object into a dict
create_manual_account_request_object_dict = create_manual_account_request_object_instance.to_dict()
# create an instance of CreateManualAccountRequestObject from a dict
create_manual_account_request_object_from_dict = CreateManualAccountRequestObject.from_dict(create_manual_account_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


