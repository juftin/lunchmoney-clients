# \TransactionsFilesAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AttachFileToTransaction**](TransactionsFilesAPI.md#AttachFileToTransaction) | **Post** /transactions/{transaction_id}/attachments | Attach a file to a transaction
[**DeleteTransactionAttachment**](TransactionsFilesAPI.md#DeleteTransactionAttachment) | **Delete** /transactions/attachments/{file_id} | Delete a file attachment
[**GetTransactionAttachmentUrl**](TransactionsFilesAPI.md#GetTransactionAttachmentUrl) | **Get** /transactions/attachments/{file_id} | Get a url to download a file attachment



## AttachFileToTransaction

> TransactionAttachmentObject AttachFileToTransaction(ctx, transactionId).File(file).Notes(notes).Execute()

Attach a file to a transaction



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/juftin/lunchmoney-clients"
)

func main() {
	transactionId := int64(2112150655) // int64 | 
	file := os.NewFile(1234, "some_file") // *os.File | The file to attach via multipart form encoding.  File size may not exceed 10MB. 
	notes := "notes_example" // string | Optional notes about the file (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsFilesAPI.AttachFileToTransaction(context.Background(), transactionId).File(file).Notes(notes).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsFilesAPI.AttachFileToTransaction``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AttachFileToTransaction`: TransactionAttachmentObject
	fmt.Fprintf(os.Stdout, "Response from `TransactionsFilesAPI.AttachFileToTransaction`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**transactionId** | **int64** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiAttachFileToTransactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **file** | ***os.File** | The file to attach via multipart form encoding.  File size may not exceed 10MB.  | 
 **notes** | **string** | Optional notes about the file | 

### Return type

[**TransactionAttachmentObject**](TransactionAttachmentObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTransactionAttachment

> DeleteTransactionAttachment(ctx, fileId).Execute()

Delete a file attachment



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/juftin/lunchmoney-clients"
)

func main() {
	fileId := int32(1234567890) // int32 | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransactionsFilesAPI.DeleteTransactionAttachment(context.Background(), fileId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsFilesAPI.DeleteTransactionAttachment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fileId** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTransactionAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTransactionAttachmentUrl

> GetTransactionAttachmentUrl200Response GetTransactionAttachmentUrl(ctx, fileId).Execute()

Get a url to download a file attachment



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/juftin/lunchmoney-clients"
)

func main() {
	fileId := int32(1234567890) // int32 | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsFilesAPI.GetTransactionAttachmentUrl(context.Background(), fileId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsFilesAPI.GetTransactionAttachmentUrl``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTransactionAttachmentUrl`: GetTransactionAttachmentUrl200Response
	fmt.Fprintf(os.Stdout, "Response from `TransactionsFilesAPI.GetTransactionAttachmentUrl`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**fileId** | **int32** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTransactionAttachmentUrlRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetTransactionAttachmentUrl200Response**](GetTransactionAttachmentUrl200Response.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

