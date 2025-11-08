# DeleteCategoryResponseWithDependenciesDependents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Budget** | **int32** | The number of budgets depending on the category | 
**CategoryRules** | **int32** | The number of category rules depending on the category | 
**Transactions** | **int32** | The number of transactions depending on the category | 
**Children** | **int32** | The number of child categories in the category group | 
**Recurring** | **int32** | The number of recurring transactions depending on the category | 
**PlaidCats** | **int32** | The number of auto created categories based on Plaid categories | 

## Methods

### NewDeleteCategoryResponseWithDependenciesDependents

`func NewDeleteCategoryResponseWithDependenciesDependents(budget int32, categoryRules int32, transactions int32, children int32, recurring int32, plaidCats int32, ) *DeleteCategoryResponseWithDependenciesDependents`

NewDeleteCategoryResponseWithDependenciesDependents instantiates a new DeleteCategoryResponseWithDependenciesDependents object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeleteCategoryResponseWithDependenciesDependentsWithDefaults

`func NewDeleteCategoryResponseWithDependenciesDependentsWithDefaults() *DeleteCategoryResponseWithDependenciesDependents`

NewDeleteCategoryResponseWithDependenciesDependentsWithDefaults instantiates a new DeleteCategoryResponseWithDependenciesDependents object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBudget

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetBudget() int32`

GetBudget returns the Budget field if non-nil, zero value otherwise.

### GetBudgetOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetBudgetOk() (*int32, bool)`

GetBudgetOk returns a tuple with the Budget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBudget

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetBudget(v int32)`

SetBudget sets Budget field to given value.


### GetCategoryRules

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetCategoryRules() int32`

GetCategoryRules returns the CategoryRules field if non-nil, zero value otherwise.

### GetCategoryRulesOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetCategoryRulesOk() (*int32, bool)`

GetCategoryRulesOk returns a tuple with the CategoryRules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryRules

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetCategoryRules(v int32)`

SetCategoryRules sets CategoryRules field to given value.


### GetTransactions

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetTransactions() int32`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetTransactionsOk() (*int32, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetTransactions(v int32)`

SetTransactions sets Transactions field to given value.


### GetChildren

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetChildren() int32`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetChildrenOk() (*int32, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetChildren(v int32)`

SetChildren sets Children field to given value.


### GetRecurring

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetRecurring() int32`

GetRecurring returns the Recurring field if non-nil, zero value otherwise.

### GetRecurringOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetRecurringOk() (*int32, bool)`

GetRecurringOk returns a tuple with the Recurring field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecurring

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetRecurring(v int32)`

SetRecurring sets Recurring field to given value.


### GetPlaidCats

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetPlaidCats() int32`

GetPlaidCats returns the PlaidCats field if non-nil, zero value otherwise.

### GetPlaidCatsOk

`func (o *DeleteCategoryResponseWithDependenciesDependents) GetPlaidCatsOk() (*int32, bool)`

GetPlaidCatsOk returns a tuple with the PlaidCats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidCats

`func (o *DeleteCategoryResponseWithDependenciesDependents) SetPlaidCats(v int32)`

SetPlaidCats sets PlaidCats field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


