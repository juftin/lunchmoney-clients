# ErrorResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | **string** | overall error message | 
**Errors** | [**[]ErrorResponseObjectErrorsInner**](ErrorResponseObjectErrorsInner.md) |  | 

## Methods

### NewErrorResponseObject

`func NewErrorResponseObject(message string, errors []ErrorResponseObjectErrorsInner, ) *ErrorResponseObject`

NewErrorResponseObject instantiates a new ErrorResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewErrorResponseObjectWithDefaults

`func NewErrorResponseObjectWithDefaults() *ErrorResponseObject`

NewErrorResponseObjectWithDefaults instantiates a new ErrorResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *ErrorResponseObject) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ErrorResponseObject) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ErrorResponseObject) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetErrors

`func (o *ErrorResponseObject) GetErrors() []ErrorResponseObjectErrorsInner`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *ErrorResponseObject) GetErrorsOk() (*[]ErrorResponseObjectErrorsInner, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *ErrorResponseObject) SetErrors(v []ErrorResponseObjectErrorsInner)`

SetErrors sets Errors field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


