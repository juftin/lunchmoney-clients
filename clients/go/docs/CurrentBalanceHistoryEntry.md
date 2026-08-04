# CurrentBalanceHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as an ephemeral current-month snapshot. | 
**Month** | **string** | Calendar month for this entry in YYYY-MM format. For current entries this is the current month. | 
**Balance** | **string** | Calculated balance for the current month, as a numeric string with up to four decimal places. Trailing zeros and decimal places are not guaranteed in responses. For manual and Plaid accounts this is in the account currency. For crypto accounts this is in the user&#39;s primary currency. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the calculated &#x60;balance&#x60;. For crypto entries this is the user&#39;s primary currency. | 
**ToBase** | **float64** | Calculated balance converted to the user&#39;s primary currency. When the entry currency is the user&#39;s primary currency, this is the numeric value of &#x60;balance&#x60;. | 
**CryptoBalance** | **NullableString** | Crypto quantity for this calculated entry, when available. This may be present for crypto entries and is &#x60;null&#x60; otherwise. | 

## Methods

### NewCurrentBalanceHistoryEntry

`func NewCurrentBalanceHistoryEntry(type_ string, month string, balance string, currency CurrencyEnum, toBase float64, cryptoBalance NullableString, ) *CurrentBalanceHistoryEntry`

NewCurrentBalanceHistoryEntry instantiates a new CurrentBalanceHistoryEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCurrentBalanceHistoryEntryWithDefaults

`func NewCurrentBalanceHistoryEntryWithDefaults() *CurrentBalanceHistoryEntry`

NewCurrentBalanceHistoryEntryWithDefaults instantiates a new CurrentBalanceHistoryEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *CurrentBalanceHistoryEntry) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CurrentBalanceHistoryEntry) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CurrentBalanceHistoryEntry) SetType(v string)`

SetType sets Type field to given value.


### GetMonth

`func (o *CurrentBalanceHistoryEntry) GetMonth() string`

GetMonth returns the Month field if non-nil, zero value otherwise.

### GetMonthOk

`func (o *CurrentBalanceHistoryEntry) GetMonthOk() (*string, bool)`

GetMonthOk returns a tuple with the Month field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonth

`func (o *CurrentBalanceHistoryEntry) SetMonth(v string)`

SetMonth sets Month field to given value.


### GetBalance

`func (o *CurrentBalanceHistoryEntry) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *CurrentBalanceHistoryEntry) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *CurrentBalanceHistoryEntry) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetCurrency

`func (o *CurrentBalanceHistoryEntry) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *CurrentBalanceHistoryEntry) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *CurrentBalanceHistoryEntry) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *CurrentBalanceHistoryEntry) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *CurrentBalanceHistoryEntry) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *CurrentBalanceHistoryEntry) SetToBase(v float64)`

SetToBase sets ToBase field to given value.


### GetCryptoBalance

`func (o *CurrentBalanceHistoryEntry) GetCryptoBalance() string`

GetCryptoBalance returns the CryptoBalance field if non-nil, zero value otherwise.

### GetCryptoBalanceOk

`func (o *CurrentBalanceHistoryEntry) GetCryptoBalanceOk() (*string, bool)`

GetCryptoBalanceOk returns a tuple with the CryptoBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoBalance

`func (o *CurrentBalanceHistoryEntry) SetCryptoBalance(v string)`

SetCryptoBalance sets CryptoBalance field to given value.


### SetCryptoBalanceNil

`func (o *CurrentBalanceHistoryEntry) SetCryptoBalanceNil(b bool)`

 SetCryptoBalanceNil sets the value for CryptoBalance to be an explicit nil

### UnsetCryptoBalance
`func (o *CurrentBalanceHistoryEntry) UnsetCryptoBalance()`

UnsetCryptoBalance ensures that no value is present for CryptoBalance, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


