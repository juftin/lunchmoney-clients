# BalanceHistoryAccountObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Source** | [**BalanceHistoryAccountObjectSource**](BalanceHistoryAccountObjectSource.md) |  | 
**Balances** | [**[]BalanceHistoryEntry**](BalanceHistoryEntry.md) | Monthly balance entries for this account source. A &#x60;historical&#x60; entry is a stored snapshot of a past month and includes an &#x60;id&#x60;. A &#x60;current&#x60; entry is an ephemeral snapshot based on the account&#39;s current balances and has no balance-entry &#x60;id&#x60;. On PUT upsert responses, this array includes only the &#x60;type: historical&#x60; entries modified by that request.  | 

## Methods

### NewBalanceHistoryAccountObject

`func NewBalanceHistoryAccountObject(source BalanceHistoryAccountObjectSource, balances []BalanceHistoryEntry, ) *BalanceHistoryAccountObject`

NewBalanceHistoryAccountObject instantiates a new BalanceHistoryAccountObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBalanceHistoryAccountObjectWithDefaults

`func NewBalanceHistoryAccountObjectWithDefaults() *BalanceHistoryAccountObject`

NewBalanceHistoryAccountObjectWithDefaults instantiates a new BalanceHistoryAccountObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSource

`func (o *BalanceHistoryAccountObject) GetSource() BalanceHistoryAccountObjectSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *BalanceHistoryAccountObject) GetSourceOk() (*BalanceHistoryAccountObjectSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *BalanceHistoryAccountObject) SetSource(v BalanceHistoryAccountObjectSource)`

SetSource sets Source field to given value.


### GetBalances

`func (o *BalanceHistoryAccountObject) GetBalances() []BalanceHistoryEntry`

GetBalances returns the Balances field if non-nil, zero value otherwise.

### GetBalancesOk

`func (o *BalanceHistoryAccountObject) GetBalancesOk() (*[]BalanceHistoryEntry, bool)`

GetBalancesOk returns a tuple with the Balances field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalances

`func (o *BalanceHistoryAccountObject) SetBalances(v []BalanceHistoryEntry)`

SetBalances sets Balances field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


