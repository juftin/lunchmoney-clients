# DeleteCategoryResponseWithDependencies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryName** | **string** | The name of the category | 
**Dependents** | [**DeleteCategoryResponseWithDependenciesDependents**](DeleteCategoryResponseWithDependenciesDependents.md) |  | 

## Methods

### NewDeleteCategoryResponseWithDependencies

`func NewDeleteCategoryResponseWithDependencies(categoryName string, dependents DeleteCategoryResponseWithDependenciesDependents, ) *DeleteCategoryResponseWithDependencies`

NewDeleteCategoryResponseWithDependencies instantiates a new DeleteCategoryResponseWithDependencies object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeleteCategoryResponseWithDependenciesWithDefaults

`func NewDeleteCategoryResponseWithDependenciesWithDefaults() *DeleteCategoryResponseWithDependencies`

NewDeleteCategoryResponseWithDependenciesWithDefaults instantiates a new DeleteCategoryResponseWithDependencies object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategoryName

`func (o *DeleteCategoryResponseWithDependencies) GetCategoryName() string`

GetCategoryName returns the CategoryName field if non-nil, zero value otherwise.

### GetCategoryNameOk

`func (o *DeleteCategoryResponseWithDependencies) GetCategoryNameOk() (*string, bool)`

GetCategoryNameOk returns a tuple with the CategoryName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategoryName

`func (o *DeleteCategoryResponseWithDependencies) SetCategoryName(v string)`

SetCategoryName sets CategoryName field to given value.


### GetDependents

`func (o *DeleteCategoryResponseWithDependencies) GetDependents() DeleteCategoryResponseWithDependenciesDependents`

GetDependents returns the Dependents field if non-nil, zero value otherwise.

### GetDependentsOk

`func (o *DeleteCategoryResponseWithDependencies) GetDependentsOk() (*DeleteCategoryResponseWithDependenciesDependents, bool)`

GetDependentsOk returns a tuple with the Dependents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependents

`func (o *DeleteCategoryResponseWithDependencies) SetDependents(v DeleteCategoryResponseWithDependenciesDependents)`

SetDependents sets Dependents field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


