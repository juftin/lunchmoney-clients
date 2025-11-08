# UpdateTransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int64** | System defined unique identifier of this transaction. Ignored if set. | [optional] 
**Date** | Pointer to **string** | Date of transaction in ISO 8601 format | [optional] 
**Amount** | Pointer to [**UpdateTransactionObjectAmount**](UpdateTransactionObjectAmount.md) |  | [optional] 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format.&lt;br&gt; May not be updated on transactions that belong to a synced account with the \&quot;Allow Modifications to Transactions\&quot; property disabled. | [optional] 
**RecurringId** | Pointer to **NullableInt32** | The unique identifier of the associated recurring item that this transaction matches. | [optional] 
**Payee** | Pointer to **string** | The new payee for the transaction.  | [optional] 
**CategoryId** | Pointer to **NullableInt32** | Unique identifier of the category for this transaction. Set this to 0 to clear the transaction&#39;s category. | [optional] 
**Notes** | Pointer to **NullableString** | New notes for the transaction. Set this to an empty string to clear the existing notes.  | [optional] 
**ManualAccountId** | Pointer to **NullableInt32** | The unique identifier of the manual account associated with this transaction. Set this to zero to disassociate the transaction with an account. If set &#x60;plaid_account_id&#x60; may not also be set to a non zero value. Moving an existing transaction to to another account will not work if the transaction belongs to a synced account who&#39;s \&quot;Allow Modifications to Transactions\&quot; property is not set. | [optional] 
**PlaidAccountId** | Pointer to **NullableInt32** | The unique identifier of the plaid account associated with this transaction. If set &#x60;manual_account_id&#x60; may not also be set to a non zero value. Moving an existing transaction to to an existing Plaid account will not work if the account&#39;s \&quot;Allow Modifications to Transactions\&quot; property is not set. | [optional] 
**TagIds** | Pointer to **[]int32** | A list of tag_ids for the tags associated with this transaction. If set, this property will overwrite any existing tags. Use &#x60;additional_tag_ids&#x60; to add tags to the existing transaction&#39;s tags. Set this to an empty array to remove all tags from a transaction. If set &#x60;additional_tag_ids&#x60; may not be set. | [optional] 
**AdditionalTagIds** | Pointer to **[]int32** | A list of tag_ids for the tags associated with this transaction. If set, the tags listed in this property be added to any existing transaction tags. Use &#x60;tag_ids&#x60; to overwrite or clear transaction tags. If set &#x60;tag_ids&#x60; may not be set. | [optional] 
**ExternalId** | Pointer to **NullableString** | A user-defined external ID for the transaction. The update will fail if the transaction does not also have a &#x60;manual_account_id&#x60; or if there is already an existing transaction with the same &#x60;manual_account_id&#x60;/&#x60;external_id&#x60; combination. | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | User defined JSON data that can be set or cleared via the API. | [optional] 
**Status** | Pointer to **string** | Status of the transaction, may be one of: - &#x60;reviewed&#x60;: User has reviewed the transaction, or it was automatically marked as reviewed due to reviewed recurring_item logic - &#x60;unreviewed&#x60;: User has not reviewed the transaction and it does not match any reviewed recurring_items.  | [optional] 
**ToBase** | Pointer to **float64** | System defined amount of this transaction in the user&#39;s primary currency. Ignored if set. | [optional] 
**IsPending** | Pointer to **bool** | System defined flag set for pending transactions. Ignored if set. | [optional] 
**PlaidMetadata** | Pointer to **map[string]interface{}** | System set metadata from a Plaid account sync. Ignored if set. | [optional] 
**CreatedAt** | Pointer to **time.Time** | System defined date and time of when the transaction was created. Ignored if set. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System defined date and time of when the transaction was last updated. Ignored if set. | [optional] 
**IsParent** | Pointer to **bool** | System defined boolean indicating if this transaction was split. To split or unsplit a transaction use the &#x60;/transactions/split&#x60; endpoint. Ignored if set. | [optional] 
**Children** | Pointer to [**[]ChildTransactionObject**](ChildTransactionObject.md) | An array of child transactions that exists when a transaction has been split or if the transaction is a group. Split and Grouped transactions may not be modified using this API. Ignored if set. | [optional] 
**ParentId** | Pointer to **NullableInt64** | A transaction ID if this is a split transaction. Split transactions may not be modified this API. Use the &#x60;transactions/split&#x60; endpoint instead. Ignored if set. | [optional] 
**IsGroup** | Pointer to **bool** | System defined boolean indicating if this transaction represents a group of transactions. Grouped transactions may not be modified with this API. Use the &#x60;transactions/group&#x60; endpoint instead. Ignored if set. | [optional] 
**GroupId** | Pointer to **NullableInt64** | A transaction group ID if this transaction is part of a group. Grouped transactions may not be modified with this API. Use the &#x60;transactions/group&#x60; endpoint instead. Ignored if set. | [optional] 
**Source** | Pointer to **NullableString** | System defined original source of the transaction. Ignored if set.  | [optional] 

## Methods

### NewUpdateTransactionObject

`func NewUpdateTransactionObject() *UpdateTransactionObject`

NewUpdateTransactionObject instantiates a new UpdateTransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateTransactionObjectWithDefaults

`func NewUpdateTransactionObjectWithDefaults() *UpdateTransactionObject`

NewUpdateTransactionObjectWithDefaults instantiates a new UpdateTransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateTransactionObject) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateTransactionObject) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateTransactionObject) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateTransactionObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetDate

`func (o *UpdateTransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *UpdateTransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *UpdateTransactionObject) SetDate(v string)`

SetDate sets Date field to given value.

### HasDate

`func (o *UpdateTransactionObject) HasDate() bool`

HasDate returns a boolean if a field has been set.

### GetAmount

`func (o *UpdateTransactionObject) GetAmount() UpdateTransactionObjectAmount`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *UpdateTransactionObject) GetAmountOk() (*UpdateTransactionObjectAmount, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *UpdateTransactionObject) SetAmount(v UpdateTransactionObjectAmount)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *UpdateTransactionObject) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCurrency

`func (o *UpdateTransactionObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *UpdateTransactionObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *UpdateTransactionObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *UpdateTransactionObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetRecurringId

`func (o *UpdateTransactionObject) GetRecurringId() int32`

GetRecurringId returns the RecurringId field if non-nil, zero value otherwise.

### GetRecurringIdOk

`func (o *UpdateTransactionObject) GetRecurringIdOk() (*int32, bool)`

GetRecurringIdOk returns a tuple with the RecurringId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringId

`func (o *UpdateTransactionObject) SetRecurringId(v int32)`

SetRecurringId sets RecurringId field to given value.

### HasRecurringId

`func (o *UpdateTransactionObject) HasRecurringId() bool`

HasRecurringId returns a boolean if a field has been set.

### SetRecurringIdNil

`func (o *UpdateTransactionObject) SetRecurringIdNil(b bool)`

 SetRecurringIdNil sets the value for RecurringId to be an explicit nil

### UnsetRecurringId
`func (o *UpdateTransactionObject) UnsetRecurringId()`

UnsetRecurringId ensures that no value is present for RecurringId, not even an explicit nil
### GetPayee

`func (o *UpdateTransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *UpdateTransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *UpdateTransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *UpdateTransactionObject) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### GetCategoryId

`func (o *UpdateTransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *UpdateTransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *UpdateTransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *UpdateTransactionObject) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### SetCategoryIdNil

`func (o *UpdateTransactionObject) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *UpdateTransactionObject) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetNotes

`func (o *UpdateTransactionObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *UpdateTransactionObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *UpdateTransactionObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *UpdateTransactionObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *UpdateTransactionObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *UpdateTransactionObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetManualAccountId

`func (o *UpdateTransactionObject) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *UpdateTransactionObject) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *UpdateTransactionObject) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.

### HasManualAccountId

`func (o *UpdateTransactionObject) HasManualAccountId() bool`

HasManualAccountId returns a boolean if a field has been set.

### SetManualAccountIdNil

`func (o *UpdateTransactionObject) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *UpdateTransactionObject) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil
### GetPlaidAccountId

`func (o *UpdateTransactionObject) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *UpdateTransactionObject) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *UpdateTransactionObject) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.

### HasPlaidAccountId

`func (o *UpdateTransactionObject) HasPlaidAccountId() bool`

HasPlaidAccountId returns a boolean if a field has been set.

### SetPlaidAccountIdNil

`func (o *UpdateTransactionObject) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *UpdateTransactionObject) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetTagIds

`func (o *UpdateTransactionObject) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *UpdateTransactionObject) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *UpdateTransactionObject) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.

### HasTagIds

`func (o *UpdateTransactionObject) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### GetAdditionalTagIds

`func (o *UpdateTransactionObject) GetAdditionalTagIds() []int32`

GetAdditionalTagIds returns the AdditionalTagIds field if non-nil, zero value otherwise.

### GetAdditionalTagIdsOk

`func (o *UpdateTransactionObject) GetAdditionalTagIdsOk() (*[]int32, bool)`

GetAdditionalTagIdsOk returns a tuple with the AdditionalTagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalTagIds

`func (o *UpdateTransactionObject) SetAdditionalTagIds(v []int32)`

SetAdditionalTagIds sets AdditionalTagIds field to given value.

### HasAdditionalTagIds

`func (o *UpdateTransactionObject) HasAdditionalTagIds() bool`

HasAdditionalTagIds returns a boolean if a field has been set.

### GetExternalId

`func (o *UpdateTransactionObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *UpdateTransactionObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *UpdateTransactionObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.

### HasExternalId

`func (o *UpdateTransactionObject) HasExternalId() bool`

HasExternalId returns a boolean if a field has been set.

### SetExternalIdNil

`func (o *UpdateTransactionObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *UpdateTransactionObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *UpdateTransactionObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *UpdateTransactionObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *UpdateTransactionObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *UpdateTransactionObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *UpdateTransactionObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *UpdateTransactionObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetStatus

`func (o *UpdateTransactionObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateTransactionObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateTransactionObject) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateTransactionObject) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetToBase

`func (o *UpdateTransactionObject) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *UpdateTransactionObject) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *UpdateTransactionObject) SetToBase(v float64)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *UpdateTransactionObject) HasToBase() bool`

HasToBase returns a boolean if a field has been set.

### GetIsPending

`func (o *UpdateTransactionObject) GetIsPending() bool`

GetIsPending returns the IsPending field if non-nil, zero value otherwise.

### GetIsPendingOk

`func (o *UpdateTransactionObject) GetIsPendingOk() (*bool, bool)`

GetIsPendingOk returns a tuple with the IsPending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPending

`func (o *UpdateTransactionObject) SetIsPending(v bool)`

SetIsPending sets IsPending field to given value.

### HasIsPending

`func (o *UpdateTransactionObject) HasIsPending() bool`

HasIsPending returns a boolean if a field has been set.

### GetPlaidMetadata

`func (o *UpdateTransactionObject) GetPlaidMetadata() map[string]interface{}`

GetPlaidMetadata returns the PlaidMetadata field if non-nil, zero value otherwise.

### GetPlaidMetadataOk

`func (o *UpdateTransactionObject) GetPlaidMetadataOk() (*map[string]interface{}, bool)`

GetPlaidMetadataOk returns a tuple with the PlaidMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidMetadata

`func (o *UpdateTransactionObject) SetPlaidMetadata(v map[string]interface{})`

SetPlaidMetadata sets PlaidMetadata field to given value.

### HasPlaidMetadata

`func (o *UpdateTransactionObject) HasPlaidMetadata() bool`

HasPlaidMetadata returns a boolean if a field has been set.

### SetPlaidMetadataNil

`func (o *UpdateTransactionObject) SetPlaidMetadataNil(b bool)`

 SetPlaidMetadataNil sets the value for PlaidMetadata to be an explicit nil

### UnsetPlaidMetadata
`func (o *UpdateTransactionObject) UnsetPlaidMetadata()`

UnsetPlaidMetadata ensures that no value is present for PlaidMetadata, not even an explicit nil
### GetCreatedAt

`func (o *UpdateTransactionObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateTransactionObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateTransactionObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateTransactionObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *UpdateTransactionObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateTransactionObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateTransactionObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateTransactionObject) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetIsParent

`func (o *UpdateTransactionObject) GetIsParent() bool`

GetIsParent returns the IsParent field if non-nil, zero value otherwise.

### GetIsParentOk

`func (o *UpdateTransactionObject) GetIsParentOk() (*bool, bool)`

GetIsParentOk returns a tuple with the IsParent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsParent

`func (o *UpdateTransactionObject) SetIsParent(v bool)`

SetIsParent sets IsParent field to given value.

### HasIsParent

`func (o *UpdateTransactionObject) HasIsParent() bool`

HasIsParent returns a boolean if a field has been set.

### GetChildren

`func (o *UpdateTransactionObject) GetChildren() []ChildTransactionObject`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *UpdateTransactionObject) GetChildrenOk() (*[]ChildTransactionObject, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *UpdateTransactionObject) SetChildren(v []ChildTransactionObject)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *UpdateTransactionObject) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetParentId

`func (o *UpdateTransactionObject) GetParentId() int64`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *UpdateTransactionObject) GetParentIdOk() (*int64, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *UpdateTransactionObject) SetParentId(v int64)`

SetParentId sets ParentId field to given value.

### HasParentId

`func (o *UpdateTransactionObject) HasParentId() bool`

HasParentId returns a boolean if a field has been set.

### SetParentIdNil

`func (o *UpdateTransactionObject) SetParentIdNil(b bool)`

 SetParentIdNil sets the value for ParentId to be an explicit nil

### UnsetParentId
`func (o *UpdateTransactionObject) UnsetParentId()`

UnsetParentId ensures that no value is present for ParentId, not even an explicit nil
### GetIsGroup

`func (o *UpdateTransactionObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *UpdateTransactionObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *UpdateTransactionObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.

### HasIsGroup

`func (o *UpdateTransactionObject) HasIsGroup() bool`

HasIsGroup returns a boolean if a field has been set.

### GetGroupId

`func (o *UpdateTransactionObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *UpdateTransactionObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *UpdateTransactionObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.

### HasGroupId

`func (o *UpdateTransactionObject) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupIdNil

`func (o *UpdateTransactionObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *UpdateTransactionObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetSource

`func (o *UpdateTransactionObject) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *UpdateTransactionObject) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *UpdateTransactionObject) SetSource(v string)`

SetSource sets Source field to given value.

### HasSource

`func (o *UpdateTransactionObject) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *UpdateTransactionObject) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *UpdateTransactionObject) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


