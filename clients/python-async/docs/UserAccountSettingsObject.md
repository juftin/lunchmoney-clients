# UserAccountSettingsObject

Settings specific to the authorized user within the current budgeting account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_review_transaction_on_update** | **bool** | If &#x60;true&#x60;, transactions are marked as reviewed when their date, category, payee, amount, account, or notes are changed. | [default to True]
**auto_review_transaction_on_creation** | **bool** | If &#x60;true&#x60;, new manual transactions start as reviewed. If &#x60;false&#x60;, they start as unreviewed. | [default to True]
**default_manual_account_id** | **int** | Manual account selected by default when the user creates a manual transaction in the current budgeting account. Must identify a manual account returned by [GET /manual_accounts](#tag/manual_accounts/GET/manual_accounts) for the current budgeting account. Set to &#x60;null&#x60; to clear the selection. | 

## Example

```python
from lunchmoney.models.user_account_settings_object import UserAccountSettingsObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountSettingsObject from a JSON string
user_account_settings_object_instance = UserAccountSettingsObject.from_json(json)
# print the JSON string representation of the object
print(UserAccountSettingsObject.to_json())

# convert the object into a dict
user_account_settings_object_dict = user_account_settings_object_instance.to_dict()
# create an instance of UserAccountSettingsObject from a dict
user_account_settings_object_from_dict = UserAccountSettingsObject.from_dict(user_account_settings_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


