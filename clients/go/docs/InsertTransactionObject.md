# InsertTransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Date** | **string** | Date of transaction in ISO 8601 format | 
**Amount** | [**InsertTransactionObjectAmount**](InsertTransactionObjectAmount.md) |  | 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format. Must match one of the [supported currencies](https://alpha.lunchmoney.dev/v2/currencies). If not set defaults to the user account&#39;s primary currency. | [optional] 
**Payee** | Pointer to **string** | Name of payee for the transaction | [optional] 
**OriginalName** | Pointer to **NullableString** | Original payee name. If not provided, defaults to &#x60;payee&#x60; value. | [optional] 
**CategoryId** | Pointer to **NullableInt32** | The ID of the category associated with the transactions. If set, the category ID must exist for the user&#39;s account and it cannot be a category group. | [optional] 
**Notes** | Pointer to **NullableString** | Any transaction notes set by the user or by a matched recurring item. This will match the value displayed in notes field on the transactions page in the GUI.  | [optional] 
**ManualAccountId** | Pointer to **NullableInt32** | The unique identifier for the associated manually managed account If set, this must match an existing manual account id associated with the user&#39;s account. If not set, and &#x60;plaid_account_id&#x60; is also not set, no account is associated with the transaction and it will appear as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. It is an error if this, and &#x60;plaid_account_id&#x60; is also set on the same transaction. | [optional] 
**PlaidAccountId** | Pointer to **NullableInt32** | The Unique identifier for the associated plaid synced account. If set, this must match an existing plaid account id associated with the user&#39;s account. If not set, and &#x60;manual_account_id&#x60; is also not set, no account is associated with the transaction and it will appear as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. It is an error if this, and &#x60;manual_account_id&#x60; is also set on the same transaction. In addition the specified plaid account must have the \&quot;Allow Modifications To Transactions\&quot; property set (which is enabled by default), or the insert will fail. | [optional] 
**RecurringId** | Pointer to **NullableInt32** | Unique identifier for associated recurring item. Recurring item must be associated with the same account. | [optional] 
**Status** | Pointer to **string** | If set must be either &#x60;reviewed&#x60; or &#x60;unreviewed&#x60;. If not set, defaults to &#x60;unreviewed&#x60;. | [optional] 
**TagIds** | Pointer to **[]int32** | A list of IDs for the tags associated with this transaction. Each ID must match an existing tag associated with the user&#39;s account. If not set, no tags will be associated with the created transaction. | [optional] 
**ExternalId** | Pointer to **NullableString** | A user-defined external ID for the transaction. If set, and &#x60;manual_account_id&#x60; is set, the creation of the new transaction will fail if a transaction with this id already exists for the specified manual account. | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | An optional JSON object that includes additional data related to this transaction. This must be a valid JSON object and, when stringified, must not exceed 4096 characters. This data may be available in the future for processing by rules. | [optional] 

## Methods

### NewInsertTransactionObject

`func NewInsertTransactionObject(date string, amount InsertTransactionObjectAmount, ) *InsertTransactionObject`

NewInsertTransactionObject instantiates a new InsertTransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInsertTransactionObjectWithDefaults

`func NewInsertTransactionObjectWithDefaults() *InsertTransactionObject`

NewInsertTransactionObjectWithDefaults instantiates a new InsertTransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDate

`func (o *InsertTransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *InsertTransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *InsertTransactionObject) SetDate(v string)`

SetDate sets Date field to given value.


### GetAmount

`func (o *InsertTransactionObject) GetAmount() InsertTransactionObjectAmount`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *InsertTransactionObject) GetAmountOk() (*InsertTransactionObjectAmount, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *InsertTransactionObject) SetAmount(v InsertTransactionObjectAmount)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *InsertTransactionObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *InsertTransactionObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *InsertTransactionObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *InsertTransactionObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetPayee

`func (o *InsertTransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *InsertTransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *InsertTransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *InsertTransactionObject) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### GetOriginalName

`func (o *InsertTransactionObject) GetOriginalName() string`

GetOriginalName returns the OriginalName field if non-nil, zero value otherwise.

### GetOriginalNameOk

`func (o *InsertTransactionObject) GetOriginalNameOk() (*string, bool)`

GetOriginalNameOk returns a tuple with the OriginalName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalName

`func (o *InsertTransactionObject) SetOriginalName(v string)`

SetOriginalName sets OriginalName field to given value.

### HasOriginalName

`func (o *InsertTransactionObject) HasOriginalName() bool`

HasOriginalName returns a boolean if a field has been set.

### SetOriginalNameNil

`func (o *InsertTransactionObject) SetOriginalNameNil(b bool)`

 SetOriginalNameNil sets the value for OriginalName to be an explicit nil

### UnsetOriginalName
`func (o *InsertTransactionObject) UnsetOriginalName()`

UnsetOriginalName ensures that no value is present for OriginalName, not even an explicit nil
### GetCategoryId

`func (o *InsertTransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *InsertTransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *InsertTransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *InsertTransactionObject) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### SetCategoryIdNil

`func (o *InsertTransactionObject) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *InsertTransactionObject) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetNotes

`func (o *InsertTransactionObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *InsertTransactionObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *InsertTransactionObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *InsertTransactionObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *InsertTransactionObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *InsertTransactionObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetManualAccountId

`func (o *InsertTransactionObject) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *InsertTransactionObject) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *InsertTransactionObject) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.

### HasManualAccountId

`func (o *InsertTransactionObject) HasManualAccountId() bool`

HasManualAccountId returns a boolean if a field has been set.

### SetManualAccountIdNil

`func (o *InsertTransactionObject) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *InsertTransactionObject) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil
### GetPlaidAccountId

`func (o *InsertTransactionObject) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *InsertTransactionObject) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *InsertTransactionObject) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.

### HasPlaidAccountId

`func (o *InsertTransactionObject) HasPlaidAccountId() bool`

HasPlaidAccountId returns a boolean if a field has been set.

### SetPlaidAccountIdNil

`func (o *InsertTransactionObject) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *InsertTransactionObject) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetRecurringId

`func (o *InsertTransactionObject) GetRecurringId() int32`

GetRecurringId returns the RecurringId field if non-nil, zero value otherwise.

### GetRecurringIdOk

`func (o *InsertTransactionObject) GetRecurringIdOk() (*int32, bool)`

GetRecurringIdOk returns a tuple with the RecurringId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringId

`func (o *InsertTransactionObject) SetRecurringId(v int32)`

SetRecurringId sets RecurringId field to given value.

### HasRecurringId

`func (o *InsertTransactionObject) HasRecurringId() bool`

HasRecurringId returns a boolean if a field has been set.

### SetRecurringIdNil

`func (o *InsertTransactionObject) SetRecurringIdNil(b bool)`

 SetRecurringIdNil sets the value for RecurringId to be an explicit nil

### UnsetRecurringId
`func (o *InsertTransactionObject) UnsetRecurringId()`

UnsetRecurringId ensures that no value is present for RecurringId, not even an explicit nil
### GetStatus

`func (o *InsertTransactionObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *InsertTransactionObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *InsertTransactionObject) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *InsertTransactionObject) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetTagIds

`func (o *InsertTransactionObject) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *InsertTransactionObject) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *InsertTransactionObject) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.

### HasTagIds

`func (o *InsertTransactionObject) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### GetExternalId

`func (o *InsertTransactionObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *InsertTransactionObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *InsertTransactionObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.

### HasExternalId

`func (o *InsertTransactionObject) HasExternalId() bool`

HasExternalId returns a boolean if a field has been set.

### SetExternalIdNil

`func (o *InsertTransactionObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *InsertTransactionObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *InsertTransactionObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *InsertTransactionObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *InsertTransactionObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *InsertTransactionObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *InsertTransactionObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *InsertTransactionObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


