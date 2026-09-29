# UpdateUserAccountSettingsRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AutoReviewTransactionOnUpdate** | Pointer to **bool** | If set, updates whether transactions are marked as reviewed when their date, category, payee, amount, account, or notes are changed. | [optional] 
**AutoReviewTransactionOnCreation** | Pointer to **bool** | If set, updates whether new manual transactions start as reviewed or unreviewed. | [optional] 
**DefaultManualAccountId** | Pointer to **NullableInt32** | If set, updates the manual account selected by default when the user creates a manual transaction in the current budgeting account. Must identify a manual account returned by [GET /manual_accounts](#tag/manual_accounts/GET/manual_accounts) for the current budgeting account. Set to &#x60;null&#x60; to clear the selection. | [optional] 

## Methods

### NewUpdateUserAccountSettingsRequestObject

`func NewUpdateUserAccountSettingsRequestObject() *UpdateUserAccountSettingsRequestObject`

NewUpdateUserAccountSettingsRequestObject instantiates a new UpdateUserAccountSettingsRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateUserAccountSettingsRequestObjectWithDefaults

`func NewUpdateUserAccountSettingsRequestObjectWithDefaults() *UpdateUserAccountSettingsRequestObject`

NewUpdateUserAccountSettingsRequestObjectWithDefaults instantiates a new UpdateUserAccountSettingsRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAutoReviewTransactionOnUpdate

`func (o *UpdateUserAccountSettingsRequestObject) GetAutoReviewTransactionOnUpdate() bool`

GetAutoReviewTransactionOnUpdate returns the AutoReviewTransactionOnUpdate field if non-nil, zero value otherwise.

### GetAutoReviewTransactionOnUpdateOk

`func (o *UpdateUserAccountSettingsRequestObject) GetAutoReviewTransactionOnUpdateOk() (*bool, bool)`

GetAutoReviewTransactionOnUpdateOk returns a tuple with the AutoReviewTransactionOnUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReviewTransactionOnUpdate

`func (o *UpdateUserAccountSettingsRequestObject) SetAutoReviewTransactionOnUpdate(v bool)`

SetAutoReviewTransactionOnUpdate sets AutoReviewTransactionOnUpdate field to given value.

### HasAutoReviewTransactionOnUpdate

`func (o *UpdateUserAccountSettingsRequestObject) HasAutoReviewTransactionOnUpdate() bool`

HasAutoReviewTransactionOnUpdate returns a boolean if a field has been set.

### GetAutoReviewTransactionOnCreation

`func (o *UpdateUserAccountSettingsRequestObject) GetAutoReviewTransactionOnCreation() bool`

GetAutoReviewTransactionOnCreation returns the AutoReviewTransactionOnCreation field if non-nil, zero value otherwise.

### GetAutoReviewTransactionOnCreationOk

`func (o *UpdateUserAccountSettingsRequestObject) GetAutoReviewTransactionOnCreationOk() (*bool, bool)`

GetAutoReviewTransactionOnCreationOk returns a tuple with the AutoReviewTransactionOnCreation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoReviewTransactionOnCreation

`func (o *UpdateUserAccountSettingsRequestObject) SetAutoReviewTransactionOnCreation(v bool)`

SetAutoReviewTransactionOnCreation sets AutoReviewTransactionOnCreation field to given value.

### HasAutoReviewTransactionOnCreation

`func (o *UpdateUserAccountSettingsRequestObject) HasAutoReviewTransactionOnCreation() bool`

HasAutoReviewTransactionOnCreation returns a boolean if a field has been set.

### GetDefaultManualAccountId

`func (o *UpdateUserAccountSettingsRequestObject) GetDefaultManualAccountId() int32`

GetDefaultManualAccountId returns the DefaultManualAccountId field if non-nil, zero value otherwise.

### GetDefaultManualAccountIdOk

`func (o *UpdateUserAccountSettingsRequestObject) GetDefaultManualAccountIdOk() (*int32, bool)`

GetDefaultManualAccountIdOk returns a tuple with the DefaultManualAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultManualAccountId

`func (o *UpdateUserAccountSettingsRequestObject) SetDefaultManualAccountId(v int32)`

SetDefaultManualAccountId sets DefaultManualAccountId field to given value.

### HasDefaultManualAccountId

`func (o *UpdateUserAccountSettingsRequestObject) HasDefaultManualAccountId() bool`

HasDefaultManualAccountId returns a boolean if a field has been set.

### SetDefaultManualAccountIdNil

`func (o *UpdateUserAccountSettingsRequestObject) SetDefaultManualAccountIdNil(b bool)`

 SetDefaultManualAccountIdNil sets the value for DefaultManualAccountId to be an explicit nil

### UnsetDefaultManualAccountId
`func (o *UpdateUserAccountSettingsRequestObject) UnsetDefaultManualAccountId()`

UnsetDefaultManualAccountId ensures that no value is present for DefaultManualAccountId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


