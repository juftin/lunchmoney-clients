# UpdateManualAccountRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** | System defined unique identifier of this account. Ignored if set | [optional] 
**Name** | Pointer to **string** | If set, the new name of the manual account | [optional] 
**InstitutionName** | Pointer to **NullableString** | If set, the name of institution holding the account | [optional] 
**DisplayName** | Pointer to **NullableString** | If set, the new display name for the manual account.&lt;br&gt; This must be unique for the user. | [optional] 
**Type** | Pointer to [**AccountTypeEnum**](AccountTypeEnum.md) | If set, the new type of the manual account | [optional] 
**Subtype** | Pointer to **string** | If set, an optional account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | [optional] 
**Balance** | Pointer to [**UpdateManualAccountRequestObjectBalance**](UpdateManualAccountRequestObjectBalance.md) |  | [optional] 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | If set, the new three-letter lowercase currency code of the manual account balance. | [optional] 
**BalanceAsOf** | Pointer to **NullableString** | A new date for the &#x60;updated_at&#x60; property. May be set as a date, ie: YYYY-MM-DD, or date-time string in ISO 8601 extended format. This property is ignored if &#x60;balance&#x60; is not also set. If &#x60;balance&#x60; is set and this property is not set the current time is used. | [optional] 
**Status** | Pointer to **string** | If set, the status of the manual account. If set to &#x60;closed&#x60;, the &#x60;closed_on_date&#x60; date will be set to the current date, unless it is also set. | [optional] 
**ClosedOn** | Pointer to [**NullableUpdateManualAccountRequestObjectClosedOn**](UpdateManualAccountRequestObjectClosedOn.md) |  | [optional] 
**ExternalId** | Pointer to **NullableString** | An optional user-defined ID for the manual account | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | An optional JSON object that includes additional data related to this account. This must be a valid JSON object and, when stringified, must not exceed 4096 characters. | [optional] 
**ExcludeFromTransactions** | Pointer to **bool** | If set, transactions may not be assigned to this manual account | [optional] 
**ToBase** | Pointer to **float32** | System defined balance converted to the user&#39;s primary currency. Ignored if set. Use &#x60;balance&#x60; to update the balance in the account | [optional] 
**CreatedAt** | Pointer to **time.Time** | System defined date/time the account was created in ISO 8601 extended format. Ignored if set. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System defined date/time the account was created in ISO 8601 extended format. Ignored if set. | [optional] 
**CreatedByName** | Pointer to **string** | System defined name of the user who created the account. Ignored if set | [optional] 

## Methods

### NewUpdateManualAccountRequestObject

`func NewUpdateManualAccountRequestObject() *UpdateManualAccountRequestObject`

NewUpdateManualAccountRequestObject instantiates a new UpdateManualAccountRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateManualAccountRequestObjectWithDefaults

`func NewUpdateManualAccountRequestObjectWithDefaults() *UpdateManualAccountRequestObject`

NewUpdateManualAccountRequestObjectWithDefaults instantiates a new UpdateManualAccountRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateManualAccountRequestObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateManualAccountRequestObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateManualAccountRequestObject) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateManualAccountRequestObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetName

`func (o *UpdateManualAccountRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateManualAccountRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateManualAccountRequestObject) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateManualAccountRequestObject) HasName() bool`

HasName returns a boolean if a field has been set.

### GetInstitutionName

`func (o *UpdateManualAccountRequestObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *UpdateManualAccountRequestObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *UpdateManualAccountRequestObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.

### HasInstitutionName

`func (o *UpdateManualAccountRequestObject) HasInstitutionName() bool`

HasInstitutionName returns a boolean if a field has been set.

### SetInstitutionNameNil

`func (o *UpdateManualAccountRequestObject) SetInstitutionNameNil(b bool)`

 SetInstitutionNameNil sets the value for InstitutionName to be an explicit nil

### UnsetInstitutionName
`func (o *UpdateManualAccountRequestObject) UnsetInstitutionName()`

UnsetInstitutionName ensures that no value is present for InstitutionName, not even an explicit nil
### GetDisplayName

`func (o *UpdateManualAccountRequestObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *UpdateManualAccountRequestObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *UpdateManualAccountRequestObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *UpdateManualAccountRequestObject) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### SetDisplayNameNil

`func (o *UpdateManualAccountRequestObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *UpdateManualAccountRequestObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetType

`func (o *UpdateManualAccountRequestObject) GetType() AccountTypeEnum`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *UpdateManualAccountRequestObject) GetTypeOk() (*AccountTypeEnum, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *UpdateManualAccountRequestObject) SetType(v AccountTypeEnum)`

SetType sets Type field to given value.

### HasType

`func (o *UpdateManualAccountRequestObject) HasType() bool`

HasType returns a boolean if a field has been set.

### GetSubtype

`func (o *UpdateManualAccountRequestObject) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *UpdateManualAccountRequestObject) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *UpdateManualAccountRequestObject) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.

### HasSubtype

`func (o *UpdateManualAccountRequestObject) HasSubtype() bool`

HasSubtype returns a boolean if a field has been set.

### GetBalance

`func (o *UpdateManualAccountRequestObject) GetBalance() UpdateManualAccountRequestObjectBalance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *UpdateManualAccountRequestObject) GetBalanceOk() (*UpdateManualAccountRequestObjectBalance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *UpdateManualAccountRequestObject) SetBalance(v UpdateManualAccountRequestObjectBalance)`

SetBalance sets Balance field to given value.

### HasBalance

`func (o *UpdateManualAccountRequestObject) HasBalance() bool`

HasBalance returns a boolean if a field has been set.

### GetCurrency

`func (o *UpdateManualAccountRequestObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *UpdateManualAccountRequestObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *UpdateManualAccountRequestObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *UpdateManualAccountRequestObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetBalanceAsOf

`func (o *UpdateManualAccountRequestObject) GetBalanceAsOf() string`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *UpdateManualAccountRequestObject) GetBalanceAsOfOk() (*string, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *UpdateManualAccountRequestObject) SetBalanceAsOf(v string)`

SetBalanceAsOf sets BalanceAsOf field to given value.

### HasBalanceAsOf

`func (o *UpdateManualAccountRequestObject) HasBalanceAsOf() bool`

HasBalanceAsOf returns a boolean if a field has been set.

### SetBalanceAsOfNil

`func (o *UpdateManualAccountRequestObject) SetBalanceAsOfNil(b bool)`

 SetBalanceAsOfNil sets the value for BalanceAsOf to be an explicit nil

### UnsetBalanceAsOf
`func (o *UpdateManualAccountRequestObject) UnsetBalanceAsOf()`

UnsetBalanceAsOf ensures that no value is present for BalanceAsOf, not even an explicit nil
### GetStatus

`func (o *UpdateManualAccountRequestObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateManualAccountRequestObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateManualAccountRequestObject) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateManualAccountRequestObject) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetClosedOn

`func (o *UpdateManualAccountRequestObject) GetClosedOn() UpdateManualAccountRequestObjectClosedOn`

GetClosedOn returns the ClosedOn field if non-nil, zero value otherwise.

### GetClosedOnOk

`func (o *UpdateManualAccountRequestObject) GetClosedOnOk() (*UpdateManualAccountRequestObjectClosedOn, bool)`

GetClosedOnOk returns a tuple with the ClosedOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedOn

`func (o *UpdateManualAccountRequestObject) SetClosedOn(v UpdateManualAccountRequestObjectClosedOn)`

SetClosedOn sets ClosedOn field to given value.

### HasClosedOn

`func (o *UpdateManualAccountRequestObject) HasClosedOn() bool`

HasClosedOn returns a boolean if a field has been set.

### SetClosedOnNil

`func (o *UpdateManualAccountRequestObject) SetClosedOnNil(b bool)`

 SetClosedOnNil sets the value for ClosedOn to be an explicit nil

### UnsetClosedOn
`func (o *UpdateManualAccountRequestObject) UnsetClosedOn()`

UnsetClosedOn ensures that no value is present for ClosedOn, not even an explicit nil
### GetExternalId

`func (o *UpdateManualAccountRequestObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *UpdateManualAccountRequestObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *UpdateManualAccountRequestObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.

### HasExternalId

`func (o *UpdateManualAccountRequestObject) HasExternalId() bool`

HasExternalId returns a boolean if a field has been set.

### SetExternalIdNil

`func (o *UpdateManualAccountRequestObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *UpdateManualAccountRequestObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *UpdateManualAccountRequestObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *UpdateManualAccountRequestObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *UpdateManualAccountRequestObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *UpdateManualAccountRequestObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *UpdateManualAccountRequestObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *UpdateManualAccountRequestObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetExcludeFromTransactions

`func (o *UpdateManualAccountRequestObject) GetExcludeFromTransactions() bool`

GetExcludeFromTransactions returns the ExcludeFromTransactions field if non-nil, zero value otherwise.

### GetExcludeFromTransactionsOk

`func (o *UpdateManualAccountRequestObject) GetExcludeFromTransactionsOk() (*bool, bool)`

GetExcludeFromTransactionsOk returns a tuple with the ExcludeFromTransactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTransactions

`func (o *UpdateManualAccountRequestObject) SetExcludeFromTransactions(v bool)`

SetExcludeFromTransactions sets ExcludeFromTransactions field to given value.

### HasExcludeFromTransactions

`func (o *UpdateManualAccountRequestObject) HasExcludeFromTransactions() bool`

HasExcludeFromTransactions returns a boolean if a field has been set.

### GetToBase

`func (o *UpdateManualAccountRequestObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *UpdateManualAccountRequestObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *UpdateManualAccountRequestObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *UpdateManualAccountRequestObject) HasToBase() bool`

HasToBase returns a boolean if a field has been set.

### GetCreatedAt

`func (o *UpdateManualAccountRequestObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateManualAccountRequestObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateManualAccountRequestObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateManualAccountRequestObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *UpdateManualAccountRequestObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateManualAccountRequestObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateManualAccountRequestObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateManualAccountRequestObject) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetCreatedByName

`func (o *UpdateManualAccountRequestObject) GetCreatedByName() string`

GetCreatedByName returns the CreatedByName field if non-nil, zero value otherwise.

### GetCreatedByNameOk

`func (o *UpdateManualAccountRequestObject) GetCreatedByNameOk() (*string, bool)`

GetCreatedByNameOk returns a tuple with the CreatedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedByName

`func (o *UpdateManualAccountRequestObject) SetCreatedByName(v string)`

SetCreatedByName sets CreatedByName field to given value.

### HasCreatedByName

`func (o *UpdateManualAccountRequestObject) HasCreatedByName() bool`

HasCreatedByName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


