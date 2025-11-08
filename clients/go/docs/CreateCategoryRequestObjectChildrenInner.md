# CreateCategoryRequestObjectChildrenInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | A system defined unique identifier for the category. | 
**Name** | **string** | The name of the category. | 
**Description** | **NullableString** | The description of the category or &#x60;null&#x60; if not set. | 
**IsIncome** | **bool** | If &#x60;true&#x60;, the transactions in this category will be treated as income. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | 
**ExcludeFromBudget** | **bool** | If &#x60;true&#x60;, the transactions in this category will be excluded from the budget. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | 
**ExcludeFromTotals** | **bool** | If &#x60;true&#x60;, the transactions in this category will be excluded from totals. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | 
**UpdatedAt** | **time.Time** | The date and time of when the category was last updated (in the ISO 8601 extended format). | 
**CreatedAt** | **time.Time** | The date and time of when the category was created (in the ISO 8601 extended format). | 
**GroupId** | **NullableInt64** | The ID of the category group this category belongs to or &#x60;null&#x60; if the category doesn&#39;t belong to a group, or is itself a category group. | 
**IsGroup** | **bool** | If &#x60;true&#x60;, the category is created as a category group. | 
**Children** | Pointer to [**[]ChildCategoryObject**](ChildCategoryObject.md) | For category groups, this will populate with details about the categories that belong to this group. The objects in this array are similar to Category Objects but do not include the &#x60;is_income&#x60;, &#x60;exclude_from_budget&#x60;, and &#x60;exclude_from_totals&#x60; properties as these are inherited from the category group. In addition, the &#x60;is_group&#x60; property will always be &#x60;false&#x60;, and there will be no &#x60;children&#x60; attribute. | [optional] 
**Archived** | **bool** | If true, the category is archived and not displayed in relevant areas of the Lunch Money app. | 
**ArchivedAt** | **NullableTime** | The date and time of when the category was last archived (in the ISO 8601 extended format). | 
**Order** | **NullableInt32** | An  specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order  is relative to the other categories within the group.&lt;br&gt; This value for this property will be &#x60;null&#x60; for categories created via the API until they are modified on the Categories page in the Lunch Money GUI.&lt;br&gt; This property cannot be set or updated via the API. | 

## Methods

### NewCreateCategoryRequestObjectChildrenInner

`func NewCreateCategoryRequestObjectChildrenInner(id int32, name string, description NullableString, isIncome bool, excludeFromBudget bool, excludeFromTotals bool, updatedAt time.Time, createdAt time.Time, groupId NullableInt64, isGroup bool, archived bool, archivedAt NullableTime, order NullableInt32, ) *CreateCategoryRequestObjectChildrenInner`

NewCreateCategoryRequestObjectChildrenInner instantiates a new CreateCategoryRequestObjectChildrenInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCategoryRequestObjectChildrenInnerWithDefaults

`func NewCreateCategoryRequestObjectChildrenInnerWithDefaults() *CreateCategoryRequestObjectChildrenInner`

NewCreateCategoryRequestObjectChildrenInnerWithDefaults instantiates a new CreateCategoryRequestObjectChildrenInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CreateCategoryRequestObjectChildrenInner) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CreateCategoryRequestObjectChildrenInner) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *CreateCategoryRequestObjectChildrenInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateCategoryRequestObjectChildrenInner) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateCategoryRequestObjectChildrenInner) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateCategoryRequestObjectChildrenInner) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *CreateCategoryRequestObjectChildrenInner) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *CreateCategoryRequestObjectChildrenInner) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsIncome

`func (o *CreateCategoryRequestObjectChildrenInner) GetIsIncome() bool`

GetIsIncome returns the IsIncome field if non-nil, zero value otherwise.

### GetIsIncomeOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetIsIncomeOk() (*bool, bool)`

GetIsIncomeOk returns a tuple with the IsIncome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIncome

`func (o *CreateCategoryRequestObjectChildrenInner) SetIsIncome(v bool)`

SetIsIncome sets IsIncome field to given value.


### GetExcludeFromBudget

`func (o *CreateCategoryRequestObjectChildrenInner) GetExcludeFromBudget() bool`

GetExcludeFromBudget returns the ExcludeFromBudget field if non-nil, zero value otherwise.

### GetExcludeFromBudgetOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetExcludeFromBudgetOk() (*bool, bool)`

GetExcludeFromBudgetOk returns a tuple with the ExcludeFromBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromBudget

`func (o *CreateCategoryRequestObjectChildrenInner) SetExcludeFromBudget(v bool)`

SetExcludeFromBudget sets ExcludeFromBudget field to given value.


### GetExcludeFromTotals

`func (o *CreateCategoryRequestObjectChildrenInner) GetExcludeFromTotals() bool`

GetExcludeFromTotals returns the ExcludeFromTotals field if non-nil, zero value otherwise.

### GetExcludeFromTotalsOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetExcludeFromTotalsOk() (*bool, bool)`

GetExcludeFromTotalsOk returns a tuple with the ExcludeFromTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTotals

`func (o *CreateCategoryRequestObjectChildrenInner) SetExcludeFromTotals(v bool)`

SetExcludeFromTotals sets ExcludeFromTotals field to given value.


### GetUpdatedAt

`func (o *CreateCategoryRequestObjectChildrenInner) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *CreateCategoryRequestObjectChildrenInner) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetCreatedAt

`func (o *CreateCategoryRequestObjectChildrenInner) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CreateCategoryRequestObjectChildrenInner) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetGroupId

`func (o *CreateCategoryRequestObjectChildrenInner) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *CreateCategoryRequestObjectChildrenInner) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.


### SetGroupIdNil

`func (o *CreateCategoryRequestObjectChildrenInner) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *CreateCategoryRequestObjectChildrenInner) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetIsGroup

`func (o *CreateCategoryRequestObjectChildrenInner) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *CreateCategoryRequestObjectChildrenInner) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.


### GetChildren

`func (o *CreateCategoryRequestObjectChildrenInner) GetChildren() []ChildCategoryObject`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetChildrenOk() (*[]ChildCategoryObject, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *CreateCategoryRequestObjectChildrenInner) SetChildren(v []ChildCategoryObject)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *CreateCategoryRequestObjectChildrenInner) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetArchived

`func (o *CreateCategoryRequestObjectChildrenInner) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *CreateCategoryRequestObjectChildrenInner) SetArchived(v bool)`

SetArchived sets Archived field to given value.


### GetArchivedAt

`func (o *CreateCategoryRequestObjectChildrenInner) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *CreateCategoryRequestObjectChildrenInner) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.


### SetArchivedAtNil

`func (o *CreateCategoryRequestObjectChildrenInner) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *CreateCategoryRequestObjectChildrenInner) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil
### GetOrder

`func (o *CreateCategoryRequestObjectChildrenInner) GetOrder() int32`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *CreateCategoryRequestObjectChildrenInner) GetOrderOk() (*int32, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *CreateCategoryRequestObjectChildrenInner) SetOrder(v int32)`

SetOrder sets Order field to given value.


### SetOrderNil

`func (o *CreateCategoryRequestObjectChildrenInner) SetOrderNil(b bool)`

 SetOrderNil sets the value for Order to be an explicit nil

### UnsetOrder
`func (o *CreateCategoryRequestObjectChildrenInner) UnsetOrder()`

UnsetOrder ensures that no value is present for Order, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


