# UpdateTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**[]UpdateTransactionsRequestTransactionsInner**](UpdateTransactionsRequestTransactionsInner.md) | List of transactions to update. Each transaction must have an &#x60;id&#x60; property and at least one other property to update. | 

## Methods

### NewUpdateTransactionsRequest

`func NewUpdateTransactionsRequest(transactions []UpdateTransactionsRequestTransactionsInner, ) *UpdateTransactionsRequest`

NewUpdateTransactionsRequest instantiates a new UpdateTransactionsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateTransactionsRequestWithDefaults

`func NewUpdateTransactionsRequestWithDefaults() *UpdateTransactionsRequest`

NewUpdateTransactionsRequestWithDefaults instantiates a new UpdateTransactionsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactions

`func (o *UpdateTransactionsRequest) GetTransactions() []UpdateTransactionsRequestTransactionsInner`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *UpdateTransactionsRequest) GetTransactionsOk() (*[]UpdateTransactionsRequestTransactionsInner, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *UpdateTransactionsRequest) SetTransactions(v []UpdateTransactionsRequestTransactionsInner)`

SetTransactions sets Transactions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


