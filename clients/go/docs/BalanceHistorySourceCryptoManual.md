# BalanceHistorySourceCryptoManual

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to a manual crypto account. | 
**CryptoManualId** | **int32** | ID of the manual crypto account associated with this entry. | 
**Symbol** | Pointer to **NullableString** | Crypto symbol associated with the manual crypto account, when available. | [optional] 

## Methods

### NewBalanceHistorySourceCryptoManual

`func NewBalanceHistorySourceCryptoManual(type_ string, cryptoManualId int32, ) *BalanceHistorySourceCryptoManual`

NewBalanceHistorySourceCryptoManual instantiates a new BalanceHistorySourceCryptoManual object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistorySourceCryptoManualWithDefaults

`func NewBalanceHistorySourceCryptoManualWithDefaults() *BalanceHistorySourceCryptoManual`

NewBalanceHistorySourceCryptoManualWithDefaults instantiates a new BalanceHistorySourceCryptoManual object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistorySourceCryptoManual) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistorySourceCryptoManual) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistorySourceCryptoManual) SetType(v string)`

SetType sets Type field to given value.


### GetCryptoManualId

`func (o *BalanceHistorySourceCryptoManual) GetCryptoManualId() int32`

GetCryptoManualId returns the CryptoManualId field if non-nil, zero value otherwise.

### GetCryptoManualIdOk

`func (o *BalanceHistorySourceCryptoManual) GetCryptoManualIdOk() (*int32, bool)`

GetCryptoManualIdOk returns a tuple with the CryptoManualId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoManualId

`func (o *BalanceHistorySourceCryptoManual) SetCryptoManualId(v int32)`

SetCryptoManualId sets CryptoManualId field to given value.


### GetSymbol

`func (o *BalanceHistorySourceCryptoManual) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *BalanceHistorySourceCryptoManual) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *BalanceHistorySourceCryptoManual) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.

### HasSymbol

`func (o *BalanceHistorySourceCryptoManual) HasSymbol() bool`

HasSymbol returns a boolean if a field has been set.

### SetSymbolNil

`func (o *BalanceHistorySourceCryptoManual) SetSymbolNil(b bool)`

 SetSymbolNil sets the value for Symbol to be an explicit nil

### UnsetSymbol
`func (o *BalanceHistorySourceCryptoManual) UnsetSymbol()`

UnsetSymbol ensures that no value is present for Symbol, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


