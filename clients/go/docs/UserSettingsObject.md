# UserSettingsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShowDebitsAsNegative** | **bool** | Display preference for how amounts are shown in the Lunch Money app. When &#x60;true&#x60;, debits are shown as negative values and credits as positive values.&lt;p&gt; This setting does **not** change amount sign conventions in API responses. Amount fields such as &#x60;amount&#x60; and &#x60;to_base&#x60; on transaction objects always use positive values for debits and negative values for credits. | [default to true]
**AutoSuggestPayee** | **bool** | If &#x60;true&#x60;, payee suggestions are shown when entering transactions in the Lunch Money app. | [default to true]
**MonthYearFormat** | [**MonthYearFormatEnum**](MonthYearFormatEnum.md) | Format string used when displaying month and year values. | [default to MMM_YYYY]
**MonthDayYearFormat** | [**MonthDayYearFormatEnum**](MonthDayYearFormatEnum.md) | Format string used when displaying full dates (month, day, and year). | [default to MMM_D_YYYY]
**MonthDayFormat** | [**MonthDayFormatEnum**](MonthDayFormatEnum.md) | Format string used when displaying month and day values without a year. | [default to MMM_D]
**ShowAmPm** | **bool** | If &#x60;true&#x60;, times are displayed using a 12-hour clock with AM/PM. If &#x60;false&#x60;, times are displayed using a 24-hour clock. | [default to true]
**WeekStartsOn** | [**WeekStartsOnEnum**](WeekStartsOnEnum.md) | The day on which a calendar week begins. | [default to SUNDAY]
**AlwaysDisplayYear** | **bool** | If &#x60;true&#x60;, dates always include the year and &#x60;month_day_format&#x60; is not used. | [default to false]
**AlwaysDisplayWeekday** | **bool** | If &#x60;true&#x60;, weekday names are included when displaying dates. | [default to true]

## Methods

### NewUserSettingsObject

`func NewUserSettingsObject(showDebitsAsNegative bool, autoSuggestPayee bool, monthYearFormat MonthYearFormatEnum, monthDayYearFormat MonthDayYearFormatEnum, monthDayFormat MonthDayFormatEnum, showAmPm bool, weekStartsOn WeekStartsOnEnum, alwaysDisplayYear bool, alwaysDisplayWeekday bool, ) *UserSettingsObject`

NewUserSettingsObject instantiates a new UserSettingsObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserSettingsObjectWithDefaults

`func NewUserSettingsObjectWithDefaults() *UserSettingsObject`

NewUserSettingsObjectWithDefaults instantiates a new UserSettingsObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShowDebitsAsNegative

`func (o *UserSettingsObject) GetShowDebitsAsNegative() bool`

GetShowDebitsAsNegative returns the ShowDebitsAsNegative field if non-nil, zero value otherwise.

### GetShowDebitsAsNegativeOk

`func (o *UserSettingsObject) GetShowDebitsAsNegativeOk() (*bool, bool)`

GetShowDebitsAsNegativeOk returns a tuple with the ShowDebitsAsNegative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowDebitsAsNegative

`func (o *UserSettingsObject) SetShowDebitsAsNegative(v bool)`

SetShowDebitsAsNegative sets ShowDebitsAsNegative field to given value.


### GetAutoSuggestPayee

`func (o *UserSettingsObject) GetAutoSuggestPayee() bool`

GetAutoSuggestPayee returns the AutoSuggestPayee field if non-nil, zero value otherwise.

### GetAutoSuggestPayeeOk

`func (o *UserSettingsObject) GetAutoSuggestPayeeOk() (*bool, bool)`

GetAutoSuggestPayeeOk returns a tuple with the AutoSuggestPayee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoSuggestPayee

`func (o *UserSettingsObject) SetAutoSuggestPayee(v bool)`

SetAutoSuggestPayee sets AutoSuggestPayee field to given value.


### GetMonthYearFormat

`func (o *UserSettingsObject) GetMonthYearFormat() MonthYearFormatEnum`

GetMonthYearFormat returns the MonthYearFormat field if non-nil, zero value otherwise.

### GetMonthYearFormatOk

`func (o *UserSettingsObject) GetMonthYearFormatOk() (*MonthYearFormatEnum, bool)`

GetMonthYearFormatOk returns a tuple with the MonthYearFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthYearFormat

`func (o *UserSettingsObject) SetMonthYearFormat(v MonthYearFormatEnum)`

SetMonthYearFormat sets MonthYearFormat field to given value.


### GetMonthDayYearFormat

`func (o *UserSettingsObject) GetMonthDayYearFormat() MonthDayYearFormatEnum`

GetMonthDayYearFormat returns the MonthDayYearFormat field if non-nil, zero value otherwise.

### GetMonthDayYearFormatOk

`func (o *UserSettingsObject) GetMonthDayYearFormatOk() (*MonthDayYearFormatEnum, bool)`

GetMonthDayYearFormatOk returns a tuple with the MonthDayYearFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthDayYearFormat

`func (o *UserSettingsObject) SetMonthDayYearFormat(v MonthDayYearFormatEnum)`

SetMonthDayYearFormat sets MonthDayYearFormat field to given value.


### GetMonthDayFormat

`func (o *UserSettingsObject) GetMonthDayFormat() MonthDayFormatEnum`

GetMonthDayFormat returns the MonthDayFormat field if non-nil, zero value otherwise.

### GetMonthDayFormatOk

`func (o *UserSettingsObject) GetMonthDayFormatOk() (*MonthDayFormatEnum, bool)`

GetMonthDayFormatOk returns a tuple with the MonthDayFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthDayFormat

`func (o *UserSettingsObject) SetMonthDayFormat(v MonthDayFormatEnum)`

SetMonthDayFormat sets MonthDayFormat field to given value.


### GetShowAmPm

`func (o *UserSettingsObject) GetShowAmPm() bool`

GetShowAmPm returns the ShowAmPm field if non-nil, zero value otherwise.

### GetShowAmPmOk

`func (o *UserSettingsObject) GetShowAmPmOk() (*bool, bool)`

GetShowAmPmOk returns a tuple with the ShowAmPm field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShowAmPm

`func (o *UserSettingsObject) SetShowAmPm(v bool)`

SetShowAmPm sets ShowAmPm field to given value.


### GetWeekStartsOn

`func (o *UserSettingsObject) GetWeekStartsOn() WeekStartsOnEnum`

GetWeekStartsOn returns the WeekStartsOn field if non-nil, zero value otherwise.

### GetWeekStartsOnOk

`func (o *UserSettingsObject) GetWeekStartsOnOk() (*WeekStartsOnEnum, bool)`

GetWeekStartsOnOk returns a tuple with the WeekStartsOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeekStartsOn

`func (o *UserSettingsObject) SetWeekStartsOn(v WeekStartsOnEnum)`

SetWeekStartsOn sets WeekStartsOn field to given value.


### GetAlwaysDisplayYear

`func (o *UserSettingsObject) GetAlwaysDisplayYear() bool`

GetAlwaysDisplayYear returns the AlwaysDisplayYear field if non-nil, zero value otherwise.

### GetAlwaysDisplayYearOk

`func (o *UserSettingsObject) GetAlwaysDisplayYearOk() (*bool, bool)`

GetAlwaysDisplayYearOk returns a tuple with the AlwaysDisplayYear field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysDisplayYear

`func (o *UserSettingsObject) SetAlwaysDisplayYear(v bool)`

SetAlwaysDisplayYear sets AlwaysDisplayYear field to given value.


### GetAlwaysDisplayWeekday

`func (o *UserSettingsObject) GetAlwaysDisplayWeekday() bool`

GetAlwaysDisplayWeekday returns the AlwaysDisplayWeekday field if non-nil, zero value otherwise.

### GetAlwaysDisplayWeekdayOk

`func (o *UserSettingsObject) GetAlwaysDisplayWeekdayOk() (*bool, bool)`

GetAlwaysDisplayWeekdayOk returns a tuple with the AlwaysDisplayWeekday field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlwaysDisplayWeekday

`func (o *UserSettingsObject) SetAlwaysDisplayWeekday(v bool)`

SetAlwaysDisplayWeekday sets AlwaysDisplayWeekday field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


