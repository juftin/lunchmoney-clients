# \ManualAccountsAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateManualAccount**](ManualAccountsAPI.md#CreateManualAccount) | **Post** /manual_accounts | Create a manual account
[**DeleteManualAccount**](ManualAccountsAPI.md#DeleteManualAccount) | **Delete** /manual_accounts/{id} | Delete a manual account
[**GetAllManualAccounts**](ManualAccountsAPI.md#GetAllManualAccounts) | **Get** /manual_accounts | Get all manual accounts
[**GetManualAccountById**](ManualAccountsAPI.md#GetManualAccountById) | **Get** /manual_accounts/{id} | Get a single manual account
[**UpdateManualAccount**](ManualAccountsAPI.md#UpdateManualAccount) | **Put** /manual_accounts/{id} | Update an existing manual account



## CreateManualAccount

> ManualAccountObject CreateManualAccount(ctx).CreateManualAccountRequestObject(createManualAccountRequestObject).Execute()

Create a manual account



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
	createManualAccountRequestObject := *openapiclient.NewCreateManualAccountRequestObject("My Savings Account", openapiclient.accountTypeEnum("cash"), openapiclient.createManualAccountRequestObject_balance{Float64: new(float64)}) // CreateManualAccountRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManualAccountsAPI.CreateManualAccount(context.Background()).CreateManualAccountRequestObject(createManualAccountRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManualAccountsAPI.CreateManualAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateManualAccount`: ManualAccountObject
	fmt.Fprintf(os.Stdout, "Response from `ManualAccountsAPI.CreateManualAccount`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateManualAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createManualAccountRequestObject** | [**CreateManualAccountRequestObject**](CreateManualAccountRequestObject.md) |  | 

### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteManualAccount

> DeleteManualAccount(ctx, id).DeleteItems(deleteItems).DeleteBalanceHistory(deleteBalanceHistory).Execute()

Delete a manual account



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
	id := int32(119807) // int32 | ID of the manual account to delete
	deleteItems := true // bool | When set to true will also delete any transactions, rules, and recurring items associated with this account. Use this option with caution, it is irreversible! (optional) (default to false)
	deleteBalanceHistory := true // bool | When set to true will delete any balance history associated with this account. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ManualAccountsAPI.DeleteManualAccount(context.Background(), id).DeleteItems(deleteItems).DeleteBalanceHistory(deleteBalanceHistory).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManualAccountsAPI.DeleteManualAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual account to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteManualAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **deleteItems** | **bool** | When set to true will also delete any transactions, rules, and recurring items associated with this account. Use this option with caution, it is irreversible! | [default to false]
 **deleteBalanceHistory** | **bool** | When set to true will delete any balance history associated with this account. | [default to false]

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


## GetAllManualAccounts

> GetAllManualAccounts200Response GetAllManualAccounts(ctx).Execute()

Get all manual accounts



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
	resp, r, err := apiClient.ManualAccountsAPI.GetAllManualAccounts(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManualAccountsAPI.GetAllManualAccounts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllManualAccounts`: GetAllManualAccounts200Response
	fmt.Fprintf(os.Stdout, "Response from `ManualAccountsAPI.GetAllManualAccounts`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllManualAccountsRequest struct via the builder pattern


### Return type

[**GetAllManualAccounts200Response**](GetAllManualAccounts200Response.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetManualAccountById

> ManualAccountObject GetManualAccountById(ctx, id).Execute()

Get a single manual account



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
	id := int32(119807) // int32 | ID of the manual account to retrieve

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManualAccountsAPI.GetManualAccountById(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManualAccountsAPI.GetManualAccountById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetManualAccountById`: ManualAccountObject
	fmt.Fprintf(os.Stdout, "Response from `ManualAccountsAPI.GetManualAccountById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual account to retrieve | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetManualAccountByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateManualAccount

> ManualAccountObject UpdateManualAccount(ctx, id).UpdateManualAccountRequestObject(updateManualAccountRequestObject).Execute()

Update an existing manual account



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
	id := int32(119807) // int32 | ID of the manual account to update
	updateManualAccountRequestObject := *openapiclient.NewUpdateManualAccountRequestObject() // UpdateManualAccountRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ManualAccountsAPI.UpdateManualAccount(context.Background(), id).UpdateManualAccountRequestObject(updateManualAccountRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ManualAccountsAPI.UpdateManualAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateManualAccount`: ManualAccountObject
	fmt.Fprintf(os.Stdout, "Response from `ManualAccountsAPI.UpdateManualAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual account to update | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateManualAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateManualAccountRequestObject** | [**UpdateManualAccountRequestObject**](UpdateManualAccountRequestObject.md) |  | 

### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

