# NonAlignedSummaryCategoryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryId** | **int32** | ID of the category associated with the totals. | 
**Totals** | [**NonAlignedCategoryTotalsObject**](NonAlignedCategoryTotalsObject.md) |  | 

## Methods

### NewNonAlignedSummaryCategoryObject

`func NewNonAlignedSummaryCategoryObject(categoryId int32, totals NonAlignedCategoryTotalsObject, ) *NonAlignedSummaryCategoryObject`

NewNonAlignedSummaryCategoryObject instantiates a new NonAlignedSummaryCategoryObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNonAlignedSummaryCategoryObjectWithDefaults

`func NewNonAlignedSummaryCategoryObjectWithDefaults() *NonAlignedSummaryCategoryObject`

NewNonAlignedSummaryCategoryObjectWithDefaults instantiates a new NonAlignedSummaryCategoryObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategoryId

`func (o *NonAlignedSummaryCategoryObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *NonAlignedSummaryCategoryObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *NonAlignedSummaryCategoryObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetTotals

`func (o *NonAlignedSummaryCategoryObject) GetTotals() NonAlignedCategoryTotalsObject`

GetTotals returns the Totals field if non-nil, zero value otherwise.

### GetTotalsOk

`func (o *NonAlignedSummaryCategoryObject) GetTotalsOk() (*NonAlignedCategoryTotalsObject, bool)`

GetTotalsOk returns a tuple with the Totals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotals

`func (o *NonAlignedSummaryCategoryObject) SetTotals(v NonAlignedCategoryTotalsObject)`

SetTotals sets Totals field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


