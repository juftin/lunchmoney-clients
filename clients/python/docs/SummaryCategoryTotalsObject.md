# SummaryCategoryTotalsObject

Total activity for the given category within the given date range when it is aligned with the budget period setting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other_activity** | **float** | Total non-recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the recurring_activity. | 
**recurring_activity** | **float** | Total recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the other_activity. | 
**budgeted** | **float** | Total budgeted amount, in the user&#39;s default currency, for the category within the given date range or null if the category is not budgeted. This property will not be present in a non-aligned response. | [optional] 
**available** | **float** | Total amount of funds available, in the user&#39;s default currency, for the category within the given date range. This property will not be present in a non-aligned response. | [optional] 
**recurring_remaining** | **float** | Total expected recurring activity, in the user&#39;s default currency, that has not yet occurred for the category within the given date range. | 
**recurring_expected** | **float** | Total expected recurring activity for the category within the given date range. | 

## Example

```python
from lunchmoney.models.summary_category_totals_object import SummaryCategoryTotalsObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryCategoryTotalsObject from a JSON string
summary_category_totals_object_instance = SummaryCategoryTotalsObject.from_json(json)
# print the JSON string representation of the object
print(SummaryCategoryTotalsObject.to_json())

# convert the object into a dict
summary_category_totals_object_dict = summary_category_totals_object_instance.to_dict()
# create an instance of SummaryCategoryTotalsObject from a dict
summary_category_totals_object_from_dict = SummaryCategoryTotalsObject.from_dict(summary_category_totals_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


