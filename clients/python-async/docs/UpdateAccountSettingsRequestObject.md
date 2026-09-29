# UpdateAccountSettingsRequestObject

Request body for updating account settings. Include at least one property to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_currency** | [**CurrencyEnum**](CurrencyEnum.md) | If set, updates the account&#39;s primary currency. | [optional] 
**supported_currencies** | [**List[CurrencyEnum]**](CurrencyEnum.md) | If set, replaces the list of supported currencies for the account. | [optional] 
**display_name** | **str** | If set, updates the display name of the budgeting account. | [optional] 
**locale** | [**LocaleEnum**](LocaleEnum.md) | If set, updates the locale used for formatting numbers and currency amounts in the Lunch Money app. See [Supported Locales](https://lunchmoney.dev/v2/locales) for accepted values. Date presentation is configured separately through [GET /me/user/settings](#tag/me/GET/me/user/settings) and [PUT /me/user/settings](#tag/me/PUT/me/user/settings). | [optional] 
**auto_create_category_rules** | **bool** | If set, updates whether category rules are created automatically. | [optional] 
**auto_create_suggested_transaction_rules** | **bool** | If set, updates whether suggested transaction rules are created automatically. | [optional] 
**include_pending_in_totals** | **bool** | If set, updates whether pending transactions are included in account totals. | [optional] 

## Example

```python
from lunchmoney.models.update_account_settings_request_object import UpdateAccountSettingsRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountSettingsRequestObject from a JSON string
update_account_settings_request_object_instance = UpdateAccountSettingsRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountSettingsRequestObject.to_json())

# convert the object into a dict
update_account_settings_request_object_dict = update_account_settings_request_object_instance.to_dict()
# create an instance of UpdateAccountSettingsRequestObject from a dict
update_account_settings_request_object_from_dict = UpdateAccountSettingsRequestObject.from_dict(update_account_settings_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


