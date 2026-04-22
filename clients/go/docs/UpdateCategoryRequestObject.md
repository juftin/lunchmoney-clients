# UpdateCategoryRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | If set, the new name of the category. Must be between 1 and 100 characters. | [optional] 
**Description** | Pointer to **NullableString** | If set, the new description of the category. Must not exceed 200 characters. | [optional] 
**IsIncome** | Pointer to **bool** | If set, will indicate if this category will be treated as income. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] 
**ExcludeFromBudget** | Pointer to **bool** | If set, will indicate if this category will be excluded from budgets. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] 
**ExcludeFromTotals** | Pointer to **bool** | If set, will indicate if this category will be excluded from totals. (See &lt;a href&#x3D;\&quot;https://support.lunchmoney.app/setup/categories/category-properties\&quot;&gt;Category Properties&lt;/a&gt; for more details) | [optional] 
**Archived** | Pointer to **bool** | If set, will indicate if this category is archived. | [optional] 
**GroupId** | Pointer to **NullableInt64** | If set to the ID of an existing category group, and this category is not itself a category group, this category will be a child of the specified group. | [optional] 
**IsGroup** | Pointer to **NullableBool** | This attribute may not be set to a value that is different than the current status of the category or category group. In other words, this API may not be used to convert a category to a category group or vice versa. | [optional] [default to false]
**Children** | Pointer to [**[]CreateCategoryRequestObjectChildrenInner**](CreateCategoryRequestObjectChildrenInner.md) | The list of existing category objects, or existing category IDs or names of new categories to add to the new category group. This attribute should only be set if modifying an existing category group.&lt;br&gt; The categories or IDs specified must already exist and not belong to an existing category group. Categories that already belong to another category group will be moved. If strings are specified, they will be used as the names of new categories that will be added to the new category group. The request will fail if any names are the same as the name of an existing category.&lt;br&gt; It is permissible to provide both full category objects and IDs as well as strings for names in the same request. | [optional] 
**Order** | Pointer to **NullableInt32** | An index specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order is relative to the other categories within the group.&lt;br&gt;While this property can be set via the API it is generally set by the user in the Lunch Money GUI. API. | [optional] 
**Collapsed** | Pointer to **NullableBool** | If &#x60;true&#x60;, the category is collapsed in the Lunch Money GUI.&lt;br&gt;While this property can be set via the API it is generally set by the user in the Lunch Money GUI. | [optional] 
**Id** | Pointer to **int64** | System defined unique identifier for the category. Ignored if set. | [optional] 
**ArchivedAt** | Pointer to **NullableTime** | If set, updates the archived timestamp for the category. Provide an ISO 8601 extended datetime or &#x60;null&#x60; to clear it. | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System set date and time of when the category was last updated (in the ISO 8601 extended format). Ignored if set. | [optional] 
**CreatedAt** | Pointer to **time.Time** | System set date and time of when the category was created (in the ISO 8601 extended format). Ignored if set. (in the ISO 8601 extended format). Ignored if set. | [optional] 

## Methods

### NewUpdateCategoryRequestObject

`func NewUpdateCategoryRequestObject() *UpdateCategoryRequestObject`

NewUpdateCategoryRequestObject instantiates a new UpdateCategoryRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateCategoryRequestObjectWithDefaults

`func NewUpdateCategoryRequestObjectWithDefaults() *UpdateCategoryRequestObject`

NewUpdateCategoryRequestObjectWithDefaults instantiates a new UpdateCategoryRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateCategoryRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateCategoryRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateCategoryRequestObject) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateCategoryRequestObject) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *UpdateCategoryRequestObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateCategoryRequestObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateCategoryRequestObject) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateCategoryRequestObject) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *UpdateCategoryRequestObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *UpdateCategoryRequestObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsIncome

`func (o *UpdateCategoryRequestObject) GetIsIncome() bool`

GetIsIncome returns the IsIncome field if non-nil, zero value otherwise.

### GetIsIncomeOk

`func (o *UpdateCategoryRequestObject) GetIsIncomeOk() (*bool, bool)`

GetIsIncomeOk returns a tuple with the IsIncome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIncome

`func (o *UpdateCategoryRequestObject) SetIsIncome(v bool)`

SetIsIncome sets IsIncome field to given value.

### HasIsIncome

`func (o *UpdateCategoryRequestObject) HasIsIncome() bool`

HasIsIncome returns a boolean if a field has been set.

### GetExcludeFromBudget

`func (o *UpdateCategoryRequestObject) GetExcludeFromBudget() bool`

GetExcludeFromBudget returns the ExcludeFromBudget field if non-nil, zero value otherwise.

### GetExcludeFromBudgetOk

`func (o *UpdateCategoryRequestObject) GetExcludeFromBudgetOk() (*bool, bool)`

GetExcludeFromBudgetOk returns a tuple with the ExcludeFromBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromBudget

`func (o *UpdateCategoryRequestObject) SetExcludeFromBudget(v bool)`

SetExcludeFromBudget sets ExcludeFromBudget field to given value.

### HasExcludeFromBudget

`func (o *UpdateCategoryRequestObject) HasExcludeFromBudget() bool`

HasExcludeFromBudget returns a boolean if a field has been set.

### GetExcludeFromTotals

`func (o *UpdateCategoryRequestObject) GetExcludeFromTotals() bool`

GetExcludeFromTotals returns the ExcludeFromTotals field if non-nil, zero value otherwise.

### GetExcludeFromTotalsOk

`func (o *UpdateCategoryRequestObject) GetExcludeFromTotalsOk() (*bool, bool)`

GetExcludeFromTotalsOk returns a tuple with the ExcludeFromTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTotals

`func (o *UpdateCategoryRequestObject) SetExcludeFromTotals(v bool)`

SetExcludeFromTotals sets ExcludeFromTotals field to given value.

### HasExcludeFromTotals

`func (o *UpdateCategoryRequestObject) HasExcludeFromTotals() bool`

HasExcludeFromTotals returns a boolean if a field has been set.

### GetArchived

`func (o *UpdateCategoryRequestObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *UpdateCategoryRequestObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *UpdateCategoryRequestObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *UpdateCategoryRequestObject) HasArchived() bool`

HasArchived returns a boolean if a field has been set.

### GetGroupId

`func (o *UpdateCategoryRequestObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *UpdateCategoryRequestObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *UpdateCategoryRequestObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.

### HasGroupId

`func (o *UpdateCategoryRequestObject) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupIdNil

`func (o *UpdateCategoryRequestObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *UpdateCategoryRequestObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetIsGroup

`func (o *UpdateCategoryRequestObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *UpdateCategoryRequestObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *UpdateCategoryRequestObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.

### HasIsGroup

`func (o *UpdateCategoryRequestObject) HasIsGroup() bool`

HasIsGroup returns a boolean if a field has been set.

### SetIsGroupNil

`func (o *UpdateCategoryRequestObject) SetIsGroupNil(b bool)`

 SetIsGroupNil sets the value for IsGroup to be an explicit nil

### UnsetIsGroup
`func (o *UpdateCategoryRequestObject) UnsetIsGroup()`

UnsetIsGroup ensures that no value is present for IsGroup, not even an explicit nil
### GetChildren

`func (o *UpdateCategoryRequestObject) GetChildren() []CreateCategoryRequestObjectChildrenInner`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *UpdateCategoryRequestObject) GetChildrenOk() (*[]CreateCategoryRequestObjectChildrenInner, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *UpdateCategoryRequestObject) SetChildren(v []CreateCategoryRequestObjectChildrenInner)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *UpdateCategoryRequestObject) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetOrder

`func (o *UpdateCategoryRequestObject) GetOrder() int32`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *UpdateCategoryRequestObject) GetOrderOk() (*int32, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *UpdateCategoryRequestObject) SetOrder(v int32)`

SetOrder sets Order field to given value.

### HasOrder

`func (o *UpdateCategoryRequestObject) HasOrder() bool`

HasOrder returns a boolean if a field has been set.

### SetOrderNil

`func (o *UpdateCategoryRequestObject) SetOrderNil(b bool)`

 SetOrderNil sets the value for Order to be an explicit nil

### UnsetOrder
`func (o *UpdateCategoryRequestObject) UnsetOrder()`

UnsetOrder ensures that no value is present for Order, not even an explicit nil
### GetCollapsed

`func (o *UpdateCategoryRequestObject) GetCollapsed() bool`

GetCollapsed returns the Collapsed field if non-nil, zero value otherwise.

### GetCollapsedOk

`func (o *UpdateCategoryRequestObject) GetCollapsedOk() (*bool, bool)`

GetCollapsedOk returns a tuple with the Collapsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollapsed

`func (o *UpdateCategoryRequestObject) SetCollapsed(v bool)`

SetCollapsed sets Collapsed field to given value.

### HasCollapsed

`func (o *UpdateCategoryRequestObject) HasCollapsed() bool`

HasCollapsed returns a boolean if a field has been set.

### SetCollapsedNil

`func (o *UpdateCategoryRequestObject) SetCollapsedNil(b bool)`

 SetCollapsedNil sets the value for Collapsed to be an explicit nil

### UnsetCollapsed
`func (o *UpdateCategoryRequestObject) UnsetCollapsed()`

UnsetCollapsed ensures that no value is present for Collapsed, not even an explicit nil
### GetId

`func (o *UpdateCategoryRequestObject) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateCategoryRequestObject) GetIdOk() (*int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateCategoryRequestObject) SetId(v int64)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateCategoryRequestObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetArchivedAt

`func (o *UpdateCategoryRequestObject) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *UpdateCategoryRequestObject) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *UpdateCategoryRequestObject) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.

### HasArchivedAt

`func (o *UpdateCategoryRequestObject) HasArchivedAt() bool`

HasArchivedAt returns a boolean if a field has been set.

### SetArchivedAtNil

`func (o *UpdateCategoryRequestObject) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *UpdateCategoryRequestObject) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil
### GetUpdatedAt

`func (o *UpdateCategoryRequestObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateCategoryRequestObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateCategoryRequestObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateCategoryRequestObject) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetCreatedAt

`func (o *UpdateCategoryRequestObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateCategoryRequestObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateCategoryRequestObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateCategoryRequestObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


