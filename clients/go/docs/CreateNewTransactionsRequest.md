# CreateNewTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**[]InsertTransactionObject**](InsertTransactionObject.md) | List of transactions to insert. | 
**ApplyRules** | Pointer to **bool** | If explicitly set to &#x60;true&#x60;, any rules associated with the account specified by the &#x60;manual_account_id&#x60; property for each transaction will be applied. | [optional] [default to false]
**SkipDuplicates** | Pointer to **bool** | If &#x60;true&#x60;, the system will flag new transactions that have the same &#x60;date&#x60;, &#x60;payee&#x60;, &#x60;amount&#x60;, and account_id (plaid or manual), as an existing transaction, as a duplicate. &lt;br&gt;&lt;br&gt; Note that deduplication based on &#x60;external_id&#x60; will always occur regardless of how this property is set. | [optional] [default to false]
**SkipBalanceUpdate** | Pointer to **bool** | If &#x60;true&#x60;, and new transactions include a &#x60;manual_account_id&#x60;, the balances of these accounts will not be updated, when the transactions are inserted. | [optional] [default to false]

## Methods

### NewCreateNewTransactionsRequest

`func NewCreateNewTransactionsRequest(transactions []InsertTransactionObject, ) *CreateNewTransactionsRequest`

NewCreateNewTransactionsRequest instantiates a new CreateNewTransactionsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateNewTransactionsRequestWithDefaults

`func NewCreateNewTransactionsRequestWithDefaults() *CreateNewTransactionsRequest`

NewCreateNewTransactionsRequestWithDefaults instantiates a new CreateNewTransactionsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactions

`func (o *CreateNewTransactionsRequest) GetTransactions() []InsertTransactionObject`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *CreateNewTransactionsRequest) GetTransactionsOk() (*[]InsertTransactionObject, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *CreateNewTransactionsRequest) SetTransactions(v []InsertTransactionObject)`

SetTransactions sets Transactions field to given value.


### GetApplyRules

`func (o *CreateNewTransactionsRequest) GetApplyRules() bool`

GetApplyRules returns the ApplyRules field if non-nil, zero value otherwise.

### GetApplyRulesOk

`func (o *CreateNewTransactionsRequest) GetApplyRulesOk() (*bool, bool)`

GetApplyRulesOk returns a tuple with the ApplyRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplyRules

`func (o *CreateNewTransactionsRequest) SetApplyRules(v bool)`

SetApplyRules sets ApplyRules field to given value.

### HasApplyRules

`func (o *CreateNewTransactionsRequest) HasApplyRules() bool`

HasApplyRules returns a boolean if a field has been set.

### GetSkipDuplicates

`func (o *CreateNewTransactionsRequest) GetSkipDuplicates() bool`

GetSkipDuplicates returns the SkipDuplicates field if non-nil, zero value otherwise.

### GetSkipDuplicatesOk

`func (o *CreateNewTransactionsRequest) GetSkipDuplicatesOk() (*bool, bool)`

GetSkipDuplicatesOk returns a tuple with the SkipDuplicates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkipDuplicates

`func (o *CreateNewTransactionsRequest) SetSkipDuplicates(v bool)`

SetSkipDuplicates sets SkipDuplicates field to given value.

### HasSkipDuplicates

`func (o *CreateNewTransactionsRequest) HasSkipDuplicates() bool`

HasSkipDuplicates returns a boolean if a field has been set.

### GetSkipBalanceUpdate

`func (o *CreateNewTransactionsRequest) GetSkipBalanceUpdate() bool`

GetSkipBalanceUpdate returns the SkipBalanceUpdate field if non-nil, zero value otherwise.

### GetSkipBalanceUpdateOk

`func (o *CreateNewTransactionsRequest) GetSkipBalanceUpdateOk() (*bool, bool)`

GetSkipBalanceUpdateOk returns a tuple with the SkipBalanceUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSkipBalanceUpdate

`func (o *CreateNewTransactionsRequest) SetSkipBalanceUpdate(v bool)`

SetSkipBalanceUpdate sets SkipBalanceUpdate field to given value.

### HasSkipBalanceUpdate

`func (o *CreateNewTransactionsRequest) HasSkipBalanceUpdate() bool`

HasSkipBalanceUpdate returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


