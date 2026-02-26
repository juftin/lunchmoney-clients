# BudgetInvalidPeriodErrorObject

Returned when the requested start_date is not a valid budget period start for the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Overall error message (e.g. Invalid Request) | 
**requested_start_date** | **date** | The start_date value that was rejected | 
**previous_valid_start_date** | **date** | The previous valid budget period start date before the requested date | [optional] 
**next_valid_start_date** | **date** | The next valid budget period start date after the requested date | [optional] 
**err_msg** | **str** | Human-readable error message | 

## Example

```python
from lunchmoney.models.budget_invalid_period_error_object import BudgetInvalidPeriodErrorObject

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetInvalidPeriodErrorObject from a JSON string
budget_invalid_period_error_object_instance = BudgetInvalidPeriodErrorObject.from_json(json)
# print the JSON string representation of the object
print(BudgetInvalidPeriodErrorObject.to_json())

# convert the object into a dict
budget_invalid_period_error_object_dict = budget_invalid_period_error_object_instance.to_dict()
# create an instance of BudgetInvalidPeriodErrorObject from a dict
budget_invalid_period_error_object_from_dict = BudgetInvalidPeriodErrorObject.from_dict(budget_invalid_period_error_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


