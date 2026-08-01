# UpsertBalanceHistoryRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Balances** | [**[]BalanceHistoryUpdateItemObject**](BalanceHistoryUpdateItemObject.md) | One or more monthly balance history entries to upsert. Each entry uses &#x60;month&#x60; (YYYY-MM) and &#x60;balance&#x60;. Do not include response-only fields such as &#x60;type&#x60;. PUT responses return only the &#x60;type: historical&#x60; entries modified by the request.  | 

## Methods

### NewUpsertBalanceHistoryRequestObject

`func NewUpsertBalanceHistoryRequestObject(balances []BalanceHistoryUpdateItemObject, ) *UpsertBalanceHistoryRequestObject`

NewUpsertBalanceHistoryRequestObject instantiates a new UpsertBalanceHistoryRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpsertBalanceHistoryRequestObjectWithDefaults

`func NewUpsertBalanceHistoryRequestObjectWithDefaults() *UpsertBalanceHistoryRequestObject`

NewUpsertBalanceHistoryRequestObjectWithDefaults instantiates a new UpsertBalanceHistoryRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBalances

`func (o *UpsertBalanceHistoryRequestObject) GetBalances() []BalanceHistoryUpdateItemObject`

GetBalances returns the Balances field if non-nil, zero value otherwise.

### GetBalancesOk

`func (o *UpsertBalanceHistoryRequestObject) GetBalancesOk() (*[]BalanceHistoryUpdateItemObject, bool)`

GetBalancesOk returns a tuple with the Balances field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalances

`func (o *UpsertBalanceHistoryRequestObject) SetBalances(v []BalanceHistoryUpdateItemObject)`

SetBalances sets Balances field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


