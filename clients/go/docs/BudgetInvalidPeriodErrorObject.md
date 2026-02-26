# BudgetInvalidPeriodErrorObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | **string** | Overall error message (e.g. Invalid Request) | 
**RequestedStartDate** | **string** | The start_date value that was rejected | 
**PreviousValidStartDate** | Pointer to **NullableString** | The previous valid budget period start date before the requested date | [optional] 
**NextValidStartDate** | Pointer to **NullableString** | The next valid budget period start date after the requested date | [optional] 
**ErrMsg** | **string** | Human-readable error message | 

## Methods

### NewBudgetInvalidPeriodErrorObject

`func NewBudgetInvalidPeriodErrorObject(message string, requestedStartDate string, errMsg string, ) *BudgetInvalidPeriodErrorObject`

NewBudgetInvalidPeriodErrorObject instantiates a new BudgetInvalidPeriodErrorObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBudgetInvalidPeriodErrorObjectWithDefaults

`func NewBudgetInvalidPeriodErrorObjectWithDefaults() *BudgetInvalidPeriodErrorObject`

NewBudgetInvalidPeriodErrorObjectWithDefaults instantiates a new BudgetInvalidPeriodErrorObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *BudgetInvalidPeriodErrorObject) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *BudgetInvalidPeriodErrorObject) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *BudgetInvalidPeriodErrorObject) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetRequestedStartDate

`func (o *BudgetInvalidPeriodErrorObject) GetRequestedStartDate() string`

GetRequestedStartDate returns the RequestedStartDate field if non-nil, zero value otherwise.

### GetRequestedStartDateOk

`func (o *BudgetInvalidPeriodErrorObject) GetRequestedStartDateOk() (*string, bool)`

GetRequestedStartDateOk returns a tuple with the RequestedStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestedStartDate

`func (o *BudgetInvalidPeriodErrorObject) SetRequestedStartDate(v string)`

SetRequestedStartDate sets RequestedStartDate field to given value.


### GetPreviousValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) GetPreviousValidStartDate() string`

GetPreviousValidStartDate returns the PreviousValidStartDate field if non-nil, zero value otherwise.

### GetPreviousValidStartDateOk

`func (o *BudgetInvalidPeriodErrorObject) GetPreviousValidStartDateOk() (*string, bool)`

GetPreviousValidStartDateOk returns a tuple with the PreviousValidStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) SetPreviousValidStartDate(v string)`

SetPreviousValidStartDate sets PreviousValidStartDate field to given value.

### HasPreviousValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) HasPreviousValidStartDate() bool`

HasPreviousValidStartDate returns a boolean if a field has been set.

### SetPreviousValidStartDateNil

`func (o *BudgetInvalidPeriodErrorObject) SetPreviousValidStartDateNil(b bool)`

 SetPreviousValidStartDateNil sets the value for PreviousValidStartDate to be an explicit nil

### UnsetPreviousValidStartDate
`func (o *BudgetInvalidPeriodErrorObject) UnsetPreviousValidStartDate()`

UnsetPreviousValidStartDate ensures that no value is present for PreviousValidStartDate, not even an explicit nil
### GetNextValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) GetNextValidStartDate() string`

GetNextValidStartDate returns the NextValidStartDate field if non-nil, zero value otherwise.

### GetNextValidStartDateOk

`func (o *BudgetInvalidPeriodErrorObject) GetNextValidStartDateOk() (*string, bool)`

GetNextValidStartDateOk returns a tuple with the NextValidStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) SetNextValidStartDate(v string)`

SetNextValidStartDate sets NextValidStartDate field to given value.

### HasNextValidStartDate

`func (o *BudgetInvalidPeriodErrorObject) HasNextValidStartDate() bool`

HasNextValidStartDate returns a boolean if a field has been set.

### SetNextValidStartDateNil

`func (o *BudgetInvalidPeriodErrorObject) SetNextValidStartDateNil(b bool)`

 SetNextValidStartDateNil sets the value for NextValidStartDate to be an explicit nil

### UnsetNextValidStartDate
`func (o *BudgetInvalidPeriodErrorObject) UnsetNextValidStartDate()`

UnsetNextValidStartDate ensures that no value is present for NextValidStartDate, not even an explicit nil
### GetErrMsg

`func (o *BudgetInvalidPeriodErrorObject) GetErrMsg() string`

GetErrMsg returns the ErrMsg field if non-nil, zero value otherwise.

### GetErrMsgOk

`func (o *BudgetInvalidPeriodErrorObject) GetErrMsgOk() (*string, bool)`

GetErrMsgOk returns a tuple with the ErrMsg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrMsg

`func (o *BudgetInvalidPeriodErrorObject) SetErrMsg(v string)`

SetErrMsg sets ErrMsg field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


