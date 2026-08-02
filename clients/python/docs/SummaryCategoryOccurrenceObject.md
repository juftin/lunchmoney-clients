# SummaryCategoryOccurrenceObject



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_range** | **bool** | &#x60;true&#x60; if this occurrence is within the given date range, &#x60;false&#x60; if it was included because the &#x60;include_past_budget_periods&#x60; parameter was set to &#x60;true&#x60;. | 
**start_date** | **date** | The start date of the budget period | 
**end_date** | **date** | The end date of the budget period | 
**other_activity** | **float** | Total non-recurring activity, in the user&#39;s default currency, for the budget period. The total activity for this category in the period is the sum of this and the recurring_activity. | 
**recurring_activity** | **float** | Total recurring activity, in the user&#39;s default currency, for the budget period. The total activity for this category in the budget period is the sum of this and the other_activity. | 
**budgeted** | **float** | Total budgeted amount, in the user&#39;s primary currency, for the period, or &#x60;null&#x60; if no budget was set. | 
**budgeted_amount** | **str** | Total budgeted amount, in the budgeted currency, for the category within the period, or &#x60;null&#x60; if no budget was set. | 
**budgeted_currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the budgeted amount | 
**notes** | **str** | Any notes set for the budget period. | 

## Example

```python
from lunchmoney.models.summary_category_occurrence_object import SummaryCategoryOccurrenceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryCategoryOccurrenceObject from a JSON string
summary_category_occurrence_object_instance = SummaryCategoryOccurrenceObject.from_json(json)
# print the JSON string representation of the object
print(SummaryCategoryOccurrenceObject.to_json())

# convert the object into a dict
summary_category_occurrence_object_dict = summary_category_occurrence_object_instance.to_dict()
# create an instance of SummaryCategoryOccurrenceObject from a dict
summary_category_occurrence_object_from_dict = SummaryCategoryOccurrenceObject.from_dict(summary_category_occurrence_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


