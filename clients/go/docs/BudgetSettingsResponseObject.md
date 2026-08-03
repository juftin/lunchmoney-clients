# BudgetSettingsResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BudgetPeriodGranularity** | **string** | Budget period granularity | 
**BudgetPeriodQuantity** | **int32** | The number of &#x60;granularity&#x60; units that make up a single budgeting period. | 
**BudgetPeriodAnchorDate** | **string** | The date from which the budgeting period is calculated. All future (and past) periods are derived by applying &#x60;quantity&#x60; × &#x60;granularity&#x60; forward and backward from this date. | 
**BudgetHideNoActivity** | **bool** | Display preference for hiding categories in budget view that have no activity and no budgeted value | [default to false]
**BudgetUseLastDayOfMonth** | **bool** | Display preference for using the last day of the month as the period end for monthly periods | [default to false]
**BudgetIncomeOption** | **string** | Determines which income value is used as the base when calculating available funds for a budgeting period | 
**BudgetRolloverLeftToBudget** | **bool** | Determines whether the remaining unallocated funds (“Left to Budget”) at the end of a budgeting period are carried forward to the next period | [default to false]

## Methods

### NewBudgetSettingsResponseObject

`func NewBudgetSettingsResponseObject(budgetPeriodGranularity string, budgetPeriodQuantity int32, budgetPeriodAnchorDate string, budgetHideNoActivity bool, budgetUseLastDayOfMonth bool, budgetIncomeOption string, budgetRolloverLeftToBudget bool, ) *BudgetSettingsResponseObject`

NewBudgetSettingsResponseObject instantiates a new BudgetSettingsResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBudgetSettingsResponseObjectWithDefaults

`func NewBudgetSettingsResponseObjectWithDefaults() *BudgetSettingsResponseObject`

NewBudgetSettingsResponseObjectWithDefaults instantiates a new BudgetSettingsResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBudgetPeriodGranularity

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodGranularity() string`

GetBudgetPeriodGranularity returns the BudgetPeriodGranularity field if non-nil, zero value otherwise.

### GetBudgetPeriodGranularityOk

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodGranularityOk() (*string, bool)`

GetBudgetPeriodGranularityOk returns a tuple with the BudgetPeriodGranularity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetPeriodGranularity

`func (o *BudgetSettingsResponseObject) SetBudgetPeriodGranularity(v string)`

SetBudgetPeriodGranularity sets BudgetPeriodGranularity field to given value.


### GetBudgetPeriodQuantity

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodQuantity() int32`

GetBudgetPeriodQuantity returns the BudgetPeriodQuantity field if non-nil, zero value otherwise.

### GetBudgetPeriodQuantityOk

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodQuantityOk() (*int32, bool)`

GetBudgetPeriodQuantityOk returns a tuple with the BudgetPeriodQuantity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetPeriodQuantity

`func (o *BudgetSettingsResponseObject) SetBudgetPeriodQuantity(v int32)`

SetBudgetPeriodQuantity sets BudgetPeriodQuantity field to given value.


### GetBudgetPeriodAnchorDate

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodAnchorDate() string`

GetBudgetPeriodAnchorDate returns the BudgetPeriodAnchorDate field if non-nil, zero value otherwise.

### GetBudgetPeriodAnchorDateOk

`func (o *BudgetSettingsResponseObject) GetBudgetPeriodAnchorDateOk() (*string, bool)`

GetBudgetPeriodAnchorDateOk returns a tuple with the BudgetPeriodAnchorDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetPeriodAnchorDate

`func (o *BudgetSettingsResponseObject) SetBudgetPeriodAnchorDate(v string)`

SetBudgetPeriodAnchorDate sets BudgetPeriodAnchorDate field to given value.


### GetBudgetHideNoActivity

`func (o *BudgetSettingsResponseObject) GetBudgetHideNoActivity() bool`

GetBudgetHideNoActivity returns the BudgetHideNoActivity field if non-nil, zero value otherwise.

### GetBudgetHideNoActivityOk

`func (o *BudgetSettingsResponseObject) GetBudgetHideNoActivityOk() (*bool, bool)`

GetBudgetHideNoActivityOk returns a tuple with the BudgetHideNoActivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetHideNoActivity

`func (o *BudgetSettingsResponseObject) SetBudgetHideNoActivity(v bool)`

SetBudgetHideNoActivity sets BudgetHideNoActivity field to given value.


### GetBudgetUseLastDayOfMonth

`func (o *BudgetSettingsResponseObject) GetBudgetUseLastDayOfMonth() bool`

GetBudgetUseLastDayOfMonth returns the BudgetUseLastDayOfMonth field if non-nil, zero value otherwise.

### GetBudgetUseLastDayOfMonthOk

`func (o *BudgetSettingsResponseObject) GetBudgetUseLastDayOfMonthOk() (*bool, bool)`

GetBudgetUseLastDayOfMonthOk returns a tuple with the BudgetUseLastDayOfMonth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetUseLastDayOfMonth

`func (o *BudgetSettingsResponseObject) SetBudgetUseLastDayOfMonth(v bool)`

SetBudgetUseLastDayOfMonth sets BudgetUseLastDayOfMonth field to given value.


### GetBudgetIncomeOption

`func (o *BudgetSettingsResponseObject) GetBudgetIncomeOption() string`

GetBudgetIncomeOption returns the BudgetIncomeOption field if non-nil, zero value otherwise.

### GetBudgetIncomeOptionOk

`func (o *BudgetSettingsResponseObject) GetBudgetIncomeOptionOk() (*string, bool)`

GetBudgetIncomeOptionOk returns a tuple with the BudgetIncomeOption field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetIncomeOption

`func (o *BudgetSettingsResponseObject) SetBudgetIncomeOption(v string)`

SetBudgetIncomeOption sets BudgetIncomeOption field to given value.


### GetBudgetRolloverLeftToBudget

`func (o *BudgetSettingsResponseObject) GetBudgetRolloverLeftToBudget() bool`

GetBudgetRolloverLeftToBudget returns the BudgetRolloverLeftToBudget field if non-nil, zero value otherwise.

### GetBudgetRolloverLeftToBudgetOk

`func (o *BudgetSettingsResponseObject) GetBudgetRolloverLeftToBudgetOk() (*bool, bool)`

GetBudgetRolloverLeftToBudgetOk returns a tuple with the BudgetRolloverLeftToBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetRolloverLeftToBudget

`func (o *BudgetSettingsResponseObject) SetBudgetRolloverLeftToBudget(v bool)`

SetBudgetRolloverLeftToBudget sets BudgetRolloverLeftToBudget field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


