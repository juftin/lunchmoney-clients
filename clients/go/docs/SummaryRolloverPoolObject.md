# SummaryRolloverPoolObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BudgetedToBase** | **float32** | Amount of funds, in the user&#39;s default currency, currently available to rollover. | 
**AllAdjustments** | [**[]SummaryRolloverPoolAdjustmentObject**](SummaryRolloverPoolAdjustmentObject.md) | List of previous adjustments to the rollover pool | 

## Methods

### NewSummaryRolloverPoolObject

`func NewSummaryRolloverPoolObject(budgetedToBase float32, allAdjustments []SummaryRolloverPoolAdjustmentObject, ) *SummaryRolloverPoolObject`

NewSummaryRolloverPoolObject instantiates a new SummaryRolloverPoolObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryRolloverPoolObjectWithDefaults

`func NewSummaryRolloverPoolObjectWithDefaults() *SummaryRolloverPoolObject`

NewSummaryRolloverPoolObjectWithDefaults instantiates a new SummaryRolloverPoolObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBudgetedToBase

`func (o *SummaryRolloverPoolObject) GetBudgetedToBase() float32`

GetBudgetedToBase returns the BudgetedToBase field if non-nil, zero value otherwise.

### GetBudgetedToBaseOk

`func (o *SummaryRolloverPoolObject) GetBudgetedToBaseOk() (*float32, bool)`

GetBudgetedToBaseOk returns a tuple with the BudgetedToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetedToBase

`func (o *SummaryRolloverPoolObject) SetBudgetedToBase(v float32)`

SetBudgetedToBase sets BudgetedToBase field to given value.


### GetAllAdjustments

`func (o *SummaryRolloverPoolObject) GetAllAdjustments() []SummaryRolloverPoolAdjustmentObject`

GetAllAdjustments returns the AllAdjustments field if non-nil, zero value otherwise.

### GetAllAdjustmentsOk

`func (o *SummaryRolloverPoolObject) GetAllAdjustmentsOk() (*[]SummaryRolloverPoolAdjustmentObject, bool)`

GetAllAdjustmentsOk returns a tuple with the AllAdjustments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllAdjustments

`func (o *SummaryRolloverPoolObject) SetAllAdjustments(v []SummaryRolloverPoolAdjustmentObject)`

SetAllAdjustments sets AllAdjustments field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


