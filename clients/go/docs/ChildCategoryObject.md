# ChildCategoryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | A system defined unique identifier for the category | 
**Name** | **string** | The name of the category | 
**Description** | **NullableString** | The description of the category or &#x60;null&#x60; if not set | 
**IsIncome** | **bool** | If true, the transactions in this category will be treated as income. Inherited from Category Group. | 
**ExcludeFromBudget** | **bool** | If true, the transactions in this category will be excluded from the budget. Inherited from Category Group. | 
**ExcludeFromTotals** | **bool** | If true, the transactions in this category will be excluded from totals. Inherited from Category Group. | 
**UpdatedAt** | **time.Time** | The date and time of when the category was last updated (in the ISO 8601 extended format). | 
**CreatedAt** | **time.Time** | The date and time of when the category was created (in the ISO 8601 extended format). | 
**GroupId** | **NullableInt64** | The ID of the category group this category belongs to or &#x60;null&#x60; if the category doesn&#39;t belong to a group, or is itself a category group. | 
**IsGroup** | **bool** | Will always be false for a category that is part of category group | 
**Archived** | **bool** | If true, the category is archived and not displayed in relevant areas of the Lunch Money app. | 
**ArchivedAt** | **NullableTime** | The date and time of when the category was last archived (in the ISO 8601 extended format). | 
**Order** | **NullableInt32** | An index specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order is relative to the other categories within the group.&lt;br&gt; API. | 
**Collapsed** | **bool** | Always &#x60;false&#x60; for a child category. Child categories cannot be collapsed. | 

## Methods

### NewChildCategoryObject

`func NewChildCategoryObject(id int32, name string, description NullableString, isIncome bool, excludeFromBudget bool, excludeFromTotals bool, updatedAt time.Time, createdAt time.Time, groupId NullableInt64, isGroup bool, archived bool, archivedAt NullableTime, order NullableInt32, collapsed bool, ) *ChildCategoryObject`

NewChildCategoryObject instantiates a new ChildCategoryObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChildCategoryObjectWithDefaults

`func NewChildCategoryObjectWithDefaults() *ChildCategoryObject`

NewChildCategoryObjectWithDefaults instantiates a new ChildCategoryObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ChildCategoryObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ChildCategoryObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ChildCategoryObject) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *ChildCategoryObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ChildCategoryObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ChildCategoryObject) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ChildCategoryObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ChildCategoryObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ChildCategoryObject) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *ChildCategoryObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ChildCategoryObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsIncome

`func (o *ChildCategoryObject) GetIsIncome() bool`

GetIsIncome returns the IsIncome field if non-nil, zero value otherwise.

### GetIsIncomeOk

`func (o *ChildCategoryObject) GetIsIncomeOk() (*bool, bool)`

GetIsIncomeOk returns a tuple with the IsIncome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIncome

`func (o *ChildCategoryObject) SetIsIncome(v bool)`

SetIsIncome sets IsIncome field to given value.


### GetExcludeFromBudget

`func (o *ChildCategoryObject) GetExcludeFromBudget() bool`

GetExcludeFromBudget returns the ExcludeFromBudget field if non-nil, zero value otherwise.

### GetExcludeFromBudgetOk

`func (o *ChildCategoryObject) GetExcludeFromBudgetOk() (*bool, bool)`

GetExcludeFromBudgetOk returns a tuple with the ExcludeFromBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromBudget

`func (o *ChildCategoryObject) SetExcludeFromBudget(v bool)`

SetExcludeFromBudget sets ExcludeFromBudget field to given value.


### GetExcludeFromTotals

`func (o *ChildCategoryObject) GetExcludeFromTotals() bool`

GetExcludeFromTotals returns the ExcludeFromTotals field if non-nil, zero value otherwise.

### GetExcludeFromTotalsOk

`func (o *ChildCategoryObject) GetExcludeFromTotalsOk() (*bool, bool)`

GetExcludeFromTotalsOk returns a tuple with the ExcludeFromTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTotals

`func (o *ChildCategoryObject) SetExcludeFromTotals(v bool)`

SetExcludeFromTotals sets ExcludeFromTotals field to given value.


### GetUpdatedAt

`func (o *ChildCategoryObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *ChildCategoryObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *ChildCategoryObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetCreatedAt

`func (o *ChildCategoryObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ChildCategoryObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ChildCategoryObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetGroupId

`func (o *ChildCategoryObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *ChildCategoryObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *ChildCategoryObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.


### SetGroupIdNil

`func (o *ChildCategoryObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *ChildCategoryObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetIsGroup

`func (o *ChildCategoryObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *ChildCategoryObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *ChildCategoryObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetArchived

`func (o *ChildCategoryObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *ChildCategoryObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *ChildCategoryObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.


### GetArchivedAt

`func (o *ChildCategoryObject) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *ChildCategoryObject) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *ChildCategoryObject) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.


### SetArchivedAtNil

`func (o *ChildCategoryObject) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *ChildCategoryObject) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil
### GetOrder

`func (o *ChildCategoryObject) GetOrder() int32`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *ChildCategoryObject) GetOrderOk() (*int32, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *ChildCategoryObject) SetOrder(v int32)`

SetOrder sets Order field to given value.


### SetOrderNil

`func (o *ChildCategoryObject) SetOrderNil(b bool)`

 SetOrderNil sets the value for Order to be an explicit nil

### UnsetOrder
`func (o *ChildCategoryObject) UnsetOrder()`

UnsetOrder ensures that no value is present for Order, not even an explicit nil
### GetCollapsed

`func (o *ChildCategoryObject) GetCollapsed() bool`

GetCollapsed returns the Collapsed field if non-nil, zero value otherwise.

### GetCollapsedOk

`func (o *ChildCategoryObject) GetCollapsedOk() (*bool, bool)`

GetCollapsedOk returns a tuple with the Collapsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollapsed

`func (o *ChildCategoryObject) SetCollapsed(v bool)`

SetCollapsed sets Collapsed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


