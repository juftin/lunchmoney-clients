# UserSettingsObject

User-level display and formatting preferences for the user associated with the authorized API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_debits_as_negative** | **bool** | Display preference for how amounts are shown in the Lunch Money app. When &#x60;true&#x60;, debits are shown as negative values and credits as positive values.&lt;p&gt; This setting does **not** change amount sign conventions in API responses. Amount fields such as &#x60;amount&#x60; and &#x60;to_base&#x60; on transaction objects always use positive values for debits and negative values for credits. | [default to True]
**auto_suggest_payee** | **bool** | If &#x60;true&#x60;, payee suggestions are shown when entering transactions in the Lunch Money app. | [default to True]
**month_year_format** | [**MonthYearFormatEnum**](MonthYearFormatEnum.md) | Format string used when displaying month and year values. | 
**month_day_year_format** | [**MonthDayYearFormatEnum**](MonthDayYearFormatEnum.md) | Format string used when displaying full dates (month, day, and year). | 
**month_day_format** | [**MonthDayFormatEnum**](MonthDayFormatEnum.md) | Format string used when displaying month and day values without a year. | 
**show_am_pm** | **bool** | If &#x60;true&#x60;, times are displayed using a 12-hour clock with AM/PM. If &#x60;false&#x60;, times are displayed using a 24-hour clock. | [default to True]
**week_starts_on** | [**WeekStartsOnEnum**](WeekStartsOnEnum.md) | The day on which a calendar week begins. | 
**always_display_year** | **bool** | If &#x60;true&#x60;, dates always include the year and &#x60;month_day_format&#x60; is not used. | [default to False]
**always_display_weekday** | **bool** | If &#x60;true&#x60;, weekday names are included when displaying dates. | [default to True]

## Example

```python
from lunchmoney.models.user_settings_object import UserSettingsObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsObject from a JSON string
user_settings_object_instance = UserSettingsObject.from_json(json)
# print the JSON string representation of the object
print(UserSettingsObject.to_json())

# convert the object into a dict
user_settings_object_dict = user_settings_object_instance.to_dict()
# create an instance of UserSettingsObject from a dict
user_settings_object_from_dict = UserSettingsObject.from_dict(user_settings_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


