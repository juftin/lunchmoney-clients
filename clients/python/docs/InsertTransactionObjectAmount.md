# InsertTransactionObjectAmount

Numeric value of the amount without a currency symbol. For example, $4.25 should be provided as 4.25. May be a string or a number in double format. Positive values indicate a debit transaction, negative values indicate a credit transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney.models.insert_transaction_object_amount import InsertTransactionObjectAmount

# TODO update the JSON string below
json = "{}"
# create an instance of InsertTransactionObjectAmount from a JSON string
insert_transaction_object_amount_instance = InsertTransactionObjectAmount.from_json(json)
# print the JSON string representation of the object
print(InsertTransactionObjectAmount.to_json())

# convert the object into a dict
insert_transaction_object_amount_dict = insert_transaction_object_amount_instance.to_dict()
# create an instance of InsertTransactionObjectAmount from a dict
insert_transaction_object_amount_from_dict = InsertTransactionObjectAmount.from_dict(insert_transaction_object_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


