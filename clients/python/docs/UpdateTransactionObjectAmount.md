# UpdateTransactionObjectAmount

Numeric value of amount without currency symbol. i.e. $4.25 should be denoted as 4.25. May be a string or a number in double format. Positive values indicate a debit transaction, negative values indicate a credit transaction. <br> May not be updated on transactions that belong to a synced account with the \"Allow Modifications to Transactions\" property disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from lunchmoney-python.models.update_transaction_object_amount import UpdateTransactionObjectAmount

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionObjectAmount from a JSON string
update_transaction_object_amount_instance = UpdateTransactionObjectAmount.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionObjectAmount.to_json())

# convert the object into a dict
update_transaction_object_amount_dict = update_transaction_object_amount_instance.to_dict()
# create an instance of UpdateTransactionObjectAmount from a dict
update_transaction_object_amount_from_dict = UpdateTransactionObjectAmount.from_dict(update_transaction_object_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


