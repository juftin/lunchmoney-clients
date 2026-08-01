# SummaryCategoryOccurrenceObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InRange** | **bool** | &#x60;true&#x60; if this occurrence is within the given date range, &#x60;false&#x60; if it was included because the &#x60;include_past_budget_periods&#x60; parameter was set to &#x60;true&#x60;. | 
**StartDate** | **string** | The start date of the budget period | 
**EndDate** | **string** | The end date of the budget period | 
**OtherActivity** | **float32** | Total non-recurring activity, in the user&#39;s default currency, for the budget period. The total activity for this category in the period is the sum of this and the recurring_activity. | 
**RecurringActivity** | **float32** | Total recurring activity, in the user&#39;s default currency, for the budget period. The total activity for this category in the budget period is the sum of this and the other_activity. | 
**Budgeted** | **NullableFloat32** | Total budgeted amount, in the user&#39;s primary currency, for the period, or &#x60;null&#x60; if no budget was set. | 
**BudgetedAmount** | **NullableString** | Total budgeted amount, in the budgeted currency, for the category within the period, or &#x60;null&#x60; if no budget was set. | 
**BudgetedCurrency** | [**NullableCurrencyEnum**](CurrencyEnum.md) | Currency of the budgeted amount | 
**Notes** | **NullableString** | Any notes set for the budget period. | 

## Methods

### NewSummaryCategoryOccurrenceObject

`func NewSummaryCategoryOccurrenceObject(inRange bool, startDate string, endDate string, otherActivity float32, recurringActivity float32, budgeted NullableFloat32, budgetedAmount NullableString, budgetedCurrency NullableCurrencyEnum, notes NullableString, ) *SummaryCategoryOccurrenceObject`

NewSummaryCategoryOccurrenceObject instantiates a new SummaryCategoryOccurrenceObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryCategoryOccurrenceObjectWithDefaults

`func NewSummaryCategoryOccurrenceObjectWithDefaults() *SummaryCategoryOccurrenceObject`

NewSummaryCategoryOccurrenceObjectWithDefaults instantiates a new SummaryCategoryOccurrenceObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInRange

`func (o *SummaryCategoryOccurrenceObject) GetInRange() bool`

GetInRange returns the InRange field if non-nil, zero value otherwise.

### GetInRangeOk

`func (o *SummaryCategoryOccurrenceObject) GetInRangeOk() (*bool, bool)`

GetInRangeOk returns a tuple with the InRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInRange

`func (o *SummaryCategoryOccurrenceObject) SetInRange(v bool)`

SetInRange sets InRange field to given value.


### GetStartDate

`func (o *SummaryCategoryOccurrenceObject) GetStartDate() string`

GetStartDate returns the StartDate field if non-nil, zero value otherwise.

### GetStartDateOk

`func (o *SummaryCategoryOccurrenceObject) GetStartDateOk() (*string, bool)`

GetStartDateOk returns a tuple with the StartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartDate

`func (o *SummaryCategoryOccurrenceObject) SetStartDate(v string)`

SetStartDate sets StartDate field to given value.


### GetEndDate

`func (o *SummaryCategoryOccurrenceObject) GetEndDate() string`

GetEndDate returns the EndDate field if non-nil, zero value otherwise.

### GetEndDateOk

`func (o *SummaryCategoryOccurrenceObject) GetEndDateOk() (*string, bool)`

GetEndDateOk returns a tuple with the EndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndDate

`func (o *SummaryCategoryOccurrenceObject) SetEndDate(v string)`

SetEndDate sets EndDate field to given value.


### GetOtherActivity

`func (o *SummaryCategoryOccurrenceObject) GetOtherActivity() float32`

GetOtherActivity returns the OtherActivity field if non-nil, zero value otherwise.

### GetOtherActivityOk

`func (o *SummaryCategoryOccurrenceObject) GetOtherActivityOk() (*float32, bool)`

GetOtherActivityOk returns a tuple with the OtherActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOtherActivity

`func (o *SummaryCategoryOccurrenceObject) SetOtherActivity(v float32)`

SetOtherActivity sets OtherActivity field to given value.


### GetRecurringActivity

`func (o *SummaryCategoryOccurrenceObject) GetRecurringActivity() float32`

GetRecurringActivity returns the RecurringActivity field if non-nil, zero value otherwise.

### GetRecurringActivityOk

`func (o *SummaryCategoryOccurrenceObject) GetRecurringActivityOk() (*float32, bool)`

GetRecurringActivityOk returns a tuple with the RecurringActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurringActivity

`func (o *SummaryCategoryOccurrenceObject) SetRecurringActivity(v float32)`

SetRecurringActivity sets RecurringActivity field to given value.


### GetBudgeted

`func (o *SummaryCategoryOccurrenceObject) GetBudgeted() float32`

GetBudgeted returns the Budgeted field if non-nil, zero value otherwise.

### GetBudgetedOk

`func (o *SummaryCategoryOccurrenceObject) GetBudgetedOk() (*float32, bool)`

GetBudgetedOk returns a tuple with the Budgeted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgeted

`func (o *SummaryCategoryOccurrenceObject) SetBudgeted(v float32)`

SetBudgeted sets Budgeted field to given value.


### SetBudgetedNil

`func (o *SummaryCategoryOccurrenceObject) SetBudgetedNil(b bool)`

 SetBudgetedNil sets the value for Budgeted to be an explicit nil

### UnsetBudgeted
`func (o *SummaryCategoryOccurrenceObject) UnsetBudgeted()`

UnsetBudgeted ensures that no value is present for Budgeted, not even an explicit nil
### GetBudgetedAmount

`func (o *SummaryCategoryOccurrenceObject) GetBudgetedAmount() string`

GetBudgetedAmount returns the BudgetedAmount field if non-nil, zero value otherwise.

### GetBudgetedAmountOk

`func (o *SummaryCategoryOccurrenceObject) GetBudgetedAmountOk() (*string, bool)`

GetBudgetedAmountOk returns a tuple with the BudgetedAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetedAmount

`func (o *SummaryCategoryOccurrenceObject) SetBudgetedAmount(v string)`

SetBudgetedAmount sets BudgetedAmount field to given value.


### SetBudgetedAmountNil

`func (o *SummaryCategoryOccurrenceObject) SetBudgetedAmountNil(b bool)`

 SetBudgetedAmountNil sets the value for BudgetedAmount to be an explicit nil

### UnsetBudgetedAmount
`func (o *SummaryCategoryOccurrenceObject) UnsetBudgetedAmount()`

UnsetBudgetedAmount ensures that no value is present for BudgetedAmount, not even an explicit nil
### GetBudgetedCurrency

`func (o *SummaryCategoryOccurrenceObject) GetBudgetedCurrency() CurrencyEnum`

GetBudgetedCurrency returns the BudgetedCurrency field if non-nil, zero value otherwise.

### GetBudgetedCurrencyOk

`func (o *SummaryCategoryOccurrenceObject) GetBudgetedCurrencyOk() (*CurrencyEnum, bool)`

GetBudgetedCurrencyOk returns a tuple with the BudgetedCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetedCurrency

`func (o *SummaryCategoryOccurrenceObject) SetBudgetedCurrency(v CurrencyEnum)`

SetBudgetedCurrency sets BudgetedCurrency field to given value.


### SetBudgetedCurrencyNil

`func (o *SummaryCategoryOccurrenceObject) SetBudgetedCurrencyNil(b bool)`

 SetBudgetedCurrencyNil sets the value for BudgetedCurrency to be an explicit nil

### UnsetBudgetedCurrency
`func (o *SummaryCategoryOccurrenceObject) UnsetBudgetedCurrency()`

UnsetBudgetedCurrency ensures that no value is present for BudgetedCurrency, not even an explicit nil
### GetNotes

`func (o *SummaryCategoryOccurrenceObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *SummaryCategoryOccurrenceObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *SummaryCategoryOccurrenceObject) SetNotes(v string)`

SetNotes sets Notes field to given value.


### SetNotesNil

`func (o *SummaryCategoryOccurrenceObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *SummaryCategoryOccurrenceObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


