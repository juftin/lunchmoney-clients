# InsertTransactionsResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**[]TransactionObject**](TransactionObject.md) | An array of the inserted transactions. | 
**SkippedDuplicates** | [**[]SkippedExistingExternalIdObject**](SkippedExistingExternalIdObject.md) | An array of the requested transactions that were duplicates of existing transactions and were not inserted. | 

## Methods

### NewInsertTransactionsResponseObject

`func NewInsertTransactionsResponseObject(transactions []TransactionObject, skippedDuplicates []SkippedExistingExternalIdObject, ) *InsertTransactionsResponseObject`

NewInsertTransactionsResponseObject instantiates a new InsertTransactionsResponseObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInsertTransactionsResponseObjectWithDefaults

`func NewInsertTransactionsResponseObjectWithDefaults() *InsertTransactionsResponseObject`

NewInsertTransactionsResponseObjectWithDefaults instantiates a new InsertTransactionsResponseObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactions

`func (o *InsertTransactionsResponseObject) GetTransactions() []TransactionObject`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *InsertTransactionsResponseObject) GetTransactionsOk() (*[]TransactionObject, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *InsertTransactionsResponseObject) SetTransactions(v []TransactionObject)`

SetTransactions sets Transactions field to given value.


### GetSkippedDuplicates

`func (o *InsertTransactionsResponseObject) GetSkippedDuplicates() []SkippedExistingExternalIdObject`

GetSkippedDuplicates returns the SkippedDuplicates field if non-nil, zero value otherwise.

### GetSkippedDuplicatesOk

`func (o *InsertTransactionsResponseObject) GetSkippedDuplicatesOk() (*[]SkippedExistingExternalIdObject, bool)`

GetSkippedDuplicatesOk returns a tuple with the SkippedDuplicates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkippedDuplicates

`func (o *InsertTransactionsResponseObject) SetSkippedDuplicates(v []SkippedExistingExternalIdObject)`

SetSkippedDuplicates sets SkippedDuplicates field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


