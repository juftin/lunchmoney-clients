# UpdateTagRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | If set, the new name of the category. Must be between 1 and 100 characters. | [optional] 
**Description** | Pointer to **NullableString** | If set, the new description of the category. Must not exceed 200 characters. | [optional] 
**TextColor** | Pointer to **NullableString** | The text color of the tag | [optional] 
**BackgroundColor** | Pointer to **NullableString** | The background color of the tag | [optional] 
**Archived** | Pointer to **bool** | If set, will indicate if this category is archived | [optional] 
**Id** | Pointer to **int32** | System-defined unique identifier for the category. Ignored if set | [optional] 
**UpdatedAt** | Pointer to **time.Time** | System-set time the tag was last updated. Ignored if set | [optional] 
**CreatedAt** | Pointer to **time.Time** | System-set time the tag was created. Ignored if set | [optional] 
**ArchivedAt** | Pointer to **NullableTime** | System-set time the tag was archived. Ignored if set | [optional] 

## Methods

### NewUpdateTagRequestObject

`func NewUpdateTagRequestObject() *UpdateTagRequestObject`

NewUpdateTagRequestObject instantiates a new UpdateTagRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateTagRequestObjectWithDefaults

`func NewUpdateTagRequestObjectWithDefaults() *UpdateTagRequestObject`

NewUpdateTagRequestObjectWithDefaults instantiates a new UpdateTagRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *UpdateTagRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UpdateTagRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UpdateTagRequestObject) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UpdateTagRequestObject) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *UpdateTagRequestObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *UpdateTagRequestObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *UpdateTagRequestObject) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *UpdateTagRequestObject) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *UpdateTagRequestObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *UpdateTagRequestObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTextColor

`func (o *UpdateTagRequestObject) GetTextColor() string`

GetTextColor returns the TextColor field if non-nil, zero value otherwise.

### GetTextColorOk

`func (o *UpdateTagRequestObject) GetTextColorOk() (*string, bool)`

GetTextColorOk returns a tuple with the TextColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextColor

`func (o *UpdateTagRequestObject) SetTextColor(v string)`

SetTextColor sets TextColor field to given value.

### HasTextColor

`func (o *UpdateTagRequestObject) HasTextColor() bool`

HasTextColor returns a boolean if a field has been set.

### SetTextColorNil

`func (o *UpdateTagRequestObject) SetTextColorNil(b bool)`

 SetTextColorNil sets the value for TextColor to be an explicit nil

### UnsetTextColor
`func (o *UpdateTagRequestObject) UnsetTextColor()`

UnsetTextColor ensures that no value is present for TextColor, not even an explicit nil
### GetBackgroundColor

`func (o *UpdateTagRequestObject) GetBackgroundColor() string`

GetBackgroundColor returns the BackgroundColor field if non-nil, zero value otherwise.

### GetBackgroundColorOk

`func (o *UpdateTagRequestObject) GetBackgroundColorOk() (*string, bool)`

GetBackgroundColorOk returns a tuple with the BackgroundColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackgroundColor

`func (o *UpdateTagRequestObject) SetBackgroundColor(v string)`

SetBackgroundColor sets BackgroundColor field to given value.

### HasBackgroundColor

`func (o *UpdateTagRequestObject) HasBackgroundColor() bool`

HasBackgroundColor returns a boolean if a field has been set.

### SetBackgroundColorNil

`func (o *UpdateTagRequestObject) SetBackgroundColorNil(b bool)`

 SetBackgroundColorNil sets the value for BackgroundColor to be an explicit nil

### UnsetBackgroundColor
`func (o *UpdateTagRequestObject) UnsetBackgroundColor()`

UnsetBackgroundColor ensures that no value is present for BackgroundColor, not even an explicit nil
### GetArchived

`func (o *UpdateTagRequestObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *UpdateTagRequestObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *UpdateTagRequestObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *UpdateTagRequestObject) HasArchived() bool`

HasArchived returns a boolean if a field has been set.

### GetId

`func (o *UpdateTagRequestObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateTagRequestObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateTagRequestObject) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *UpdateTagRequestObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetUpdatedAt

`func (o *UpdateTagRequestObject) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *UpdateTagRequestObject) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *UpdateTagRequestObject) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *UpdateTagRequestObject) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### GetCreatedAt

`func (o *UpdateTagRequestObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UpdateTagRequestObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UpdateTagRequestObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *UpdateTagRequestObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetArchivedAt

`func (o *UpdateTagRequestObject) GetArchivedAt() time.Time`

GetArchivedAt returns the ArchivedAt field if non-nil, zero value otherwise.

### GetArchivedAtOk

`func (o *UpdateTagRequestObject) GetArchivedAtOk() (*time.Time, bool)`

GetArchivedAtOk returns a tuple with the ArchivedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchivedAt

`func (o *UpdateTagRequestObject) SetArchivedAt(v time.Time)`

SetArchivedAt sets ArchivedAt field to given value.

### HasArchivedAt

`func (o *UpdateTagRequestObject) HasArchivedAt() bool`

HasArchivedAt returns a boolean if a field has been set.

### SetArchivedAtNil

`func (o *UpdateTagRequestObject) SetArchivedAtNil(b bool)`

 SetArchivedAtNil sets the value for ArchivedAt to be an explicit nil

### UnsetArchivedAt
`func (o *UpdateTagRequestObject) UnsetArchivedAt()`

UnsetArchivedAt ensures that no value is present for ArchivedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


