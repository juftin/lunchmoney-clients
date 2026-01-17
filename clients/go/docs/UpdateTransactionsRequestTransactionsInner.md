# UpdateTransactionsRequestTransactionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int64** | The ID of the transaction to update | 
**Date** | Pointer to **string** | Date of transaction in ISO 8601 format | [optional] 
**Amount** | Pointer to [**UpdateTransactionObjectAmount**](UpdateTransactionObjectAmount.md) |  | [optional] 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format.&lt;br&gt; May not be updated on transactions that belong to a synced account with the \&quot;Allow Modifications to Transactions\&quot; property disabled. | [optional] 
**RecurringId** | Pointer to **NullableInt32** | The unique identifier of the associated recurring item that this transaction matches. | [optional] 
**Payee** | Pointer to **string** | The new payee for the transaction.  | [optional] 
**CategoryId** | Pointer to **NullableInt32** | Unique identifier of the category for this transaction. Set this to null to clear the transaction&#39;s category. | [optional] 
**Notes** | Pointer to **NullableString** | New notes for the transaction. Set this to an empty string to clear the existing notes.  | [optional] 
**ManualAccountId** | Pointer to **NullableInt32** | The unique identifier of the manual account associated with this transaction. Set this to null to disassociate the transaction with an account. If set &#x60;plaid_account_id&#x60; may not also be set to a non null value. Moving an existing transaction to to another account will not work if the transaction belongs to a synced account who&#39;s \&quot;Allow Modifications to Transactions\&quot; property is not set. | [optional] 
**PlaidAccountId** | Pointer to **NullableInt32** | The unique identifier of the plaid account associated with this transaction. If set &#x60;manual_account_id&#x60; may not also be set to a non null value. Attempting to modify this on a transaction associated with a Plaid account will not work if the account&#39;s \&quot;Allow Modifications to Transactions\&quot; property is not set. Similarly, this cannot be set to an id associated with this type of locked Plaid account. | [optional] 
**TagIds** | Pointer to **[]int32** | A list of tag_ids for the tags associated with this transaction. If set, this property will overwrite any existing tags. Use &#x60;additional_tag_ids&#x60; to add tags to the existing transaction&#39;s tags. Set this to an empty array to remove all tags from a transaction. If set &#x60;additional_tag_ids&#x60; may not be set. | [optional] 
**AdditionalTagIds** | Pointer to **[]int32** | A list of tag_ids for the tags associated with this transaction. If set, the tags listed in this property be added to any existing transaction tags. Use &#x60;tag_ids&#x60; to overwrite or clear transaction tags. If set &#x60;tag_ids&#x60; may not be set. | [optional] 
**ExternalId** | Pointer to **NullableString** | A user-defined external ID for the transaction. The update will fail if the transaction does not also have a &#x60;manual_account_id&#x60; or if there is already an existing transaction with the same &#x60;manual_account_id&#x60;/&#x60;external_id&#x60; combination. | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | User defined JSON data that can be set or cleared via the API. | [optional] 
**Status** | Pointer to **string** | Status of the transaction, may be one of: - &#x60;reviewed&#x60;: User has reviewed the transaction, or it was automatically marked as reviewed due to reviewed recurring_item logic - &#x60;unreviewed&#x60;: User has not reviewed the transaction and it does not match any reviewed recurring_items.  | [optional] 
**ToBase** | Pointer to **float64** | System defined amount of this transaction in the user&#39;s primary currency. Ignored if set. Use &#x60;amount&#x60; to update the amount in the transaction. | [optional] 
**IsPending** | Pointer to **bool** | System defined flag set for pending transactions. Ignored if set. | [optional] 
**PlaidMetadata** | Pointer to **map[string]interface{}** | System set metadata from a Plaid account sync. Ignored if set. | [optional] 
**CreatedAt** | Pointer to **time.Time** | System defined date and time of when the transaction was created. Ignored if set. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System defined date and time of when the transaction was last updated. Ignored if set. | [optional] 
**IsSplitParent** | Pointer to **bool** | System defined boolean indicating if this transaction was split. To split or unsplit a transaction use the &#x60;/transactions/split&#x60; endpoint. Ignored if set. | [optional] 
**Children** | Pointer to [**[]ChildTransactionObject**](ChildTransactionObject.md) | An array of child transactions that exists when a transaction has been split or if the transaction is a group. Split | [optional] 
**SplitParentId** | Pointer to **NullableInt64** | A transaction ID if this is a split transaction. Split transactions may not be modified this API. Use the &#x60;transactions/split&#x60; endpoint instead. Ignored if set. | [optional] 
**IsGroupParent** | Pointer to **bool** | System defined boolean indicating if this transaction represents a group of transactions. Grouped transactions may not be modified with this API. Use the &#x60;transactions/group&#x60; endpoint instead. Ignored if set. | [optional] 
**GroupParentId** | Pointer to **NullableInt64** | A transaction group ID if this transaction is part of a group. Grouped transactions may not be modified with this API. Use the &#x60;transactions/group&#x60; endpoint instead. Ignored if set. | [optional] 
**Source** | Pointer to **NullableString** | System defined original source of the transaction. Ignored if set.  | [optional] 

## Methods

### NewUpdateTransactionsRequestTransactionsInner

`func NewUpdateTransactionsRequestTransactionsInner(id int64, ) *UpdateTransactionsRequestTransactionsInner`

NewUpdateTransactionsRequestTransactionsInner instantiates a new UpdateTransactionsRequestTransactionsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateTransactionsRequestTransactionsInnerWithDefaults

`func NewUpdateTransactionsRequestTransactionsInnerWithDefaults() *UpdateTransactionsRequestTransactionsInner`

NewUpdateTransactionsRequestTransactionsInnerWithDefaults instantiates a new UpdateTransactionsRequestTransactionsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateTransactionsRequestTransactionsInner) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateTransactionsRequestTransactionsInner) SetId(v int64)`

SetId sets Id field to given value.


### GetDate

`func (o *UpdateTransactionsRequestTransactionsInner) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *UpdateTransactionsRequestTransactionsInner) SetDate(v string)`

SetDate sets Date field to given value.

### HasDate

`func (o *UpdateTransactionsRequestTransactionsInner) HasDate() bool`

HasDate returns a boolean if a field has been set.

### GetAmount

`func (o *UpdateTransactionsRequestTransactionsInner) GetAmount() UpdateTransactionObjectAmount`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetAmountOk() (*UpdateTransactionObjectAmount, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *UpdateTransactionsRequestTransactionsInner) SetAmount(v UpdateTransactionObjectAmount)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *UpdateTransactionsRequestTransactionsInner) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCurrency

`func (o *UpdateTransactionsRequestTransactionsInner) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *UpdateTransactionsRequestTransactionsInner) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *UpdateTransactionsRequestTransactionsInner) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetRecurringId

`func (o *UpdateTransactionsRequestTransactionsInner) GetRecurringId() int32`

GetRecurringId returns the RecurringId field if non-nil, zero value otherwise.

### GetRecurringIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetRecurringIdOk() (*int32, bool)`

GetRecurringIdOk returns a tuple with the RecurringId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringId

`func (o *UpdateTransactionsRequestTransactionsInner) SetRecurringId(v int32)`

SetRecurringId sets RecurringId field to given value.

### HasRecurringId

`func (o *UpdateTransactionsRequestTransactionsInner) HasRecurringId() bool`

HasRecurringId returns a boolean if a field has been set.

### SetRecurringIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetRecurringIdNil(b bool)`

 SetRecurringIdNil sets the value for RecurringId to be an explicit nil

### UnsetRecurringId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetRecurringId()`

UnsetRecurringId ensures that no value is present for RecurringId, not even an explicit nil
### GetPayee

`func (o *UpdateTransactionsRequestTransactionsInner) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *UpdateTransactionsRequestTransactionsInner) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *UpdateTransactionsRequestTransactionsInner) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### GetCategoryId

`func (o *UpdateTransactionsRequestTransactionsInner) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *UpdateTransactionsRequestTransactionsInner) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *UpdateTransactionsRequestTransactionsInner) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### SetCategoryIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetNotes

`func (o *UpdateTransactionsRequestTransactionsInner) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *UpdateTransactionsRequestTransactionsInner) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *UpdateTransactionsRequestTransactionsInner) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetManualAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.

### HasManualAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) HasManualAccountId() bool`

HasManualAccountId returns a boolean if a field has been set.

### SetManualAccountIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil
### GetPlaidAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.

### HasPlaidAccountId

`func (o *UpdateTransactionsRequestTransactionsInner) HasPlaidAccountId() bool`

HasPlaidAccountId returns a boolean if a field has been set.

### SetPlaidAccountIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.

### HasTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### GetAdditionalTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) GetAdditionalTagIds() []int32`

GetAdditionalTagIds returns the AdditionalTagIds field if non-nil, zero value otherwise.

### GetAdditionalTagIdsOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetAdditionalTagIdsOk() (*[]int32, bool)`

GetAdditionalTagIdsOk returns a tuple with the AdditionalTagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) SetAdditionalTagIds(v []int32)`

SetAdditionalTagIds sets AdditionalTagIds field to given value.

### HasAdditionalTagIds

`func (o *UpdateTransactionsRequestTransactionsInner) HasAdditionalTagIds() bool`

HasAdditionalTagIds returns a boolean if a field has been set.

### GetExternalId

`func (o *UpdateTransactionsRequestTransactionsInner) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *UpdateTransactionsRequestTransactionsInner) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.

### HasExternalId

`func (o *UpdateTransactionsRequestTransactionsInner) HasExternalId() bool`

HasExternalId returns a boolean if a field has been set.

### SetExternalIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetCustomMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetStatus

`func (o *UpdateTransactionsRequestTransactionsInner) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateTransactionsRequestTransactionsInner) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateTransactionsRequestTransactionsInner) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetToBase

`func (o *UpdateTransactionsRequestTransactionsInner) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *UpdateTransactionsRequestTransactionsInner) SetToBase(v float64)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *UpdateTransactionsRequestTransactionsInner) HasToBase() bool`

HasToBase returns a boolean if a field has been set.

### GetIsPending

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsPending() bool`

GetIsPending returns the IsPending field if non-nil, zero value otherwise.

### GetIsPendingOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsPendingOk() (*bool, bool)`

GetIsPendingOk returns a tuple with the IsPending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPending

`func (o *UpdateTransactionsRequestTransactionsInner) SetIsPending(v bool)`

SetIsPending sets IsPending field to given value.

### HasIsPending

`func (o *UpdateTransactionsRequestTransactionsInner) HasIsPending() bool`

HasIsPending returns a boolean if a field has been set.

### GetPlaidMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) GetPlaidMetadata() map[string]interface{}`

GetPlaidMetadata returns the PlaidMetadata field if non-nil, zero value otherwise.

### GetPlaidMetadataOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetPlaidMetadataOk() (*map[string]interface{}, bool)`

GetPlaidMetadataOk returns a tuple with the PlaidMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) SetPlaidMetadata(v map[string]interface{})`

SetPlaidMetadata sets PlaidMetadata field to given value.

### HasPlaidMetadata

`func (o *UpdateTransactionsRequestTransactionsInner) HasPlaidMetadata() bool`

HasPlaidMetadata returns a boolean if a field has been set.

### SetPlaidMetadataNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetPlaidMetadataNil(b bool)`

 SetPlaidMetadataNil sets the value for PlaidMetadata to be an explicit nil

### UnsetPlaidMetadata
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetPlaidMetadata()`

UnsetPlaidMetadata ensures that no value is present for PlaidMetadata, not even an explicit nil
### GetCreatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateTransactionsRequestTransactionsInner) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetIsSplitParent

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsSplitParent() bool`

GetIsSplitParent returns the IsSplitParent field if non-nil, zero value otherwise.

### GetIsSplitParentOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsSplitParentOk() (*bool, bool)`

GetIsSplitParentOk returns a tuple with the IsSplitParent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsSplitParent

`func (o *UpdateTransactionsRequestTransactionsInner) SetIsSplitParent(v bool)`

SetIsSplitParent sets IsSplitParent field to given value.

### HasIsSplitParent

`func (o *UpdateTransactionsRequestTransactionsInner) HasIsSplitParent() bool`

HasIsSplitParent returns a boolean if a field has been set.

### GetChildren

`func (o *UpdateTransactionsRequestTransactionsInner) GetChildren() []ChildTransactionObject`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetChildrenOk() (*[]ChildTransactionObject, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *UpdateTransactionsRequestTransactionsInner) SetChildren(v []ChildTransactionObject)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *UpdateTransactionsRequestTransactionsInner) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetSplitParentId

`func (o *UpdateTransactionsRequestTransactionsInner) GetSplitParentId() int64`

GetSplitParentId returns the SplitParentId field if non-nil, zero value otherwise.

### GetSplitParentIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetSplitParentIdOk() (*int64, bool)`

GetSplitParentIdOk returns a tuple with the SplitParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSplitParentId

`func (o *UpdateTransactionsRequestTransactionsInner) SetSplitParentId(v int64)`

SetSplitParentId sets SplitParentId field to given value.

### HasSplitParentId

`func (o *UpdateTransactionsRequestTransactionsInner) HasSplitParentId() bool`

HasSplitParentId returns a boolean if a field has been set.

### SetSplitParentIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetSplitParentIdNil(b bool)`

 SetSplitParentIdNil sets the value for SplitParentId to be an explicit nil

### UnsetSplitParentId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetSplitParentId()`

UnsetSplitParentId ensures that no value is present for SplitParentId, not even an explicit nil
### GetIsGroupParent

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsGroupParent() bool`

GetIsGroupParent returns the IsGroupParent field if non-nil, zero value otherwise.

### GetIsGroupParentOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetIsGroupParentOk() (*bool, bool)`

GetIsGroupParentOk returns a tuple with the IsGroupParent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroupParent

`func (o *UpdateTransactionsRequestTransactionsInner) SetIsGroupParent(v bool)`

SetIsGroupParent sets IsGroupParent field to given value.

### HasIsGroupParent

`func (o *UpdateTransactionsRequestTransactionsInner) HasIsGroupParent() bool`

HasIsGroupParent returns a boolean if a field has been set.

### GetGroupParentId

`func (o *UpdateTransactionsRequestTransactionsInner) GetGroupParentId() int64`

GetGroupParentId returns the GroupParentId field if non-nil, zero value otherwise.

### GetGroupParentIdOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetGroupParentIdOk() (*int64, bool)`

GetGroupParentIdOk returns a tuple with the GroupParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupParentId

`func (o *UpdateTransactionsRequestTransactionsInner) SetGroupParentId(v int64)`

SetGroupParentId sets GroupParentId field to given value.

### HasGroupParentId

`func (o *UpdateTransactionsRequestTransactionsInner) HasGroupParentId() bool`

HasGroupParentId returns a boolean if a field has been set.

### SetGroupParentIdNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetGroupParentIdNil(b bool)`

 SetGroupParentIdNil sets the value for GroupParentId to be an explicit nil

### UnsetGroupParentId
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetGroupParentId()`

UnsetGroupParentId ensures that no value is present for GroupParentId, not even an explicit nil
### GetSource

`func (o *UpdateTransactionsRequestTransactionsInner) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *UpdateTransactionsRequestTransactionsInner) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *UpdateTransactionsRequestTransactionsInner) SetSource(v string)`

SetSource sets Source field to given value.

### HasSource

`func (o *UpdateTransactionsRequestTransactionsInner) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *UpdateTransactionsRequestTransactionsInner) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *UpdateTransactionsRequestTransactionsInner) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


