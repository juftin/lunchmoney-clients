# BalanceHistoryAccountObjectSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to a manual account. | 
**ManualAccountId** | **int32** | ID of the manual account associated with this entry. | 
**PlaidAccountId** | **int32** | ID of the Plaid account associated with this entry. | 
**CryptoManualId** | **int32** | ID of the manual crypto account associated with this entry. | 
**Symbol** | **NullableString** | Archived &#x60;symbol&#x60; for a deleted crypto account source | 
**CryptoSyncedId** | **int32** | ID of the synced crypto connection associated with this entry. | 
**DeletedAccountId** | **int32** | Identifier for the deleted account history source | 
**Name** | **NullableString** | Archived account &#x60;name&#x60; for the deleted account source | 
**InstitutionName** | **NullableString** | Archived &#x60;institution_name&#x60; for the deleted account source | 
**DisplayName** | **NullableString** | Archived &#x60;display_name&#x60; of the deleted account | 
**AccountType** | **NullableString** | Archived &#x60;type&#x60; of the deleted account source | 
**Subtype** | **NullableString** | Archived &#x60;subtype&#x60; of the deleted account source | 
**Mask** | **NullableString** | Archived account &#x60;mask&#x60; for a deleted Plaid account source | 

## Methods

### NewBalanceHistoryAccountObjectSource

`func NewBalanceHistoryAccountObjectSource(type_ string, manualAccountId int32, plaidAccountId int32, cryptoManualId int32, symbol NullableString, cryptoSyncedId int32, deletedAccountId int32, name NullableString, institutionName NullableString, displayName NullableString, accountType NullableString, subtype NullableString, mask NullableString, ) *BalanceHistoryAccountObjectSource`

NewBalanceHistoryAccountObjectSource instantiates a new BalanceHistoryAccountObjectSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistoryAccountObjectSourceWithDefaults

`func NewBalanceHistoryAccountObjectSourceWithDefaults() *BalanceHistoryAccountObjectSource`

NewBalanceHistoryAccountObjectSourceWithDefaults instantiates a new BalanceHistoryAccountObjectSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistoryAccountObjectSource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistoryAccountObjectSource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistoryAccountObjectSource) SetType(v string)`

SetType sets Type field to given value.


### GetManualAccountId

`func (o *BalanceHistoryAccountObjectSource) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *BalanceHistoryAccountObjectSource) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *BalanceHistoryAccountObjectSource) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.


### GetPlaidAccountId

`func (o *BalanceHistoryAccountObjectSource) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *BalanceHistoryAccountObjectSource) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *BalanceHistoryAccountObjectSource) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.


### GetCryptoManualId

`func (o *BalanceHistoryAccountObjectSource) GetCryptoManualId() int32`

GetCryptoManualId returns the CryptoManualId field if non-nil, zero value otherwise.

### GetCryptoManualIdOk

`func (o *BalanceHistoryAccountObjectSource) GetCryptoManualIdOk() (*int32, bool)`

GetCryptoManualIdOk returns a tuple with the CryptoManualId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoManualId

`func (o *BalanceHistoryAccountObjectSource) SetCryptoManualId(v int32)`

SetCryptoManualId sets CryptoManualId field to given value.


### GetSymbol

`func (o *BalanceHistoryAccountObjectSource) GetSymbol() string`

GetSymbol returns the Symbol field if non-nil, zero value otherwise.

### GetSymbolOk

`func (o *BalanceHistoryAccountObjectSource) GetSymbolOk() (*string, bool)`

GetSymbolOk returns a tuple with the Symbol field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSymbol

`func (o *BalanceHistoryAccountObjectSource) SetSymbol(v string)`

SetSymbol sets Symbol field to given value.


### SetSymbolNil

`func (o *BalanceHistoryAccountObjectSource) SetSymbolNil(b bool)`

 SetSymbolNil sets the value for Symbol to be an explicit nil

### UnsetSymbol
`func (o *BalanceHistoryAccountObjectSource) UnsetSymbol()`

UnsetSymbol ensures that no value is present for Symbol, not even an explicit nil
### GetCryptoSyncedId

`func (o *BalanceHistoryAccountObjectSource) GetCryptoSyncedId() int32`

GetCryptoSyncedId returns the CryptoSyncedId field if non-nil, zero value otherwise.

### GetCryptoSyncedIdOk

`func (o *BalanceHistoryAccountObjectSource) GetCryptoSyncedIdOk() (*int32, bool)`

GetCryptoSyncedIdOk returns a tuple with the CryptoSyncedId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCryptoSyncedId

`func (o *BalanceHistoryAccountObjectSource) SetCryptoSyncedId(v int32)`

SetCryptoSyncedId sets CryptoSyncedId field to given value.


### GetDeletedAccountId

`func (o *BalanceHistoryAccountObjectSource) GetDeletedAccountId() int32`

GetDeletedAccountId returns the DeletedAccountId field if non-nil, zero value otherwise.

### GetDeletedAccountIdOk

`func (o *BalanceHistoryAccountObjectSource) GetDeletedAccountIdOk() (*int32, bool)`

GetDeletedAccountIdOk returns a tuple with the DeletedAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAccountId

`func (o *BalanceHistoryAccountObjectSource) SetDeletedAccountId(v int32)`

SetDeletedAccountId sets DeletedAccountId field to given value.


### GetName

`func (o *BalanceHistoryAccountObjectSource) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BalanceHistoryAccountObjectSource) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BalanceHistoryAccountObjectSource) SetName(v string)`

SetName sets Name field to given value.


### SetNameNil

`func (o *BalanceHistoryAccountObjectSource) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *BalanceHistoryAccountObjectSource) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetInstitutionName

`func (o *BalanceHistoryAccountObjectSource) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *BalanceHistoryAccountObjectSource) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *BalanceHistoryAccountObjectSource) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.


### SetInstitutionNameNil

`func (o *BalanceHistoryAccountObjectSource) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *BalanceHistoryAccountObjectSource) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetDisplayName

`func (o *BalanceHistoryAccountObjectSource) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *BalanceHistoryAccountObjectSource) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *BalanceHistoryAccountObjectSource) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *BalanceHistoryAccountObjectSource) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *BalanceHistoryAccountObjectSource) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetAccountType

`func (o *BalanceHistoryAccountObjectSource) GetAccountType() string`

GetAccountType returns the AccountType field if non-nil, zero value otherwise.

### GetAccountTypeOk

`func (o *BalanceHistoryAccountObjectSource) GetAccountTypeOk() (*string, bool)`

GetAccountTypeOk returns a tuple with the AccountType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountType

`func (o *BalanceHistoryAccountObjectSource) SetAccountType(v string)`

SetAccountType sets AccountType field to given value.


### SetAccountTypeNil

`func (o *BalanceHistoryAccountObjectSource) SetAccountTypeNil(b bool)`

 SetAccountTypeNil sets the value for AccountType to be an explicit nil

### UnsetAccountType
`func (o *BalanceHistoryAccountObjectSource) UnsetAccountType()`

UnsetAccountType ensures that no value is present for AccountType, not even an explicit nil
### GetSubtype

`func (o *BalanceHistoryAccountObjectSource) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *BalanceHistoryAccountObjectSource) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *BalanceHistoryAccountObjectSource) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.


### SetSubtypeNil

`func (o *BalanceHistoryAccountObjectSource) SetSubtypeNil(b bool)`

 SetSubtypeNil sets the value for Subtype to be an explicit nil

### UnsetSubtype
`func (o *BalanceHistoryAccountObjectSource) UnsetSubtype()`

UnsetSubtype ensures that no value is present for Subtype, not even an explicit nil
### GetMask

`func (o *BalanceHistoryAccountObjectSource) GetMask() string`

GetMask returns the Mask field if non-nil, zero value otherwise.

### GetMaskOk

`func (o *BalanceHistoryAccountObjectSource) GetMaskOk() (*string, bool)`

GetMaskOk returns a tuple with the Mask field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMask

`func (o *BalanceHistoryAccountObjectSource) SetMask(v string)`

SetMask sets Mask field to given value.


### SetMaskNil

`func (o *BalanceHistoryAccountObjectSource) SetMaskNil(b bool)`

 SetMaskNil sets the value for Mask to be an explicit nil

### UnsetMask
`func (o *BalanceHistoryAccountObjectSource) UnsetMask()`

UnsetMask ensures that no value is present for Mask, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


