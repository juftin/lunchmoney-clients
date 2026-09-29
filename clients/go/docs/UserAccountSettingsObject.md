# UserAccountSettingsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AutoReviewTransactionOnUpdate** | **bool** | If &#x60;true&#x60;, transactions are marked as reviewed when their date, category, payee, amount, account, or notes are changed. | [default to true]
**AutoReviewTransactionOnCreation** | **bool** | If &#x60;true&#x60;, new manual transactions start as reviewed. If &#x60;false&#x60;, they start as unreviewed. | [default to true]
**DefaultManualAccountId** | **NullableInt32** | Manual account selected by default when the user creates a manual transaction in the current budgeting account. Must identify a manual account returned by [GET /manual_accounts](#tag/manual_accounts/GET/manual_accounts) for the current budgeting account. Set to &#x60;null&#x60; to clear the selection. | 

## Methods

### NewUserAccountSettingsObject

`func NewUserAccountSettingsObject(autoReviewTransactionOnUpdate bool, autoReviewTransactionOnCreation bool, defaultManualAccountId NullableInt32, ) *UserAccountSettingsObject`

NewUserAccountSettingsObject instantiates a new UserAccountSettingsObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserAccountSettingsObjectWithDefaults

`func NewUserAccountSettingsObjectWithDefaults() *UserAccountSettingsObject`

NewUserAccountSettingsObjectWithDefaults instantiates a new UserAccountSettingsObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAutoReviewTransactionOnUpdate

`func (o *UserAccountSettingsObject) GetAutoReviewTransactionOnUpdate() bool`

GetAutoReviewTransactionOnUpdate returns the AutoReviewTransactionOnUpdate field if non-nil, zero value otherwise.

### GetAutoReviewTransactionOnUpdateOk

`func (o *UserAccountSettingsObject) GetAutoReviewTransactionOnUpdateOk() (*bool, bool)`

GetAutoReviewTransactionOnUpdateOk returns a tuple with the AutoReviewTransactionOnUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReviewTransactionOnUpdate

`func (o *UserAccountSettingsObject) SetAutoReviewTransactionOnUpdate(v bool)`

SetAutoReviewTransactionOnUpdate sets AutoReviewTransactionOnUpdate field to given value.


### GetAutoReviewTransactionOnCreation

`func (o *UserAccountSettingsObject) GetAutoReviewTransactionOnCreation() bool`

GetAutoReviewTransactionOnCreation returns the AutoReviewTransactionOnCreation field if non-nil, zero value otherwise.

### GetAutoReviewTransactionOnCreationOk

`func (o *UserAccountSettingsObject) GetAutoReviewTransactionOnCreationOk() (*bool, bool)`

GetAutoReviewTransactionOnCreationOk returns a tuple with the AutoReviewTransactionOnCreation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReviewTransactionOnCreation

`func (o *UserAccountSettingsObject) SetAutoReviewTransactionOnCreation(v bool)`

SetAutoReviewTransactionOnCreation sets AutoReviewTransactionOnCreation field to given value.


### GetDefaultManualAccountId

`func (o *UserAccountSettingsObject) GetDefaultManualAccountId() int32`

GetDefaultManualAccountId returns the DefaultManualAccountId field if non-nil, zero value otherwise.

### GetDefaultManualAccountIdOk

`func (o *UserAccountSettingsObject) GetDefaultManualAccountIdOk() (*int32, bool)`

GetDefaultManualAccountIdOk returns a tuple with the DefaultManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultManualAccountId

`func (o *UserAccountSettingsObject) SetDefaultManualAccountId(v int32)`

SetDefaultManualAccountId sets DefaultManualAccountId field to given value.


### SetDefaultManualAccountIdNil

`func (o *UserAccountSettingsObject) SetDefaultManualAccountIdNil(b bool)`

 SetDefaultManualAccountIdNil sets the value for DefaultManualAccountId to be an explicit nil

### UnsetDefaultManualAccountId
`func (o *UserAccountSettingsObject) UnsetDefaultManualAccountId()`

UnsetDefaultManualAccountId ensures that no value is present for DefaultManualAccountId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


