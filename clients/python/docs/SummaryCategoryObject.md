# SummaryCategoryObject

List of each category's budget configuration and activity for the date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | ID of the category associated with the totals. | 
**totals** | [**SummaryCategoryTotalsObject**](SummaryCategoryTotalsObject.md) |  | 
**occurrences** | [**List[SummaryCategoryOccurrenceObject]**](SummaryCategoryOccurrenceObject.md) | A list of objects describing the budget activity for each period within the range. This property is only present when &#x60;include_occurrences&#x60; is true.&lt;p&gt; For aligned ranges, there is one occurrence for each budget period in the range; for non-aligned, only periods fully contained in the range are included.&lt;p&gt; If &#x60;include_past_budget_dates&#x60; is also &#x60;true&#x60;, the three budget periods prior to the range are also included. | [optional] 

## Example

```python
from lunchmoney.models.summary_category_object import SummaryCategoryObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryCategoryObject from a JSON string
summary_category_object_instance = SummaryCategoryObject.from_json(json)
# print the JSON string representation of the object
print(SummaryCategoryObject.to_json())

# convert the object into a dict
summary_category_object_dict = summary_category_object_instance.to_dict()
# create an instance of SummaryCategoryObject from a dict
summary_category_object_from_dict = SummaryCategoryObject.from_dict(summary_category_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


