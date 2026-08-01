# SplitTransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Amount** | [**SplitTransactionObjectAmount**](SplitTransactionObjectAmount.md) |  | 
**Payee** | Pointer to **string** | The payee for the child transaction. Will inherit the original payee from the parent if not defined. | [optional] 
**Date** | Pointer to **string** | Must be in ISO 8601 format (YYYY-MM-DD). Will inherit from the parent if not defined. | [optional] 
**CategoryId** | Pointer to **NullableInt32** | Category ID for the child transaction. The category must already exist for the account. If omitted, the child inherits the parent category. If &#x60;null&#x60;, the child has no category. | [optional] 
**TagIds** | Pointer to **[]int32** | The IDs of any tags to apply to this split child transaction. Each ID must match an existing tag. | [optional] 
**Notes** | Pointer to **NullableString** | Notes for the child transaction. If omitted, the child inherits the parent notes. If &#x60;null&#x60; or an empty string, the child has no notes. | [optional] 

## Methods

### NewSplitTransactionObject

`func NewSplitTransactionObject(amount SplitTransactionObjectAmount, ) *SplitTransactionObject`

NewSplitTransactionObject instantiates a new SplitTransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSplitTransactionObjectWithDefaults

`func NewSplitTransactionObjectWithDefaults() *SplitTransactionObject`

NewSplitTransactionObjectWithDefaults instantiates a new SplitTransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAmount

`func (o *SplitTransactionObject) GetAmount() SplitTransactionObjectAmount`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *SplitTransactionObject) GetAmountOk() (*SplitTransactionObjectAmount, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *SplitTransactionObject) SetAmount(v SplitTransactionObjectAmount)`

SetAmount sets Amount field to given value.


### GetPayee

`func (o *SplitTransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *SplitTransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *SplitTransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *SplitTransactionObject) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### GetDate

`func (o *SplitTransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *SplitTransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *SplitTransactionObject) SetDate(v string)`

SetDate sets Date field to given value.

### HasDate

`func (o *SplitTransactionObject) HasDate() bool`

HasDate returns a boolean if a field has been set.

### GetCategoryId

`func (o *SplitTransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *SplitTransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *SplitTransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *SplitTransactionObject) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### SetCategoryIdNil

`func (o *SplitTransactionObject) SetCategoryIdNil(b bool)`

 SetCategoryIdNil sets the value for CategoryId to be an explicit nil

### UnsetCategoryId
`func (o *SplitTransactionObject) UnsetCategoryId()`

UnsetCategoryId ensures that no value is present for CategoryId, not even an explicit nil
### GetTagIds

`func (o *SplitTransactionObject) GetTagIds() []int32`

GetTagIds returns the TagIds field if non-nil, zero value otherwise.

### GetTagIdsOk

`func (o *SplitTransactionObject) GetTagIdsOk() (*[]int32, bool)`

GetTagIdsOk returns a tuple with the TagIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagIds

`func (o *SplitTransactionObject) SetTagIds(v []int32)`

SetTagIds sets TagIds field to given value.

### HasTagIds

`func (o *SplitTransactionObject) HasTagIds() bool`

HasTagIds returns a boolean if a field has been set.

### GetNotes

`func (o *SplitTransactionObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *SplitTransactionObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *SplitTransactionObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *SplitTransactionObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *SplitTransactionObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *SplitTransactionObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


