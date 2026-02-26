# SummaryCategoryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryId** | **int32** | ID of the category associated with the totals. | 
**Totals** | [**SummaryCategoryTotalsObject**](SummaryCategoryTotalsObject.md) |  | 
**Occurrences** | Pointer to [**[]SummaryCategoryOccurrenceObject**](SummaryCategoryOccurrenceObject.md) | A list of objects describing the budget activity for each period within the range. This property is only present when &#x60;include_occurrences&#x60; is true.&lt;p&gt; For aligned ranges, there is one occurrence for each budget period in the range; for non-aligned, only periods fully contained in the range are included.&lt;p&gt; If &#x60;include_past_budget_dates&#x60; is also &#x60;true&#x60;, the three budget periods prior to the range are also included. | [optional] 
**RolloverPool** | Pointer to [**SummaryRolloverPoolObject**](SummaryRolloverPoolObject.md) |  | [optional] 

## Methods

### NewSummaryCategoryObject

`func NewSummaryCategoryObject(categoryId int32, totals SummaryCategoryTotalsObject, ) *SummaryCategoryObject`

NewSummaryCategoryObject instantiates a new SummaryCategoryObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryCategoryObjectWithDefaults

`func NewSummaryCategoryObjectWithDefaults() *SummaryCategoryObject`

NewSummaryCategoryObjectWithDefaults instantiates a new SummaryCategoryObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategoryId

`func (o *SummaryCategoryObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *SummaryCategoryObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *SummaryCategoryObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetTotals

`func (o *SummaryCategoryObject) GetTotals() SummaryCategoryTotalsObject`

GetTotals returns the Totals field if non-nil, zero value otherwise.

### GetTotalsOk

`func (o *SummaryCategoryObject) GetTotalsOk() (*SummaryCategoryTotalsObject, bool)`

GetTotalsOk returns a tuple with the Totals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotals

`func (o *SummaryCategoryObject) SetTotals(v SummaryCategoryTotalsObject)`

SetTotals sets Totals field to given value.


### GetOccurrences

`func (o *SummaryCategoryObject) GetOccurrences() []SummaryCategoryOccurrenceObject`

GetOccurrences returns the Occurrences field if non-nil, zero value otherwise.

### GetOccurrencesOk

`func (o *SummaryCategoryObject) GetOccurrencesOk() (*[]SummaryCategoryOccurrenceObject, bool)`

GetOccurrencesOk returns a tuple with the Occurrences field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOccurrences

`func (o *SummaryCategoryObject) SetOccurrences(v []SummaryCategoryOccurrenceObject)`

SetOccurrences sets Occurrences field to given value.

### HasOccurrences

`func (o *SummaryCategoryObject) HasOccurrences() bool`

HasOccurrences returns a boolean if a field has been set.

### GetRolloverPool

`func (o *SummaryCategoryObject) GetRolloverPool() SummaryRolloverPoolObject`

GetRolloverPool returns the RolloverPool field if non-nil, zero value otherwise.

### GetRolloverPoolOk

`func (o *SummaryCategoryObject) GetRolloverPoolOk() (*SummaryRolloverPoolObject, bool)`

GetRolloverPoolOk returns a tuple with the RolloverPool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRolloverPool

`func (o *SummaryCategoryObject) SetRolloverPool(v SummaryRolloverPoolObject)`

SetRolloverPool sets RolloverPool field to given value.

### HasRolloverPool

`func (o *SummaryCategoryObject) HasRolloverPool() bool`

HasRolloverPool returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


