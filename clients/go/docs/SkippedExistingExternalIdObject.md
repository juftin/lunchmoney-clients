# SkippedExistingExternalIdObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reason** | Pointer to **string** | The reason the transaction was skipped, may be one of: - &#x60;duplicate_external_id&#x60;: The transaction has the same &#x60;manual_account_id&#x60; and &#x60;external_id&#x60; as an existing transaction - &#x60;duplicate_payee_amount_date&#x60;: The &#x60;skip_duplicates&#x60; request body property was set to &#x60;true&#x60; and the transaction has the same &#x60;amount&#x60;, &#x60;payee&#x60;, and &#x60;date&#x60; as an existing transaction associated with the same account.  | [optional] 
**RequestTransactionsIndex** | Pointer to **int64** | The index of the transaction in the request body&#39;s transactions array that was skipped. | [optional] 
**ExistingTransactionId** | Pointer to **int64** | The id of the existing transactions that the requested transaction duplicates. | [optional] 
**RequestTransaction** | Pointer to [**InsertTransactionObject**](InsertTransactionObject.md) | The requested transaction that was skipped. | [optional] 

## Methods

### NewSkippedExistingExternalIdObject

`func NewSkippedExistingExternalIdObject() *SkippedExistingExternalIdObject`

NewSkippedExistingExternalIdObject instantiates a new SkippedExistingExternalIdObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSkippedExistingExternalIdObjectWithDefaults

`func NewSkippedExistingExternalIdObjectWithDefaults() *SkippedExistingExternalIdObject`

NewSkippedExistingExternalIdObjectWithDefaults instantiates a new SkippedExistingExternalIdObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReason

`func (o *SkippedExistingExternalIdObject) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *SkippedExistingExternalIdObject) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *SkippedExistingExternalIdObject) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *SkippedExistingExternalIdObject) HasReason() bool`

HasReason returns a boolean if a field has been set.

### GetRequestTransactionsIndex

`func (o *SkippedExistingExternalIdObject) GetRequestTransactionsIndex() int64`

GetRequestTransactionsIndex returns the RequestTransactionsIndex field if non-nil, zero value otherwise.

### GetRequestTransactionsIndexOk

`func (o *SkippedExistingExternalIdObject) GetRequestTransactionsIndexOk() (*int64, bool)`

GetRequestTransactionsIndexOk returns a tuple with the RequestTransactionsIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestTransactionsIndex

`func (o *SkippedExistingExternalIdObject) SetRequestTransactionsIndex(v int64)`

SetRequestTransactionsIndex sets RequestTransactionsIndex field to given value.

### HasRequestTransactionsIndex

`func (o *SkippedExistingExternalIdObject) HasRequestTransactionsIndex() bool`

HasRequestTransactionsIndex returns a boolean if a field has been set.

### GetExistingTransactionId

`func (o *SkippedExistingExternalIdObject) GetExistingTransactionId() int64`

GetExistingTransactionId returns the ExistingTransactionId field if non-nil, zero value otherwise.

### GetExistingTransactionIdOk

`func (o *SkippedExistingExternalIdObject) GetExistingTransactionIdOk() (*int64, bool)`

GetExistingTransactionIdOk returns a tuple with the ExistingTransactionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExistingTransactionId

`func (o *SkippedExistingExternalIdObject) SetExistingTransactionId(v int64)`

SetExistingTransactionId sets ExistingTransactionId field to given value.

### HasExistingTransactionId

`func (o *SkippedExistingExternalIdObject) HasExistingTransactionId() bool`

HasExistingTransactionId returns a boolean if a field has been set.

### GetRequestTransaction

`func (o *SkippedExistingExternalIdObject) GetRequestTransaction() InsertTransactionObject`

GetRequestTransaction returns the RequestTransaction field if non-nil, zero value otherwise.

### GetRequestTransactionOk

`func (o *SkippedExistingExternalIdObject) GetRequestTransactionOk() (*InsertTransactionObject, bool)`

GetRequestTransactionOk returns a tuple with the RequestTransaction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestTransaction

`func (o *SkippedExistingExternalIdObject) SetRequestTransaction(v InsertTransactionObject)`

SetRequestTransaction sets RequestTransaction field to given value.

### HasRequestTransaction

`func (o *SkippedExistingExternalIdObject) HasRequestTransaction() bool`

HasRequestTransaction returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


