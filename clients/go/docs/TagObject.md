# TagObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | Unique identifier for the tag. | 
**Name** | **string** | Name of the tag. | 
**Description** | **NullableString** | Description of the tag. | 
**UpdatedAt** | **time.Time** | The date and time of when the tag was last updated (in the ISO 8601 extended format). | 
**CreatedAt** | **time.Time** | The date and time of when the tag was created (in the ISO 8601 extended format). | 
**Archived** | **bool** | If &#x60;true&#x60;, the tag will not show up when creating or updating transactions in the Lunch Money app. **Can it be assigned via the API** | 
**ArchivedAt** | **NullableTime** | The date and time of when the tag was last archived or &#x60;null&#x60; if not archived | 

## Methods

### NewTagObject

`func NewTagObject(id int32, name string, description NullableString, updatedAt time.Time, createdAt time.Time, archived bool, archivedAt NullableTime, ) *TagObject`

NewTagObject instantiates a new TagObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTagObjectWithDefaults

`func NewTagObjectWithDefaults() *TagObject`

NewTagObjectWithDefaults instantiates a new TagObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TagObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TagObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TagObject) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *TagObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TagObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TagObject) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *TagObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TagObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TagObject) SetDescription(v string)`

SetDescription sets Description field to given value.


### SetDescriptionNil

`func (o *TagObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *TagObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetUpdatedAt

`func (o *TagObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *TagObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *TagObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetCreatedAt

`func (o *TagObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TagObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TagObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetArchived

`func (o *TagObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *TagObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *TagObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.


### GetArchivedAt

`func (o *TagObject) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *TagObject) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *TagObject) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.


### SetArchivedAtNil

`func (o *TagObject) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *TagObject) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


