# ChildTransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int64** | System created unique identifier for transaction | 
**Date** | **string** | Date of transaction in ISO 8601 format | 
**Amount** | **string** | Amount of the transaction in numeric format to 4 decimal places. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format | 
**ToBase** | **float64** | The amount converted to the user&#39;s primary currency. If the transaction currency is the same as the user&#39;s primary currency, to_base and amount will be the same. Positive values indicate a debit transaction, negative values indicate a credit transaction. | 
**RecurringId** | **NullableInt32** | The unique identifier of the associated recurring item that this transaction matched. | 
**Payee** | **string** | Name of payee set by the user, the financial institution, or by a matched recurring item. This will match the value displayed in payee field on the transactions page in the GUI.  | 
**CategoryId** | **NullableInt32** | Unique identifier of associated category set by the user or by a matched recurring item.&lt;br&gt; Category details can be obtained by passing the value of this property to the [Get A Single Category](../operations/getCategoryById) API | 
**Notes** | **NullableString** | Any transaction notes set by the user or by a matched recurring item. This will match the value displayed in notes field on the transactions page in the GUI.  | 
**Status** | **string** | Status of the transaction.  Will be one of the following values:  | 
**IsPending** | **bool** | Denotes if the transaction is pending (not posted). Applies only to transactions in synced accounts and will always be false for transactions associated with manual accounts. | 
**CreatedAt** | **time.Time** | The date and time of when the transaction was created (in the ISO 8601 extended format). | 
**UpdatedAt** | **time.Time** | The date and time of when the transaction was last updated (in the ISO 8601 extended format). | 
**IsParent** | Pointer to **bool** | If true this transaction has been split into two or more other transactions. By default parent transactions are not returned in call to &#x60;GET /transactions&#x60; but they can be queried directly by their ID. | [optional] 
**ParentId** | **NullableInt64** | A transaction ID if this is a split transaction. Denotes the transaction ID of the original, or parent, transaction. Is null if this is not a split transaction | 
**IsGroup** | **bool** | True if this transaction represents a group of transactions. If so, amount and currency represent the totalled amount of transactions bearing this transaction&#39;s id as their group_id. Amount is calculated based on the user&#39;s primary currency. | 
**GroupId** | **NullableInt64** | Is set if this transaction is part of a group. Denotes the ID of the grouped transaction this is now included in. By default the transactions that were grouped are not returned in a call to &#x60;GET /transactions&#x60; but they can be queried directly by calling the &#x60;GET /transactions/group/{id}&#x60;, where the id passed is associated with a transaction where the &#x60;is_group&#x60; attribute is true | 
**ManualAccountId** | **NullableInt32** | The unique identifier of the manual account associated with this transaction. This will always be null if this transaction is associated with a synced account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**PlaidAccountId** | **NullableInt32** | The unique identifier of the plaid account associated with this transaction. This will always be null if this transaction is associated with a manual account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**TagIds** | **[]int32** | A list of tag_ids for the tags associated with this transaction. If the transaction has no tags this will be an empty list.&lt;br&gt; Tag details can be obtained by passing the value of this attribute as the &#x60;ids&#x60; query parameter to the [List Tags](../operations/getTags) API | 
**Source** | **NullableString** | Source of the transaction: - &#x60;api&#x60;: Transaction was added by a call to the [POST /transactions](../operations/createTransaction) API - &#x60;csv&#x60;: Transaction was added via a CSV Import - &#x60;manual&#x60;: Transaction was created via the \&quot;Add to Cash\&quot; button on the Transactions page - &#x60;merge&#x60;: Transactions were originally in an account that was merged into another account - &#x60;plaid&#x60;: Transaction came from a Financial Institution synced via Plaid - &#x60;recurring&#x60;: Transaction was created from the Recurring page - &#x60;rule&#x60;: Transaction was created by a rule to split a transaction - &#x60;split&#x60;: This is a transaction created by splitting another transaction - &#x60;user&#x60;: This is a legacy value and is replaced by either csv or manual  | 
**ExternalId** | **NullableString** | A user-defined external ID for any transaction that was added via csv import, &#x60;POST /transactions&#x60; API call, or manually added via the Lunch Money GUI. No external ID exists for transactions associated with synced accounts, and they cannot be added. For transactions associated with manual accounts, the external ID must be unique as attempts to add a subsequent transaction with the same external_id and manual_account_id will be flagged as duplicates and fail. | 
**PlaidMetadata** | Pointer to **map[string]interface{}** | If requested, the transaction&#39;s plaid_metadata that came when this transaction was obtained. This will be a json object, but the schema is variable. This will only be present for transactions associated with a plaid account. | [optional] 
**CustomMetadata** | Pointer to **map[string]interface{}** | If requested, the transaction&#39;s custom_metadata that was included when the transaction was inserted via the API. This will be a json object, but the schema is variable. | [optional] 
**Files** | Pointer to [**[]TransactionAttachmentObject**](TransactionAttachmentObject.md) | A list of objects that describe any attachments to the transaction | [optional] 

## Methods

### NewChildTransactionObject

`func NewChildTransactionObject(id int64, date string, amount string, currency CurrencyEnum, toBase float64, recurringId NullableInt32, payee string, categoryId NullableInt32, notes NullableString, status string, isPending bool, createdAt time.Time, updatedAt time.Time, parentId NullableInt64, isGroup bool, groupId NullableInt64, manualAccountId NullableInt32, plaidAccountId NullableInt32, tagIds []int32, source NullableString, externalId NullableString, ) *ChildTransactionObject`

NewChildTransactionObject instantiates a new ChildTransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChildTransactionObjectWithDefaults

`func NewChildTransactionObjectWithDefaults() *ChildTransactionObject`

NewChildTransactionObjectWithDefaults instantiates a new ChildTransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ChildTransactionObject) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ChildTransactionObject) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ChildTransactionObject) SetId(v int64)`

SetId sets Id field to given value.


### GetDate

`func (o *ChildTransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *ChildTransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *ChildTransactionObject) SetDate(v string)`

SetDate sets Date field to given value.


### GetAmount

`func (o *ChildTransactionObject) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *ChildTransactionObject) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *ChildTransactionObject) SetAmount(v string)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *ChildTransactionObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *ChildTransactionObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *ChildTransactionObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *ChildTransactionObject) GetToBase() float64`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *ChildTransactionObject) GetToBaseOk() (*float64, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *ChildTransactionObject) SetToBase(v float64)`

SetToBase sets ToBase field to given value.


### GetRecurringId

`func (o *ChildTransactionObject) GetRecurringId() int32`

GetRecurringId returns the RecurringId field if non-nil, zero value otherwise.

### GetRecurringIdOk

`func (o *ChildTransactionObject) GetRecurringIdOk() (*int32, bool)`

GetRecurringIdOk returns a tuple with the RecurringId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringId

`func (o *ChildTransactionObject) SetRecurringId(v int32)`

SetRecurringId sets RecurringId field to given value.


### SetRecurringIdNil

`func (o *ChildTransactionObject) SetRecurringIdNil(b bool)`

 SetRecurringIdNil sets the value for RecurringId to be an explicit nil

### UnsetRecurringId
`func (o *ChildTransactionObject) UnsetRecurringId()`

UnsetRecurringId ensures that no value is present for RecurringId, not even an explicit nil
### GetPayee

`func (o *ChildTransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *ChildTransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *ChildTransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.


### GetCategoryId

`func (o *ChildTransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *ChildTransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *ChildTransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### SetCategoryIdNil

`func (o *ChildTransactionObject) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *ChildTransactionObject) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetNotes

`func (o *ChildTransactionObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *ChildTransactionObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *ChildTransactionObject) SetNotes(v string)`

SetNotes sets Notes field to given value.


### SetNotesNil

`func (o *ChildTransactionObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *ChildTransactionObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetStatus

`func (o *ChildTransactionObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ChildTransactionObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ChildTransactionObject) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetIsPending

`func (o *ChildTransactionObject) GetIsPending() bool`

GetIsPending returns the IsPending field if non-nil, zero value otherwise.

### GetIsPendingOk

`func (o *ChildTransactionObject) GetIsPendingOk() (*bool, bool)`

GetIsPendingOk returns a tuple with the IsPending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPending

`func (o *ChildTransactionObject) SetIsPending(v bool)`

SetIsPending sets IsPending field to given value.


### GetCreatedAt

`func (o *ChildTransactionObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ChildTransactionObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ChildTransactionObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *ChildTransactionObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ChildTransactionObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ChildTransactionObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetIsParent

`func (o *ChildTransactionObject) GetIsParent() bool`

GetIsParent returns the IsParent field if non-nil, zero value otherwise.

### GetIsParentOk

`func (o *ChildTransactionObject) GetIsParentOk() (*bool, bool)`

GetIsParentOk returns a tuple with the IsParent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsParent

`func (o *ChildTransactionObject) SetIsParent(v bool)`

SetIsParent sets IsParent field to given value.

### HasIsParent

`func (o *ChildTransactionObject) HasIsParent() bool`

HasIsParent returns a boolean if a field has been set.

### GetParentId

`func (o *ChildTransactionObject) GetParentId() int64`

GetParentId returns the ParentId field if non-nil, zero value otherwise.

### GetParentIdOk

`func (o *ChildTransactionObject) GetParentIdOk() (*int64, bool)`

GetParentIdOk returns a tuple with the ParentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentId

`func (o *ChildTransactionObject) SetParentId(v int64)`

SetParentId sets ParentId field to given value.


### SetParentIdNil

`func (o *ChildTransactionObject) SetParentIdNil(b bool)`

 SetParentIdNil sets the value for ParentId to be an explicit nil

### UnsetParentId
`func (o *ChildTransactionObject) UnsetParentId()`

UnsetParentId ensures that no value is present for ParentId, not even an explicit nil
### GetIsGroup

`func (o *ChildTransactionObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *ChildTransactionObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *ChildTransactionObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetGroupId

`func (o *ChildTransactionObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *ChildTransactionObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *ChildTransactionObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.


### SetGroupIdNil

`func (o *ChildTransactionObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *ChildTransactionObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetManualAccountId

`func (o *ChildTransactionObject) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *ChildTransactionObject) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *ChildTransactionObject) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.


### SetManualAccountIdNil

`func (o *ChildTransactionObject) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *ChildTransactionObject) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil
### GetPlaidAccountId

`func (o *ChildTransactionObject) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *ChildTransactionObject) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *ChildTransactionObject) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.


### SetPlaidAccountIdNil

`func (o *ChildTransactionObject) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *ChildTransactionObject) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetTagIds

`func (o *ChildTransactionObject) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *ChildTransactionObject) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *ChildTransactionObject) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.


### GetSource

`func (o *ChildTransactionObject) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *ChildTransactionObject) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *ChildTransactionObject) SetSource(v string)`

SetSource sets Source field to given value.


### SetSourceNil

`func (o *ChildTransactionObject) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *ChildTransactionObject) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil
### GetExternalId

`func (o *ChildTransactionObject) GetExternalId() string`

GetExternalId returns the ExternalId field if non-nil, zero value otherwise.

### GetExternalIdOk

`func (o *ChildTransactionObject) GetExternalIdOk() (*string, bool)`

GetExternalIdOk returns a tuple with the ExternalId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalId

`func (o *ChildTransactionObject) SetExternalId(v string)`

SetExternalId sets ExternalId field to given value.


### SetExternalIdNil

`func (o *ChildTransactionObject) SetExternalIdNil(b bool)`

 SetExternalIdNil sets the value for ExternalId to be an explicit nil

### UnsetExternalId
`func (o *ChildTransactionObject) UnsetExternalId()`

UnsetExternalId ensures that no value is present for ExternalId, not even an explicit nil
### GetPlaidMetadata

`func (o *ChildTransactionObject) GetPlaidMetadata() map[string]interface{}`

GetPlaidMetadata returns the PlaidMetadata field if non-nil, zero value otherwise.

### GetPlaidMetadataOk

`func (o *ChildTransactionObject) GetPlaidMetadataOk() (*map[string]interface{}, bool)`

GetPlaidMetadataOk returns a tuple with the PlaidMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidMetadata

`func (o *ChildTransactionObject) SetPlaidMetadata(v map[string]interface{})`

SetPlaidMetadata sets PlaidMetadata field to given value.

### HasPlaidMetadata

`func (o *ChildTransactionObject) HasPlaidMetadata() bool`

HasPlaidMetadata returns a boolean if a field has been set.

### SetPlaidMetadataNil

`func (o *ChildTransactionObject) SetPlaidMetadataNil(b bool)`

 SetPlaidMetadataNil sets the value for PlaidMetadata to be an explicit nil

### UnsetPlaidMetadata
`func (o *ChildTransactionObject) UnsetPlaidMetadata()`

UnsetPlaidMetadata ensures that no value is present for PlaidMetadata, not even an explicit nil
### GetCustomMetadata

`func (o *ChildTransactionObject) GetCustomMetadata() map[string]interface{}`

GetCustomMetadata returns the CustomMetadata field if non-nil, zero value otherwise.

### GetCustomMetadataOk

`func (o *ChildTransactionObject) GetCustomMetadataOk() (*map[string]interface{}, bool)`

GetCustomMetadataOk returns a tuple with the CustomMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomMetadata

`func (o *ChildTransactionObject) SetCustomMetadata(v map[string]interface{})`

SetCustomMetadata sets CustomMetadata field to given value.

### HasCustomMetadata

`func (o *ChildTransactionObject) HasCustomMetadata() bool`

HasCustomMetadata returns a boolean if a field has been set.

### SetCustomMetadataNil

`func (o *ChildTransactionObject) SetCustomMetadataNil(b bool)`

 SetCustomMetadataNil sets the value for CustomMetadata to be an explicit nil

### UnsetCustomMetadata
`func (o *ChildTransactionObject) UnsetCustomMetadata()`

UnsetCustomMetadata ensures that no value is present for CustomMetadata, not even an explicit nil
### GetFiles

`func (o *ChildTransactionObject) GetFiles() []TransactionAttachmentObject`

GetFiles returns the Files field if non-nil, zero value otherwise.

### GetFilesOk

`func (o *ChildTransactionObject) GetFilesOk() (*[]TransactionAttachmentObject, bool)`

GetFilesOk returns a tuple with the Files field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFiles

`func (o *ChildTransactionObject) SetFiles(v []TransactionAttachmentObject)`

SetFiles sets Files field to given value.

### HasFiles

`func (o *ChildTransactionObject) HasFiles() bool`

HasFiles returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


