# CreateTagRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | The name of the new tag. Must be between 1 and 100 characters. Must not match the name of any existing tags. | 
**Description** | Pointer to **NullableString** | The description of the tag. Must not exceed 200 characters. | [optional] 
**TextColor** | Pointer to **NullableString** | The text color of the tag. | [optional] 
**BackgroundColor** | Pointer to **NullableString** | The background color of the tag. | [optional] 
**Archived** | Pointer to **bool** | If &#x60;true&#x60;, the tag is archived and not displayed in relevant areas of the Lunch Money app. | [optional] [default to false]

## Methods

### NewCreateTagRequestObject

`func NewCreateTagRequestObject(name string, ) *CreateTagRequestObject`

NewCreateTagRequestObject instantiates a new CreateTagRequestObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateTagRequestObjectWithDefaults

`func NewCreateTagRequestObjectWithDefaults() *CreateTagRequestObject`

NewCreateTagRequestObjectWithDefaults instantiates a new CreateTagRequestObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateTagRequestObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateTagRequestObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateTagRequestObject) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *CreateTagRequestObject) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateTagRequestObject) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateTagRequestObject) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateTagRequestObject) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *CreateTagRequestObject) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *CreateTagRequestObject) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTextColor

`func (o *CreateTagRequestObject) GetTextColor() string`

GetTextColor returns the TextColor field if non-nil, zero value otherwise.

### GetTextColorOk

`func (o *CreateTagRequestObject) GetTextColorOk() (*string, bool)`

GetTextColorOk returns a tuple with the TextColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextColor

`func (o *CreateTagRequestObject) SetTextColor(v string)`

SetTextColor sets TextColor field to given value.

### HasTextColor

`func (o *CreateTagRequestObject) HasTextColor() bool`

HasTextColor returns a boolean if a field has been set.

### SetTextColorNil

`func (o *CreateTagRequestObject) SetTextColorNil(b bool)`

 SetTextColorNil sets the value for TextColor to be an explicit nil

### UnsetTextColor
`func (o *CreateTagRequestObject) UnsetTextColor()`

UnsetTextColor ensures that no value is present for TextColor, not even an explicit nil
### GetBackgroundColor

`func (o *CreateTagRequestObject) GetBackgroundColor() string`

GetBackgroundColor returns the BackgroundColor field if non-nil, zero value otherwise.

### GetBackgroundColorOk

`func (o *CreateTagRequestObject) GetBackgroundColorOk() (*string, bool)`

GetBackgroundColorOk returns a tuple with the BackgroundColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBackgroundColor

`func (o *CreateTagRequestObject) SetBackgroundColor(v string)`

SetBackgroundColor sets BackgroundColor field to given value.

### HasBackgroundColor

`func (o *CreateTagRequestObject) HasBackgroundColor() bool`

HasBackgroundColor returns a boolean if a field has been set.

### SetBackgroundColorNil

`func (o *CreateTagRequestObject) SetBackgroundColorNil(b bool)`

 SetBackgroundColorNil sets the value for BackgroundColor to be an explicit nil

### UnsetBackgroundColor
`func (o *CreateTagRequestObject) UnsetBackgroundColor()`

UnsetBackgroundColor ensures that no value is present for BackgroundColor, not even an explicit nil
### GetArchived

`func (o *CreateTagRequestObject) GetArchived() bool`

GetArchived returns the Archived field if non-nil, zero value otherwise.

### GetArchivedOk

`func (o *CreateTagRequestObject) GetArchivedOk() (*bool, bool)`

GetArchivedOk returns a tuple with the Archived field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArchived

`func (o *CreateTagRequestObject) SetArchived(v bool)`

SetArchived sets Archived field to given value.

### HasArchived

`func (o *CreateTagRequestObject) HasArchived() bool`

HasArchived returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


