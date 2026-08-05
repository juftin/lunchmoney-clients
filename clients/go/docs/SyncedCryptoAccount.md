# SyncedCryptoAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | System defined unique ID for the synced crypto connection | 
**Provider** | **string** | Provider used for the synced crypto connection | 
**Status** | **string** | Status of the synced crypto account. If not &#x60;active&#x60;, see the [Knowledge Base](https://support.lunchmoney.app/setup/crypto#why-is-my-synced-crypto-account-showing-not-supported) for details. | 
**CreatedByName** | **NullableString** | Name of the user who created the crypto connection | 
**CreatedAt** | **time.Time** | Date/time the synced crypto connection was created in ISO 8601 extended format | 
**UpdatedAt** | **time.Time** | Date/time the synced crypto connection was last updated in ISO 8601 extended format | 
**LastImport** | Pointer to **NullableTime** | System defined timestamp in ISO 8601 extended format of the last successful import. | [optional] 
**DisplayName** | **NullableString** | Optional display name for the synced crypto connection | 
**Balances** | [**[]CryptoSyncedBalance**](CryptoSyncedBalance.md) | Balances currently held in the synced crypto connection | 

## Methods

### NewSyncedCryptoAccount

`func NewSyncedCryptoAccount(id int32, provider string, status string, createdByName NullableString, createdAt time.Time, updatedAt time.Time, displayName NullableString, balances []CryptoSyncedBalance, ) *SyncedCryptoAccount`

NewSyncedCryptoAccount instantiates a new SyncedCryptoAccount object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSyncedCryptoAccountWithDefaults

`func NewSyncedCryptoAccountWithDefaults() *SyncedCryptoAccount`

NewSyncedCryptoAccountWithDefaults instantiates a new SyncedCryptoAccount object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SyncedCryptoAccount) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SyncedCryptoAccount) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SyncedCryptoAccount) SetId(v int32)`

SetId sets Id field to given value.


### GetProvider

`func (o *SyncedCryptoAccount) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *SyncedCryptoAccount) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *SyncedCryptoAccount) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetStatus

`func (o *SyncedCryptoAccount) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SyncedCryptoAccount) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SyncedCryptoAccount) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedByName

`func (o *SyncedCryptoAccount) GetCreatedByName() string`

GetCreatedByName returns the CreatedByName field if non-nil, zero value otherwise.

### GetCreatedByNameOk

`func (o *SyncedCryptoAccount) GetCreatedByNameOk() (*string, bool)`

GetCreatedByNameOk returns a tuple with the CreatedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedByName

`func (o *SyncedCryptoAccount) SetCreatedByName(v string)`

SetCreatedByName sets CreatedByName field to given value.


### SetCreatedByNameNil

`func (o *SyncedCryptoAccount) SetCreatedByNameNil(b bool)`

 SetCreatedByNameNil sets the value for CreatedByName to be an explicit nil

### UnsetCreatedByName
`func (o *SyncedCryptoAccount) UnsetCreatedByName()`

UnsetCreatedByName ensures that no value is present for CreatedByName, not even an explicit nil
### GetCreatedAt

`func (o *SyncedCryptoAccount) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SyncedCryptoAccount) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SyncedCryptoAccount) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *SyncedCryptoAccount) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SyncedCryptoAccount) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SyncedCryptoAccount) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetLastImport

`func (o *SyncedCryptoAccount) GetLastImport() time.Time`

GetLastImport returns the LastImport field if non-nil, zero value otherwise.

### GetLastImportOk

`func (o *SyncedCryptoAccount) GetLastImportOk() (*time.Time, bool)`

GetLastImportOk returns a tuple with the LastImport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastImport

`func (o *SyncedCryptoAccount) SetLastImport(v time.Time)`

SetLastImport sets LastImport field to given value.

### HasLastImport

`func (o *SyncedCryptoAccount) HasLastImport() bool`

HasLastImport returns a boolean if a field has been set.

### SetLastImportNil

`func (o *SyncedCryptoAccount) SetLastImportNil(b bool)`

 SetLastImportNil sets the value for LastImport to be an explicit nil

### UnsetLastImport
`func (o *SyncedCryptoAccount) UnsetLastImport()`

UnsetLastImport ensures that no value is present for LastImport, not even an explicit nil
### GetDisplayName

`func (o *SyncedCryptoAccount) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *SyncedCryptoAccount) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *SyncedCryptoAccount) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *SyncedCryptoAccount) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *SyncedCryptoAccount) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetBalances

`func (o *SyncedCryptoAccount) GetBalances() []CryptoSyncedBalance`

GetBalances returns the Balances field if non-nil, zero value otherwise.

### GetBalancesOk

`func (o *SyncedCryptoAccount) GetBalancesOk() (*[]CryptoSyncedBalance, bool)`

GetBalancesOk returns a tuple with the Balances field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalances

`func (o *SyncedCryptoAccount) SetBalances(v []CryptoSyncedBalance)`

SetBalances sets Balances field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


