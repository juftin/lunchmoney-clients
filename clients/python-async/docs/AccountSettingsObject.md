# AccountSettingsObject

Account-level settings for the budgeting account associated with the authorized API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_currency** | [**CurrencyEnum**](CurrencyEnum.md) | Primary currency for the account. | 
**supported_currencies** | [**List[CurrencyEnum]**](CurrencyEnum.md) | Currencies available when creating or editing transactions, balances, and other amounts in the Lunch Money app. | 
**display_name** | **str** | Display name of the budgeting account in the Lunch Money app. | 
**locale** | [**LocaleEnum**](LocaleEnum.md) | Locale used for formatting numbers and currency amounts in the Lunch Money app (for example, &#x60;en-US&#x60;). See [Supported Locales](https://lunchmoney.dev/v2/locales) for accepted values. Date presentation is configured separately through [GET /me/user/settings](#tag/me/GET/me/user/settings) and [PUT /me/user/settings](#tag/me/PUT/me/user/settings). When no locale is explicitly stored for the account, the effective locale is derived from the &#x60;default_locale&#x60; associated with &#x60;primary_currency&#x60; in the currencies table (for example, &#x60;usd&#x60; → &#x60;en-US&#x60;, &#x60;cad&#x60; → &#x60;en-CA&#x60;, &#x60;gbp&#x60; → &#x60;en-GB&#x60;). | 
**auto_create_category_rules** | **bool** | If &#x60;true&#x60;, category rules are created automatically when categorizing transactions. | [default to True]
**auto_create_suggested_transaction_rules** | **bool** | If &#x60;true&#x60;, suggested transaction rules are created automatically. | [default to True]
**include_pending_in_totals** | **bool** | If &#x60;true&#x60;, pending transactions are included in account totals. | [default to True]

## Example

```python
from lunchmoney.models.account_settings_object import AccountSettingsObject

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSettingsObject from a JSON string
account_settings_object_instance = AccountSettingsObject.from_json(json)
# print the JSON string representation of the object
print(AccountSettingsObject.to_json())

# convert the object into a dict
account_settings_object_dict = account_settings_object_instance.to_dict()
# create an instance of AccountSettingsObject from a dict
account_settings_object_from_dict = AccountSettingsObject.from_dict(account_settings_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


