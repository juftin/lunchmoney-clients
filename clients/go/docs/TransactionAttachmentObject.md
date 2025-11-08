# TransactionAttachmentObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **int32** | The unique identifier of the attachment | [optional] 
**UploadedBy** | Pointer to **int64** | The id of the user who uploaded the attachment | [optional] 
**Name** | Pointer to **string** | The name of the file | [optional] 
**Type** | Pointer to **string** | The MIME type of the file | [optional] 
**Size** | Pointer to **int32** | The size of the file in kilobytes | [optional] 
**Notes** | Pointer to **NullableString** | Optional notes about the attachment | [optional] 
**CreatedAt** | Pointer to **time.Time** | The date and time when the attachment was created in ISO 8601 format | [optional] 

## Methods

### NewTransactionAttachmentObject

`func NewTransactionAttachmentObject() *TransactionAttachmentObject`

NewTransactionAttachmentObject instantiates a new TransactionAttachmentObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransactionAttachmentObjectWithDefaults

`func NewTransactionAttachmentObjectWithDefaults() *TransactionAttachmentObject`

NewTransactionAttachmentObjectWithDefaults instantiates a new TransactionAttachmentObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TransactionAttachmentObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TransactionAttachmentObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TransactionAttachmentObject) SetId(v int32)`

SetId sets Id field to given value.

### HasId

`func (o *TransactionAttachmentObject) HasId() bool`

HasId returns a boolean if a field has been set.

### GetUploadedBy

`func (o *TransactionAttachmentObject) GetUploadedBy() int64`

GetUploadedBy returns the UploadedBy field if non-nil, zero value otherwise.

### GetUploadedByOk

`func (o *TransactionAttachmentObject) GetUploadedByOk() (*int64, bool)`

GetUploadedByOk returns a tuple with the UploadedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUploadedBy

`func (o *TransactionAttachmentObject) SetUploadedBy(v int64)`

SetUploadedBy sets UploadedBy field to given value.

### HasUploadedBy

`func (o *TransactionAttachmentObject) HasUploadedBy() bool`

HasUploadedBy returns a boolean if a field has been set.

### GetName

`func (o *TransactionAttachmentObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TransactionAttachmentObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TransactionAttachmentObject) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *TransactionAttachmentObject) HasName() bool`

HasName returns a boolean if a field has been set.

### GetType

`func (o *TransactionAttachmentObject) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TransactionAttachmentObject) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TransactionAttachmentObject) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *TransactionAttachmentObject) HasType() bool`

HasType returns a boolean if a field has been set.

### GetSize

`func (o *TransactionAttachmentObject) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *TransactionAttachmentObject) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *TransactionAttachmentObject) SetSize(v int32)`

SetSize sets Size field to given value.

### HasSize

`func (o *TransactionAttachmentObject) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetNotes

`func (o *TransactionAttachmentObject) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *TransactionAttachmentObject) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *TransactionAttachmentObject) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *TransactionAttachmentObject) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *TransactionAttachmentObject) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *TransactionAttachmentObject) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetCreatedAt

`func (o *TransactionAttachmentObject) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TransactionAttachmentObject) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TransactionAttachmentObject) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TransactionAttachmentObject) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


