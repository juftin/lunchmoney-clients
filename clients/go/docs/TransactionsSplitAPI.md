# \TransactionsSplitAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SplitTransaction**](TransactionsSplitAPI.md#SplitTransaction) | **Post** /transactions/split/{id} | Split a transaction
[**UnsplitTransaction**](TransactionsSplitAPI.md#UnsplitTransaction) | **Delete** /transactions/split/{id} | Unsplit a previously split transactions



## SplitTransaction

> TransactionObject SplitTransaction(ctx, id).SplitTransactionRequest(splitTransactionRequest).Execute()

Split a transaction



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
	id := int64(2112150650) // int64 | ID of the transaction to spit
	splitTransactionRequest := *openapiclient.NewSplitTransactionRequest([]openapiclient.SplitTransactionObject{*openapiclient.NewSplitTransactionObject(openapiclient.splitTransactionObject_amount{Float64: new(float64)})}) // SplitTransactionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsSplitAPI.SplitTransaction(context.Background(), id).SplitTransactionRequest(splitTransactionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsSplitAPI.SplitTransaction``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SplitTransaction`: TransactionObject
	fmt.Fprintf(os.Stdout, "Response from `TransactionsSplitAPI.SplitTransaction`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int64** | ID of the transaction to spit | 

### Other Parameters

Other parameters are passed through a pointer to a apiSplitTransactionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **splitTransactionRequest** | [**SplitTransactionRequest**](SplitTransactionRequest.md) |  | 

### Return type

[**TransactionObject**](TransactionObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UnsplitTransaction

> UnsplitTransaction(ctx, id).Execute()

Unsplit a previously split transactions



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
	id := int64(2112140459) // int64 | ID of the previously split transaction to delete.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransactionsSplitAPI.UnsplitTransaction(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsSplitAPI.UnsplitTransaction``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int64** | ID of the previously split transaction to delete. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUnsplitTransactionRequest struct via the builder pattern


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

