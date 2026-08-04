# UpsertBudget400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | **string** | High level error type, for example &#39;Not Found&#39; or &#39;Request Validation Failure&#39; | 
**RequestedStartDate** | **string** | The start_date value that was rejected | 
**PreviousValidStartDate** | Pointer to **NullableString** | The previous valid budget period start date before the requested date | [optional] 
**NextValidStartDate** | Pointer to **NullableString** | The next valid budget period start date after the requested date | [optional] 
**ErrMsg** | **string** | Human-readable error message | 
**Errors** | [**[]ErrorResponseObjectErrorsInner**](ErrorResponseObjectErrorsInner.md) | A list of objects that describe the errors encountered while processing the request.&lt;br&gt; If multiple errors were encountered, the list will contain multiple objects.&lt;br&gt; Each &#x60;error&#x60; object is guaranteed to have an &#x60;errMsg&#x60;, but it may also contain other error-specific properties such as &#x60;code&#x60; (for example &#x60;VALIDATION_ERROR&#x60;), or other properties that are useful to map the error to the relevant part of the request. | 

## Methods

### NewUpsertBudget400Response

`func NewUpsertBudget400Response(message string, requestedStartDate string, errMsg string, errors []ErrorResponseObjectErrorsInner, ) *UpsertBudget400Response`

NewUpsertBudget400Response instantiates a new UpsertBudget400Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpsertBudget400ResponseWithDefaults

`func NewUpsertBudget400ResponseWithDefaults() *UpsertBudget400Response`

NewUpsertBudget400ResponseWithDefaults instantiates a new UpsertBudget400Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *UpsertBudget400Response) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *UpsertBudget400Response) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *UpsertBudget400Response) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetRequestedStartDate

`func (o *UpsertBudget400Response) GetRequestedStartDate() string`

GetRequestedStartDate returns the RequestedStartDate field if non-nil, zero value otherwise.

### GetRequestedStartDateOk

`func (o *UpsertBudget400Response) GetRequestedStartDateOk() (*string, bool)`

GetRequestedStartDateOk returns a tuple with the RequestedStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestedStartDate

`func (o *UpsertBudget400Response) SetRequestedStartDate(v string)`

SetRequestedStartDate sets RequestedStartDate field to given value.


### GetPreviousValidStartDate

`func (o *UpsertBudget400Response) GetPreviousValidStartDate() string`

GetPreviousValidStartDate returns the PreviousValidStartDate field if non-nil, zero value otherwise.

### GetPreviousValidStartDateOk

`func (o *UpsertBudget400Response) GetPreviousValidStartDateOk() (*string, bool)`

GetPreviousValidStartDateOk returns a tuple with the PreviousValidStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreviousValidStartDate

`func (o *UpsertBudget400Response) SetPreviousValidStartDate(v string)`

SetPreviousValidStartDate sets PreviousValidStartDate field to given value.

### HasPreviousValidStartDate

`func (o *UpsertBudget400Response) HasPreviousValidStartDate() bool`

HasPreviousValidStartDate returns a boolean if a field has been set.

### SetPreviousValidStartDateNil

`func (o *UpsertBudget400Response) SetPreviousValidStartDateNil(b bool)`

 SetPreviousValidStartDateNil sets the value for PreviousValidStartDate to be an explicit nil

### UnsetPreviousValidStartDate
`func (o *UpsertBudget400Response) UnsetPreviousValidStartDate()`

UnsetPreviousValidStartDate ensures that no value is present for PreviousValidStartDate, not even an explicit nil
### GetNextValidStartDate

`func (o *UpsertBudget400Response) GetNextValidStartDate() string`

GetNextValidStartDate returns the NextValidStartDate field if non-nil, zero value otherwise.

### GetNextValidStartDateOk

`func (o *UpsertBudget400Response) GetNextValidStartDateOk() (*string, bool)`

GetNextValidStartDateOk returns a tuple with the NextValidStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextValidStartDate

`func (o *UpsertBudget400Response) SetNextValidStartDate(v string)`

SetNextValidStartDate sets NextValidStartDate field to given value.

### HasNextValidStartDate

`func (o *UpsertBudget400Response) HasNextValidStartDate() bool`

HasNextValidStartDate returns a boolean if a field has been set.

### SetNextValidStartDateNil

`func (o *UpsertBudget400Response) SetNextValidStartDateNil(b bool)`

 SetNextValidStartDateNil sets the value for NextValidStartDate to be an explicit nil

### UnsetNextValidStartDate
`func (o *UpsertBudget400Response) UnsetNextValidStartDate()`

UnsetNextValidStartDate ensures that no value is present for NextValidStartDate, not even an explicit nil
### GetErrMsg

`func (o *UpsertBudget400Response) GetErrMsg() string`

GetErrMsg returns the ErrMsg field if non-nil, zero value otherwise.

### GetErrMsgOk

`func (o *UpsertBudget400Response) GetErrMsgOk() (*string, bool)`

GetErrMsgOk returns a tuple with the ErrMsg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrMsg

`func (o *UpsertBudget400Response) SetErrMsg(v string)`

SetErrMsg sets ErrMsg field to given value.


### GetErrors

`func (o *UpsertBudget400Response) GetErrors() []ErrorResponseObjectErrorsInner`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *UpsertBudget400Response) GetErrorsOk() (*[]ErrorResponseObjectErrorsInner, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *UpsertBudget400Response) SetErrors(v []ErrorResponseObjectErrorsInner)`

SetErrors sets Errors field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


