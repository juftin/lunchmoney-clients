# GetTransactionAttachmentUrl200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** | The signed url to download the file attachment | 
**ExpiresAt** | **time.Time** | The date and time the signed url will expire | 

## Methods

### NewGetTransactionAttachmentUrl200Response

`func NewGetTransactionAttachmentUrl200Response(url string, expiresAt time.Time, ) *GetTransactionAttachmentUrl200Response`

NewGetTransactionAttachmentUrl200Response instantiates a new GetTransactionAttachmentUrl200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetTransactionAttachmentUrl200ResponseWithDefaults

`func NewGetTransactionAttachmentUrl200ResponseWithDefaults() *GetTransactionAttachmentUrl200Response`

NewGetTransactionAttachmentUrl200ResponseWithDefaults instantiates a new GetTransactionAttachmentUrl200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *GetTransactionAttachmentUrl200Response) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *GetTransactionAttachmentUrl200Response) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *GetTransactionAttachmentUrl200Response) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetExpiresAt

`func (o *GetTransactionAttachmentUrl200Response) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GetTransactionAttachmentUrl200Response) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GetTransactionAttachmentUrl200Response) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


