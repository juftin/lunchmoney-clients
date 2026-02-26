# SummaryResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Aligned** | **bool** | &#x60;true&#x60; if start_date and end_date are aligned with the user&#39;s budget period setting; &#x60;false&#x60; otherwise.&lt;p&gt; When the response is not aligned, category &#x60;totals&#x60; will not include values for the &#x60;budgeted&#x60; and &#x60;available&#x60; properties, so aligned responses are usually preferred.&lt;p&gt; If unsure how to set an aligned date range, set a range of at least one month and set the &#x60;include_occurrences&#x60; parameter to &#x60;true&#x60;. Then examine the objects in the &#x60;occurrences&#x60; array for the first category to find start and end dates that will produce aligned responses.  Setting &#x60;include_past_budget_dates&#x60; to &#x60;true&#x60; will add the three budget periods prior to the range in the &#x60;occurrences&#x60; array. | 
**Categories** | [**[]SummaryCategoryObject**](SummaryCategoryObject.md) |  | 
**Totals** | Pointer to [**SummaryTotalsObject**](SummaryTotalsObject.md) |  | [optional] 
**RolloverPool** | Pointer to [**SummaryRolloverPoolObject**](SummaryRolloverPoolObject.md) |  | [optional] 

## Methods

### NewSummaryResponseObject

`func NewSummaryResponseObject(aligned bool, categories []SummaryCategoryObject, ) *SummaryResponseObject`

NewSummaryResponseObject instantiates a new SummaryResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryResponseObjectWithDefaults

`func NewSummaryResponseObjectWithDefaults() *SummaryResponseObject`

NewSummaryResponseObjectWithDefaults instantiates a new SummaryResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAligned

`func (o *SummaryResponseObject) GetAligned() bool`

GetAligned returns the Aligned field if non-nil, zero value otherwise.

### GetAlignedOk

`func (o *SummaryResponseObject) GetAlignedOk() (*bool, bool)`

GetAlignedOk returns a tuple with the Aligned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAligned

`func (o *SummaryResponseObject) SetAligned(v bool)`

SetAligned sets Aligned field to given value.


### GetCategories

`func (o *SummaryResponseObject) GetCategories() []SummaryCategoryObject`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *SummaryResponseObject) GetCategoriesOk() (*[]SummaryCategoryObject, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *SummaryResponseObject) SetCategories(v []SummaryCategoryObject)`

SetCategories sets Categories field to given value.


### GetTotals

`func (o *SummaryResponseObject) GetTotals() SummaryTotalsObject`

GetTotals returns the Totals field if non-nil, zero value otherwise.

### GetTotalsOk

`func (o *SummaryResponseObject) GetTotalsOk() (*SummaryTotalsObject, bool)`

GetTotalsOk returns a tuple with the Totals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotals

`func (o *SummaryResponseObject) SetTotals(v SummaryTotalsObject)`

SetTotals sets Totals field to given value.

### HasTotals

`func (o *SummaryResponseObject) HasTotals() bool`

HasTotals returns a boolean if a field has been set.

### GetRolloverPool

`func (o *SummaryResponseObject) GetRolloverPool() SummaryRolloverPoolObject`

GetRolloverPool returns the RolloverPool field if non-nil, zero value otherwise.

### GetRolloverPoolOk

`func (o *SummaryResponseObject) GetRolloverPoolOk() (*SummaryRolloverPoolObject, bool)`

GetRolloverPoolOk returns a tuple with the RolloverPool field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRolloverPool

`func (o *SummaryResponseObject) SetRolloverPool(v SummaryRolloverPoolObject)`

SetRolloverPool sets RolloverPool field to given value.

### HasRolloverPool

`func (o *SummaryResponseObject) HasRolloverPool() bool`

HasRolloverPool returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


