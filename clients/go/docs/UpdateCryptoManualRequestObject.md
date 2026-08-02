# UpdateCryptoManualRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** | System defined unique ID for the manual crypto asset. Ignored if set | [optional] 
**Name** | Pointer to **NullableString** | If set, the new name of the manual crypto asset | [optional] 
**DisplayName** | Pointer to **NullableString** | If set, the new display name for the manual crypto asset | [optional] 
**InstitutionName** | Pointer to **NullableString** | If set, the new institution or wallet provider display name | [optional] 
**Balance** | Pointer to [**UpdateCryptoManualRequestObjectBalance**](UpdateCryptoManualRequestObjectBalance.md) |  | [optional] 
**Symbol** | Pointer to **string** | Existing cryptocurrency symbol. Ignored if set. | [optional] 
**CoingeckoId** | Pointer to **NullableString** | System-defined CoinGecko identifier for this symbol. Ignored if set. | [optional] 
**ToBase** | Pointer to **float32** | System defined balance converted to the user&#39;s primary currency. Ignored if set | [optional] 
**BalanceAsOf** | Pointer to **NullableTime** | System defined date/time the manual balance record was last updated in ISO 8601 extended format. Ignored if set | [optional] 
**ExchangeRateAsOf** | Pointer to **NullableTime** | System defined date/time the exchange rate used to calculate to_base was observed in ISO 8601 extended format. Ignored if set | [optional] 
**CreatedByName** | Pointer to **NullableString** | System defined name of the user who created the crypto asset. Ignored if set | [optional] 
**CreatedAt** | Pointer to **time.Time** | System defined date/time the crypto asset was created in ISO 8601 extended format. Ignored if set | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System defined date/time the crypto asset was last updated in ISO 8601 extended format. Ignored if set | [optional] 

## Methods

### NewUpdateCryptoManualRequestObject

`func NewUpdateCryptoManualRequestObject() *UpdateCryptoManualRequestObject`

NewUpdateCryptoManualRequestObject instantiates a new UpdateCryptoManualRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateCryptoManualRequestObjectWithDefaults

`func NewUpdateCryptoManualRequestObjectWithDefaults() *UpdateCryptoManualRequestObject`

NewUpdateCryptoManualRequestObjectWithDefaults instantiates a new UpdateCryptoManualRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateCryptoManualRequestObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateCryptoManualRequestObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateCryptoManualRequestObject) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateCryptoManualRequestObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *UpdateCryptoManualRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateCryptoManualRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateCryptoManualRequestObject) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateCryptoManualRequestObject) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *UpdateCryptoManualRequestObject) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *UpdateCryptoManualRequestObject) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetDisplayName

`func (o *UpdateCryptoManualRequestObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *UpdateCryptoManualRequestObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *UpdateCryptoManualRequestObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *UpdateCryptoManualRequestObject) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### SetDisplayNameNil

`func (o *UpdateCryptoManualRequestObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *UpdateCryptoManualRequestObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetInstitutionName

`func (o *UpdateCryptoManualRequestObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *UpdateCryptoManualRequestObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *UpdateCryptoManualRequestObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.

### HasInstitutionName

`func (o *UpdateCryptoManualRequestObject) HasInstitutionName() bool`

HasInstitutionName returns a boolean if a field has been set.

### SetInstitutionNameNil

`func (o *UpdateCryptoManualRequestObject) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *UpdateCryptoManualRequestObject) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetBalance

`func (o *UpdateCryptoManualRequestObject) GetBalance() UpdateCryptoManualRequestObjectBalance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *UpdateCryptoManualRequestObject) GetBalanceOk() (*UpdateCryptoManualRequestObjectBalance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *UpdateCryptoManualRequestObject) SetBalance(v UpdateCryptoManualRequestObjectBalance)`

SetBalance sets Balance field to given value.

### HasBalance

`func (o *UpdateCryptoManualRequestObject) HasBalance() bool`

HasBalance returns a boolean if a field has been set.

### GetSymbol

`func (o *UpdateCryptoManualRequestObject) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *UpdateCryptoManualRequestObject) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *UpdateCryptoManualRequestObject) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.

### HasSymbol

`func (o *UpdateCryptoManualRequestObject) HasSymbol() bool`

HasSymbol returns a boolean if a field has been set.

### GetCoingeckoId

`func (o *UpdateCryptoManualRequestObject) GetCoingeckoId() string`

GetCoingeckoId returns the CoingeckoId field if non-nil, zero value otherwise.

### GetCoingeckoIdOk

`func (o *UpdateCryptoManualRequestObject) GetCoingeckoIdOk() (*string, bool)`

GetCoingeckoIdOk returns a tuple with the CoingeckoId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoingeckoId

`func (o *UpdateCryptoManualRequestObject) SetCoingeckoId(v string)`

SetCoingeckoId sets CoingeckoId field to given value.

### HasCoingeckoId

`func (o *UpdateCryptoManualRequestObject) HasCoingeckoId() bool`

HasCoingeckoId returns a boolean if a field has been set.

### SetCoingeckoIdNil

`func (o *UpdateCryptoManualRequestObject) SetCoingeckoIdNil(b bool)`

 SetCoingeckoIdNil sets the value for CoingeckoId to be an explicit nil

### UnsetCoingeckoId
`func (o *UpdateCryptoManualRequestObject) UnsetCoingeckoId()`

UnsetCoingeckoId ensures that no value is present for CoingeckoId, not even an explicit nil
### GetToBase

`func (o *UpdateCryptoManualRequestObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *UpdateCryptoManualRequestObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *UpdateCryptoManualRequestObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *UpdateCryptoManualRequestObject) HasToBase() bool`

HasToBase returns a boolean if a field has been set.

### GetBalanceAsOf

`func (o *UpdateCryptoManualRequestObject) GetBalanceAsOf() time.Time`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *UpdateCryptoManualRequestObject) GetBalanceAsOfOk() (*time.Time, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *UpdateCryptoManualRequestObject) SetBalanceAsOf(v time.Time)`

SetBalanceAsOf sets BalanceAsOf field to given value.

### HasBalanceAsOf

`func (o *UpdateCryptoManualRequestObject) HasBalanceAsOf() bool`

HasBalanceAsOf returns a boolean if a field has been set.

### SetBalanceAsOfNil

`func (o *UpdateCryptoManualRequestObject) SetBalanceAsOfNil(b bool)`

 SetBalanceAsOfNil sets the value for BalanceAsOf to be an explicit nil

### UnsetBalanceAsOf
`func (o *UpdateCryptoManualRequestObject) UnsetBalanceAsOf()`

UnsetBalanceAsOf ensures that no value is present for BalanceAsOf, not even an explicit nil
### GetExchangeRateAsOf

`func (o *UpdateCryptoManualRequestObject) GetExchangeRateAsOf() time.Time`

GetExchangeRateAsOf returns the ExchangeRateAsOf field if non-nil, zero value otherwise.

### GetExchangeRateAsOfOk

`func (o *UpdateCryptoManualRequestObject) GetExchangeRateAsOfOk() (*time.Time, bool)`

GetExchangeRateAsOfOk returns a tuple with the ExchangeRateAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExchangeRateAsOf

`func (o *UpdateCryptoManualRequestObject) SetExchangeRateAsOf(v time.Time)`

SetExchangeRateAsOf sets ExchangeRateAsOf field to given value.

### HasExchangeRateAsOf

`func (o *UpdateCryptoManualRequestObject) HasExchangeRateAsOf() bool`

HasExchangeRateAsOf returns a boolean if a field has been set.

### SetExchangeRateAsOfNil

`func (o *UpdateCryptoManualRequestObject) SetExchangeRateAsOfNil(b bool)`

 SetExchangeRateAsOfNil sets the value for ExchangeRateAsOf to be an explicit nil

### UnsetExchangeRateAsOf
`func (o *UpdateCryptoManualRequestObject) UnsetExchangeRateAsOf()`

UnsetExchangeRateAsOf ensures that no value is present for ExchangeRateAsOf, not even an explicit nil
### GetCreatedByName

`func (o *UpdateCryptoManualRequestObject) GetCreatedByName() string`

GetCreatedByName returns the CreatedByName field if non-nil, zero value otherwise.

### GetCreatedByNameOk

`func (o *UpdateCryptoManualRequestObject) GetCreatedByNameOk() (*string, bool)`

GetCreatedByNameOk returns a tuple with the CreatedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedByName

`func (o *UpdateCryptoManualRequestObject) SetCreatedByName(v string)`

SetCreatedByName sets CreatedByName field to given value.

### HasCreatedByName

`func (o *UpdateCryptoManualRequestObject) HasCreatedByName() bool`

HasCreatedByName returns a boolean if a field has been set.

### SetCreatedByNameNil

`func (o *UpdateCryptoManualRequestObject) SetCreatedByNameNil(b bool)`

 SetCreatedByNameNil sets the value for CreatedByName to be an explicit nil

### UnsetCreatedByName
`func (o *UpdateCryptoManualRequestObject) UnsetCreatedByName()`

UnsetCreatedByName ensures that no value is present for CreatedByName, not even an explicit nil
### GetCreatedAt

`func (o *UpdateCryptoManualRequestObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateCryptoManualRequestObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateCryptoManualRequestObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateCryptoManualRequestObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *UpdateCryptoManualRequestObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateCryptoManualRequestObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateCryptoManualRequestObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateCryptoManualRequestObject) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


