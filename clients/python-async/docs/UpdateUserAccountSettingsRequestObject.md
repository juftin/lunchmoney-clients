# UpdateUserAccountSettingsRequestObject

Request body for updating settings specific to the authorized user within the current budgeting account. Include at least one property to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_review_transaction_on_update** | **bool** | If set, updates whether transactions are marked as reviewed when their date, category, payee, amount, account, or notes are changed. | [optional] 
**auto_review_transaction_on_creation** | **bool** | If set, updates whether new manual transactions start as reviewed or unreviewed. | [optional] 
**default_manual_account_id** | **int** | If set, updates the manual account selected by default when the user creates a manual transaction in the current budgeting account. Must identify a manual account returned by [GET /manual_accounts](#tag/manual_accounts/GET/manual_accounts) for the current budgeting account. Set to &#x60;null&#x60; to clear the selection. | [optional] 

## Example

```python
from lunchmoney.models.update_user_account_settings_request_object import UpdateUserAccountSettingsRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserAccountSettingsRequestObject from a JSON string
update_user_account_settings_request_object_instance = UpdateUserAccountSettingsRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateUserAccountSettingsRequestObject.to_json())

# convert the object into a dict
update_user_account_settings_request_object_dict = update_user_account_settings_request_object_instance.to_dict()
# create an instance of UpdateUserAccountSettingsRequestObject from a dict
update_user_account_settings_request_object_from_dict = UpdateUserAccountSettingsRequestObject.from_dict(update_user_account_settings_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


