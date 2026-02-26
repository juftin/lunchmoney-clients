# ErrorResponseObject

The object returned will any 4XX error response. Each response is guaranteed to have a `message` and at least one `error` object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | High level error type, for example &#39;Not Found&#39; or &#39;Request Validation Failure&#39; | 
**errors** | [**List[ErrorResponseObjectErrorsInner]**](ErrorResponseObjectErrorsInner.md) | An list of objects that describe the errors encountered while processing the request.&lt;br&gt; If multiple errors were encountered, the list will contain multiple objects.&lt;br&gt; Each &#x60;error&#x60; object is guaranteed to have an &#x60;errMsg&#x60;, but it may also contain other error specific properties. | 

## Example

```python
from lunchmoney.models.error_response_object import ErrorResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseObject from a JSON string
error_response_object_instance = ErrorResponseObject.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseObject.to_json())

# convert the object into a dict
error_response_object_dict = error_response_object_instance.to_dict()
# create an instance of ErrorResponseObject from a dict
error_response_object_from_dict = ErrorResponseObject.from_dict(error_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


