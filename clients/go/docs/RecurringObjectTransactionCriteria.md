# RecurringObjectTransactionCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StartDate** | Pointer to **NullableString** | The beginning of the date range for matching transactions. If &#x60;null&#x60;, any transactions before end_date may be considered. | [optional] 
**EndDate** | Pointer to **NullableString** | The end of the date range for matching transactions. If &#x60;null&#x60;, any transactions after start_date may be considered. | [optional] 
**Granularity** | Pointer to **string** | The unit of time used to define the cadence of the recurring item. | [optional] 
**Quantity** | Pointer to **int32** | The number of granularity units between each recurrence. | [optional] 
**AnchorDate** | Pointer to **string** | The date used in conjunction with the &#x60;quantity&#x60; and &#x60;granularity&#x60; properties to calculate expected occurrences of recurring transactions. | [optional] 
**Payee** | Pointer to **NullableString** | If set, represents the original transaction payee name that triggered this recurring item&#39;s creation. | [optional] 
**Amount** | Pointer to **string** | The expected amount for a transaction that will match this recurring item. For recurring items that have a flexible amount this is the average of the specified min and max amounts. | [optional] 
**Currency** | Pointer to **string** | Three-letter lowercase currency code of the recurring item. | [optional] 
**PlaidAccountId** | Pointer to **NullableInt64** | The Plaid account ID associated with the recurring item, if any. | [optional] 
**ManualAccountId** | Pointer to **NullableInt64** | The manual account ID associated with the recurring item, if any. | [optional] 

## Methods

### NewRecurringObjectTransactionCriteria

`func NewRecurringObjectTransactionCriteria() *RecurringObjectTransactionCriteria`

NewRecurringObjectTransactionCriteria instantiates a new RecurringObjectTransactionCriteria object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRecurringObjectTransactionCriteriaWithDefaults

`func NewRecurringObjectTransactionCriteriaWithDefaults() *RecurringObjectTransactionCriteria`

NewRecurringObjectTransactionCriteriaWithDefaults instantiates a new RecurringObjectTransactionCriteria object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStartDate

`func (o *RecurringObjectTransactionCriteria) GetStartDate() string`

GetStartDate returns the StartDate field if non-nil, zero value otherwise.

### GetStartDateOk

`func (o *RecurringObjectTransactionCriteria) GetStartDateOk() (*string, bool)`

GetStartDateOk returns a tuple with the StartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartDate

`func (o *RecurringObjectTransactionCriteria) SetStartDate(v string)`

SetStartDate sets StartDate field to given value.

### HasStartDate

`func (o *RecurringObjectTransactionCriteria) HasStartDate() bool`

HasStartDate returns a boolean if a field has been set.

### SetStartDateNil

`func (o *RecurringObjectTransactionCriteria) SetStartDateNil(b bool)`

 SetStartDateNil sets the value for StartDate to be an explicit nil

### UnsetStartDate
`func (o *RecurringObjectTransactionCriteria) UnsetStartDate()`

UnsetStartDate ensures that no value is present for StartDate, not even an explicit nil
### GetEndDate

`func (o *RecurringObjectTransactionCriteria) GetEndDate() string`

GetEndDate returns the EndDate field if non-nil, zero value otherwise.

### GetEndDateOk

`func (o *RecurringObjectTransactionCriteria) GetEndDateOk() (*string, bool)`

GetEndDateOk returns a tuple with the EndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndDate

`func (o *RecurringObjectTransactionCriteria) SetEndDate(v string)`

SetEndDate sets EndDate field to given value.

### HasEndDate

`func (o *RecurringObjectTransactionCriteria) HasEndDate() bool`

HasEndDate returns a boolean if a field has been set.

### SetEndDateNil

`func (o *RecurringObjectTransactionCriteria) SetEndDateNil(b bool)`

 SetEndDateNil sets the value for EndDate to be an explicit nil

### UnsetEndDate
`func (o *RecurringObjectTransactionCriteria) UnsetEndDate()`

UnsetEndDate ensures that no value is present for EndDate, not even an explicit nil
### GetGranularity

`func (o *RecurringObjectTransactionCriteria) GetGranularity() string`

GetGranularity returns the Granularity field if non-nil, zero value otherwise.

### GetGranularityOk

`func (o *RecurringObjectTransactionCriteria) GetGranularityOk() (*string, bool)`

GetGranularityOk returns a tuple with the Granularity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGranularity

`func (o *RecurringObjectTransactionCriteria) SetGranularity(v string)`

SetGranularity sets Granularity field to given value.

### HasGranularity

`func (o *RecurringObjectTransactionCriteria) HasGranularity() bool`

HasGranularity returns a boolean if a field has been set.

### GetQuantity

`func (o *RecurringObjectTransactionCriteria) GetQuantity() int32`

GetQuantity returns the Quantity field if non-nil, zero value otherwise.

### GetQuantityOk

`func (o *RecurringObjectTransactionCriteria) GetQuantityOk() (*int32, bool)`

GetQuantityOk returns a tuple with the Quantity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantity

`func (o *RecurringObjectTransactionCriteria) SetQuantity(v int32)`

SetQuantity sets Quantity field to given value.

### HasQuantity

`func (o *RecurringObjectTransactionCriteria) HasQuantity() bool`

HasQuantity returns a boolean if a field has been set.

### GetAnchorDate

`func (o *RecurringObjectTransactionCriteria) GetAnchorDate() string`

GetAnchorDate returns the AnchorDate field if non-nil, zero value otherwise.

### GetAnchorDateOk

`func (o *RecurringObjectTransactionCriteria) GetAnchorDateOk() (*string, bool)`

GetAnchorDateOk returns a tuple with the AnchorDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAnchorDate

`func (o *RecurringObjectTransactionCriteria) SetAnchorDate(v string)`

SetAnchorDate sets AnchorDate field to given value.

### HasAnchorDate

`func (o *RecurringObjectTransactionCriteria) HasAnchorDate() bool`

HasAnchorDate returns a boolean if a field has been set.

### GetPayee

`func (o *RecurringObjectTransactionCriteria) GetPayee() string`

GetPayee returns the Payee field if non-nil, zero value otherwise.

### GetPayeeOk

`func (o *RecurringObjectTransactionCriteria) GetPayeeOk() (*string, bool)`

GetPayeeOk returns a tuple with the Payee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayee

`func (o *RecurringObjectTransactionCriteria) SetPayee(v string)`

SetPayee sets Payee field to given value.

### HasPayee

`func (o *RecurringObjectTransactionCriteria) HasPayee() bool`

HasPayee returns a boolean if a field has been set.

### SetPayeeNil

`func (o *RecurringObjectTransactionCriteria) SetPayeeNil(b bool)`

 SetPayeeNil sets the value for Payee to be an explicit nil

### UnsetPayee
`func (o *RecurringObjectTransactionCriteria) UnsetPayee()`

UnsetPayee ensures that no value is present for Payee, not even an explicit nil
### GetAmount

`func (o *RecurringObjectTransactionCriteria) GetAmount() string`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *RecurringObjectTransactionCriteria) GetAmountOk() (*string, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *RecurringObjectTransactionCriteria) SetAmount(v string)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *RecurringObjectTransactionCriteria) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetCurrency

`func (o *RecurringObjectTransactionCriteria) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *RecurringObjectTransactionCriteria) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *RecurringObjectTransactionCriteria) SetCurrency(v string)`

SetCurrency sets Currency field to given value.

### HasCurrency

`func (o *RecurringObjectTransactionCriteria) HasCurrency() bool`

HasCurrency returns a boolean if a field has been set.

### GetPlaidAccountId

`func (o *RecurringObjectTransactionCriteria) GetPlaidAccountId() int64`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *RecurringObjectTransactionCriteria) GetPlaidAccountIdOk() (*int64, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *RecurringObjectTransactionCriteria) SetPlaidAccountId(v int64)`

SetPlaidAccountId sets PlaidAccountId field to given value.

### HasPlaidAccountId

`func (o *RecurringObjectTransactionCriteria) HasPlaidAccountId() bool`

HasPlaidAccountId returns a boolean if a field has been set.

### SetPlaidAccountIdNil

`func (o *RecurringObjectTransactionCriteria) SetPlaidAccountIdNil(b bool)`

 SetPlaidAccountIdNil sets the value for PlaidAccountId to be an explicit nil

### UnsetPlaidAccountId
`func (o *RecurringObjectTransactionCriteria) UnsetPlaidAccountId()`

UnsetPlaidAccountId ensures that no value is present for PlaidAccountId, not even an explicit nil
### GetManualAccountId

`func (o *RecurringObjectTransactionCriteria) GetManualAccountId() int64`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *RecurringObjectTransactionCriteria) GetManualAccountIdOk() (*int64, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *RecurringObjectTransactionCriteria) SetManualAccountId(v int64)`

SetManualAccountId sets ManualAccountId field to given value.

### HasManualAccountId

`func (o *RecurringObjectTransactionCriteria) HasManualAccountId() bool`

HasManualAccountId returns a boolean if a field has been set.

### SetManualAccountIdNil

`func (o *RecurringObjectTransactionCriteria) SetManualAccountIdNil(b bool)`

 SetManualAccountIdNil sets the value for ManualAccountId to be an explicit nil

### UnsetManualAccountId
`func (o *RecurringObjectTransactionCriteria) UnsetManualAccountId()`

UnsetManualAccountId ensures that no value is present for ManualAccountId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


