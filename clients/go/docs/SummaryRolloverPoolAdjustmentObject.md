# SummaryRolloverPoolAdjustmentObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InRange** | **bool** | &#x60;true&#x60; if this rollover pool adjustment is for a budget period that falls within the given date range. | 
**Date** | **string** | Date the adjustment was made. | 
**Amount** | **string** | Amount of the rollover pool, in the budget&#39;s currency, at the time of the adjustment. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the rollover pool at the time of the adjustment. | 
**ToBase** | **float32** | Amount of the rollover pool, in the user&#39;s default currency, at the time of the adjustment. | 

## Methods

### NewSummaryRolloverPoolAdjustmentObject

`func NewSummaryRolloverPoolAdjustmentObject(inRange bool, date string, amount string, currency CurrencyEnum, toBase float32, ) *SummaryRolloverPoolAdjustmentObject`

NewSummaryRolloverPoolAdjustmentObject instantiates a new SummaryRolloverPoolAdjustmentObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryRolloverPoolAdjustmentObjectWithDefaults

`func NewSummaryRolloverPoolAdjustmentObjectWithDefaults() *SummaryRolloverPoolAdjustmentObject`

NewSummaryRolloverPoolAdjustmentObjectWithDefaults instantiates a new SummaryRolloverPoolAdjustmentObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInRange

`func (o *SummaryRolloverPoolAdjustmentObject) GetInRange() bool`

GetInRange returns the InRange field if non-nil, zero value otherwise.

### GetInRangeOk

`func (o *SummaryRolloverPoolAdjustmentObject) GetInRangeOk() (*bool, bool)`

GetInRangeOk returns a tuple with the InRange field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInRange

`func (o *SummaryRolloverPoolAdjustmentObject) SetInRange(v bool)`

SetInRange sets InRange field to given value.


### GetDate

`func (o *SummaryRolloverPoolAdjustmentObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *SummaryRolloverPoolAdjustmentObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *SummaryRolloverPoolAdjustmentObject) SetDate(v string)`

SetDate sets Date field to given value.


### GetAmount

`func (o *SummaryRolloverPoolAdjustmentObject) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *SummaryRolloverPoolAdjustmentObject) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *SummaryRolloverPoolAdjustmentObject) SetAmount(v string)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *SummaryRolloverPoolAdjustmentObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *SummaryRolloverPoolAdjustmentObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *SummaryRolloverPoolAdjustmentObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *SummaryRolloverPoolAdjustmentObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *SummaryRolloverPoolAdjustmentObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *SummaryRolloverPoolAdjustmentObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


