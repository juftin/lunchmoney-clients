# UpdateUserSettingsRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShowDebitsAsNegative** | Pointer to **bool** | If set, updates the display preference for amount signs in the Lunch Money app. Does not affect amount sign conventions in API responses. | [optional] 
**AutoSuggestPayee** | Pointer to **bool** | If set, updates whether payee suggestions are shown. | [optional] 
**MonthYearFormat** | Pointer to [**MonthYearFormatEnum**](MonthYearFormatEnum.md) | If set, updates the month and year display format. | [optional] 
**MonthDayYearFormat** | Pointer to [**MonthDayYearFormatEnum**](MonthDayYearFormatEnum.md) | If set, updates the full date display format. | [optional] 
**MonthDayFormat** | Pointer to [**MonthDayFormatEnum**](MonthDayFormatEnum.md) | If set, updates the month and day display format. | [optional] 
**ShowAmPm** | Pointer to **bool** | If set, updates whether times use a 12-hour (AM/PM) or 24-hour clock. | [optional] 
**WeekStartsOn** | Pointer to [**WeekStartsOnEnum**](WeekStartsOnEnum.md) | If set, updates the day on which a calendar week begins. | [optional] 
**AlwaysDisplayYear** | Pointer to **bool** | If set, updates whether dates always include the year. | [optional] 
**AlwaysDisplayWeekday** | Pointer to **bool** | If set, updates whether weekday names are shown when displaying dates. | [optional] 

## Methods

### NewUpdateUserSettingsRequestObject

`func NewUpdateUserSettingsRequestObject() *UpdateUserSettingsRequestObject`

NewUpdateUserSettingsRequestObject instantiates a new UpdateUserSettingsRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateUserSettingsRequestObjectWithDefaults

`func NewUpdateUserSettingsRequestObjectWithDefaults() *UpdateUserSettingsRequestObject`

NewUpdateUserSettingsRequestObjectWithDefaults instantiates a new UpdateUserSettingsRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShowDebitsAsNegative

`func (o *UpdateUserSettingsRequestObject) GetShowDebitsAsNegative() bool`

GetShowDebitsAsNegative returns the ShowDebitsAsNegative field if non-nil, zero value otherwise.

### GetShowDebitsAsNegativeOk

`func (o *UpdateUserSettingsRequestObject) GetShowDebitsAsNegativeOk() (*bool, bool)`

GetShowDebitsAsNegativeOk returns a tuple with the ShowDebitsAsNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowDebitsAsNegative

`func (o *UpdateUserSettingsRequestObject) SetShowDebitsAsNegative(v bool)`

SetShowDebitsAsNegative sets ShowDebitsAsNegative field to given value.

### HasShowDebitsAsNegative

`func (o *UpdateUserSettingsRequestObject) HasShowDebitsAsNegative() bool`

HasShowDebitsAsNegative returns a boolean if a field has been set.

### GetAutoSuggestPayee

`func (o *UpdateUserSettingsRequestObject) GetAutoSuggestPayee() bool`

GetAutoSuggestPayee returns the AutoSuggestPayee field if non-nil, zero value otherwise.

### GetAutoSuggestPayeeOk

`func (o *UpdateUserSettingsRequestObject) GetAutoSuggestPayeeOk() (*bool, bool)`

GetAutoSuggestPayeeOk returns a tuple with the AutoSuggestPayee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoSuggestPayee

`func (o *UpdateUserSettingsRequestObject) SetAutoSuggestPayee(v bool)`

SetAutoSuggestPayee sets AutoSuggestPayee field to given value.

### HasAutoSuggestPayee

`func (o *UpdateUserSettingsRequestObject) HasAutoSuggestPayee() bool`

HasAutoSuggestPayee returns a boolean if a field has been set.

### GetMonthYearFormat

`func (o *UpdateUserSettingsRequestObject) GetMonthYearFormat() MonthYearFormatEnum`

GetMonthYearFormat returns the MonthYearFormat field if non-nil, zero value otherwise.

### GetMonthYearFormatOk

`func (o *UpdateUserSettingsRequestObject) GetMonthYearFormatOk() (*MonthYearFormatEnum, bool)`

GetMonthYearFormatOk returns a tuple with the MonthYearFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthYearFormat

`func (o *UpdateUserSettingsRequestObject) SetMonthYearFormat(v MonthYearFormatEnum)`

SetMonthYearFormat sets MonthYearFormat field to given value.

### HasMonthYearFormat

`func (o *UpdateUserSettingsRequestObject) HasMonthYearFormat() bool`

HasMonthYearFormat returns a boolean if a field has been set.

### GetMonthDayYearFormat

`func (o *UpdateUserSettingsRequestObject) GetMonthDayYearFormat() MonthDayYearFormatEnum`

GetMonthDayYearFormat returns the MonthDayYearFormat field if non-nil, zero value otherwise.

### GetMonthDayYearFormatOk

`func (o *UpdateUserSettingsRequestObject) GetMonthDayYearFormatOk() (*MonthDayYearFormatEnum, bool)`

GetMonthDayYearFormatOk returns a tuple with the MonthDayYearFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthDayYearFormat

`func (o *UpdateUserSettingsRequestObject) SetMonthDayYearFormat(v MonthDayYearFormatEnum)`

SetMonthDayYearFormat sets MonthDayYearFormat field to given value.

### HasMonthDayYearFormat

`func (o *UpdateUserSettingsRequestObject) HasMonthDayYearFormat() bool`

HasMonthDayYearFormat returns a boolean if a field has been set.

### GetMonthDayFormat

`func (o *UpdateUserSettingsRequestObject) GetMonthDayFormat() MonthDayFormatEnum`

GetMonthDayFormat returns the MonthDayFormat field if non-nil, zero value otherwise.

### GetMonthDayFormatOk

`func (o *UpdateUserSettingsRequestObject) GetMonthDayFormatOk() (*MonthDayFormatEnum, bool)`

GetMonthDayFormatOk returns a tuple with the MonthDayFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthDayFormat

`func (o *UpdateUserSettingsRequestObject) SetMonthDayFormat(v MonthDayFormatEnum)`

SetMonthDayFormat sets MonthDayFormat field to given value.

### HasMonthDayFormat

`func (o *UpdateUserSettingsRequestObject) HasMonthDayFormat() bool`

HasMonthDayFormat returns a boolean if a field has been set.

### GetShowAmPm

`func (o *UpdateUserSettingsRequestObject) GetShowAmPm() bool`

GetShowAmPm returns the ShowAmPm field if non-nil, zero value otherwise.

### GetShowAmPmOk

`func (o *UpdateUserSettingsRequestObject) GetShowAmPmOk() (*bool, bool)`

GetShowAmPmOk returns a tuple with the ShowAmPm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowAmPm

`func (o *UpdateUserSettingsRequestObject) SetShowAmPm(v bool)`

SetShowAmPm sets ShowAmPm field to given value.

### HasShowAmPm

`func (o *UpdateUserSettingsRequestObject) HasShowAmPm() bool`

HasShowAmPm returns a boolean if a field has been set.

### GetWeekStartsOn

`func (o *UpdateUserSettingsRequestObject) GetWeekStartsOn() WeekStartsOnEnum`

GetWeekStartsOn returns the WeekStartsOn field if non-nil, zero value otherwise.

### GetWeekStartsOnOk

`func (o *UpdateUserSettingsRequestObject) GetWeekStartsOnOk() (*WeekStartsOnEnum, bool)`

GetWeekStartsOnOk returns a tuple with the WeekStartsOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeekStartsOn

`func (o *UpdateUserSettingsRequestObject) SetWeekStartsOn(v WeekStartsOnEnum)`

SetWeekStartsOn sets WeekStartsOn field to given value.

### HasWeekStartsOn

`func (o *UpdateUserSettingsRequestObject) HasWeekStartsOn() bool`

HasWeekStartsOn returns a boolean if a field has been set.

### GetAlwaysDisplayYear

`func (o *UpdateUserSettingsRequestObject) GetAlwaysDisplayYear() bool`

GetAlwaysDisplayYear returns the AlwaysDisplayYear field if non-nil, zero value otherwise.

### GetAlwaysDisplayYearOk

`func (o *UpdateUserSettingsRequestObject) GetAlwaysDisplayYearOk() (*bool, bool)`

GetAlwaysDisplayYearOk returns a tuple with the AlwaysDisplayYear field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysDisplayYear

`func (o *UpdateUserSettingsRequestObject) SetAlwaysDisplayYear(v bool)`

SetAlwaysDisplayYear sets AlwaysDisplayYear field to given value.

### HasAlwaysDisplayYear

`func (o *UpdateUserSettingsRequestObject) HasAlwaysDisplayYear() bool`

HasAlwaysDisplayYear returns a boolean if a field has been set.

### GetAlwaysDisplayWeekday

`func (o *UpdateUserSettingsRequestObject) GetAlwaysDisplayWeekday() bool`

GetAlwaysDisplayWeekday returns the AlwaysDisplayWeekday field if non-nil, zero value otherwise.

### GetAlwaysDisplayWeekdayOk

`func (o *UpdateUserSettingsRequestObject) GetAlwaysDisplayWeekdayOk() (*bool, bool)`

GetAlwaysDisplayWeekdayOk returns a tuple with the AlwaysDisplayWeekday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysDisplayWeekday

`func (o *UpdateUserSettingsRequestObject) SetAlwaysDisplayWeekday(v bool)`

SetAlwaysDisplayWeekday sets AlwaysDisplayWeekday field to given value.

### HasAlwaysDisplayWeekday

`func (o *UpdateUserSettingsRequestObject) HasAlwaysDisplayWeekday() bool`

HasAlwaysDisplayWeekday returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


