# HistoricalBalanceHistoryEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as a stored snapshot of a past month. | 
**Id** | **int32** | Unique identifier for this historical balance entry. | 
**Month** | **string** | Calendar month for this entry in YYYY-MM format. | 
**Balance** | **string** | Historical balance for this entry, as a numeric string with up to four decimal places. Trailing zeros and decimal places are not guaranteed in responses. For manual and Plaid accounts this is in the account currency. For crypto accounts this is in the user&#39;s primary currency. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of &#x60;balance&#x60;. For crypto entries this is the user&#39;s primary currency. | 
**ToBase** | **float64** | Historical balance converted to the user&#39;s primary currency. When the entry currency is the user&#39;s primary currency, this is the numeric value of &#x60;balance&#x60;. | 
**CryptoBalance** | **NullableString** | Crypto quantity for this balance entry, when available. This may be present for crypto or deleted-account entries and is &#x60;null&#x60; otherwise. | 

## Methods

### NewHistoricalBalanceHistoryEntry

`func NewHistoricalBalanceHistoryEntry(type_ string, id int32, month string, balance string, currency CurrencyEnum, toBase float64, cryptoBalance NullableString, ) *HistoricalBalanceHistoryEntry`

NewHistoricalBalanceHistoryEntry instantiates a new HistoricalBalanceHistoryEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHistoricalBalanceHistoryEntryWithDefaults

`func NewHistoricalBalanceHistoryEntryWithDefaults() *HistoricalBalanceHistoryEntry`

NewHistoricalBalanceHistoryEntryWithDefaults instantiates a new HistoricalBalanceHistoryEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *HistoricalBalanceHistoryEntry) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *HistoricalBalanceHistoryEntry) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *HistoricalBalanceHistoryEntry) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *HistoricalBalanceHistoryEntry) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *HistoricalBalanceHistoryEntry) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *HistoricalBalanceHistoryEntry) SetId(v int32)`

SetId sets Id field to given value.


### GetMonth

`func (o *HistoricalBalanceHistoryEntry) GetMonth() string`

GetMonth returns the Month field if non-nil, zero value otherwise.

### GetMonthOk

`func (o *HistoricalBalanceHistoryEntry) GetMonthOk() (*string, bool)`

GetMonthOk returns a tuple with the Month field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonth

`func (o *HistoricalBalanceHistoryEntry) SetMonth(v string)`

SetMonth sets Month field to given value.


### GetBalance

`func (o *HistoricalBalanceHistoryEntry) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *HistoricalBalanceHistoryEntry) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *HistoricalBalanceHistoryEntry) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetCurrency

`func (o *HistoricalBalanceHistoryEntry) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *HistoricalBalanceHistoryEntry) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *HistoricalBalanceHistoryEntry) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *HistoricalBalanceHistoryEntry) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *HistoricalBalanceHistoryEntry) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *HistoricalBalanceHistoryEntry) SetToBase(v float64)`

SetToBase sets ToBase field to given value.


### GetCryptoBalance

`func (o *HistoricalBalanceHistoryEntry) GetCryptoBalance() string`

GetCryptoBalance returns the CryptoBalance field if non-nil, zero value otherwise.

### GetCryptoBalanceOk

`func (o *HistoricalBalanceHistoryEntry) GetCryptoBalanceOk() (*string, bool)`

GetCryptoBalanceOk returns a tuple with the CryptoBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoBalance

`func (o *HistoricalBalanceHistoryEntry) SetCryptoBalance(v string)`

SetCryptoBalance sets CryptoBalance field to given value.


### SetCryptoBalanceNil

`func (o *HistoricalBalanceHistoryEntry) SetCryptoBalanceNil(b bool)`

 SetCryptoBalanceNil sets the value for CryptoBalance to be an explicit nil

### UnsetCryptoBalance
`func (o *HistoricalBalanceHistoryEntry) UnsetCryptoBalance()`

UnsetCryptoBalance ensures that no value is present for CryptoBalance, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


