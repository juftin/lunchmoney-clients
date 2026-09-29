# UpdateUserSettingsRequestObject

Request body for updating user settings. Include at least one property to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_debits_as_negative** | **bool** | If set, updates the display preference for amount signs in the Lunch Money app. Does not affect amount sign conventions in API responses. | [optional] 
**auto_suggest_payee** | **bool** | If set, updates whether payee suggestions are shown. | [optional] 
**month_year_format** | [**MonthYearFormatEnum**](MonthYearFormatEnum.md) | If set, updates the month and year display format. | [optional] 
**month_day_year_format** | [**MonthDayYearFormatEnum**](MonthDayYearFormatEnum.md) | If set, updates the full date display format. | [optional] 
**month_day_format** | [**MonthDayFormatEnum**](MonthDayFormatEnum.md) | If set, updates the month and day display format. | [optional] 
**show_am_pm** | **bool** | If set, updates whether times use a 12-hour (AM/PM) or 24-hour clock. | [optional] 
**week_starts_on** | [**WeekStartsOnEnum**](WeekStartsOnEnum.md) | If set, updates the day on which a calendar week begins. | [optional] 
**always_display_year** | **bool** | If set, updates whether dates always include the year. | [optional] 
**always_display_weekday** | **bool** | If set, updates whether weekday names are shown when displaying dates. | [optional] 

## Example

```python
from lunchmoney.models.update_user_settings_request_object import UpdateUserSettingsRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserSettingsRequestObject from a JSON string
update_user_settings_request_object_instance = UpdateUserSettingsRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateUserSettingsRequestObject.to_json())

# convert the object into a dict
update_user_settings_request_object_dict = update_user_settings_request_object_instance.to_dict()
# create an instance of UpdateUserSettingsRequestObject from a dict
update_user_settings_request_object_from_dict = UpdateUserSettingsRequestObject.from_dict(update_user_settings_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


