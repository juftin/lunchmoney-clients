# \CryptoSyncedAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAllCryptoSynced**](CryptoSyncedAPI.md#GetAllCryptoSynced) | **Get** /crypto/synced | Get all synced crypto accounts
[**GetCryptoSyncedBalanceBySymbol**](CryptoSyncedAPI.md#GetCryptoSyncedBalanceBySymbol) | **Get** /crypto/synced/{id}/{symbol} | Get a synced crypto balance by symbol
[**GetCryptoSyncedById**](CryptoSyncedAPI.md#GetCryptoSyncedById) | **Get** /crypto/synced/{id} | Get a single synced crypto account
[**RefreshCryptoSynced**](CryptoSyncedAPI.md#RefreshCryptoSynced) | **Post** /crypto/synced/{id}/refresh | Refresh balances for a synced crypto account



## GetAllCryptoSynced

> CryptoSyncedListResponseObject GetAllCryptoSynced(ctx).Execute()

Get all synced crypto accounts



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoSyncedAPI.GetAllCryptoSynced(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoSyncedAPI.GetAllCryptoSynced``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllCryptoSynced`: CryptoSyncedListResponseObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoSyncedAPI.GetAllCryptoSynced`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllCryptoSyncedRequest struct via the builder pattern


### Return type

[**CryptoSyncedListResponseObject**](CryptoSyncedListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCryptoSyncedBalanceBySymbol

> CryptoSyncedBalance GetCryptoSyncedBalanceBySymbol(ctx, id, symbol).Execute()

Get a synced crypto balance by symbol



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
	id := int32(56) // int32 | Synced crypto account ID
	symbol := "symbol_example" // string | Crypto symbol within the synced account

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoSyncedAPI.GetCryptoSyncedBalanceBySymbol(context.Background(), id, symbol).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoSyncedAPI.GetCryptoSyncedBalanceBySymbol``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCryptoSyncedBalanceBySymbol`: CryptoSyncedBalance
	fmt.Fprintf(os.Stdout, "Response from `CryptoSyncedAPI.GetCryptoSyncedBalanceBySymbol`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | Synced crypto account ID | 
**symbol** | **string** | Crypto symbol within the synced account | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCryptoSyncedBalanceBySymbolRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**CryptoSyncedBalance**](CryptoSyncedBalance.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCryptoSyncedById

> SyncedCryptoAccount GetCryptoSyncedById(ctx, id).Execute()

Get a single synced crypto account



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
	id := int32(33004) // int32 | Synced crypto account ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoSyncedAPI.GetCryptoSyncedById(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoSyncedAPI.GetCryptoSyncedById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCryptoSyncedById`: SyncedCryptoAccount
	fmt.Fprintf(os.Stdout, "Response from `CryptoSyncedAPI.GetCryptoSyncedById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | Synced crypto account ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCryptoSyncedByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SyncedCryptoAccount**](SyncedCryptoAccount.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RefreshCryptoSynced

> SyncedCryptoAccount RefreshCryptoSynced(ctx, id).Execute()

Refresh balances for a synced crypto account



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
	id := int32(33004) // int32 | Synced crypto account ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoSyncedAPI.RefreshCryptoSynced(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoSyncedAPI.RefreshCryptoSynced``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RefreshCryptoSynced`: SyncedCryptoAccount
	fmt.Fprintf(os.Stdout, "Response from `CryptoSyncedAPI.RefreshCryptoSynced`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | Synced crypto account ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiRefreshCryptoSyncedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SyncedCryptoAccount**](SyncedCryptoAccount.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

