# SummaryCategoryTotalsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OtherActivity** | **float32** | Total non recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the recurring_activity. | 
**RecurringActivity** | **float32** | Total recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the other_activity. | 
**Budgeted** | Pointer to **NullableFloat32** | Total budgeted amount, in the user&#39;s default currency, for the category within the given date range or null if the category is not budgeted. This property will not be present in a non-aligned response. | [optional] 
**Available** | Pointer to **NullableFloat32** | Total amount of funds available, in the user&#39;s default currency, for the category within the given date range. This property will not be present in a non-aligned response. | [optional] 
**RecurringRemaining** | **float32** | Total expected recurring activity, in the user&#39;s default currency, that has not yet occurred for the category within the given date range. | 
**RecurringExpected** | **float32** | Total expected recurring activity for the category within the given date range. | 

## Methods

### NewSummaryCategoryTotalsObject

`func NewSummaryCategoryTotalsObject(otherActivity float32, recurringActivity float32, recurringRemaining float32, recurringExpected float32, ) *SummaryCategoryTotalsObject`

NewSummaryCategoryTotalsObject instantiates a new SummaryCategoryTotalsObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryCategoryTotalsObjectWithDefaults

`func NewSummaryCategoryTotalsObjectWithDefaults() *SummaryCategoryTotalsObject`

NewSummaryCategoryTotalsObjectWithDefaults instantiates a new SummaryCategoryTotalsObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOtherActivity

`func (o *SummaryCategoryTotalsObject) GetOtherActivity() float32`

GetOtherActivity returns the OtherActivity field if non-nil, zero value otherwise.

### GetOtherActivityOk

`func (o *SummaryCategoryTotalsObject) GetOtherActivityOk() (*float32, bool)`

GetOtherActivityOk returns a tuple with the OtherActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherActivity

`func (o *SummaryCategoryTotalsObject) SetOtherActivity(v float32)`

SetOtherActivity sets OtherActivity field to given value.


### GetRecurringActivity

`func (o *SummaryCategoryTotalsObject) GetRecurringActivity() float32`

GetRecurringActivity returns the RecurringActivity field if non-nil, zero value otherwise.

### GetRecurringActivityOk

`func (o *SummaryCategoryTotalsObject) GetRecurringActivityOk() (*float32, bool)`

GetRecurringActivityOk returns a tuple with the RecurringActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringActivity

`func (o *SummaryCategoryTotalsObject) SetRecurringActivity(v float32)`

SetRecurringActivity sets RecurringActivity field to given value.


### GetBudgeted

`func (o *SummaryCategoryTotalsObject) GetBudgeted() float32`

GetBudgeted returns the Budgeted field if non-nil, zero value otherwise.

### GetBudgetedOk

`func (o *SummaryCategoryTotalsObject) GetBudgetedOk() (*float32, bool)`

GetBudgetedOk returns a tuple with the Budgeted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgeted

`func (o *SummaryCategoryTotalsObject) SetBudgeted(v float32)`

SetBudgeted sets Budgeted field to given value.

### HasBudgeted

`func (o *SummaryCategoryTotalsObject) HasBudgeted() bool`

HasBudgeted returns a boolean if a field has been set.

### SetBudgetedNil

`func (o *SummaryCategoryTotalsObject) SetBudgetedNil(b bool)`

 SetBudgetedNil sets the value for Budgeted to be an explicit nil

### UnsetBudgeted
`func (o *SummaryCategoryTotalsObject) UnsetBudgeted()`

UnsetBudgeted ensures that no value is present for Budgeted, not even an explicit nil
### GetAvailable

`func (o *SummaryCategoryTotalsObject) GetAvailable() float32`

GetAvailable returns the Available field if non-nil, zero value otherwise.

### GetAvailableOk

`func (o *SummaryCategoryTotalsObject) GetAvailableOk() (*float32, bool)`

GetAvailableOk returns a tuple with the Available field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvailable

`func (o *SummaryCategoryTotalsObject) SetAvailable(v float32)`

SetAvailable sets Available field to given value.

### HasAvailable

`func (o *SummaryCategoryTotalsObject) HasAvailable() bool`

HasAvailable returns a boolean if a field has been set.

### SetAvailableNil

`func (o *SummaryCategoryTotalsObject) SetAvailableNil(b bool)`

 SetAvailableNil sets the value for Available to be an explicit nil

### UnsetAvailable
`func (o *SummaryCategoryTotalsObject) UnsetAvailable()`

UnsetAvailable ensures that no value is present for Available, not even an explicit nil
### GetRecurringRemaining

`func (o *SummaryCategoryTotalsObject) GetRecurringRemaining() float32`

GetRecurringRemaining returns the RecurringRemaining field if non-nil, zero value otherwise.

### GetRecurringRemainingOk

`func (o *SummaryCategoryTotalsObject) GetRecurringRemainingOk() (*float32, bool)`

GetRecurringRemainingOk returns a tuple with the RecurringRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringRemaining

`func (o *SummaryCategoryTotalsObject) SetRecurringRemaining(v float32)`

SetRecurringRemaining sets RecurringRemaining field to given value.


### GetRecurringExpected

`func (o *SummaryCategoryTotalsObject) GetRecurringExpected() float32`

GetRecurringExpected returns the RecurringExpected field if non-nil, zero value otherwise.

### GetRecurringExpectedOk

`func (o *SummaryCategoryTotalsObject) GetRecurringExpectedOk() (*float32, bool)`

GetRecurringExpectedOk returns a tuple with the RecurringExpected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringExpected

`func (o *SummaryCategoryTotalsObject) SetRecurringExpected(v float32)`

SetRecurringExpected sets RecurringExpected field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


