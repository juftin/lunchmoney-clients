# CategoryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | System defined unique ID for the category | 
**Name** | **string** | Name of the category | 
**Description** | **NullableString** | Category description, or &#x60;null&#x60; if none is set | 
**IsIncome** | **bool** | If &#x60;true&#x60;, transactions in this category are treated as income. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**ExcludeFromBudget** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from the budget. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**ExcludeFromTotals** | **bool** | If &#x60;true&#x60;, transactions in this category are excluded from totals. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | 
**UpdatedAt** | **time.Time** | Date and time the category was last updated (in the ISO 8601 extended format). | 
**CreatedAt** | **time.Time** | Date and time of when the category was created (ISO 8601 extended format). | 
**GroupId** | **NullableInt64** | ID of the category group this category belongs to, or &#x60;null&#x60; if it does not belong to a group, or is itself a group. | 
**IsGroup** | **bool** | If &#x60;true&#x60;, this category is created as a category group | 
**Children** | Pointer to [**[]ChildCategoryObject**](ChildCategoryObject.md) | For category groups, contains details about the categories in the group. These objects are similar to Category Objects but the &#x60;is_group&#x60; property will always be &#x60;false&#x60;, and there will be no &#x60;children&#x60; attribute. | [optional] 
**Archived** | **bool** | If true, the category is archived and hidden in relevant areas of the Lunch Money app. | 
**ArchivedAt** | **NullableTime** | Date and time the category was last archived ( ISO 8601 extended format). | 
**Order** | **NullableInt32** | Position of the category on the categories page in the Lunch Money app. For grouped categories, the order is relative to others in the same group.&lt;br&gt; Categories with &#x60;order: null&#x60; are shown alphabetically before ordered categories | 
**Collapsed** | **bool** | If &#x60;true&#x60;, the category appears collapsed in the Lunch Money app | [default to false]

## Methods

### NewCategoryObject

`func NewCategoryObject(id int32, name string, description NullableString, isIncome bool, excludeFromBudget bool, excludeFromTotals bool, updatedAt time.Time, createdAt time.Time, groupId NullableInt64, isGroup bool, archived bool, archivedAt NullableTime, order NullableInt32, collapsed bool, ) *CategoryObject`

NewCategoryObject instantiates a new CategoryObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCategoryObjectWithDefaults

`func NewCategoryObjectWithDefaults() *CategoryObject`

NewCategoryObjectWithDefaults instantiates a new CategoryObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CategoryObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CategoryObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CategoryObject) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *CategoryObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CategoryObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CategoryObject) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CategoryObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CategoryObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CategoryObject) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *CategoryObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *CategoryObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsIncome

`func (o *CategoryObject) GetIsIncome() bool`

GetIsIncome returns the IsIncome field if non-nil, zero value otherwise.

### GetIsIncomeOk

`func (o *CategoryObject) GetIsIncomeOk() (*bool, bool)`

GetIsIncomeOk returns a tuple with the IsIncome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIncome

`func (o *CategoryObject) SetIsIncome(v bool)`

SetIsIncome sets IsIncome field to given value.


### GetExcludeFromBudget

`func (o *CategoryObject) GetExcludeFromBudget() bool`

GetExcludeFromBudget returns the ExcludeFromBudget field if non-nil, zero value otherwise.

### GetExcludeFromBudgetOk

`func (o *CategoryObject) GetExcludeFromBudgetOk() (*bool, bool)`

GetExcludeFromBudgetOk returns a tuple with the ExcludeFromBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromBudget

`func (o *CategoryObject) SetExcludeFromBudget(v bool)`

SetExcludeFromBudget sets ExcludeFromBudget field to given value.


### GetExcludeFromTotals

`func (o *CategoryObject) GetExcludeFromTotals() bool`

GetExcludeFromTotals returns the ExcludeFromTotals field if non-nil, zero value otherwise.

### GetExcludeFromTotalsOk

`func (o *CategoryObject) GetExcludeFromTotalsOk() (*bool, bool)`

GetExcludeFromTotalsOk returns a tuple with the ExcludeFromTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTotals

`func (o *CategoryObject) SetExcludeFromTotals(v bool)`

SetExcludeFromTotals sets ExcludeFromTotals field to given value.


### GetUpdatedAt

`func (o *CategoryObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CategoryObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CategoryObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetCreatedAt

`func (o *CategoryObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CategoryObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CategoryObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetGroupId

`func (o *CategoryObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *CategoryObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *CategoryObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.


### SetGroupIdNil

`func (o *CategoryObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *CategoryObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetIsGroup

`func (o *CategoryObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *CategoryObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *CategoryObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetChildren

`func (o *CategoryObject) GetChildren() []ChildCategoryObject`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *CategoryObject) GetChildrenOk() (*[]ChildCategoryObject, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *CategoryObject) SetChildren(v []ChildCategoryObject)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *CategoryObject) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetArchived

`func (o *CategoryObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *CategoryObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *CategoryObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.


### GetArchivedAt

`func (o *CategoryObject) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *CategoryObject) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *CategoryObject) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.


### SetArchivedAtNil

`func (o *CategoryObject) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *CategoryObject) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil
### GetOrder

`func (o *CategoryObject) GetOrder() int32`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *CategoryObject) GetOrderOk() (*int32, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *CategoryObject) SetOrder(v int32)`

SetOrder sets Order field to given value.


### SetOrderNil

`func (o *CategoryObject) SetOrderNil(b bool)`

 SetOrderNil sets the value for Order to be an explicit nil

### UnsetOrder
`func (o *CategoryObject) UnsetOrder()`

UnsetOrder ensures that no value is present for Order, not even an explicit nil
### GetCollapsed

`func (o *CategoryObject) GetCollapsed() bool`

GetCollapsed returns the Collapsed field if non-nil, zero value otherwise.

### GetCollapsedOk

`func (o *CategoryObject) GetCollapsedOk() (*bool, bool)`

GetCollapsedOk returns a tuple with the Collapsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollapsed

`func (o *CategoryObject) SetCollapsed(v bool)`

SetCollapsed sets Collapsed field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


