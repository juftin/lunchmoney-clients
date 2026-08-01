# CryptoCurrencyResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cryptocurrencies** | [**[]CryptoCurrencyObject**](CryptoCurrencyObject.md) | List of cryptocurrencies currently supported for manual tracking. | 

## Methods

### NewCryptoCurrencyResponseObject

`func NewCryptoCurrencyResponseObject(cryptocurrencies []CryptoCurrencyObject, ) *CryptoCurrencyResponseObject`

NewCryptoCurrencyResponseObject instantiates a new CryptoCurrencyResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCryptoCurrencyResponseObjectWithDefaults

`func NewCryptoCurrencyResponseObjectWithDefaults() *CryptoCurrencyResponseObject`

NewCryptoCurrencyResponseObjectWithDefaults instantiates a new CryptoCurrencyResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCryptocurrencies

`func (o *CryptoCurrencyResponseObject) GetCryptocurrencies() []CryptoCurrencyObject`

GetCryptocurrencies returns the Cryptocurrencies field if non-nil, zero value otherwise.

### GetCryptocurrenciesOk

`func (o *CryptoCurrencyResponseObject) GetCryptocurrenciesOk() (*[]CryptoCurrencyObject, bool)`

GetCryptocurrenciesOk returns a tuple with the Cryptocurrencies field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptocurrencies

`func (o *CryptoCurrencyResponseObject) SetCryptocurrencies(v []CryptoCurrencyObject)`

SetCryptocurrencies sets Cryptocurrencies field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


