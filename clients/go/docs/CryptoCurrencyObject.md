# CryptoCurrencyObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | System-defined unique identifier for this cryptocurrency in Lunch Money. | 
**CoingeckoId** | **string** | System-defined CoinGecko identifier used to fetch the USD-based prices for this cryptocurrency. | 
**Symbol** | **string** | Lowercase currency symbol that must be used as &#x60;symbol&#x60; when creating a manual crypto balance. | 
**FullName** | **string** | Human-readable name of the cryptocurrency. | 

## Methods

### NewCryptoCurrencyObject

`func NewCryptoCurrencyObject(id int32, coingeckoId string, symbol string, fullName string, ) *CryptoCurrencyObject`

NewCryptoCurrencyObject instantiates a new CryptoCurrencyObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCryptoCurrencyObjectWithDefaults

`func NewCryptoCurrencyObjectWithDefaults() *CryptoCurrencyObject`

NewCryptoCurrencyObjectWithDefaults instantiates a new CryptoCurrencyObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CryptoCurrencyObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CryptoCurrencyObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CryptoCurrencyObject) SetId(v int32)`

SetId sets Id field to given value.


### GetCoingeckoId

`func (o *CryptoCurrencyObject) GetCoingeckoId() string`

GetCoingeckoId returns the CoingeckoId field if non-nil, zero value otherwise.

### GetCoingeckoIdOk

`func (o *CryptoCurrencyObject) GetCoingeckoIdOk() (*string, bool)`

GetCoingeckoIdOk returns a tuple with the CoingeckoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoingeckoId

`func (o *CryptoCurrencyObject) SetCoingeckoId(v string)`

SetCoingeckoId sets CoingeckoId field to given value.


### GetSymbol

`func (o *CryptoCurrencyObject) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *CryptoCurrencyObject) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *CryptoCurrencyObject) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.


### GetFullName

`func (o *CryptoCurrencyObject) GetFullName() string`

GetFullName returns the FullName field if non-nil, zero value otherwise.

### GetFullNameOk

`func (o *CryptoCurrencyObject) GetFullNameOk() (*string, bool)`

GetFullNameOk returns a tuple with the FullName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFullName

`func (o *CryptoCurrencyObject) SetFullName(v string)`

SetFullName sets FullName field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


