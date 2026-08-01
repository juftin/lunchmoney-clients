# CreateCryptoManualRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | User-defined name for the manual crypto asset | 
**DisplayName** | Pointer to **NullableString** | Display name for the manual crypto asset. If omitted or &#x60;null&#x60;, clients may derive one from &#x60;institution_name&#x60; + &#x60;name&#x60;. | [optional] 
**InstitutionName** | Pointer to **NullableString** | Institution or wallet provider display name. If omitted or &#x60;null&#x60;, no institution name is set. | [optional] 
**Balance** | [**CreateCryptoManualRequestObjectBalance**](CreateCryptoManualRequestObjectBalance.md) |  | 
**Symbol** | **string** | Cryptocurrency symbol to track. Must match the &#x60;symbol&#x60; of one of the supported cryptocurrencies returned by &#x60;GET /cryptocurrencies&#x60;. | 

## Methods

### NewCreateCryptoManualRequestObject

`func NewCreateCryptoManualRequestObject(name string, balance CreateCryptoManualRequestObjectBalance, symbol string, ) *CreateCryptoManualRequestObject`

NewCreateCryptoManualRequestObject instantiates a new CreateCryptoManualRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCryptoManualRequestObjectWithDefaults

`func NewCreateCryptoManualRequestObjectWithDefaults() *CreateCryptoManualRequestObject`

NewCreateCryptoManualRequestObjectWithDefaults instantiates a new CreateCryptoManualRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateCryptoManualRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateCryptoManualRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateCryptoManualRequestObject) SetName(v string)`

SetName sets Name field to given value.


### GetDisplayName

`func (o *CreateCryptoManualRequestObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *CreateCryptoManualRequestObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *CreateCryptoManualRequestObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *CreateCryptoManualRequestObject) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### SetDisplayNameNil

`func (o *CreateCryptoManualRequestObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *CreateCryptoManualRequestObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetInstitutionName

`func (o *CreateCryptoManualRequestObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *CreateCryptoManualRequestObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *CreateCryptoManualRequestObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.

### HasInstitutionName

`func (o *CreateCryptoManualRequestObject) HasInstitutionName() bool`

HasInstitutionName returns a boolean if a field has been set.

### SetInstitutionNameNil

`func (o *CreateCryptoManualRequestObject) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *CreateCryptoManualRequestObject) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetBalance

`func (o *CreateCryptoManualRequestObject) GetBalance() CreateCryptoManualRequestObjectBalance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *CreateCryptoManualRequestObject) GetBalanceOk() (*CreateCryptoManualRequestObjectBalance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *CreateCryptoManualRequestObject) SetBalance(v CreateCryptoManualRequestObjectBalance)`

SetBalance sets Balance field to given value.


### GetSymbol

`func (o *CreateCryptoManualRequestObject) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *CreateCryptoManualRequestObject) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *CreateCryptoManualRequestObject) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


