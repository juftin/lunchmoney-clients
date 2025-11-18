# TransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int64** | System created unique identifier for transaction | 
**Date** | **string** | Date of transaction in ISO 8601 format | 
**Amount** | **string** | Amount of the transaction in numeric format to 4 decimal places. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format. | 
**ToBase** | **float64** | The amount converted to the user&#39;s primary currency. If the multi-currency feature is not being used, to_base and amount will be the same. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**RecurringId** | **NullableInt32** | The unique identifier of the associated recurring item that this transaction matched. | 
**Payee** | **string** | Name of payee set by the user, the financial institution, or by a matched recurring item. This will match the value displayed in payee field on the transactions page in the GUI.  | 
**CategoryId** | **NullableInt32** | Unique identifier of associated category set by the user or by a matched recurring_item.&lt;br&gt; Category details can be obtained by passing the value of this property to the [Get A Single Category](../operations/getCategoryById) API | 
**PlaidAccountId** | **NullableInt32** | The unique identifier of the plaid account associated with this transaction. This will always be null if this transaction is associated with a manual account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**ManualAccountId** | **NullableInt32** | The unique identifier of the manual account associated with this transaction. This will always be null if this transaction is associated with a synced account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**ExternalId** | **NullableString** | A user-defined external ID for any transaction that was added via csv import, &#x60;POST /transactions&#x60; API call, or manually added via the Lunch Money GUI. No external ID exists for transactions associated with synced accounts, and they cannot be added. For transactions associated with manual accounts, the external ID must be unique as attempts to add a subsequent transaction with the same external_id and manual_account_id will be flagged as duplicates and fail. | 
**TagIds** | **[]int32** | A list of tag_ids for the tags associated with this transaction. If the transaction has no tags this will be an empty list.&lt;br&gt; Tag details can be obtained by passing the value of this attribute as the &#x60;ids&#x60; query parameter to the [List Tags](../operations/getTags) API | 
**Notes** | **NullableString** | Any transaction notes set by the user or by a matched recurring item. This will match the value displayed in notes field on the transactions page in the GUI.  | 
**Status** | **string** | Status of the transaction: - &#x60;reviewed&#x60;: User has reviewed the transaction, or it was automatically marked as reviewed due to reviewed recurring_item logic - &#x60;unreviewed&#x60;: User has not reviewed the transaction and it does not match any reviewed recurring_items. Note that any transactions where &#x60;is_pending&#x60; is true will be returned with a status of unreviewed. - &#x60;delete_pending&#x60;: The synced account deleted this transaction after it was updated by the user. Requires manual intervention.  | 
**IsPending** | **bool** | Denotes if the transaction is pending (not posted). Applies only to transactions in synced accounts and will always be false for transactions associated with manual accounts. | 
**CreatedAt** | **time.Time** | The date and time of when the transaction was created (in the ISO 8601 extended format). | 
**UpdatedAt** | **time.Time** | The date and time of when the transaction was last updated (in the ISO 8601 extended format). | 
**IsParent** | Pointer to **bool** | If &#x60;true&#x60;, this transaction has been split into two or more other transactions. By default, parent transactions are not returned in call to &#x60;GET /transactions&#x60; but they can be queried directly by their ID. | [optional] 
**ParentId** | **NullableInt64** | A transaction ID if this is a split transaction. Denotes the transaction ID of the original, or parent, transaction. Is null if this is not a split transaction | 
**IsGroup** | **bool** | &#x60;true&#x60; if this transaction represents a group of transactions. If so, amount and currency represent the totalled amount of transactions bearing this transaction&#39;s id as their group_id. Amount is calculated based on the user&#39;s primary currency. | 
**GroupId** | **NullableInt64** | Is set if this transaction is part of a group. Denotes the ID of the grouped transaction this is now included in. By default the transactions that were grouped are not returned in a call to &#x60;GET /transactions&#x60; but they can be queried directly by calling the &#x60;GET /transactions/group/{id}&#x60;, where the id passed is associated with a transaction where the &#x60;is_group&#x60; attribute is true | 
**Children** | Pointer to [**[]ChildTransactionObject**](ChildTransactionObject.md) | Exists only for transactions which are the parent of a split transaction or for transaction groups. It will not exist in the response unless the &#x60;include_children&#x60; query parameter is set to &#x60;true&#x60;.&lt;br&gt; For parents of split transactions, it contains a list of the associated transactions that it was split into. For transaction groups, it contains the transactions that were grouped together. Examine the &#x60;is_parent&#x60; and &#x60;is_group&#x60; properties to determine which of these it is. | [optional] 
**PlaidMetadata** | Pointer to **map[string]interface{}** | If requested, the transaction&#39;s plaid_metadata that came when this transaction was obtained. This will be a json object, but the schema is variable. This is only present when the &#x60;include_metadata&#x60; query parameter is set to true. | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | If requested, the transaction&#39;s custom_metadata that was included when the transaction was inserted via the API. This will be a json object, but the schema is variable. This is only present when the &#x60;include_metadata&#x60; query parameter is set to true. | [optional] 
**Files** | Pointer to [**[]TransactionAttachmentObject**](TransactionAttachmentObject.md) | A list of objects that describe any attachments to the Transactions. This is only present when the &#x60;include_files&#x60; query parameter is set to true. | [optional] 
**Source** | **NullableString** | Source of the transaction: - &#x60;api&#x60;: Transaction was added by a call to the [POST /transactions](../operations/createTransaction) API - &#x60;csv&#x60;: Transaction was added via a CSV Import - &#x60;manual&#x60;: Transaction was created via the \&quot;Add to Cash\&quot; button on the Transactions page - &#x60;merge&#x60;: Transactions were originally in an account that was merged into another account - &#x60;plaid&#x60;: Transaction came from a Financial Institution synced via Plaid - &#x60;recurring&#x60;: Transaction was created from the Recurring page - &#x60;rule&#x60;: Transaction was created by a rule to split a transaction - &#x60;split&#x60;: Transaction was created by splitting another transaction - &#x60;user&#x60;: This is a legacy value and is replaced by either csv or manual  | 

## Methods

### NewTransactionObject

`func NewTransactionObject(id int64, date string, amount string, currency CurrencyEnum, toBase float64, recurringId NullableInt32, payee string, categoryId NullableInt32, plaidAccountId NullableInt32, manualAccountId NullableInt32, externalId NullableString, tagIds []int32, notes NullableString, status string, isPending bool, createdAt time.Time, updatedAt time.Time, parentId NullableInt64, isGroup bool, groupId NullableInt64, source NullableString, ) *TransactionObject`

NewTransactionObject instantiates a new TransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransactionObjectWithDefaults

`func NewTransactionObjectWithDefaults() *TransactionObject`

NewTransactionObjectWithDefaults instantiates a new TransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TransactionObject) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TransactionObject) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TransactionObject) SetId(v int64)`

SetId sets Id field to given value.


### GetDate

`func (o *TransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *TransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *TransactionObject) SetDate(v string)`

SetDate sets Date field to given value.


### GetAmount

`func (o *TransactionObject) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *TransactionObject) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *TransactionObject) SetAmount(v string)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *TransactionObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *TransactionObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *TransactionObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *TransactionObject) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *TransactionObject) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *TransactionObject) SetToBase(v float64)`

SetToBase sets ToBase field to given value.


### GetRecurringId

`func (o *TransactionObject) GetRecurringId() int32`

GetRecurringId returns the RecurringId field if non-nil, zero value otherwise.

### GetRecurringIdOk

`func (o *TransactionObject) GetRecurringIdOk() (*int32, bool)`

GetRecurringIdOk returns a tuple with the RecurringId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringId

`func (o *TransactionObject) SetRecurringId(v int32)`

SetRecurringId sets RecurringId field to given value.


### SetRecurringIdNil

`func (o *TransactionObject) SetRecurringIdNil(b bool)`

 SetRecurringIdNil sets the value for RecurringId to be an explicit nil

### UnsetRecurringId
`func (o *TransactionObject) UnsetRecurringId()`

UnsetRecurringId ensures that no value is present for RecurringId, not even an explicit nil
### GetPayee

`func (o *TransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *TransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *TransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.


### GetCategoryId

`func (o *TransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *TransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *TransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### SetCategoryIdNil

`func (o *TransactionObject) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *TransactionObject) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetPlaidAccountId

`func (o *TransactionObject) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *TransactionObject) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *TransactionObject) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.


### SetPlaidAccountIdNil

`func (o *TransactionObject) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *TransactionObject) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetManualAccountId

`func (o *TransactionObject) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *TransactionObject) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *TransactionObject) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.


### SetManualAccountIdNil

`func (o *TransactionObject) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *TransactionObject) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil
### GetExternalId

`func (o *TransactionObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *TransactionObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *TransactionObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.


### SetExternalIdNil

`func (o *TransactionObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *TransactionObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetTagIds

`func (o *TransactionObject) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *TransactionObject) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *TransactionObject) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.


### GetNotes

`func (o *TransactionObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *TransactionObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *TransactionObject) SetNotes(v string)`

SetNotes sets Notes field to given value.


### SetNotesNil

`func (o *TransactionObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *TransactionObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetStatus

`func (o *TransactionObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TransactionObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TransactionObject) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetIsPending

`func (o *TransactionObject) GetIsPending() bool`

GetIsPending returns the IsPending field if non-nil, zero value otherwise.

### GetIsPendingOk

`func (o *TransactionObject) GetIsPendingOk() (*bool, bool)`

GetIsPendingOk returns a tuple with the IsPending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPending

`func (o *TransactionObject) SetIsPending(v bool)`

SetIsPending sets IsPending field to given value.


### GetCreatedAt

`func (o *TransactionObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TransactionObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TransactionObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *TransactionObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *TransactionObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *TransactionObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetIsParent

`func (o *TransactionObject) GetIsParent() bool`

GetIsParent returns the IsParent field if non-nil, zero value otherwise.

### GetIsParentOk

`func (o *TransactionObject) GetIsParentOk() (*bool, bool)`

GetIsParentOk returns a tuple with the IsParent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsParent

`func (o *TransactionObject) SetIsParent(v bool)`

SetIsParent sets IsParent field to given value.

### HasIsParent

`func (o *TransactionObject) HasIsParent() bool`

HasIsParent returns a boolean if a field has been set.

### GetParentId

`func (o *TransactionObject) GetParentId() int64`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *TransactionObject) GetParentIdOk() (*int64, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *TransactionObject) SetParentId(v int64)`

SetParentId sets ParentId field to given value.


### SetParentIdNil

`func (o *TransactionObject) SetParentIdNil(b bool)`

 SetParentIdNil sets the value for ParentId to be an explicit nil

### UnsetParentId
`func (o *TransactionObject) UnsetParentId()`

UnsetParentId ensures that no value is present for ParentId, not even an explicit nil
### GetIsGroup

`func (o *TransactionObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *TransactionObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *TransactionObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetGroupId

`func (o *TransactionObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *TransactionObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *TransactionObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.


### SetGroupIdNil

`func (o *TransactionObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *TransactionObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetChildren

`func (o *TransactionObject) GetChildren() []ChildTransactionObject`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *TransactionObject) GetChildrenOk() (*[]ChildTransactionObject, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *TransactionObject) SetChildren(v []ChildTransactionObject)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *TransactionObject) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetPlaidMetadata

`func (o *TransactionObject) GetPlaidMetadata() map[string]interface{}`

GetPlaidMetadata returns the PlaidMetadata field if non-nil, zero value otherwise.

### GetPlaidMetadataOk

`func (o *TransactionObject) GetPlaidMetadataOk() (*map[string]interface{}, bool)`

GetPlaidMetadataOk returns a tuple with the PlaidMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidMetadata

`func (o *TransactionObject) SetPlaidMetadata(v map[string]interface{})`

SetPlaidMetadata sets PlaidMetadata field to given value.

### HasPlaidMetadata

`func (o *TransactionObject) HasPlaidMetadata() bool`

HasPlaidMetadata returns a boolean if a field has been set.

### SetPlaidMetadataNil

`func (o *TransactionObject) SetPlaidMetadataNil(b bool)`

 SetPlaidMetadataNil sets the value for PlaidMetadata to be an explicit nil

### UnsetPlaidMetadata
`func (o *TransactionObject) UnsetPlaidMetadata()`

UnsetPlaidMetadata ensures that no value is present for PlaidMetadata, not even an explicit nil
### GetCustomMetadata

`func (o *TransactionObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *TransactionObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *TransactionObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *TransactionObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *TransactionObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *TransactionObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetFiles

`func (o *TransactionObject) GetFiles() []TransactionAttachmentObject`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *TransactionObject) GetFilesOk() (*[]TransactionAttachmentObject, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *TransactionObject) SetFiles(v []TransactionAttachmentObject)`

SetFiles sets Files field to given value.

### HasFiles

`func (o *TransactionObject) HasFiles() bool`

HasFiles returns a boolean if a field has been set.

### GetSource

`func (o *TransactionObject) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *TransactionObject) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *TransactionObject) SetSource(v string)`

SetSource sets Source field to given value.


### SetSourceNil

`func (o *TransactionObject) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *TransactionObject) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


