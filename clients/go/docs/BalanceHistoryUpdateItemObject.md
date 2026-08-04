# BalanceHistoryUpdateItemObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** | System-defined balance history entry id. Ignored if set. | [optional] 
**Month** | **string** | Calendar month to upsert, in YYYY-MM format. Must be a past month. The current month cannot be written through PUT endpoints.  | 
**Balance** | [**BalanceHistoryUpdateItemObjectBalance**](BalanceHistoryUpdateItemObjectBalance.md) |  | 
**Symbol** | Pointer to **NullableString** | Optional for crypto balances. If set, it must match the account&#39;s symbol. Tolerated for deleted-account balances. Do not provide this for manual or Plaid balances. On the synced crypto path endpoint, if provided it must match the &#x60;symbol&#x60; path parameter.  | [optional] 
**CryptoBalance** | Pointer to **NullableString** | Optional crypto quantity for crypto_manual, crypto_synced, and deleted balances. Do not provide this for manual or Plaid balances. | [optional] 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Optional currency for this balance entry. If omitted, it defaults to the account currency for manual/Plaid accounts, or the user&#39;s primary currency for crypto/deleted accounts. | [optional] 
**ToBase** | Pointer to **float64** | System-defined historical balance converted to the user&#39;s primary currency. Ignored if set. Use &#x60;balance&#x60; to update the historical balance. | [optional] 

## Methods

### NewBalanceHistoryUpdateItemObject

`func NewBalanceHistoryUpdateItemObject(month string, balance BalanceHistoryUpdateItemObjectBalance, ) *BalanceHistoryUpdateItemObject`

NewBalanceHistoryUpdateItemObject instantiates a new BalanceHistoryUpdateItemObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistoryUpdateItemObjectWithDefaults

`func NewBalanceHistoryUpdateItemObjectWithDefaults() *BalanceHistoryUpdateItemObject`

NewBalanceHistoryUpdateItemObjectWithDefaults instantiates a new BalanceHistoryUpdateItemObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BalanceHistoryUpdateItemObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BalanceHistoryUpdateItemObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BalanceHistoryUpdateItemObject) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *BalanceHistoryUpdateItemObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetMonth

`func (o *BalanceHistoryUpdateItemObject) GetMonth() string`

GetMonth returns the Month field if non-nil, zero value otherwise.

### GetMonthOk

`func (o *BalanceHistoryUpdateItemObject) GetMonthOk() (*string, bool)`

GetMonthOk returns a tuple with the Month field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonth

`func (o *BalanceHistoryUpdateItemObject) SetMonth(v string)`

SetMonth sets Month field to given value.


### GetBalance

`func (o *BalanceHistoryUpdateItemObject) GetBalance() BalanceHistoryUpdateItemObjectBalance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *BalanceHistoryUpdateItemObject) GetBalanceOk() (*BalanceHistoryUpdateItemObjectBalance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *BalanceHistoryUpdateItemObject) SetBalance(v BalanceHistoryUpdateItemObjectBalance)`

SetBalance sets Balance field to given value.


### GetSymbol

`func (o *BalanceHistoryUpdateItemObject) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *BalanceHistoryUpdateItemObject) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *BalanceHistoryUpdateItemObject) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.

### HasSymbol

`func (o *BalanceHistoryUpdateItemObject) HasSymbol() bool`

HasSymbol returns a boolean if a field has been set.

### SetSymbolNil

`func (o *BalanceHistoryUpdateItemObject) SetSymbolNil(b bool)`

 SetSymbolNil sets the value for Symbol to be an explicit nil

### UnsetSymbol
`func (o *BalanceHistoryUpdateItemObject) UnsetSymbol()`

UnsetSymbol ensures that no value is present for Symbol, not even an explicit nil
### GetCryptoBalance

`func (o *BalanceHistoryUpdateItemObject) GetCryptoBalance() string`

GetCryptoBalance returns the CryptoBalance field if non-nil, zero value otherwise.

### GetCryptoBalanceOk

`func (o *BalanceHistoryUpdateItemObject) GetCryptoBalanceOk() (*string, bool)`

GetCryptoBalanceOk returns a tuple with the CryptoBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoBalance

`func (o *BalanceHistoryUpdateItemObject) SetCryptoBalance(v string)`

SetCryptoBalance sets CryptoBalance field to given value.

### HasCryptoBalance

`func (o *BalanceHistoryUpdateItemObject) HasCryptoBalance() bool`

HasCryptoBalance returns a boolean if a field has been set.

### SetCryptoBalanceNil

`func (o *BalanceHistoryUpdateItemObject) SetCryptoBalanceNil(b bool)`

 SetCryptoBalanceNil sets the value for CryptoBalance to be an explicit nil

### UnsetCryptoBalance
`func (o *BalanceHistoryUpdateItemObject) UnsetCryptoBalance()`

UnsetCryptoBalance ensures that no value is present for CryptoBalance, not even an explicit nil
### GetCurrency

`func (o *BalanceHistoryUpdateItemObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *BalanceHistoryUpdateItemObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *BalanceHistoryUpdateItemObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *BalanceHistoryUpdateItemObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetToBase

`func (o *BalanceHistoryUpdateItemObject) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *BalanceHistoryUpdateItemObject) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *BalanceHistoryUpdateItemObject) SetToBase(v float64)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *BalanceHistoryUpdateItemObject) HasToBase() bool`

HasToBase returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


