# NonAlignedCategoryTotalsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OtherActivity** | **float32** | Total non recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the recurring_activity. | 
**RecurringActivity** | **float32** | Total recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the other_activity. | 
**RecurringRemaining** | **float32** | Total expected recurring activity, in the user&#39;s default currency, that has not yet occurred for the category within the given date range. | 
**RecurringExpected** | **float32** | Total expected recurring activity for the category within the given date range. | 

## Methods

### NewNonAlignedCategoryTotalsObject

`func NewNonAlignedCategoryTotalsObject(otherActivity float32, recurringActivity float32, recurringRemaining float32, recurringExpected float32, ) *NonAlignedCategoryTotalsObject`

NewNonAlignedCategoryTotalsObject instantiates a new NonAlignedCategoryTotalsObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNonAlignedCategoryTotalsObjectWithDefaults

`func NewNonAlignedCategoryTotalsObjectWithDefaults() *NonAlignedCategoryTotalsObject`

NewNonAlignedCategoryTotalsObjectWithDefaults instantiates a new NonAlignedCategoryTotalsObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOtherActivity

`func (o *NonAlignedCategoryTotalsObject) GetOtherActivity() float32`

GetOtherActivity returns the OtherActivity field if non-nil, zero value otherwise.

### GetOtherActivityOk

`func (o *NonAlignedCategoryTotalsObject) GetOtherActivityOk() (*float32, bool)`

GetOtherActivityOk returns a tuple with the OtherActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherActivity

`func (o *NonAlignedCategoryTotalsObject) SetOtherActivity(v float32)`

SetOtherActivity sets OtherActivity field to given value.


### GetRecurringActivity

`func (o *NonAlignedCategoryTotalsObject) GetRecurringActivity() float32`

GetRecurringActivity returns the RecurringActivity field if non-nil, zero value otherwise.

### GetRecurringActivityOk

`func (o *NonAlignedCategoryTotalsObject) GetRecurringActivityOk() (*float32, bool)`

GetRecurringActivityOk returns a tuple with the RecurringActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringActivity

`func (o *NonAlignedCategoryTotalsObject) SetRecurringActivity(v float32)`

SetRecurringActivity sets RecurringActivity field to given value.


### GetRecurringRemaining

`func (o *NonAlignedCategoryTotalsObject) GetRecurringRemaining() float32`

GetRecurringRemaining returns the RecurringRemaining field if non-nil, zero value otherwise.

### GetRecurringRemainingOk

`func (o *NonAlignedCategoryTotalsObject) GetRecurringRemainingOk() (*float32, bool)`

GetRecurringRemainingOk returns a tuple with the RecurringRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringRemaining

`func (o *NonAlignedCategoryTotalsObject) SetRecurringRemaining(v float32)`

SetRecurringRemaining sets RecurringRemaining field to given value.


### GetRecurringExpected

`func (o *NonAlignedCategoryTotalsObject) GetRecurringExpected() float32`

GetRecurringExpected returns the RecurringExpected field if non-nil, zero value otherwise.

### GetRecurringExpectedOk

`func (o *NonAlignedCategoryTotalsObject) GetRecurringExpectedOk() (*float32, bool)`

GetRecurringExpectedOk returns a tuple with the RecurringExpected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringExpected

`func (o *NonAlignedCategoryTotalsObject) SetRecurringExpected(v float32)`

SetRecurringExpected sets RecurringExpected field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


