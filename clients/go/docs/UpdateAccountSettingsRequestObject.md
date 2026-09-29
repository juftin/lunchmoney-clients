# UpdateAccountSettingsRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PrimaryCurrency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | If set, updates the account&#39;s primary currency. | [optional] 
**SupportedCurrencies** | Pointer to [**[]CurrencyEnum**](CurrencyEnum.md) | If set, replaces the list of supported currencies for the account. | [optional] 
**DisplayName** | Pointer to **NullableString** | If set, updates the display name of the budgeting account. | [optional] 
**Locale** | Pointer to [**LocaleEnum**](LocaleEnum.md) | If set, updates the locale used for formatting numbers and currency amounts in the Lunch Money app. See [Supported Locales](https://lunchmoney.dev/v2/locales) for accepted values. Date presentation is configured separately through [GET /me/user/settings](#tag/me/GET/me/user/settings) and [PUT /me/user/settings](#tag/me/PUT/me/user/settings). | [optional] 
**AutoCreateCategoryRules** | Pointer to **bool** | If set, updates whether category rules are created automatically. | [optional] 
**AutoCreateSuggestedTransactionRules** | Pointer to **bool** | If set, updates whether suggested transaction rules are created automatically. | [optional] 
**IncludePendingInTotals** | Pointer to **bool** | If set, updates whether pending transactions are included in account totals. | [optional] 

## Methods

### NewUpdateAccountSettingsRequestObject

`func NewUpdateAccountSettingsRequestObject() *UpdateAccountSettingsRequestObject`

NewUpdateAccountSettingsRequestObject instantiates a new UpdateAccountSettingsRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateAccountSettingsRequestObjectWithDefaults

`func NewUpdateAccountSettingsRequestObjectWithDefaults() *UpdateAccountSettingsRequestObject`

NewUpdateAccountSettingsRequestObjectWithDefaults instantiates a new UpdateAccountSettingsRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrimaryCurrency

`func (o *UpdateAccountSettingsRequestObject) GetPrimaryCurrency() CurrencyEnum`

GetPrimaryCurrency returns the PrimaryCurrency field if non-nil, zero value otherwise.

### GetPrimaryCurrencyOk

`func (o *UpdateAccountSettingsRequestObject) GetPrimaryCurrencyOk() (*CurrencyEnum, bool)`

GetPrimaryCurrencyOk returns a tuple with the PrimaryCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryCurrency

`func (o *UpdateAccountSettingsRequestObject) SetPrimaryCurrency(v CurrencyEnum)`

SetPrimaryCurrency sets PrimaryCurrency field to given value.

### HasPrimaryCurrency

`func (o *UpdateAccountSettingsRequestObject) HasPrimaryCurrency() bool`

HasPrimaryCurrency returns a boolean if a field has been set.

### GetSupportedCurrencies

`func (o *UpdateAccountSettingsRequestObject) GetSupportedCurrencies() []CurrencyEnum`

GetSupportedCurrencies returns the SupportedCurrencies field if non-nil, zero value otherwise.

### GetSupportedCurrenciesOk

`func (o *UpdateAccountSettingsRequestObject) GetSupportedCurrenciesOk() (*[]CurrencyEnum, bool)`

GetSupportedCurrenciesOk returns a tuple with the SupportedCurrencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSupportedCurrencies

`func (o *UpdateAccountSettingsRequestObject) SetSupportedCurrencies(v []CurrencyEnum)`

SetSupportedCurrencies sets SupportedCurrencies field to given value.

### HasSupportedCurrencies

`func (o *UpdateAccountSettingsRequestObject) HasSupportedCurrencies() bool`

HasSupportedCurrencies returns a boolean if a field has been set.

### GetDisplayName

`func (o *UpdateAccountSettingsRequestObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *UpdateAccountSettingsRequestObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *UpdateAccountSettingsRequestObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *UpdateAccountSettingsRequestObject) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### SetDisplayNameNil

`func (o *UpdateAccountSettingsRequestObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *UpdateAccountSettingsRequestObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetLocale

`func (o *UpdateAccountSettingsRequestObject) GetLocale() LocaleEnum`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *UpdateAccountSettingsRequestObject) GetLocaleOk() (*LocaleEnum, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocale

`func (o *UpdateAccountSettingsRequestObject) SetLocale(v LocaleEnum)`

SetLocale sets Locale field to given value.

### HasLocale

`func (o *UpdateAccountSettingsRequestObject) HasLocale() bool`

HasLocale returns a boolean if a field has been set.

### GetAutoCreateCategoryRules

`func (o *UpdateAccountSettingsRequestObject) GetAutoCreateCategoryRules() bool`

GetAutoCreateCategoryRules returns the AutoCreateCategoryRules field if non-nil, zero value otherwise.

### GetAutoCreateCategoryRulesOk

`func (o *UpdateAccountSettingsRequestObject) GetAutoCreateCategoryRulesOk() (*bool, bool)`

GetAutoCreateCategoryRulesOk returns a tuple with the AutoCreateCategoryRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoCreateCategoryRules

`func (o *UpdateAccountSettingsRequestObject) SetAutoCreateCategoryRules(v bool)`

SetAutoCreateCategoryRules sets AutoCreateCategoryRules field to given value.

### HasAutoCreateCategoryRules

`func (o *UpdateAccountSettingsRequestObject) HasAutoCreateCategoryRules() bool`

HasAutoCreateCategoryRules returns a boolean if a field has been set.

### GetAutoCreateSuggestedTransactionRules

`func (o *UpdateAccountSettingsRequestObject) GetAutoCreateSuggestedTransactionRules() bool`

GetAutoCreateSuggestedTransactionRules returns the AutoCreateSuggestedTransactionRules field if non-nil, zero value otherwise.

### GetAutoCreateSuggestedTransactionRulesOk

`func (o *UpdateAccountSettingsRequestObject) GetAutoCreateSuggestedTransactionRulesOk() (*bool, bool)`

GetAutoCreateSuggestedTransactionRulesOk returns a tuple with the AutoCreateSuggestedTransactionRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoCreateSuggestedTransactionRules

`func (o *UpdateAccountSettingsRequestObject) SetAutoCreateSuggestedTransactionRules(v bool)`

SetAutoCreateSuggestedTransactionRules sets AutoCreateSuggestedTransactionRules field to given value.

### HasAutoCreateSuggestedTransactionRules

`func (o *UpdateAccountSettingsRequestObject) HasAutoCreateSuggestedTransactionRules() bool`

HasAutoCreateSuggestedTransactionRules returns a boolean if a field has been set.

### GetIncludePendingInTotals

`func (o *UpdateAccountSettingsRequestObject) GetIncludePendingInTotals() bool`

GetIncludePendingInTotals returns the IncludePendingInTotals field if non-nil, zero value otherwise.

### GetIncludePendingInTotalsOk

`func (o *UpdateAccountSettingsRequestObject) GetIncludePendingInTotalsOk() (*bool, bool)`

GetIncludePendingInTotalsOk returns a tuple with the IncludePendingInTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludePendingInTotals

`func (o *UpdateAccountSettingsRequestObject) SetIncludePendingInTotals(v bool)`

SetIncludePendingInTotals sets IncludePendingInTotals field to given value.

### HasIncludePendingInTotals

`func (o *UpdateAccountSettingsRequestObject) HasIncludePendingInTotals() bool`

HasIncludePendingInTotals returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


