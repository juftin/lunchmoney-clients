# RecurringObjectTransactionCriteria

The set of properties used to identify matching transactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | The beginning of the date range for matching transactions. If &#x60;null&#x60;, any transactions before end_date may be considered. | 
**end_date** | **date** | The end of the date range for matching transactions. If &#x60;null&#x60;, any transactions after start_date may be considered. | 
**granularity** | **str** | The unit of time used to define the cadence of the recurring item | 
**quantity** | **int** | The number of granularity units between each recurrence | 
**anchor_date** | **date** | The date used in conjunction with the &#x60;quantity&#x60; and &#x60;granularity&#x60; properties to calculate expected occurrences of recurring transactions. | 
**payee** | **str** | If set, represents the original transaction payee name that triggered this recurring item&#39;s creation. | 
**amount** | **str** | The expected amount for a transaction that will match this recurring item. For recurring items that have a flexible amount this is the average of the specified min and max amounts. | 
**to_base** | **float** | The amount converted to the user&#39;s primary currency | 
**currency** | **str** | Three-letter lowercase currency code of the recurring item | 
**plaid_account_id** | **int** | The Plaid account ID associated with the recurring item, if any | 
**manual_account_id** | **int** | The manual account ID associated with the recurring item, if any | 

## Example

```python
from lunchmoney.models.recurring_object_transaction_criteria import RecurringObjectTransactionCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringObjectTransactionCriteria from a JSON string
recurring_object_transaction_criteria_instance = RecurringObjectTransactionCriteria.from_json(json)
# print the JSON string representation of the object
print(RecurringObjectTransactionCriteria.to_json())

# convert the object into a dict
recurring_object_transaction_criteria_dict = recurring_object_transaction_criteria_instance.to_dict()
# create an instance of RecurringObjectTransactionCriteria from a dict
recurring_object_transaction_criteria_from_dict = RecurringObjectTransactionCriteria.from_dict(recurring_object_transaction_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


