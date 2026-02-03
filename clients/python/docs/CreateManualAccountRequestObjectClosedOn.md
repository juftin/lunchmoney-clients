# CreateManualAccountRequestObjectClosedOn

The date this manual account was closed in YYYY-MM-DD format. If set, `status` must also be set to `closed`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.create_manual_account_request_object_closed_on import CreateManualAccountRequestObjectClosedOn

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManualAccountRequestObjectClosedOn from a JSON string
create_manual_account_request_object_closed_on_instance = CreateManualAccountRequestObjectClosedOn.from_json(json)
# print the JSON string representation of the object
print(CreateManualAccountRequestObjectClosedOn.to_json())

# convert the object into a dict
create_manual_account_request_object_closed_on_dict = create_manual_account_request_object_closed_on_instance.to_dict()
# create an instance of CreateManualAccountRequestObjectClosedOn from a dict
create_manual_account_request_object_closed_on_from_dict = CreateManualAccountRequestObjectClosedOn.from_dict(create_manual_account_request_object_closed_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


