# UpsertBudget400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | High level error type, for example &#39;Not Found&#39; or &#39;Request Validation Failure&#39; | 
**requested_start_date** | **date** | The start_date value that was rejected | 
**previous_valid_start_date** | **date** | The previous valid budget period start date before the requested date | [optional] 
**next_valid_start_date** | **date** | The next valid budget period start date after the requested date | [optional] 
**err_msg** | **str** | Human-readable error message | 
**errors** | [**List[ErrorResponseObjectErrorsInner]**](ErrorResponseObjectErrorsInner.md) | An list of objects that describe the errors encountered while processing the request.&lt;br&gt; If multiple errors were encountered, the list will contain multiple objects.&lt;br&gt; Each &#x60;error&#x60; object is guaranteed to have an &#x60;errMsg&#x60;, but it may also contain other error specific properties. | 

## Example

```python
from lunchmoney.models.upsert_budget400_response import UpsertBudget400Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertBudget400Response from a JSON string
upsert_budget400_response_instance = UpsertBudget400Response.from_json(json)
# print the JSON string representation of the object
print(UpsertBudget400Response.to_json())

# convert the object into a dict
upsert_budget400_response_dict = upsert_budget400_response_instance.to_dict()
# create an instance of UpsertBudget400Response from a dict
upsert_budget400_response_from_dict = UpsertBudget400Response.from_dict(upsert_budget400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


