# BudgetSettingsResponseObject

Budget period and display settings for the current budgeting account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_period_granularity** | **str** | Budget period granularity | 
**budget_period_quantity** | **int** | The number of &#x60;granularity&#x60; units that make up a single budgeting period. | 
**budget_period_anchor_date** | **date** | The date from which the budgeting period is calculated. All future (and past) periods are derived by applying &#x60;quantity&#x60; × &#x60;granularity&#x60; forward and backward from this date. | 
**budget_hide_no_activity** | **bool** | Display preference for hiding categories in budget view that have no activity and no budgeted value | [default to False]
**budget_use_last_day_of_month** | **bool** | Display preference for using the last day of the month as the period end for monthly periods | [default to False]
**budget_income_option** | **str** | Determines which income value is used as the base when calculating available funds for a budgeting period | 
**budget_rollover_left_to_budget** | **bool** | Determines whether the remaining unallocated funds (“Left to Budget”) at the end of a budgeting period are carried forward to the next period | [default to False]

## Example

```python
from lunchmoney.models.budget_settings_response_object import BudgetSettingsResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetSettingsResponseObject from a JSON string
budget_settings_response_object_instance = BudgetSettingsResponseObject.from_json(json)
# print the JSON string representation of the object
print(BudgetSettingsResponseObject.to_json())

# convert the object into a dict
budget_settings_response_object_dict = budget_settings_response_object_instance.to_dict()
# create an instance of BudgetSettingsResponseObject from a dict
budget_settings_response_object_from_dict = BudgetSettingsResponseObject.from_dict(budget_settings_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


