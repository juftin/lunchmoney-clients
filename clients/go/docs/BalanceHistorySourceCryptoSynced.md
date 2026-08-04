# BalanceHistorySourceCryptoSynced

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to a synced crypto connection. | 
**CryptoSyncedId** | **int32** | ID of the synced crypto connection associated with this entry. | 
**Symbol** | **string** | Crypto symbol (e.g. &#x60;eth&#x60;, &#x60;btc&#x60;) identifying the specific currency within the synced account. | 

## Methods

### NewBalanceHistorySourceCryptoSynced

`func NewBalanceHistorySourceCryptoSynced(type_ string, cryptoSyncedId int32, symbol string, ) *BalanceHistorySourceCryptoSynced`

NewBalanceHistorySourceCryptoSynced instantiates a new BalanceHistorySourceCryptoSynced object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistorySourceCryptoSyncedWithDefaults

`func NewBalanceHistorySourceCryptoSyncedWithDefaults() *BalanceHistorySourceCryptoSynced`

NewBalanceHistorySourceCryptoSyncedWithDefaults instantiates a new BalanceHistorySourceCryptoSynced object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistorySourceCryptoSynced) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistorySourceCryptoSynced) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistorySourceCryptoSynced) SetType(v string)`

SetType sets Type field to given value.


### GetCryptoSyncedId

`func (o *BalanceHistorySourceCryptoSynced) GetCryptoSyncedId() int32`

GetCryptoSyncedId returns the CryptoSyncedId field if non-nil, zero value otherwise.

### GetCryptoSyncedIdOk

`func (o *BalanceHistorySourceCryptoSynced) GetCryptoSyncedIdOk() (*int32, bool)`

GetCryptoSyncedIdOk returns a tuple with the CryptoSyncedId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoSyncedId

`func (o *BalanceHistorySourceCryptoSynced) SetCryptoSyncedId(v int32)`

SetCryptoSyncedId sets CryptoSyncedId field to given value.


### GetSymbol

`func (o *BalanceHistorySourceCryptoSynced) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *BalanceHistorySourceCryptoSynced) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *BalanceHistorySourceCryptoSynced) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


