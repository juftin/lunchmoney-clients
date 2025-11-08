# RecurringObjectOverrides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Payee** | Pointer to **string** | If present, the payee name that will be displayed for any matching transactions. | [optional] 
**Notes** | Pointer to **string** | If present, the notes that will be displayed for any matching transactions. | [optional] 
**CategoryId** | Pointer to **int32** | If present, the ID of the category that matching transactions will be assigned to. | [optional] 

## Methods

### NewRecurringObjectOverrides

`func NewRecurringObjectOverrides() *RecurringObjectOverrides`

NewRecurringObjectOverrides instantiates a new RecurringObjectOverrides object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRecurringObjectOverridesWithDefaults

`func NewRecurringObjectOverridesWithDefaults() *RecurringObjectOverrides`

NewRecurringObjectOverridesWithDefaults instantiates a new RecurringObjectOverrides object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPayee

`func (o *RecurringObjectOverrides) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *RecurringObjectOverrides) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *RecurringObjectOverrides) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *RecurringObjectOverrides) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### GetNotes

`func (o *RecurringObjectOverrides) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *RecurringObjectOverrides) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *RecurringObjectOverrides) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *RecurringObjectOverrides) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### GetCategoryId

`func (o *RecurringObjectOverrides) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *RecurringObjectOverrides) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *RecurringObjectOverrides) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *RecurringObjectOverrides) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


