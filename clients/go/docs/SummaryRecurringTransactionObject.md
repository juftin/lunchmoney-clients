# SummaryRecurringTransactionObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Date** | **string** |  | 
**CategoryId** | **int32** |  | 
**Payee** | **string** |  | 
**ToBase** | **float32** |  | 
**Amount** | **string** |  | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) |  | 

## Methods

### NewSummaryRecurringTransactionObject

`func NewSummaryRecurringTransactionObject(date string, categoryId int32, payee string, toBase float32, amount string, currency CurrencyEnum, ) *SummaryRecurringTransactionObject`

NewSummaryRecurringTransactionObject instantiates a new SummaryRecurringTransactionObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSummaryRecurringTransactionObjectWithDefaults

`func NewSummaryRecurringTransactionObjectWithDefaults() *SummaryRecurringTransactionObject`

NewSummaryRecurringTransactionObjectWithDefaults instantiates a new SummaryRecurringTransactionObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDate

`func (o *SummaryRecurringTransactionObject) GetDate() string`

GetDate returns the Date field if non-nil, zero value otherwise.

### GetDateOk

`func (o *SummaryRecurringTransactionObject) GetDateOk() (*string, bool)`

GetDateOk returns a tuple with the Date field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDate

`func (o *SummaryRecurringTransactionObject) SetDate(v string)`

SetDate sets Date field to given value.


### GetCategoryId

`func (o *SummaryRecurringTransactionObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *SummaryRecurringTransactionObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *SummaryRecurringTransactionObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetPayee

`func (o *SummaryRecurringTransactionObject) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *SummaryRecurringTransactionObject) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *SummaryRecurringTransactionObject) SetPayee(v string)`

SetPayee sets Payee field to given value.


### GetToBase

`func (o *SummaryRecurringTransactionObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *SummaryRecurringTransactionObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *SummaryRecurringTransactionObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.


### GetAmount

`func (o *SummaryRecurringTransactionObject) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *SummaryRecurringTransactionObject) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *SummaryRecurringTransactionObject) SetAmount(v string)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *SummaryRecurringTransactionObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *SummaryRecurringTransactionObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *SummaryRecurringTransactionObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


