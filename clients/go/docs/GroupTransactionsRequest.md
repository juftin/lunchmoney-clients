# GroupTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Ids** | **[]int64** | List of existing transaction IDs to group. Split and recurring transactions may not be grouped. Transactions that are already grouped must be ungrouped before being regrouped. | 
**Date** | **string** | Date for the new grouped transaction in ISO 8601 format. | 
**Payee** | **string** | The payee for the new grouped transaction.  | 
**CategoryId** | Pointer to **NullableInt64** | The ID of an existing category to assign to the grouped transaction. If not set and all the grouped transactions have the same category, the grouped transaction will inherit the category, otherwise the new transaction will have no category. | [optional] 
**Notes** | Pointer to **NullableString** | Notes for the grouped transaction.  | [optional] 
**Status** | Pointer to **string** | If set, must be either &#x60;reviewed&#x60; or &#x60;unreviewed&#x60;. If not set, defaults to &#x60;reviewed&#x60;. | [optional] 
**TagIds** | Pointer to **[]int64** | A list of IDs for the tags associated with the grouped transaction. Each ID must match an existing tag associated with the user&#39;s account. If not set, no tags will be associated with the created transaction. | [optional] 

## Methods

### NewGroupTransactionsRequest

`func NewGroupTransactionsRequest(ids []int64, date string, payee string, ) *GroupTransactionsRequest`

NewGroupTransactionsRequest instantiates a new GroupTransactionsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGroupTransactionsRequestWithDefaults

`func NewGroupTransactionsRequestWithDefaults() *GroupTransactionsRequest`

NewGroupTransactionsRequestWithDefaults instantiates a new GroupTransactionsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIds

`func (o *GroupTransactionsRequest) GetIds() []int64`

GetIds returns the Ids field if non-nil, zero value otherwise.

### GetIdsOk

`func (o *GroupTransactionsRequest) GetIdsOk() (*[]int64, bool)`

GetIdsOk returns a tuple with the Ids field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIds

`func (o *GroupTransactionsRequest) SetIds(v []int64)`

SetIds sets Ids field to given value.


### GetDate

`func (o *GroupTransactionsRequest) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *GroupTransactionsRequest) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *GroupTransactionsRequest) SetDate(v string)`

SetDate sets Date field to given value.


### GetPayee

`func (o *GroupTransactionsRequest) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *GroupTransactionsRequest) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *GroupTransactionsRequest) SetPayee(v string)`

SetPayee sets Payee field to given value.


### GetCategoryId

`func (o *GroupTransactionsRequest) GetCategoryId() int64`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *GroupTransactionsRequest) GetCategoryIdOk() (*int64, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *GroupTransactionsRequest) SetCategoryId(v int64)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *GroupTransactionsRequest) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### SetCategoryIdNil

`func (o *GroupTransactionsRequest) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *GroupTransactionsRequest) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetNotes

`func (o *GroupTransactionsRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *GroupTransactionsRequest) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *GroupTransactionsRequest) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *GroupTransactionsRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *GroupTransactionsRequest) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *GroupTransactionsRequest) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetStatus

`func (o *GroupTransactionsRequest) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *GroupTransactionsRequest) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *GroupTransactionsRequest) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *GroupTransactionsRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetTagIds

`func (o *GroupTransactionsRequest) GetTagIds() []int64`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *GroupTransactionsRequest) GetTagIdsOk() (*[]int64, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *GroupTransactionsRequest) SetTagIds(v []int64)`

SetTagIds sets TagIds field to given value.

### HasTagIds

`func (o *GroupTransactionsRequest) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


