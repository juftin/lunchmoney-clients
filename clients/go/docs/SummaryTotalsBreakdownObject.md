# SummaryTotalsBreakdownObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OtherActivity** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of non recurring activity for the given date range | [optional] 
**RecurringActivity** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of recurring activity that has occurred for the given date range | [optional] 
**RecurringRemaining** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of expected recurring activity that has not yet occurred | [optional] 
**RecurringExpected** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of expected recurring activity for the given date range | [optional] 
**Uncategorized** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of non recurring activity coming from un-categorized transactions | [optional] 
**UncategorizedCount** | Pointer to **int32** | Number of un-categorized transactions for the given date range | [optional] 
**UncategorizedRecurring** | Pointer to **float32** | Total amount, in the user&#39;s default currency, of recurring activity coming from un-categorized transactions. | [optional] 

## Methods

### NewSummaryTotalsBreakdownObject

`func NewSummaryTotalsBreakdownObject() *SummaryTotalsBreakdownObject`

NewSummaryTotalsBreakdownObject instantiates a new SummaryTotalsBreakdownObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryTotalsBreakdownObjectWithDefaults

`func NewSummaryTotalsBreakdownObjectWithDefaults() *SummaryTotalsBreakdownObject`

NewSummaryTotalsBreakdownObjectWithDefaults instantiates a new SummaryTotalsBreakdownObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOtherActivity

`func (o *SummaryTotalsBreakdownObject) GetOtherActivity() float32`

GetOtherActivity returns the OtherActivity field if non-nil, zero value otherwise.

### GetOtherActivityOk

`func (o *SummaryTotalsBreakdownObject) GetOtherActivityOk() (*float32, bool)`

GetOtherActivityOk returns a tuple with the OtherActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherActivity

`func (o *SummaryTotalsBreakdownObject) SetOtherActivity(v float32)`

SetOtherActivity sets OtherActivity field to given value.

### HasOtherActivity

`func (o *SummaryTotalsBreakdownObject) HasOtherActivity() bool`

HasOtherActivity returns a boolean if a field has been set.

### GetRecurringActivity

`func (o *SummaryTotalsBreakdownObject) GetRecurringActivity() float32`

GetRecurringActivity returns the RecurringActivity field if non-nil, zero value otherwise.

### GetRecurringActivityOk

`func (o *SummaryTotalsBreakdownObject) GetRecurringActivityOk() (*float32, bool)`

GetRecurringActivityOk returns a tuple with the RecurringActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringActivity

`func (o *SummaryTotalsBreakdownObject) SetRecurringActivity(v float32)`

SetRecurringActivity sets RecurringActivity field to given value.

### HasRecurringActivity

`func (o *SummaryTotalsBreakdownObject) HasRecurringActivity() bool`

HasRecurringActivity returns a boolean if a field has been set.

### GetRecurringRemaining

`func (o *SummaryTotalsBreakdownObject) GetRecurringRemaining() float32`

GetRecurringRemaining returns the RecurringRemaining field if non-nil, zero value otherwise.

### GetRecurringRemainingOk

`func (o *SummaryTotalsBreakdownObject) GetRecurringRemainingOk() (*float32, bool)`

GetRecurringRemainingOk returns a tuple with the RecurringRemaining field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringRemaining

`func (o *SummaryTotalsBreakdownObject) SetRecurringRemaining(v float32)`

SetRecurringRemaining sets RecurringRemaining field to given value.

### HasRecurringRemaining

`func (o *SummaryTotalsBreakdownObject) HasRecurringRemaining() bool`

HasRecurringRemaining returns a boolean if a field has been set.

### GetRecurringExpected

`func (o *SummaryTotalsBreakdownObject) GetRecurringExpected() float32`

GetRecurringExpected returns the RecurringExpected field if non-nil, zero value otherwise.

### GetRecurringExpectedOk

`func (o *SummaryTotalsBreakdownObject) GetRecurringExpectedOk() (*float32, bool)`

GetRecurringExpectedOk returns a tuple with the RecurringExpected field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringExpected

`func (o *SummaryTotalsBreakdownObject) SetRecurringExpected(v float32)`

SetRecurringExpected sets RecurringExpected field to given value.

### HasRecurringExpected

`func (o *SummaryTotalsBreakdownObject) HasRecurringExpected() bool`

HasRecurringExpected returns a boolean if a field has been set.

### GetUncategorized

`func (o *SummaryTotalsBreakdownObject) GetUncategorized() float32`

GetUncategorized returns the Uncategorized field if non-nil, zero value otherwise.

### GetUncategorizedOk

`func (o *SummaryTotalsBreakdownObject) GetUncategorizedOk() (*float32, bool)`

GetUncategorizedOk returns a tuple with the Uncategorized field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUncategorized

`func (o *SummaryTotalsBreakdownObject) SetUncategorized(v float32)`

SetUncategorized sets Uncategorized field to given value.

### HasUncategorized

`func (o *SummaryTotalsBreakdownObject) HasUncategorized() bool`

HasUncategorized returns a boolean if a field has been set.

### GetUncategorizedCount

`func (o *SummaryTotalsBreakdownObject) GetUncategorizedCount() int32`

GetUncategorizedCount returns the UncategorizedCount field if non-nil, zero value otherwise.

### GetUncategorizedCountOk

`func (o *SummaryTotalsBreakdownObject) GetUncategorizedCountOk() (*int32, bool)`

GetUncategorizedCountOk returns a tuple with the UncategorizedCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUncategorizedCount

`func (o *SummaryTotalsBreakdownObject) SetUncategorizedCount(v int32)`

SetUncategorizedCount sets UncategorizedCount field to given value.

### HasUncategorizedCount

`func (o *SummaryTotalsBreakdownObject) HasUncategorizedCount() bool`

HasUncategorizedCount returns a boolean if a field has been set.

### GetUncategorizedRecurring

`func (o *SummaryTotalsBreakdownObject) GetUncategorizedRecurring() float32`

GetUncategorizedRecurring returns the UncategorizedRecurring field if non-nil, zero value otherwise.

### GetUncategorizedRecurringOk

`func (o *SummaryTotalsBreakdownObject) GetUncategorizedRecurringOk() (*float32, bool)`

GetUncategorizedRecurringOk returns a tuple with the UncategorizedRecurring field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUncategorizedRecurring

`func (o *SummaryTotalsBreakdownObject) SetUncategorizedRecurring(v float32)`

SetUncategorizedRecurring sets UncategorizedRecurring field to given value.

### HasUncategorizedRecurring

`func (o *SummaryTotalsBreakdownObject) HasUncategorizedRecurring() bool`

HasUncategorizedRecurring returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


