# BalanceHistorySourcePlaid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to a Plaid-synced account. | 
**PlaidAccountId** | **int32** | ID of the Plaid account associated with this entry. | 

## Methods

### NewBalanceHistorySourcePlaid

`func NewBalanceHistorySourcePlaid(type_ string, plaidAccountId int32, ) *BalanceHistorySourcePlaid`

NewBalanceHistorySourcePlaid instantiates a new BalanceHistorySourcePlaid object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistorySourcePlaidWithDefaults

`func NewBalanceHistorySourcePlaidWithDefaults() *BalanceHistorySourcePlaid`

NewBalanceHistorySourcePlaidWithDefaults instantiates a new BalanceHistorySourcePlaid object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistorySourcePlaid) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistorySourcePlaid) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistorySourcePlaid) SetType(v string)`

SetType sets Type field to given value.


### GetPlaidAccountId

`func (o *BalanceHistorySourcePlaid) GetPlaidAccountId() int32`

GetPlaidAccountId returns the PlaidAccountId field if non-nil, zero value otherwise.

### GetPlaidAccountIdOk

`func (o *BalanceHistorySourcePlaid) GetPlaidAccountIdOk() (*int32, bool)`

GetPlaidAccountIdOk returns a tuple with the PlaidAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidAccountId

`func (o *BalanceHistorySourcePlaid) SetPlaidAccountId(v int32)`

SetPlaidAccountId sets PlaidAccountId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


