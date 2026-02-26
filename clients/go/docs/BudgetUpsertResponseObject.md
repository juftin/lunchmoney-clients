# BudgetUpsertResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryId** | Pointer to **int32** | Category ID | [optional] 
**StartDate** | Pointer to **string** | Start date of the budget period | [optional] 
**Amount** | Pointer to **string** | Budget amount in the stored currency (string for consistency with other amount fields in the API) | [optional] 
**Currency** | Pointer to **string** | Currency code for the budget | [optional] 
**ToBase** | Pointer to **float32** | Amount converted to the user&#39;s primary currency | [optional] 
**Notes** | Pointer to **NullableString** | Notes for the budget period | [optional] 

## Methods

### NewBudgetUpsertResponseObject

`func NewBudgetUpsertResponseObject() *BudgetUpsertResponseObject`

NewBudgetUpsertResponseObject instantiates a new BudgetUpsertResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBudgetUpsertResponseObjectWithDefaults

`func NewBudgetUpsertResponseObjectWithDefaults() *BudgetUpsertResponseObject`

NewBudgetUpsertResponseObjectWithDefaults instantiates a new BudgetUpsertResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategoryId

`func (o *BudgetUpsertResponseObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *BudgetUpsertResponseObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *BudgetUpsertResponseObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.

### HasCategoryId

`func (o *BudgetUpsertResponseObject) HasCategoryId() bool`

HasCategoryId returns a boolean if a field has been set.

### GetStartDate

`func (o *BudgetUpsertResponseObject) GetStartDate() string`

GetStartDate returns the StartDate field if non-nil, zero value otherwise.

### GetStartDateOk

`func (o *BudgetUpsertResponseObject) GetStartDateOk() (*string, bool)`

GetStartDateOk returns a tuple with the StartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartDate

`func (o *BudgetUpsertResponseObject) SetStartDate(v string)`

SetStartDate sets StartDate field to given value.

### HasStartDate

`func (o *BudgetUpsertResponseObject) HasStartDate() bool`

HasStartDate returns a boolean if a field has been set.

### GetAmount

`func (o *BudgetUpsertResponseObject) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *BudgetUpsertResponseObject) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *BudgetUpsertResponseObject) SetAmount(v string)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *BudgetUpsertResponseObject) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCurrency

`func (o *BudgetUpsertResponseObject) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *BudgetUpsertResponseObject) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *BudgetUpsertResponseObject) SetCurrency(v string)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *BudgetUpsertResponseObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetToBase

`func (o *BudgetUpsertResponseObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *BudgetUpsertResponseObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *BudgetUpsertResponseObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.

### HasToBase

`func (o *BudgetUpsertResponseObject) HasToBase() bool`

HasToBase returns a boolean if a field has been set.

### GetNotes

`func (o *BudgetUpsertResponseObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *BudgetUpsertResponseObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *BudgetUpsertResponseObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *BudgetUpsertResponseObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *BudgetUpsertResponseObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *BudgetUpsertResponseObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


