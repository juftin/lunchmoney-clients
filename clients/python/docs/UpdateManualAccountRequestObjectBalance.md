# UpdateManualAccountRequestObjectBalance

Numeric value of the current balance, up to four decimal places, of the manual account as a number or string. Do not include any special characters aside from a decimal point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.update_manual_account_request_object_balance import UpdateManualAccountRequestObjectBalance

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManualAccountRequestObjectBalance from a JSON string
update_manual_account_request_object_balance_instance = UpdateManualAccountRequestObjectBalance.from_json(json)
# print the JSON string representation of the object
print(UpdateManualAccountRequestObjectBalance.to_json())

# convert the object into a dict
update_manual_account_request_object_balance_dict = update_manual_account_request_object_balance_instance.to_dict()
# create an instance of UpdateManualAccountRequestObjectBalance from a dict
update_manual_account_request_object_balance_from_dict = UpdateManualAccountRequestObjectBalance.from_dict(update_manual_account_request_object_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


