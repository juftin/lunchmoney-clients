# UpdateManualAccountRequestObjectClosedOn

If set, the date this manual account was closed in YYYY-MM-DD format. If updating an account that is not already closed, `status` must also be set to `closed`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.update_manual_account_request_object_closed_on import UpdateManualAccountRequestObjectClosedOn

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManualAccountRequestObjectClosedOn from a JSON string
update_manual_account_request_object_closed_on_instance = UpdateManualAccountRequestObjectClosedOn.from_json(json)
# print the JSON string representation of the object
print(UpdateManualAccountRequestObjectClosedOn.to_json())

# convert the object into a dict
update_manual_account_request_object_closed_on_dict = update_manual_account_request_object_closed_on_instance.to_dict()
# create an instance of UpdateManualAccountRequestObjectClosedOn from a dict
update_manual_account_request_object_closed_on_from_dict = UpdateManualAccountRequestObjectClosedOn.from_dict(update_manual_account_request_object_closed_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


