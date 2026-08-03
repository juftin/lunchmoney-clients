# UpdateManualAccountRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique identifier of this account. Ignored if set | [optional] 
**name** | **str** | If set, the new name of the manual account | [optional] 
**institution_name** | **str** | If set, the name of the institution holding the account | [optional] 
**display_name** | **str** | If set, the new display name for the manual account.&lt;br&gt; This must be unique for the user. | [optional] 
**type** | [**AccountTypeEnum**](AccountTypeEnum.md) | If set, the new type of the manual account | [optional] 
**subtype** | **str** | If set, an optional account subtype. Set to &#x60;null&#x60; to clear it. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | [optional] 
**balance** | [**UpdateManualAccountRequestObjectBalance**](UpdateManualAccountRequestObjectBalance.md) |  | [optional] 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | If set, the new three-letter lowercase currency code of the manual account balance. | [optional] 
**balance_as_of** | **str** | If set, updates the &#x60;balance_as_of&#x60; value. May be provided as a date in YYYY-MM-DD format or as a date-time string in ISO 8601 extended format. This property is ignored unless &#x60;balance&#x60; is also set. If &#x60;balance&#x60; is set and this property is not set, the current time is used. | [optional] 
**status** | **str** | If set, updates the status of the manual account. If set to &#x60;closed&#x60;, &#x60;closed_on&#x60; will be set to the current date unless it is also set. | [optional] 
**closed_on** | [**UpdateManualAccountRequestObjectClosedOn**](UpdateManualAccountRequestObjectClosedOn.md) |  | [optional] 
**external_id** | **str** | An optional user-defined ID for the manual account | [optional] 
**custom_metadata** | **Dict[str, object]** | An optional JSON object that includes additional data related to this account. This must be a valid JSON object and, when stringified, must not exceed 4096 characters. | [optional] 
**exclude_from_transactions** | **bool** | If set, transactions may not be assigned to this manual account | [optional] 
**to_base** | **float** | System defined balance converted to the user&#39;s primary currency. Ignored if set. Use &#x60;balance&#x60; to update the balance in the account | [optional] 
**created_at** | **datetime** | System defined date/time the account was created in ISO 8601 extended format. Ignored if set. | [optional] 
**updated_at** | **datetime** | System defined date/time the account was last updated in ISO 8601 extended format. Ignored if set. | [optional] 
**created_by_name** | **str** | System defined name of the user who created the account. Ignored if set | [optional] 

## Example

```python
from lunchmoney.models.update_manual_account_request_object import UpdateManualAccountRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManualAccountRequestObject from a JSON string
update_manual_account_request_object_instance = UpdateManualAccountRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateManualAccountRequestObject.to_json())

# convert the object into a dict
update_manual_account_request_object_dict = update_manual_account_request_object_instance.to_dict()
# create an instance of UpdateManualAccountRequestObject from a dict
update_manual_account_request_object_from_dict = UpdateManualAccountRequestObject.from_dict(update_manual_account_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


