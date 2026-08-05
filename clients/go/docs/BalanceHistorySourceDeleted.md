# BalanceHistorySourceDeleted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to an account that has since been deleted. | 
**DeletedAccountId** | **int32** | Identifier for the deleted account history source | 
**Name** | **NullableString** | Archived account &#x60;name&#x60; for the deleted account source | 
**InstitutionName** | **NullableString** | Archived &#x60;institution_name&#x60; for the deleted account source | 
**DisplayName** | **NullableString** | Archived &#x60;display_name&#x60; of the deleted account | 
**AccountType** | **NullableString** | Archived &#x60;type&#x60; of the deleted account source | 
**Subtype** | **NullableString** | Archived &#x60;subtype&#x60; of the deleted account source | 
**Mask** | **NullableString** | Archived account &#x60;mask&#x60; for a deleted Plaid account source | 
**Symbol** | **NullableString** | Archived &#x60;symbol&#x60; for a deleted crypto account source | 

## Methods

### NewBalanceHistorySourceDeleted

`func NewBalanceHistorySourceDeleted(type_ string, deletedAccountId int32, name NullableString, institutionName NullableString, displayName NullableString, accountType NullableString, subtype NullableString, mask NullableString, symbol NullableString, ) *BalanceHistorySourceDeleted`

NewBalanceHistorySourceDeleted instantiates a new BalanceHistorySourceDeleted object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistorySourceDeletedWithDefaults

`func NewBalanceHistorySourceDeletedWithDefaults() *BalanceHistorySourceDeleted`

NewBalanceHistorySourceDeletedWithDefaults instantiates a new BalanceHistorySourceDeleted object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistorySourceDeleted) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistorySourceDeleted) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistorySourceDeleted) SetType(v string)`

SetType sets Type field to given value.


### GetDeletedAccountId

`func (o *BalanceHistorySourceDeleted) GetDeletedAccountId() int32`

GetDeletedAccountId returns the DeletedAccountId field if non-nil, zero value otherwise.

### GetDeletedAccountIdOk

`func (o *BalanceHistorySourceDeleted) GetDeletedAccountIdOk() (*int32, bool)`

GetDeletedAccountIdOk returns a tuple with the DeletedAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAccountId

`func (o *BalanceHistorySourceDeleted) SetDeletedAccountId(v int32)`

SetDeletedAccountId sets DeletedAccountId field to given value.


### GetName

`func (o *BalanceHistorySourceDeleted) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BalanceHistorySourceDeleted) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BalanceHistorySourceDeleted) SetName(v string)`

SetName sets Name field to given value.


### SetNameNil

`func (o *BalanceHistorySourceDeleted) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *BalanceHistorySourceDeleted) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetInstitutionName

`func (o *BalanceHistorySourceDeleted) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *BalanceHistorySourceDeleted) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *BalanceHistorySourceDeleted) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.


### SetInstitutionNameNil

`func (o *BalanceHistorySourceDeleted) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *BalanceHistorySourceDeleted) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetDisplayName

`func (o *BalanceHistorySourceDeleted) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *BalanceHistorySourceDeleted) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *BalanceHistorySourceDeleted) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *BalanceHistorySourceDeleted) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *BalanceHistorySourceDeleted) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetAccountType

`func (o *BalanceHistorySourceDeleted) GetAccountType() string`

GetAccountType returns the AccountType field if non-nil, zero value otherwise.

### GetAccountTypeOk

`func (o *BalanceHistorySourceDeleted) GetAccountTypeOk() (*string, bool)`

GetAccountTypeOk returns a tuple with the AccountType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountType

`func (o *BalanceHistorySourceDeleted) SetAccountType(v string)`

SetAccountType sets AccountType field to given value.


### SetAccountTypeNil

`func (o *BalanceHistorySourceDeleted) SetAccountTypeNil(b bool)`

 SetAccountTypeNil sets the value for AccountType to be an explicit nil

### UnsetAccountType
`func (o *BalanceHistorySourceDeleted) UnsetAccountType()`

UnsetAccountType ensures that no value is present for AccountType, not even an explicit nil
### GetSubtype

`func (o *BalanceHistorySourceDeleted) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *BalanceHistorySourceDeleted) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *BalanceHistorySourceDeleted) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.


### SetSubtypeNil

`func (o *BalanceHistorySourceDeleted) SetSubtypeNil(b bool)`

 SetSubtypeNil sets the value for Subtype to be an explicit nil

### UnsetSubtype
`func (o *BalanceHistorySourceDeleted) UnsetSubtype()`

UnsetSubtype ensures that no value is present for Subtype, not even an explicit nil
### GetMask

`func (o *BalanceHistorySourceDeleted) GetMask() string`

GetMask returns the Mask field if non-nil, zero value otherwise.

### GetMaskOk

`func (o *BalanceHistorySourceDeleted) GetMaskOk() (*string, bool)`

GetMaskOk returns a tuple with the Mask field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMask

`func (o *BalanceHistorySourceDeleted) SetMask(v string)`

SetMask sets Mask field to given value.


### SetMaskNil

`func (o *BalanceHistorySourceDeleted) SetMaskNil(b bool)`

 SetMaskNil sets the value for Mask to be an explicit nil

### UnsetMask
`func (o *BalanceHistorySourceDeleted) UnsetMask()`

UnsetMask ensures that no value is present for Mask, not even an explicit nil
### GetSymbol

`func (o *BalanceHistorySourceDeleted) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *BalanceHistorySourceDeleted) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *BalanceHistorySourceDeleted) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.


### SetSymbolNil

`func (o *BalanceHistorySourceDeleted) SetSymbolNil(b bool)`

 SetSymbolNil sets the value for Symbol to be an explicit nil

### UnsetSymbol
`func (o *BalanceHistorySourceDeleted) UnsetSymbol()`

UnsetSymbol ensures that no value is present for Symbol, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


