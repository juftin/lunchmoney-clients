# GetBudgetSummary200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Totals** | Pointer to [**SummaryTotalsObject**](SummaryTotalsObject.md) |  | [optional] 
**Aligned** | **bool** | &#x60;true&#x60; if start_date and end_date are aligned with budget period setting | 
**Categories** | [**[]NonAlignedSummaryCategoryObject**](NonAlignedSummaryCategoryObject.md) |  | 

## Methods

### NewGetBudgetSummary200Response

`func NewGetBudgetSummary200Response(aligned bool, categories []NonAlignedSummaryCategoryObject, ) *GetBudgetSummary200Response`

NewGetBudgetSummary200Response instantiates a new GetBudgetSummary200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetBudgetSummary200ResponseWithDefaults

`func NewGetBudgetSummary200ResponseWithDefaults() *GetBudgetSummary200Response`

NewGetBudgetSummary200ResponseWithDefaults instantiates a new GetBudgetSummary200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotals

`func (o *GetBudgetSummary200Response) GetTotals() SummaryTotalsObject`

GetTotals returns the Totals field if non-nil, zero value otherwise.

### GetTotalsOk

`func (o *GetBudgetSummary200Response) GetTotalsOk() (*SummaryTotalsObject, bool)`

GetTotalsOk returns a tuple with the Totals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotals

`func (o *GetBudgetSummary200Response) SetTotals(v SummaryTotalsObject)`

SetTotals sets Totals field to given value.

### HasTotals

`func (o *GetBudgetSummary200Response) HasTotals() bool`

HasTotals returns a boolean if a field has been set.

### GetAligned

`func (o *GetBudgetSummary200Response) GetAligned() bool`

GetAligned returns the Aligned field if non-nil, zero value otherwise.

### GetAlignedOk

`func (o *GetBudgetSummary200Response) GetAlignedOk() (*bool, bool)`

GetAlignedOk returns a tuple with the Aligned field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAligned

`func (o *GetBudgetSummary200Response) SetAligned(v bool)`

SetAligned sets Aligned field to given value.


### GetCategories

`func (o *GetBudgetSummary200Response) GetCategories() []NonAlignedSummaryCategoryObject`

GetCategories returns the Categories field if non-nil, zero value otherwise.

### GetCategoriesOk

`func (o *GetBudgetSummary200Response) GetCategoriesOk() (*[]NonAlignedSummaryCategoryObject, bool)`

GetCategoriesOk returns a tuple with the Categories field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategories

`func (o *GetBudgetSummary200Response) SetCategories(v []NonAlignedSummaryCategoryObject)`

SetCategories sets Categories field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


