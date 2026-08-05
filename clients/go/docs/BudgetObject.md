# BudgetObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int64** | System-created unique identifier for the budget entry. | 
**CategoryId** | **int32** | The ID of the category this budget applies to. | 
**Amount** | **float64** | The budgeted amount for this period. | 
**Currency** | [**CurrencyEnum**](CurrencyEnum.md) | The currency of the budgeted amount in ISO 4217 format. | 
**StartDate** | **string** | The start date of the budget period in ISO 8601 format (YYYY-MM-DD). This represents the beginning of the period for which this budget applies. | 
**NextStartDate** | **string** | The calculated start date of the next budget period based on the category&#39;s period settings (granularity, quantity, and anchor_date). This is useful for determining when the next budget period begins. | [readonly] 
**Notes** | Pointer to **NullableString** | Optional notes associated with this budget period. | [optional] 
**AutoBudgetType** | **string** | The budget preset type that determines how future periods will be automatically calculated. &#x60;nothing&#x60; means no automatic calculation (budgets must be set manually for each period). &#x60;fixed&#x60; uses a fixed amount for all future periods. &#x60;spend&#x60; uses the previous period&#39;s spending amount. &#x60;budget&#x60; uses the previous period&#39;s budgeted amount. | [readonly] 
**AutoBudgetAmount** | Pointer to **NullableFloat64** | If &#x60;auto_budget_type&#x60; is &#x60;fixed&#x60;, this is the fixed amount that will be used for future periods. | [optional] [readonly] 
**AutoBudgetCurrency** | Pointer to [**NullableCurrencyEnum**](CurrencyEnum.md) | If &#x60;auto_budget_type&#x60; is &#x60;fixed&#x60;, this is the currency of the fixed amount. | [optional] [readonly] 
**RolloverOption** | Pointer to **NullableString** | The rollover setting for this category. &#x60;same category&#x60; means unspent funds roll over to the next period for this category. &#x60;available funds&#x60; means unspent funds are added to the available funds pool. &#x60;null&#x60; means rollover is disabled. | [optional] [readonly] 
**Granularity** | **string** | The granularity of the budget period (e.g., monthly, weekly, twice a month). This is determined by the category&#39;s custom budget settings or the account&#39;s default budget period settings. | [readonly] 
**Quantity** | **int32** | The quantity of granularity units that make up each budget period. For example, if granularity is &#x60;week&#x60; and quantity is &#x60;2&#x60;, each budget period is 2 weeks. | [readonly] 
**IsGroup** | **bool** | Whether the category is a category group. Category groups can have their own budgets that apply to all subcategories, or subcategories can have individual budgets. | [readonly] 
**GroupId** | Pointer to **NullableInt32** | If this budget is for a subcategory, this is the ID of the parent category group. &#x60;null&#x60; if this is not a subcategory. | [optional] [readonly] 
**CreatedAt** | **time.Time** | The date and time when this budget entry was created (in ISO 8601 extended format). | 
**UpdatedAt** | **time.Time** | The date and time when this budget entry was last updated (in ISO 8601 extended format). | 

## Methods

### NewBudgetObject

`func NewBudgetObject(id int64, categoryId int32, amount float64, currency CurrencyEnum, startDate string, nextStartDate string, autoBudgetType string, granularity string, quantity int32, isGroup bool, createdAt time.Time, updatedAt time.Time, ) *BudgetObject`

NewBudgetObject instantiates a new BudgetObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBudgetObjectWithDefaults

`func NewBudgetObjectWithDefaults() *BudgetObject`

NewBudgetObjectWithDefaults instantiates a new BudgetObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BudgetObject) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BudgetObject) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BudgetObject) SetId(v int64)`

SetId sets Id field to given value.


### GetCategoryId

`func (o *BudgetObject) GetCategoryId() int32`

GetCategoryId returns the CategoryId field if non-nil, zero value otherwise.

### GetCategoryIdOk

`func (o *BudgetObject) GetCategoryIdOk() (*int32, bool)`

GetCategoryIdOk returns a tuple with the CategoryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryId

`func (o *BudgetObject) SetCategoryId(v int32)`

SetCategoryId sets CategoryId field to given value.


### GetAmount

`func (o *BudgetObject) GetAmount() float64`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *BudgetObject) GetAmountOk() (*float64, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *BudgetObject) SetAmount(v float64)`

SetAmount sets Amount field to given value.


### GetCurrency

`func (o *BudgetObject) GetCurrency() CurrencyEnum`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *BudgetObject) GetCurrencyOk() (*CurrencyEnum, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *BudgetObject) SetCurrency(v CurrencyEnum)`

SetCurrency sets Currency field to given value.


### GetStartDate

`func (o *BudgetObject) GetStartDate() string`

GetStartDate returns the StartDate field if non-nil, zero value otherwise.

### GetStartDateOk

`func (o *BudgetObject) GetStartDateOk() (*string, bool)`

GetStartDateOk returns a tuple with the StartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartDate

`func (o *BudgetObject) SetStartDate(v string)`

SetStartDate sets StartDate field to given value.


### GetNextStartDate

`func (o *BudgetObject) GetNextStartDate() string`

GetNextStartDate returns the NextStartDate field if non-nil, zero value otherwise.

### GetNextStartDateOk

`func (o *BudgetObject) GetNextStartDateOk() (*string, bool)`

GetNextStartDateOk returns a tuple with the NextStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextStartDate

`func (o *BudgetObject) SetNextStartDate(v string)`

SetNextStartDate sets NextStartDate field to given value.


### GetNotes

`func (o *BudgetObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *BudgetObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *BudgetObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *BudgetObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *BudgetObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *BudgetObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetAutoBudgetType

`func (o *BudgetObject) GetAutoBudgetType() string`

GetAutoBudgetType returns the AutoBudgetType field if non-nil, zero value otherwise.

### GetAutoBudgetTypeOk

`func (o *BudgetObject) GetAutoBudgetTypeOk() (*string, bool)`

GetAutoBudgetTypeOk returns a tuple with the AutoBudgetType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoBudgetType

`func (o *BudgetObject) SetAutoBudgetType(v string)`

SetAutoBudgetType sets AutoBudgetType field to given value.


### GetAutoBudgetAmount

`func (o *BudgetObject) GetAutoBudgetAmount() float64`

GetAutoBudgetAmount returns the AutoBudgetAmount field if non-nil, zero value otherwise.

### GetAutoBudgetAmountOk

`func (o *BudgetObject) GetAutoBudgetAmountOk() (*float64, bool)`

GetAutoBudgetAmountOk returns a tuple with the AutoBudgetAmount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoBudgetAmount

`func (o *BudgetObject) SetAutoBudgetAmount(v float64)`

SetAutoBudgetAmount sets AutoBudgetAmount field to given value.

### HasAutoBudgetAmount

`func (o *BudgetObject) HasAutoBudgetAmount() bool`

HasAutoBudgetAmount returns a boolean if a field has been set.

### SetAutoBudgetAmountNil

`func (o *BudgetObject) SetAutoBudgetAmountNil(b bool)`

 SetAutoBudgetAmountNil sets the value for AutoBudgetAmount to be an explicit nil

### UnsetAutoBudgetAmount
`func (o *BudgetObject) UnsetAutoBudgetAmount()`

UnsetAutoBudgetAmount ensures that no value is present for AutoBudgetAmount, not even an explicit nil
### GetAutoBudgetCurrency

`func (o *BudgetObject) GetAutoBudgetCurrency() CurrencyEnum`

GetAutoBudgetCurrency returns the AutoBudgetCurrency field if non-nil, zero value otherwise.

### GetAutoBudgetCurrencyOk

`func (o *BudgetObject) GetAutoBudgetCurrencyOk() (*CurrencyEnum, bool)`

GetAutoBudgetCurrencyOk returns a tuple with the AutoBudgetCurrency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAutoBudgetCurrency

`func (o *BudgetObject) SetAutoBudgetCurrency(v CurrencyEnum)`

SetAutoBudgetCurrency sets AutoBudgetCurrency field to given value.

### HasAutoBudgetCurrency

`func (o *BudgetObject) HasAutoBudgetCurrency() bool`

HasAutoBudgetCurrency returns a boolean if a field has been set.

### SetAutoBudgetCurrencyNil

`func (o *BudgetObject) SetAutoBudgetCurrencyNil(b bool)`

 SetAutoBudgetCurrencyNil sets the value for AutoBudgetCurrency to be an explicit nil

### UnsetAutoBudgetCurrency
`func (o *BudgetObject) UnsetAutoBudgetCurrency()`

UnsetAutoBudgetCurrency ensures that no value is present for AutoBudgetCurrency, not even an explicit nil
### GetRolloverOption

`func (o *BudgetObject) GetRolloverOption() string`

GetRolloverOption returns the RolloverOption field if non-nil, zero value otherwise.

### GetRolloverOptionOk

`func (o *BudgetObject) GetRolloverOptionOk() (*string, bool)`

GetRolloverOptionOk returns a tuple with the RolloverOption field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRolloverOption

`func (o *BudgetObject) SetRolloverOption(v string)`

SetRolloverOption sets RolloverOption field to given value.

### HasRolloverOption

`func (o *BudgetObject) HasRolloverOption() bool`

HasRolloverOption returns a boolean if a field has been set.

### SetRolloverOptionNil

`func (o *BudgetObject) SetRolloverOptionNil(b bool)`

 SetRolloverOptionNil sets the value for RolloverOption to be an explicit nil

### UnsetRolloverOption
`func (o *BudgetObject) UnsetRolloverOption()`

UnsetRolloverOption ensures that no value is present for RolloverOption, not even an explicit nil
### GetGranularity

`func (o *BudgetObject) GetGranularity() string`

GetGranularity returns the Granularity field if non-nil, zero value otherwise.

### GetGranularityOk

`func (o *BudgetObject) GetGranularityOk() (*string, bool)`

GetGranularityOk returns a tuple with the Granularity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGranularity

`func (o *BudgetObject) SetGranularity(v string)`

SetGranularity sets Granularity field to given value.


### GetQuantity

`func (o *BudgetObject) GetQuantity() int32`

GetQuantity returns the Quantity field if non-nil, zero value otherwise.

### GetQuantityOk

`func (o *BudgetObject) GetQuantityOk() (*int32, bool)`

GetQuantityOk returns a tuple with the Quantity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantity

`func (o *BudgetObject) SetQuantity(v int32)`

SetQuantity sets Quantity field to given value.


### GetIsGroup

`func (o *BudgetObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *BudgetObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *BudgetObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetGroupId

`func (o *BudgetObject) GetGroupId() int32`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *BudgetObject) GetGroupIdOk() (*int32, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *BudgetObject) SetGroupId(v int32)`

SetGroupId sets GroupId field to given value.

### HasGroupId

`func (o *BudgetObject) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupIdNil

`func (o *BudgetObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *BudgetObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetCreatedAt

`func (o *BudgetObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *BudgetObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *BudgetObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *BudgetObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *BudgetObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *BudgetObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


