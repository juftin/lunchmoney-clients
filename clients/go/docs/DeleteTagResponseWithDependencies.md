# DeleteTagResponseWithDependencies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TagName** | **string** | The name of the tag | 
**Dependents** | [**DeleteTagResponseWithDependenciesDependents**](DeleteTagResponseWithDependenciesDependents.md) |  | 

## Methods

### NewDeleteTagResponseWithDependencies

`func NewDeleteTagResponseWithDependencies(tagName string, dependents DeleteTagResponseWithDependenciesDependents, ) *DeleteTagResponseWithDependencies`

NewDeleteTagResponseWithDependencies instantiates a new DeleteTagResponseWithDependencies object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDeleteTagResponseWithDependenciesWithDefaults

`func NewDeleteTagResponseWithDependenciesWithDefaults() *DeleteTagResponseWithDependencies`

NewDeleteTagResponseWithDependenciesWithDefaults instantiates a new DeleteTagResponseWithDependencies object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTagName

`func (o *DeleteTagResponseWithDependencies) GetTagName() string`

GetTagName returns the TagName field if non-nil, zero value otherwise.

### GetTagNameOk

`func (o *DeleteTagResponseWithDependencies) GetTagNameOk() (*string, bool)`

GetTagNameOk returns a tuple with the TagName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTagName

`func (o *DeleteTagResponseWithDependencies) SetTagName(v string)`

SetTagName sets TagName field to given value.


### GetDependents

`func (o *DeleteTagResponseWithDependencies) GetDependents() DeleteTagResponseWithDependenciesDependents`

GetDependents returns the Dependents field if non-nil, zero value otherwise.

### GetDependentsOk

`func (o *DeleteTagResponseWithDependencies) GetDependentsOk() (*DeleteTagResponseWithDependenciesDependents, bool)`

GetDependentsOk returns a tuple with the Dependents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDependents

`func (o *DeleteTagResponseWithDependencies) SetDependents(v DeleteTagResponseWithDependenciesDependents)`

SetDependents sets Dependents field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


