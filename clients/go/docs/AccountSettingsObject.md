# AccountSettingsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PrimaryCurrency** | [**CurrencyEnum**](CurrencyEnum.md) | Primary currency for the account. | 
**SupportedCurrencies** | [**[]CurrencyEnum**](CurrencyEnum.md) | Currencies available when creating or editing transactions, balances, and other amounts in the Lunch Money app. | 
**DisplayName** | **NullableString** | Display name of the budgeting account in the Lunch Money app. | 
**Locale** | [**LocaleEnum**](LocaleEnum.md) | Locale used for formatting numbers and currency amounts in the Lunch Money app (for example, &#x60;en-US&#x60;). See [Supported Locales](https://lunchmoney.dev/v2/locales) for accepted values. Date presentation is configured separately through [GET /me/user/settings](#tag/me/GET/me/user/settings) and [PUT /me/user/settings](#tag/me/PUT/me/user/settings). When no locale is explicitly stored for the account, the effective locale is derived from the &#x60;default_locale&#x60; associated with &#x60;primary_currency&#x60; in the currencies table (for example, &#x60;usd&#x60; → &#x60;en-US&#x60;, &#x60;cad&#x60; → &#x60;en-CA&#x60;, &#x60;gbp&#x60; → &#x60;en-GB&#x60;). | 
**AutoCreateCategoryRules** | **bool** | If &#x60;true&#x60;, category rules are created automatically when categorizing transactions. | [default to true]
**AutoCreateSuggestedTransactionRules** | **bool** | If &#x60;true&#x60;, suggested transaction rules are created automatically. | [default to true]
**IncludePendingInTotals** | **bool** | If &#x60;true&#x60;, pending transactions are included in account totals. | [default to true]

## Methods

### NewAccountSettingsObject

`func NewAccountSettingsObject(primaryCurrency CurrencyEnum, supportedCurrencies []CurrencyEnum, displayName NullableString, locale LocaleEnum, autoCreateCategoryRules bool, autoCreateSuggestedTransactionRules bool, includePendingInTotals bool, ) *AccountSettingsObject`

NewAccountSettingsObject instantiates a new AccountSettingsObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountSettingsObjectWithDefaults

`func NewAccountSettingsObjectWithDefaults() *AccountSettingsObject`

NewAccountSettingsObjectWithDefaults instantiates a new AccountSettingsObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrimaryCurrency

`func (o *AccountSettingsObject) GetPrimaryCurrency() CurrencyEnum`

GetPrimaryCurrency returns the PrimaryCurrency field if non-nil, zero value otherwise.

### GetPrimaryCurrencyOk

`func (o *AccountSettingsObject) GetPrimaryCurrencyOk() (*CurrencyEnum, bool)`

GetPrimaryCurrencyOk returns a tuple with the PrimaryCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryCurrency

`func (o *AccountSettingsObject) SetPrimaryCurrency(v CurrencyEnum)`

SetPrimaryCurrency sets PrimaryCurrency field to given value.


### GetSupportedCurrencies

`func (o *AccountSettingsObject) GetSupportedCurrencies() []CurrencyEnum`

GetSupportedCurrencies returns the SupportedCurrencies field if non-nil, zero value otherwise.

### GetSupportedCurrenciesOk

`func (o *AccountSettingsObject) GetSupportedCurrenciesOk() (*[]CurrencyEnum, bool)`

GetSupportedCurrenciesOk returns a tuple with the SupportedCurrencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSupportedCurrencies

`func (o *AccountSettingsObject) SetSupportedCurrencies(v []CurrencyEnum)`

SetSupportedCurrencies sets SupportedCurrencies field to given value.


### GetDisplayName

`func (o *AccountSettingsObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *AccountSettingsObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *AccountSettingsObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *AccountSettingsObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *AccountSettingsObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetLocale

`func (o *AccountSettingsObject) GetLocale() LocaleEnum`

GetLocale returns the Locale field if non-nil, zero value otherwise.

### GetLocaleOk

`func (o *AccountSettingsObject) GetLocaleOk() (*LocaleEnum, bool)`

GetLocaleOk returns a tuple with the Locale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocale

`func (o *AccountSettingsObject) SetLocale(v LocaleEnum)`

SetLocale sets Locale field to given value.


### GetAutoCreateCategoryRules

`func (o *AccountSettingsObject) GetAutoCreateCategoryRules() bool`

GetAutoCreateCategoryRules returns the AutoCreateCategoryRules field if non-nil, zero value otherwise.

### GetAutoCreateCategoryRulesOk

`func (o *AccountSettingsObject) GetAutoCreateCategoryRulesOk() (*bool, bool)`

GetAutoCreateCategoryRulesOk returns a tuple with the AutoCreateCategoryRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoCreateCategoryRules

`func (o *AccountSettingsObject) SetAutoCreateCategoryRules(v bool)`

SetAutoCreateCategoryRules sets AutoCreateCategoryRules field to given value.


### GetAutoCreateSuggestedTransactionRules

`func (o *AccountSettingsObject) GetAutoCreateSuggestedTransactionRules() bool`

GetAutoCreateSuggestedTransactionRules returns the AutoCreateSuggestedTransactionRules field if non-nil, zero value otherwise.

### GetAutoCreateSuggestedTransactionRulesOk

`func (o *AccountSettingsObject) GetAutoCreateSuggestedTransactionRulesOk() (*bool, bool)`

GetAutoCreateSuggestedTransactionRulesOk returns a tuple with the AutoCreateSuggestedTransactionRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoCreateSuggestedTransactionRules

`func (o *AccountSettingsObject) SetAutoCreateSuggestedTransactionRules(v bool)`

SetAutoCreateSuggestedTransactionRules sets AutoCreateSuggestedTransactionRules field to given value.


### GetIncludePendingInTotals

`func (o *AccountSettingsObject) GetIncludePendingInTotals() bool`

GetIncludePendingInTotals returns the IncludePendingInTotals field if non-nil, zero value otherwise.

### GetIncludePendingInTotalsOk

`func (o *AccountSettingsObject) GetIncludePendingInTotalsOk() (*bool, bool)`

GetIncludePendingInTotalsOk returns a tuple with the IncludePendingInTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludePendingInTotals

`func (o *AccountSettingsObject) SetIncludePendingInTotals(v bool)`

SetIncludePendingInTotals sets IncludePendingInTotals field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


