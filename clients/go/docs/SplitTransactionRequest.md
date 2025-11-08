# SplitTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChildTransactions** | [**[]SplitTransactionObject**](SplitTransactionObject.md) | List of child transactions to create. The sum of the &#x60;amounts&#x60; must match the split transaction amount. | 

## Methods

### NewSplitTransactionRequest

`func NewSplitTransactionRequest(childTransactions []SplitTransactionObject, ) *SplitTransactionRequest`

NewSplitTransactionRequest instantiates a new SplitTransactionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSplitTransactionRequestWithDefaults

`func NewSplitTransactionRequestWithDefaults() *SplitTransactionRequest`

NewSplitTransactionRequestWithDefaults instantiates a new SplitTransactionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChildTransactions

`func (o *SplitTransactionRequest) GetChildTransactions() []SplitTransactionObject`

GetChildTransactions returns the ChildTransactions field if non-nil, zero value otherwise.

### GetChildTransactionsOk

`func (o *SplitTransactionRequest) GetChildTransactionsOk() (*[]SplitTransactionObject, bool)`

GetChildTransactionsOk returns a tuple with the ChildTransactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildTransactions

`func (o *SplitTransactionRequest) SetChildTransactions(v []SplitTransactionObject)`

SetChildTransactions sets ChildTransactions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


