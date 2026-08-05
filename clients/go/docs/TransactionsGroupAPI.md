# \TransactionsGroupAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GroupTransactions**](TransactionsGroupAPI.md#GroupTransactions) | **Post** /transactions/group | Create a transaction group
[**UngroupTransactions**](TransactionsGroupAPI.md#UngroupTransactions) | **Delete** /transactions/group/{id} | Delete a transaction group



## GroupTransactions

> TransactionObject GroupTransactions(ctx).GroupTransactionsRequest(groupTransactionsRequest).Execute()

Create a transaction group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/juftin/lunchmoney-clients"
)

func main() {
	groupTransactionsRequest := *openapiclient.NewGroupTransactionsRequest([]int64{int64(123)}, time.Now(), "Payee_example") // GroupTransactionsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsGroupAPI.GroupTransactions(context.Background()).GroupTransactionsRequest(groupTransactionsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsGroupAPI.GroupTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GroupTransactions`: TransactionObject
	fmt.Fprintf(os.Stdout, "Response from `TransactionsGroupAPI.GroupTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGroupTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupTransactionsRequest** | [**GroupTransactionsRequest**](GroupTransactionsRequest.md) |  | 

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


## UngroupTransactions

> UngroupTransactions(ctx, id).Execute()

Delete a transaction group



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
	id := int64(2112140959) // int64 | ID of the transaction group to delete

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransactionsGroupAPI.UngroupTransactions(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsGroupAPI.UngroupTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int64** | ID of the transaction group to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiUngroupTransactionsRequest struct via the builder pattern


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

