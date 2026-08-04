# CryptoSyncedBalance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | The asset name for this balance, typically the uppercased currency symbol (e.g. ETH). | 
**DisplayName** | **NullableString** | Optional display name for the synced crypto asset as set by the user. If &#x60;null&#x60;, clients may derive a display name from syncedCryptoAccount&#39;s &#x60;provider&#x60; + &#x60;name&#x60;. | 
**Balance** | **string** | Current balance in numeric format to 18 decimal places | 
**Symbol** | **string** | Symbol of the currency held in the synced account | 
**CoingeckoId** | **NullableString** | CoinGecko identifier associated with this balance | 
**ToBase** | **NullableFloat32** | Balance converted to the user&#39;s primary currency. May be null if no conversion was available. | 
**BalanceAsOf** | **NullableTime** | Date/time the balance was last updated in ISO 8601 extended format. | 
**ExchangeRateAsOf** | **NullableTime** | Date/time the exchange rate used to calculate to_base was last updated in ISO 8601 extended format. Null when no exchange rate was used or no conversion was available. | 
**UpdatedAt** | **time.Time** | Date/time the crypto asset was last updated in ISO 8601 extended format | 

## Methods

### NewCryptoSyncedBalance

`func NewCryptoSyncedBalance(name string, displayName NullableString, balance string, symbol string, coingeckoId NullableString, toBase NullableFloat32, balanceAsOf NullableTime, exchangeRateAsOf NullableTime, updatedAt time.Time, ) *CryptoSyncedBalance`

NewCryptoSyncedBalance instantiates a new CryptoSyncedBalance object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCryptoSyncedBalanceWithDefaults

`func NewCryptoSyncedBalanceWithDefaults() *CryptoSyncedBalance`

NewCryptoSyncedBalanceWithDefaults instantiates a new CryptoSyncedBalance object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CryptoSyncedBalance) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CryptoSyncedBalance) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CryptoSyncedBalance) SetName(v string)`

SetName sets Name field to given value.


### GetDisplayName

`func (o *CryptoSyncedBalance) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *CryptoSyncedBalance) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *CryptoSyncedBalance) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *CryptoSyncedBalance) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *CryptoSyncedBalance) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetBalance

`func (o *CryptoSyncedBalance) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *CryptoSyncedBalance) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *CryptoSyncedBalance) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetSymbol

`func (o *CryptoSyncedBalance) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *CryptoSyncedBalance) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *CryptoSyncedBalance) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.


### GetCoingeckoId

`func (o *CryptoSyncedBalance) GetCoingeckoId() string`

GetCoingeckoId returns the CoingeckoId field if non-nil, zero value otherwise.

### GetCoingeckoIdOk

`func (o *CryptoSyncedBalance) GetCoingeckoIdOk() (*string, bool)`

GetCoingeckoIdOk returns a tuple with the CoingeckoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoingeckoId

`func (o *CryptoSyncedBalance) SetCoingeckoId(v string)`

SetCoingeckoId sets CoingeckoId field to given value.


### SetCoingeckoIdNil

`func (o *CryptoSyncedBalance) SetCoingeckoIdNil(b bool)`

 SetCoingeckoIdNil sets the value for CoingeckoId to be an explicit nil

### UnsetCoingeckoId
`func (o *CryptoSyncedBalance) UnsetCoingeckoId()`

UnsetCoingeckoId ensures that no value is present for CoingeckoId, not even an explicit nil
### GetToBase

`func (o *CryptoSyncedBalance) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *CryptoSyncedBalance) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *CryptoSyncedBalance) SetToBase(v float32)`

SetToBase sets ToBase field to given value.


### SetToBaseNil

`func (o *CryptoSyncedBalance) SetToBaseNil(b bool)`

 SetToBaseNil sets the value for ToBase to be an explicit nil

### UnsetToBase
`func (o *CryptoSyncedBalance) UnsetToBase()`

UnsetToBase ensures that no value is present for ToBase, not even an explicit nil
### GetBalanceAsOf

`func (o *CryptoSyncedBalance) GetBalanceAsOf() time.Time`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *CryptoSyncedBalance) GetBalanceAsOfOk() (*time.Time, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *CryptoSyncedBalance) SetBalanceAsOf(v time.Time)`

SetBalanceAsOf sets BalanceAsOf field to given value.


### SetBalanceAsOfNil

`func (o *CryptoSyncedBalance) SetBalanceAsOfNil(b bool)`

 SetBalanceAsOfNil sets the value for BalanceAsOf to be an explicit nil

### UnsetBalanceAsOf
`func (o *CryptoSyncedBalance) UnsetBalanceAsOf()`

UnsetBalanceAsOf ensures that no value is present for BalanceAsOf, not even an explicit nil
### GetExchangeRateAsOf

`func (o *CryptoSyncedBalance) GetExchangeRateAsOf() time.Time`

GetExchangeRateAsOf returns the ExchangeRateAsOf field if non-nil, zero value otherwise.

### GetExchangeRateAsOfOk

`func (o *CryptoSyncedBalance) GetExchangeRateAsOfOk() (*time.Time, bool)`

GetExchangeRateAsOfOk returns a tuple with the ExchangeRateAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExchangeRateAsOf

`func (o *CryptoSyncedBalance) SetExchangeRateAsOf(v time.Time)`

SetExchangeRateAsOf sets ExchangeRateAsOf field to given value.


### SetExchangeRateAsOfNil

`func (o *CryptoSyncedBalance) SetExchangeRateAsOfNil(b bool)`

 SetExchangeRateAsOfNil sets the value for ExchangeRateAsOf to be an explicit nil

### UnsetExchangeRateAsOf
`func (o *CryptoSyncedBalance) UnsetExchangeRateAsOf()`

UnsetExchangeRateAsOf ensures that no value is present for ExchangeRateAsOf, not even an explicit nil
### GetUpdatedAt

`func (o *CryptoSyncedBalance) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CryptoSyncedBalance) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CryptoSyncedBalance) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


