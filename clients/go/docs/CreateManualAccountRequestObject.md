# CreateManualAccountRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the manual account | 
**InstitutionName** | Pointer to **string** | Name of institution holding the manual account | [optional] 
**DisplayName** | Pointer to **string** | Display name of the manual account as set by user or derived from the &#x60;institution_name&#x60; and &#x60;name&#x60; if not explicitly set.&lt;br&gt; This must be unique for the budgeting account. | [optional] 
**Type** | [**AccountTypeEnum**](AccountTypeEnum.md) | The type of manual account | 
**Subtype** | Pointer to **string** | An optional manual account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | [optional] 
**Balance** | [**CreateManualAccountRequestObjectBalance**](CreateManualAccountRequestObjectBalance.md) |  | 
**BalanceAsOf** | Pointer to **NullableString** | Date/time the balance of the manual account was last updated in ISO 8601 extended format | [optional] 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format | [optional] 
**Status** | Pointer to **string** | The status of the account | [optional] [default to "active"]
**ClosedOn** | Pointer to [**NullableCreateManualAccountRequestObjectClosedOn**](CreateManualAccountRequestObjectClosedOn.md) |  | [optional] 
**ExternalId** | Pointer to **NullableString** | An optional user-defined ID for the manual account | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | An optional JSON object that includes additional data related to this account. This must be a valid JSON object and, when stringified, must not exceed 4096 characters. | [optional] 
**ExcludeFromTransactions** | Pointer to **bool** | If &#x60;true&#x60;, transactions may not be assigned to this manual account | [optional] [default to false]

## Methods

### NewCreateManualAccountRequestObject

`func NewCreateManualAccountRequestObject(name string, type_ AccountTypeEnum, balance CreateManualAccountRequestObjectBalance, ) *CreateManualAccountRequestObject`

NewCreateManualAccountRequestObject instantiates a new CreateManualAccountRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateManualAccountRequestObjectWithDefaults

`func NewCreateManualAccountRequestObjectWithDefaults() *CreateManualAccountRequestObject`

NewCreateManualAccountRequestObjectWithDefaults instantiates a new CreateManualAccountRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateManualAccountRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateManualAccountRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateManualAccountRequestObject) SetName(v string)`

SetName sets Name field to given value.


### GetInstitutionName

`func (o *CreateManualAccountRequestObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *CreateManualAccountRequestObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *CreateManualAccountRequestObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.

### HasInstitutionName

`func (o *CreateManualAccountRequestObject) HasInstitutionName() bool`

HasInstitutionName returns a boolean if a field has been set.

### GetDisplayName

`func (o *CreateManualAccountRequestObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *CreateManualAccountRequestObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *CreateManualAccountRequestObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *CreateManualAccountRequestObject) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### GetType

`func (o *CreateManualAccountRequestObject) GetType() AccountTypeEnum`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CreateManualAccountRequestObject) GetTypeOk() (*AccountTypeEnum, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CreateManualAccountRequestObject) SetType(v AccountTypeEnum)`

SetType sets Type field to given value.


### GetSubtype

`func (o *CreateManualAccountRequestObject) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *CreateManualAccountRequestObject) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *CreateManualAccountRequestObject) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.

### HasSubtype

`func (o *CreateManualAccountRequestObject) HasSubtype() bool`

HasSubtype returns a boolean if a field has been set.

### GetBalance

`func (o *CreateManualAccountRequestObject) GetBalance() CreateManualAccountRequestObjectBalance`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *CreateManualAccountRequestObject) GetBalanceOk() (*CreateManualAccountRequestObjectBalance, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *CreateManualAccountRequestObject) SetBalance(v CreateManualAccountRequestObjectBalance)`

SetBalance sets Balance field to given value.


### GetBalanceAsOf

`func (o *CreateManualAccountRequestObject) GetBalanceAsOf() string`

GetBalanceAsOf returns the BalanceAsOf field if non-nil, zero value otherwise.

### GetBalanceAsOfOk

`func (o *CreateManualAccountRequestObject) GetBalanceAsOfOk() (*string, bool)`

GetBalanceAsOfOk returns a tuple with the BalanceAsOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceAsOf

`func (o *CreateManualAccountRequestObject) SetBalanceAsOf(v string)`

SetBalanceAsOf sets BalanceAsOf field to given value.

### HasBalanceAsOf

`func (o *CreateManualAccountRequestObject) HasBalanceAsOf() bool`

HasBalanceAsOf returns a boolean if a field has been set.

### SetBalanceAsOfNil

`func (o *CreateManualAccountRequestObject) SetBalanceAsOfNil(b bool)`

 SetBalanceAsOfNil sets the value for BalanceAsOf to be an explicit nil

### UnsetBalanceAsOf
`func (o *CreateManualAccountRequestObject) UnsetBalanceAsOf()`

UnsetBalanceAsOf ensures that no value is present for BalanceAsOf, not even an explicit nil
### GetCurrency

`func (o *CreateManualAccountRequestObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *CreateManualAccountRequestObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *CreateManualAccountRequestObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *CreateManualAccountRequestObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetStatus

`func (o *CreateManualAccountRequestObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CreateManualAccountRequestObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CreateManualAccountRequestObject) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *CreateManualAccountRequestObject) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetClosedOn

`func (o *CreateManualAccountRequestObject) GetClosedOn() CreateManualAccountRequestObjectClosedOn`

GetClosedOn returns the ClosedOn field if non-nil, zero value otherwise.

### GetClosedOnOk

`func (o *CreateManualAccountRequestObject) GetClosedOnOk() (*CreateManualAccountRequestObjectClosedOn, bool)`

GetClosedOnOk returns a tuple with the ClosedOn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClosedOn

`func (o *CreateManualAccountRequestObject) SetClosedOn(v CreateManualAccountRequestObjectClosedOn)`

SetClosedOn sets ClosedOn field to given value.

### HasClosedOn

`func (o *CreateManualAccountRequestObject) HasClosedOn() bool`

HasClosedOn returns a boolean if a field has been set.

### SetClosedOnNil

`func (o *CreateManualAccountRequestObject) SetClosedOnNil(b bool)`

 SetClosedOnNil sets the value for ClosedOn to be an explicit nil

### UnsetClosedOn
`func (o *CreateManualAccountRequestObject) UnsetClosedOn()`

UnsetClosedOn ensures that no value is present for ClosedOn, not even an explicit nil
### GetExternalId

`func (o *CreateManualAccountRequestObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *CreateManualAccountRequestObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *CreateManualAccountRequestObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.

### HasExternalId

`func (o *CreateManualAccountRequestObject) HasExternalId() bool`

HasExternalId returns a boolean if a field has been set.

### SetExternalIdNil

`func (o *CreateManualAccountRequestObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *CreateManualAccountRequestObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *CreateManualAccountRequestObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *CreateManualAccountRequestObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *CreateManualAccountRequestObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *CreateManualAccountRequestObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *CreateManualAccountRequestObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *CreateManualAccountRequestObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetExcludeFromTransactions

`func (o *CreateManualAccountRequestObject) GetExcludeFromTransactions() bool`

GetExcludeFromTransactions returns the ExcludeFromTransactions field if non-nil, zero value otherwise.

### GetExcludeFromTransactionsOk

`func (o *CreateManualAccountRequestObject) GetExcludeFromTransactionsOk() (*bool, bool)`

GetExcludeFromTransactionsOk returns a tuple with the ExcludeFromTransactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTransactions

`func (o *CreateManualAccountRequestObject) SetExcludeFromTransactions(v bool)`

SetExcludeFromTransactions sets ExcludeFromTransactions field to given value.

### HasExcludeFromTransactions

`func (o *CreateManualAccountRequestObject) HasExcludeFromTransactions() bool`

HasExcludeFromTransactions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


