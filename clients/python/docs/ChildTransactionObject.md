# ChildTransactionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System-created unique identifier for the transaction | 
**var_date** | **date** | Transaction date in ISO 8601 format | 
**amount** | **str** | Amount of the transaction in numeric format to 4 decimal places. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format | 
**to_base** | **float** | The amount converted to the user&#39;s primary currency. If the transaction currency is the same as the user&#39;s primary currency, to_base and amount will be the same. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**recurring_id** | **int** | The unique identifier of the associated recurring item that this transaction matched. | 
**payee** | **str** | Name of payee set by the user, the financial institution, or by a matched recurring item. This will match the value displayed in payee field on the transactions page in the Lunch Money app.  | 
**original_name** | **str** | Original payee name from the source (financial institution, CSV, etc.). For Plaid transactions, this is the raw name before normalization. For manual/API transactions, this typically matches &#x60;payee&#x60;. May be null for older transactions. | [optional] 
**category_id** | **int** | Unique identifier of associated category set by the user or by a matched recurring item.&lt;br&gt; Category details can be obtained by passing the value of this property to the [Get A Single Category](../operations/getCategoryById) API | 
**notes** | **str** | Any transaction notes set by the user or by a matched recurring item. This will match the value displayed in notes field on the transactions page in the Lunch Money app.  | 
**status** | **str** | Status of the transaction.  Will be one of the following values:  | 
**is_pending** | **bool** | Denotes if the transaction is pending (not posted). Applies only to transactions in synced accounts and will always be false for transactions associated with manual accounts. | 
**created_at** | **datetime** | The date and time of when the transaction was created (in the ISO 8601 extended format). | 
**updated_at** | **datetime** | The date and time of when the transaction was last updated (in the ISO 8601 extended format). | 
**is_split_parent** | **bool** | If &#x60;true&#x60;, this transaction has been split into two or more other transactions. By default, parent transactions are not returned in call to &#x60;GET /transactions&#x60; but they can be queried directly by their ID. | [optional] 
**split_parent_id** | **int** | A transaction ID if this is a split transaction. Denotes the transaction ID of the original, or parent, transaction. Is null if this is not a split transaction | 
**is_group_parent** | **bool** | True if this transaction represents a group of transactions. If so, amount and currency represent the totalled amount of transactions bearing this transaction&#39;s id as their group_parent_id. Amount is calculated based on the user&#39;s primary currency. | 
**group_parent_id** | **int** | If set, this transaction is part of a group. Denotes the ID of the grouped transaction that it is included in. By default, the transactions that were grouped are not returned in a call to &#x60;GET /transactions&#x60; but they can be queried directly by calling the &#x60;GET /transactions/group/{id}&#x60;, where the id passed is associated with a transaction where the &#x60;is_group_parent&#x60; attribute is true. | 
**manual_account_id** | **int** | The unique identifier of the manual account associated with this transaction. This will always be null if this transaction is associated with a synced account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money app. | 
**plaid_account_id** | **int** | The unique identifier of the plaid account associated with this transaction. This will always be null if this transaction is associated with a manual account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money app. | 
**tag_ids** | **List[int]** | A list of tag_ids for the tags associated with this transaction. If the transaction has no tags this will be an empty list.&lt;br&gt; Tag details can be obtained by passing the value of this attribute as the &#x60;ids&#x60; query parameter to the [List Tags](../operations/getTags) API | 
**source** | **str** | Source of the transaction: - &#x60;api&#x60;: Transaction was added by a call to the [POST /transactions](../operations/createTransaction) API - &#x60;csv&#x60;: Transaction was added via a CSV Import - &#x60;manual&#x60;: Transaction was created via the \&quot;Add to Cash\&quot; button on the Transactions page - &#x60;merge&#x60;: Transactions were originally in an account that was merged into another account - &#x60;plaid&#x60;: Transaction came from a Financial Institution synced via Plaid - &#x60;recurring&#x60;: Transaction was created from the Recurring page - &#x60;rule&#x60;: Transaction was created by a rule to split a transaction - &#x60;split&#x60;: This is a transaction created by splitting another transaction - &#x60;user&#x60;: This is a legacy value and is replaced by either csv or manual  | 
**external_id** | **str** | A user-defined external ID associated with the transaction. For transactions belonging to manual accounts, the external ID must be unique for each transaction associated with the account. | 
**plaid_metadata** | **object** | If requested, the transaction&#39;s plaid_metadata that came when this transaction was obtained. This will be a JSON object, but the schema is variable. This will only be present for transactions associated with a plaid account. | [optional] 
**custom_metadata** | **object** | If requested, the transaction&#39;s custom_metadata that was included when the transaction was inserted via the API. This will be a JSON object, but the schema is variable. | [optional] 
**files** | [**List[TransactionAttachmentObject]**](TransactionAttachmentObject.md) | A list of objects that describe any attachments to the transaction | [optional] 

## Example

```python
from lunchmoney.models.child_transaction_object import ChildTransactionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ChildTransactionObject from a JSON string
child_transaction_object_instance = ChildTransactionObject.from_json(json)
# print the JSON string representation of the object
print(ChildTransactionObject.to_json())

# convert the object into a dict
child_transaction_object_dict = child_transaction_object_instance.to_dict()
# create an instance of ChildTransactionObject from a dict
child_transaction_object_from_dict = ChildTransactionObject.from_dict(child_transaction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


