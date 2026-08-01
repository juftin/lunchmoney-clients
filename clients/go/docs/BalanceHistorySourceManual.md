# BalanceHistorySourceManual

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Identifies this entry as belonging to a manual account. | 
**ManualAccountId** | **int32** | ID of the manual account associated with this entry. | 

## Methods

### NewBalanceHistorySourceManual

`func NewBalanceHistorySourceManual(type_ string, manualAccountId int32, ) *BalanceHistorySourceManual`

NewBalanceHistorySourceManual instantiates a new BalanceHistorySourceManual object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistorySourceManualWithDefaults

`func NewBalanceHistorySourceManualWithDefaults() *BalanceHistorySourceManual`

NewBalanceHistorySourceManualWithDefaults instantiates a new BalanceHistorySourceManual object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BalanceHistorySourceManual) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BalanceHistorySourceManual) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BalanceHistorySourceManual) SetType(v string)`

SetType sets Type field to given value.


### GetManualAccountId

`func (o *BalanceHistorySourceManual) GetManualAccountId() int32`

GetManualAccountId returns the ManualAccountId field if non-nil, zero value otherwise.

### GetManualAccountIdOk

`func (o *BalanceHistorySourceManual) GetManualAccountIdOk() (*int32, bool)`

GetManualAccountIdOk returns a tuple with the ManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetManualAccountId

`func (o *BalanceHistorySourceManual) SetManualAccountId(v int32)`

SetManualAccountId sets ManualAccountId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


