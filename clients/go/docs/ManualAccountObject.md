# ManualAccountObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | The unique identifier of this account | 
**Name** | **string** | Name of the account | 
**InstitutionName** | **NullableString** | Name of institution holding the account | 
**DisplayName** | **NullableString** | Optional display name for the account as set by the user or derived from the &#x60;institution_name&#x60; and &#x60;name&#x60; if not explicitly set. | 
**Type** | [**AccountTypeEnum**](AccountTypeEnum.md) | Primary type of the account | 
**Subtype** | **NullableString** | Optional account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | 
**Balance** | **string** | Current balance of the account in numeric format to 4 decimal places | 
**Currency** | **string** | Three-letter lowercase currency code of the account balance | 
**ToBase** | **float32** | The balance converted to the user&#39;s primary currency | 
**BalanceAsOf** | **time.Time** | Date balance was last updated in ISO 8601 extended format, can be in date or date-time format | 
**Status** | **string** | The status of the account | 
**ClosedOn** | **NullableString** | The date this account was closed in YYYY-MM-DD format. Will be null if the account has not been marked as closed. | 
**ExternalId** | **NullableString** | An optional external_id that may be set or updated via the API | 
**CustomMetadata** | Pointer to **map[string]interface{}** | User defined JSON data that can be set or cleared via the API | [optional] 
**ExcludeFromTransactions** | **bool** | If true, this account will not show up as an option for assignment when creating transactions manually | [default to false]
**CreatedByName** | **string** | The name of the user who created the account | 
**CreatedAt** | **time.Time** | Date/time the account was created in ISO 8601 extended format | 
**UpdatedAt** | **time.Time** | Date/time the account was last updated in ISO 8601 extended format | 

## Methods

### NewManualAccountObject

`func NewManualAccountObject(id int32, name string, institutionName NullableString, displayName NullableString, type_ AccountTypeEnum, subtype NullableString, balance string, currency string, toBase float32, balanceAsOf time.Time, status string, closedOn NullableString, externalId NullableString, excludeFromTransactions bool, createdByName string, createdAt time.Time, updatedAt time.Time, ) *ManualAccountObject`

NewManualAccountObject instantiates a new ManualAccountObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewManualAccountObjectWithDefaults

`func NewManualAccountObjectWithDefaults() *ManualAccountObject`

NewManualAccountObjectWithDefaults instantiates a new ManualAccountObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ManualAccountObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ManualAccountObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ManualAccountObject) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *ManualAccountObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ManualAccountObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ManualAccountObject) SetName(v string)`

SetName sets Name field to given value.


### GetInstitutionName

`func (o *ManualAccountObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *ManualAccountObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *ManualAccountObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.


### SetInstitutionNameNil

`func (o *ManualAccountObject) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *ManualAccountObject) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetDisplayName

`func (o *ManualAccountObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *ManualAccountObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *ManualAccountObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *ManualAccountObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *ManualAccountObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetType

`func (o *ManualAccountObject) GetType() AccountTypeEnum`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ManualAccountObject) GetTypeOk() (*AccountTypeEnum, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ManualAccountObject) SetType(v AccountTypeEnum)`

SetType sets Type field to given value.


### GetSubtype

`func (o *ManualAccountObject) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *ManualAccountObject) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *ManualAccountObject) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.


### SetSubtypeNil

`func (o *ManualAccountObject) SetSubtypeNil(b bool)`

 SetSubtypeNil sets the value for Subtype to be an explicit nil

### UnsetSubtype
`func (o *ManualAccountObject) UnsetSubtype()`

UnsetSubtype ensures that no value is present for Subtype, not even an explicit nil
### GetBalance

`func (o *ManualAccountObject) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *ManualAccountObject) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *ManualAccountObject) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetCurrency

`func (o *ManualAccountObject) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *ManualAccountObject) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *ManualAccountObject) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *ManualAccountObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *ManualAccountObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *ManualAccountObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.


### GetBalanceAsOf

`func (o *ManualAccountObject) GetBalanceAsOf() time.Time`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *ManualAccountObject) GetBalanceAsOfOk() (*time.Time, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *ManualAccountObject) SetBalanceAsOf(v time.Time)`

SetBalanceAsOf sets BalanceAsOf field to given value.


### GetStatus

`func (o *ManualAccountObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ManualAccountObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ManualAccountObject) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetClosedOn

`func (o *ManualAccountObject) GetClosedOn() string`

GetClosedOn returns the ClosedOn field if non-nil, zero value otherwise.

### GetClosedOnOk

`func (o *ManualAccountObject) GetClosedOnOk() (*string, bool)`

GetClosedOnOk returns a tuple with the ClosedOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedOn

`func (o *ManualAccountObject) SetClosedOn(v string)`

SetClosedOn sets ClosedOn field to given value.


### SetClosedOnNil

`func (o *ManualAccountObject) SetClosedOnNil(b bool)`

 SetClosedOnNil sets the value for ClosedOn to be an explicit nil

### UnsetClosedOn
`func (o *ManualAccountObject) UnsetClosedOn()`

UnsetClosedOn ensures that no value is present for ClosedOn, not even an explicit nil
### GetExternalId

`func (o *ManualAccountObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *ManualAccountObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *ManualAccountObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.


### SetExternalIdNil

`func (o *ManualAccountObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *ManualAccountObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *ManualAccountObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *ManualAccountObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *ManualAccountObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *ManualAccountObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *ManualAccountObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *ManualAccountObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetExcludeFromTransactions

`func (o *ManualAccountObject) GetExcludeFromTransactions() bool`

GetExcludeFromTransactions returns the ExcludeFromTransactions field if non-nil, zero value otherwise.

### GetExcludeFromTransactionsOk

`func (o *ManualAccountObject) GetExcludeFromTransactionsOk() (*bool, bool)`

GetExcludeFromTransactionsOk returns a tuple with the ExcludeFromTransactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTransactions

`func (o *ManualAccountObject) SetExcludeFromTransactions(v bool)`

SetExcludeFromTransactions sets ExcludeFromTransactions field to given value.


### GetCreatedByName

`func (o *ManualAccountObject) GetCreatedByName() string`

GetCreatedByName returns the CreatedByName field if non-nil, zero value otherwise.

### GetCreatedByNameOk

`func (o *ManualAccountObject) GetCreatedByNameOk() (*string, bool)`

GetCreatedByNameOk returns a tuple with the CreatedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedByName

`func (o *ManualAccountObject) SetCreatedByName(v string)`

SetCreatedByName sets CreatedByName field to given value.


### GetCreatedAt

`func (o *ManualAccountObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ManualAccountObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ManualAccountObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *ManualAccountObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ManualAccountObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ManualAccountObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


