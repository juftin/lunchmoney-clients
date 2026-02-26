# UpsertBudgetRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartDate** | **string** | Start date of the budget period in ISO 8601 date format (YYYY-MM-DD). Must be a valid budget period start for the account. | 
**CategoryId** | **int32** | Category ID for the budget | 
**Amount** | [**UpsertBudgetRequestObjectAmount**](UpsertBudgetRequestObjectAmount.md) |  | 
**Currency** | Pointer to [**CurrencyEnum**](CurrencyEnum.md) | Three-letter currency code. If omitted, the primary currency for the user&#39;s account is used. | [optional] 
**Notes** | Pointer to **NullableString** | Optional notes for the budget period | [optional] 

## Methods

### NewUpsertBudgetRequestObject

`func NewUpsertBudgetRequestObject(startDate string, categoryId int32, amount UpsertBudgetRequestObjectAmount, ) *UpsertBudgetRequestObject`

NewUpsertBudgetRequestObject instantiates a new UpsertBudgetRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpsertBudgetRequestObjectWithDefaults

`func NewUpsertBudgetRequestObjectWithDefaults() *UpsertBudgetRequestObject`

NewUpsertBudgetRequestObjectWithDefaults instantiates a new UpsertBudgetRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStartDate

`func (o *UpsertBudgetRequestObject) GetStartDate() string`

GetStartDate returns the StartDate field if non-nil, zero value otherwise.

### GetStartDateOk

`func (o *UpsertBudgetRequestObject) GetStartDateOk() (*string, bool)`

GetStartDateOk returns a tuple with the StartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartDate

`func (o *UpsertBudgetRequestObject) SetStartDate(v string)`

SetStartDate sets StartDate field to given value.


### GetCategoryId

`func (o *UpsertBudgetRequestObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *UpsertBudgetRequestObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *UpsertBudgetRequestObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetAmount

`func (o *UpsertBudgetRequestObject) GetAmount() UpsertBudgetRequestObjectAmount`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *UpsertBudgetRequestObject) GetAmountOk() (*UpsertBudgetRequestObjectAmount, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *UpsertBudgetRequestObject) SetAmount(v UpsertBudgetRequestObjectAmount)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *UpsertBudgetRequestObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *UpsertBudgetRequestObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *UpsertBudgetRequestObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *UpsertBudgetRequestObject) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetNotes

`func (o *UpsertBudgetRequestObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *UpsertBudgetRequestObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *UpsertBudgetRequestObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *UpsertBudgetRequestObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *UpsertBudgetRequestObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *UpsertBudgetRequestObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


