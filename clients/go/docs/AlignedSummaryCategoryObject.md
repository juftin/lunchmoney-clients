# AlignedSummaryCategoryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryId** | **int32** | ID of the category associated with the totals. | 
**Totals** | [**AlignedCategoryTotalsObject**](AlignedCategoryTotalsObject.md) |  | 
**Occurrences** | Pointer to [**[]SummaryCategoryOccurrenceObject**](SummaryCategoryOccurrenceObject.md) |  | [optional] 

## Methods

### NewAlignedSummaryCategoryObject

`func NewAlignedSummaryCategoryObject(categoryId int32, totals AlignedCategoryTotalsObject, ) *AlignedSummaryCategoryObject`

NewAlignedSummaryCategoryObject instantiates a new AlignedSummaryCategoryObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAlignedSummaryCategoryObjectWithDefaults

`func NewAlignedSummaryCategoryObjectWithDefaults() *AlignedSummaryCategoryObject`

NewAlignedSummaryCategoryObjectWithDefaults instantiates a new AlignedSummaryCategoryObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategoryId

`func (o *AlignedSummaryCategoryObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *AlignedSummaryCategoryObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *AlignedSummaryCategoryObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetTotals

`func (o *AlignedSummaryCategoryObject) GetTotals() AlignedCategoryTotalsObject`

GetTotals returns the Totals field if non-nil, zero value otherwise.

### GetTotalsOk

`func (o *AlignedSummaryCategoryObject) GetTotalsOk() (*AlignedCategoryTotalsObject, bool)`

GetTotalsOk returns a tuple with the Totals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotals

`func (o *AlignedSummaryCategoryObject) SetTotals(v AlignedCategoryTotalsObject)`

SetTotals sets Totals field to given value.


### GetOccurrences

`func (o *AlignedSummaryCategoryObject) GetOccurrences() []SummaryCategoryOccurrenceObject`

GetOccurrences returns the Occurrences field if non-nil, zero value otherwise.

### GetOccurrencesOk

`func (o *AlignedSummaryCategoryObject) GetOccurrencesOk() (*[]SummaryCategoryOccurrenceObject, bool)`

GetOccurrencesOk returns a tuple with the Occurrences field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOccurrences

`func (o *AlignedSummaryCategoryObject) SetOccurrences(v []SummaryCategoryOccurrenceObject)`

SetOccurrences sets Occurrences field to given value.

### HasOccurrences

`func (o *AlignedSummaryCategoryObject) HasOccurrences() bool`

HasOccurrences returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


