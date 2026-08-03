# CryptoManualObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | System defined unique ID for the manual crypto balance | 
**Name** | **string** | User-defined name for the crypto asset | 
**DisplayName** | **NullableString** | Optional display name for the crypto asset. If &#x60;null&#x60;, clients may derive a display name from &#x60;institution_name&#x60; + &#x60;name&#x60;. | 
**InstitutionName** | **NullableString** | Institution or wallet provider display name | 
**Balance** | **string** | Current balance in numeric format to 18 decimal places | 
**Symbol** | **string** | Cryptocurrency symbol | 
**CoingeckoId** | **NullableString** | CoinGecko identifier associated with this balance | 
**ToBase** | **NullableFloat32** | Balance converted to the user&#39;s primary currency. May be null if no conversion was available. | 
**BalanceAsOf** | **NullableTime** | Date/time the manual balance record was last updated in ISO 8601 extended format. This is currently based on the manual crypto record&#39;s updated_at timestamp. | 
**ExchangeRateAsOf** | **NullableTime** | Date/time the exchange rate used to calculate to_base was last updated in ISO 8601 extended format. Null when no exchange rate was used or no conversion was available. | 
**CreatedByName** | **NullableString** | Name of the user who created the crypto asset | 
**CreatedAt** | **time.Time** | Date/time the crypto asset was created in ISO 8601 extended format | 
**UpdatedAt** | **time.Time** | Date/time the crypto asset was last updated in ISO 8601 extended format | 

## Methods

### NewCryptoManualObject

`func NewCryptoManualObject(id int32, name string, displayName NullableString, institutionName NullableString, balance string, symbol string, coingeckoId NullableString, toBase NullableFloat32, balanceAsOf NullableTime, exchangeRateAsOf NullableTime, createdByName NullableString, createdAt time.Time, updatedAt time.Time, ) *CryptoManualObject`

NewCryptoManualObject instantiates a new CryptoManualObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCryptoManualObjectWithDefaults

`func NewCryptoManualObjectWithDefaults() *CryptoManualObject`

NewCryptoManualObjectWithDefaults instantiates a new CryptoManualObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CryptoManualObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CryptoManualObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CryptoManualObject) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *CryptoManualObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CryptoManualObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CryptoManualObject) SetName(v string)`

SetName sets Name field to given value.


### GetDisplayName

`func (o *CryptoManualObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *CryptoManualObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *CryptoManualObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *CryptoManualObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *CryptoManualObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetInstitutionName

`func (o *CryptoManualObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *CryptoManualObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *CryptoManualObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.


### SetInstitutionNameNil

`func (o *CryptoManualObject) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *CryptoManualObject) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetBalance

`func (o *CryptoManualObject) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *CryptoManualObject) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *CryptoManualObject) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetSymbol

`func (o *CryptoManualObject) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *CryptoManualObject) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *CryptoManualObject) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.


### GetCoingeckoId

`func (o *CryptoManualObject) GetCoingeckoId() string`

GetCoingeckoId returns the CoingeckoId field if non-nil, zero value otherwise.

### GetCoingeckoIdOk

`func (o *CryptoManualObject) GetCoingeckoIdOk() (*string, bool)`

GetCoingeckoIdOk returns a tuple with the CoingeckoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoingeckoId

`func (o *CryptoManualObject) SetCoingeckoId(v string)`

SetCoingeckoId sets CoingeckoId field to given value.


### SetCoingeckoIdNil

`func (o *CryptoManualObject) SetCoingeckoIdNil(b bool)`

 SetCoingeckoIdNil sets the value for CoingeckoId to be an explicit nil

### UnsetCoingeckoId
`func (o *CryptoManualObject) UnsetCoingeckoId()`

UnsetCoingeckoId ensures that no value is present for CoingeckoId, not even an explicit nil
### GetToBase

`func (o *CryptoManualObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *CryptoManualObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *CryptoManualObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.


### SetToBaseNil

`func (o *CryptoManualObject) SetToBaseNil(b bool)`

 SetToBaseNil sets the value for ToBase to be an explicit nil

### UnsetToBase
`func (o *CryptoManualObject) UnsetToBase()`

UnsetToBase ensures that no value is present for ToBase, not even an explicit nil
### GetBalanceAsOf

`func (o *CryptoManualObject) GetBalanceAsOf() time.Time`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *CryptoManualObject) GetBalanceAsOfOk() (*time.Time, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *CryptoManualObject) SetBalanceAsOf(v time.Time)`

SetBalanceAsOf sets BalanceAsOf field to given value.


### SetBalanceAsOfNil

`func (o *CryptoManualObject) SetBalanceAsOfNil(b bool)`

 SetBalanceAsOfNil sets the value for BalanceAsOf to be an explicit nil

### UnsetBalanceAsOf
`func (o *CryptoManualObject) UnsetBalanceAsOf()`

UnsetBalanceAsOf ensures that no value is present for BalanceAsOf, not even an explicit nil
### GetExchangeRateAsOf

`func (o *CryptoManualObject) GetExchangeRateAsOf() time.Time`

GetExchangeRateAsOf returns the ExchangeRateAsOf field if non-nil, zero value otherwise.

### GetExchangeRateAsOfOk

`func (o *CryptoManualObject) GetExchangeRateAsOfOk() (*time.Time, bool)`

GetExchangeRateAsOfOk returns a tuple with the ExchangeRateAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExchangeRateAsOf

`func (o *CryptoManualObject) SetExchangeRateAsOf(v time.Time)`

SetExchangeRateAsOf sets ExchangeRateAsOf field to given value.


### SetExchangeRateAsOfNil

`func (o *CryptoManualObject) SetExchangeRateAsOfNil(b bool)`

 SetExchangeRateAsOfNil sets the value for ExchangeRateAsOf to be an explicit nil

### UnsetExchangeRateAsOf
`func (o *CryptoManualObject) UnsetExchangeRateAsOf()`

UnsetExchangeRateAsOf ensures that no value is present for ExchangeRateAsOf, not even an explicit nil
### GetCreatedByName

`func (o *CryptoManualObject) GetCreatedByName() string`

GetCreatedByName returns the CreatedByName field if non-nil, zero value otherwise.

### GetCreatedByNameOk

`func (o *CryptoManualObject) GetCreatedByNameOk() (*string, bool)`

GetCreatedByNameOk returns a tuple with the CreatedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedByName

`func (o *CryptoManualObject) SetCreatedByName(v string)`

SetCreatedByName sets CreatedByName field to given value.


### SetCreatedByNameNil

`func (o *CryptoManualObject) SetCreatedByNameNil(b bool)`

 SetCreatedByNameNil sets the value for CreatedByName to be an explicit nil

### UnsetCreatedByName
`func (o *CryptoManualObject) UnsetCreatedByName()`

UnsetCreatedByName ensures that no value is present for CreatedByName, not even an explicit nil
### GetCreatedAt

`func (o *CryptoManualObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CryptoManualObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CryptoManualObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *CryptoManualObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CryptoManualObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CryptoManualObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


