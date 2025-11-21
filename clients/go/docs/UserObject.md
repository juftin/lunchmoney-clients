# UserObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | User&#39;s name | 
**Email** | **string** | User&#39;s email | 
**Id** | **int32** | Unique identifier for user | 
**AccountId** | **int64** | Unique identifier for the associated budgeting account | 
**BudgetName** | **string** | Name of the associated budgeting account | 
**PrimaryCurrency** | [**CurrencyEnum**](CurrencyEnum.md) | Primary currency from user&#39;s settings | 
**ApiKeyLabel** | **NullableString** | User-defined label of the developer API key used. Returns null if nothing has been set. | 

## Methods

### NewUserObject

`func NewUserObject(name string, email string, id int32, accountId int64, budgetName string, primaryCurrency CurrencyEnum, apiKeyLabel NullableString, ) *UserObject`

NewUserObject instantiates a new UserObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserObjectWithDefaults

`func NewUserObjectWithDefaults() *UserObject`

NewUserObjectWithDefaults instantiates a new UserObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UserObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UserObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UserObject) SetName(v string)`

SetName sets Name field to given value.


### GetEmail

`func (o *UserObject) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *UserObject) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *UserObject) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetId

`func (o *UserObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UserObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UserObject) SetId(v int32)`

SetId sets Id field to given value.


### GetAccountId

`func (o *UserObject) GetAccountId() int64`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *UserObject) GetAccountIdOk() (*int64, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *UserObject) SetAccountId(v int64)`

SetAccountId sets AccountId field to given value.


### GetBudgetName

`func (o *UserObject) GetBudgetName() string`

GetBudgetName returns the BudgetName field if non-nil, zero value otherwise.

### GetBudgetNameOk

`func (o *UserObject) GetBudgetNameOk() (*string, bool)`

GetBudgetNameOk returns a tuple with the BudgetName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudgetName

`func (o *UserObject) SetBudgetName(v string)`

SetBudgetName sets BudgetName field to given value.


### GetPrimaryCurrency

`func (o *UserObject) GetPrimaryCurrency() CurrencyEnum`

GetPrimaryCurrency returns the PrimaryCurrency field if non-nil, zero value otherwise.

### GetPrimaryCurrencyOk

`func (o *UserObject) GetPrimaryCurrencyOk() (*CurrencyEnum, bool)`

GetPrimaryCurrencyOk returns a tuple with the PrimaryCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimaryCurrency

`func (o *UserObject) SetPrimaryCurrency(v CurrencyEnum)`

SetPrimaryCurrency sets PrimaryCurrency field to given value.


### GetApiKeyLabel

`func (o *UserObject) GetApiKeyLabel() string`

GetApiKeyLabel returns the ApiKeyLabel field if non-nil, zero value otherwise.

### GetApiKeyLabelOk

`func (o *UserObject) GetApiKeyLabelOk() (*string, bool)`

GetApiKeyLabelOk returns a tuple with the ApiKeyLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKeyLabel

`func (o *UserObject) SetApiKeyLabel(v string)`

SetApiKeyLabel sets ApiKeyLabel field to given value.


### SetApiKeyLabelNil

`func (o *UserObject) SetApiKeyLabelNil(b bool)`

 SetApiKeyLabelNil sets the value for ApiKeyLabel to be an explicit nil

### UnsetApiKeyLabel
`func (o *UserObject) UnsetApiKeyLabel()`

UnsetApiKeyLabel ensures that no value is present for ApiKeyLabel, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


