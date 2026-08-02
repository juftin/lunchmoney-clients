# CreateCategoryRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the new category. Must be between 1 and 100 characters. The name must not match the name of any existing categories or category groups. | 
**Description** | Pointer to **NullableString** | Description of the category. Maximum length is 200 characters. | [optional] 
**IsIncome** | Pointer to **bool** | If &#x60;true&#x60;, transactions in this category are treated as income. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to false]
**ExcludeFromBudget** | Pointer to **bool** | If &#x60;true&#x60;, transactions in this category are excluded from the budget. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to false]
**ExcludeFromTotals** | Pointer to **bool** | If &#x60;true&#x60;, transactions in this category are excluded from totals. (See [Category Properties](https://support.lunchmoney.app/setup/categories/category-properties) for details) | [optional] [default to false]
**IsGroup** | Pointer to **bool** | If &#x60;true&#x60;, this category will be created as a category group. | [optional] [default to false]
**GroupId** | Pointer to **NullableInt64** | If set to the ID of an existing category group, the new category will be added to that group. Cannot be used if &#x60;is_group&#x60; is true. | [optional] 
**Archived** | Pointer to **bool** | If &#x60;true&#x60;, the category is archived and in relevant areas of the Lunch Money app. | [optional] [default to false]
**Children** | Pointer to [**[]CreateCategoryRequestObjectChildrenInner**](CreateCategoryRequestObjectChildrenInner.md) | List of categories to include in the new category group. This field should only be set if &#x60;is_group&#x60; is also set to true.&lt;br&gt; You may provide existing category objects, existing category IDs, or names for new categories to add to the group. Categories or IDs must already exist and cannot be category groups. Categories that already belong to another group will be moved. If strings are provided, they will be used as names for new categories added to the group. The request will fail if any provided name already exists.&lt;br&gt; You may mix category objects, IDs, and new category names in the same request. | [optional] 
**Order** | Pointer to **NullableInt32** | Position of the category on the categories page in the Lunch Money app. For grouped categories, the order is relative to other categories in the same group.&lt;br&gt;While this property can be set via the API, it is usually managed by the user in the Lunch Money app. | [optional] 
**Collapsed** | Pointer to **NullableBool** | If &#x60;true&#x60;, the category group appears collapsed in the Lunch Money app. Can only be set to &#x60;true&#x60; for category groups.&lt;br&gt;While this property can be set via the API, it is usually managed by the user in the Lunch Money app. | [optional] 

## Methods

### NewCreateCategoryRequestObject

`func NewCreateCategoryRequestObject(name string, ) *CreateCategoryRequestObject`

NewCreateCategoryRequestObject instantiates a new CreateCategoryRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateCategoryRequestObjectWithDefaults

`func NewCreateCategoryRequestObjectWithDefaults() *CreateCategoryRequestObject`

NewCreateCategoryRequestObjectWithDefaults instantiates a new CreateCategoryRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateCategoryRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateCategoryRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateCategoryRequestObject) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateCategoryRequestObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateCategoryRequestObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateCategoryRequestObject) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateCategoryRequestObject) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *CreateCategoryRequestObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *CreateCategoryRequestObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIsIncome

`func (o *CreateCategoryRequestObject) GetIsIncome() bool`

GetIsIncome returns the IsIncome field if non-nil, zero value otherwise.

### GetIsIncomeOk

`func (o *CreateCategoryRequestObject) GetIsIncomeOk() (*bool, bool)`

GetIsIncomeOk returns a tuple with the IsIncome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsIncome

`func (o *CreateCategoryRequestObject) SetIsIncome(v bool)`

SetIsIncome sets IsIncome field to given value.

### HasIsIncome

`func (o *CreateCategoryRequestObject) HasIsIncome() bool`

HasIsIncome returns a boolean if a field has been set.

### GetExcludeFromBudget

`func (o *CreateCategoryRequestObject) GetExcludeFromBudget() bool`

GetExcludeFromBudget returns the ExcludeFromBudget field if non-nil, zero value otherwise.

### GetExcludeFromBudgetOk

`func (o *CreateCategoryRequestObject) GetExcludeFromBudgetOk() (*bool, bool)`

GetExcludeFromBudgetOk returns a tuple with the ExcludeFromBudget field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromBudget

`func (o *CreateCategoryRequestObject) SetExcludeFromBudget(v bool)`

SetExcludeFromBudget sets ExcludeFromBudget field to given value.

### HasExcludeFromBudget

`func (o *CreateCategoryRequestObject) HasExcludeFromBudget() bool`

HasExcludeFromBudget returns a boolean if a field has been set.

### GetExcludeFromTotals

`func (o *CreateCategoryRequestObject) GetExcludeFromTotals() bool`

GetExcludeFromTotals returns the ExcludeFromTotals field if non-nil, zero value otherwise.

### GetExcludeFromTotalsOk

`func (o *CreateCategoryRequestObject) GetExcludeFromTotalsOk() (*bool, bool)`

GetExcludeFromTotalsOk returns a tuple with the ExcludeFromTotals field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExcludeFromTotals

`func (o *CreateCategoryRequestObject) SetExcludeFromTotals(v bool)`

SetExcludeFromTotals sets ExcludeFromTotals field to given value.

### HasExcludeFromTotals

`func (o *CreateCategoryRequestObject) HasExcludeFromTotals() bool`

HasExcludeFromTotals returns a boolean if a field has been set.

### GetIsGroup

`func (o *CreateCategoryRequestObject) GetIsGroup() bool`

GetIsGroup returns the IsGroup field if non-nil, zero value otherwise.

### GetIsGroupOk

`func (o *CreateCategoryRequestObject) GetIsGroupOk() (*bool, bool)`

GetIsGroupOk returns a tuple with the IsGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsGroup

`func (o *CreateCategoryRequestObject) SetIsGroup(v bool)`

SetIsGroup sets IsGroup field to given value.

### HasIsGroup

`func (o *CreateCategoryRequestObject) HasIsGroup() bool`

HasIsGroup returns a boolean if a field has been set.

### GetGroupId

`func (o *CreateCategoryRequestObject) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *CreateCategoryRequestObject) GetGroupIdOk() (*int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupId

`func (o *CreateCategoryRequestObject) SetGroupId(v int64)`

SetGroupId sets GroupId field to given value.

### HasGroupId

`func (o *CreateCategoryRequestObject) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupIdNil

`func (o *CreateCategoryRequestObject) SetGroupIdNil(b bool)`

 SetGroupIdNil sets the value for GroupId to be an explicit nil

### UnsetGroupId
`func (o *CreateCategoryRequestObject) UnsetGroupId()`

UnsetGroupId ensures that no value is present for GroupId, not even an explicit nil
### GetArchived

`func (o *CreateCategoryRequestObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *CreateCategoryRequestObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *CreateCategoryRequestObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *CreateCategoryRequestObject) HasArchived() bool`

HasArchived returns a boolean if a field has been set.

### GetChildren

`func (o *CreateCategoryRequestObject) GetChildren() []CreateCategoryRequestObjectChildrenInner`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *CreateCategoryRequestObject) GetChildrenOk() (*[]CreateCategoryRequestObjectChildrenInner, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *CreateCategoryRequestObject) SetChildren(v []CreateCategoryRequestObjectChildrenInner)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *CreateCategoryRequestObject) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetOrder

`func (o *CreateCategoryRequestObject) GetOrder() int32`

GetOrder returns the Order field if non-nil, zero value otherwise.

### GetOrderOk

`func (o *CreateCategoryRequestObject) GetOrderOk() (*int32, bool)`

GetOrderOk returns a tuple with the Order field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrder

`func (o *CreateCategoryRequestObject) SetOrder(v int32)`

SetOrder sets Order field to given value.

### HasOrder

`func (o *CreateCategoryRequestObject) HasOrder() bool`

HasOrder returns a boolean if a field has been set.

### SetOrderNil

`func (o *CreateCategoryRequestObject) SetOrderNil(b bool)`

 SetOrderNil sets the value for Order to be an explicit nil

### UnsetOrder
`func (o *CreateCategoryRequestObject) UnsetOrder()`

UnsetOrder ensures that no value is present for Order, not even an explicit nil
### GetCollapsed

`func (o *CreateCategoryRequestObject) GetCollapsed() bool`

GetCollapsed returns the Collapsed field if non-nil, zero value otherwise.

### GetCollapsedOk

`func (o *CreateCategoryRequestObject) GetCollapsedOk() (*bool, bool)`

GetCollapsedOk returns a tuple with the Collapsed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCollapsed

`func (o *CreateCategoryRequestObject) SetCollapsed(v bool)`

SetCollapsed sets Collapsed field to given value.

### HasCollapsed

`func (o *CreateCategoryRequestObject) HasCollapsed() bool`

HasCollapsed returns a boolean if a field has been set.

### SetCollapsedNil

`func (o *CreateCategoryRequestObject) SetCollapsedNil(b bool)`

 SetCollapsedNil sets the value for Collapsed to be an explicit nil

### UnsetCollapsed
`func (o *CreateCategoryRequestObject) UnsetCollapsed()`

UnsetCollapsed ensures that no value is present for Collapsed, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


