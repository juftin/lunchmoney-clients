# GetAllTransactions200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**[]TransactionObject**](TransactionObject.md) |  | 
**HasMore** | **bool** | Set to true if more transactions are available | 
**Error** | Pointer to **string** |  | [optional] 

## Methods

### NewGetAllTransactions200Response

`func NewGetAllTransactions200Response(transactions []TransactionObject, hasMore bool, ) *GetAllTransactions200Response`

NewGetAllTransactions200Response instantiates a new GetAllTransactions200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetAllTransactions200ResponseWithDefaults

`func NewGetAllTransactions200ResponseWithDefaults() *GetAllTransactions200Response`

NewGetAllTransactions200ResponseWithDefaults instantiates a new GetAllTransactions200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactions

`func (o *GetAllTransactions200Response) GetTransactions() []TransactionObject`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *GetAllTransactions200Response) GetTransactionsOk() (*[]TransactionObject, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *GetAllTransactions200Response) SetTransactions(v []TransactionObject)`

SetTransactions sets Transactions field to given value.


### GetHasMore

`func (o *GetAllTransactions200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *GetAllTransactions200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *GetAllTransactions200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetError

`func (o *GetAllTransactions200Response) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *GetAllTransactions200Response) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *GetAllTransactions200Response) SetError(v string)`

SetError sets Error field to given value.

### HasError

`func (o *GetAllTransactions200Response) HasError() bool`

HasError returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


