# \CryptoManualAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCryptoManual**](CryptoManualAPI.md#CreateCryptoManual) | **Post** /crypto/manual | Create a manual crypto balance
[**CreateCryptocurrency**](CryptoManualAPI.md#CreateCryptocurrency) | **Post** /cryptocurrencies | Add a new supported cryptocurrency
[**DeleteCryptoManual**](CryptoManualAPI.md#DeleteCryptoManual) | **Delete** /crypto/manual/{id} | Delete a manual crypto balance
[**GetAllCryptoManual**](CryptoManualAPI.md#GetAllCryptoManual) | **Get** /crypto/manual | Get all manual crypto balances
[**GetAllCryptocurrencies**](CryptoManualAPI.md#GetAllCryptocurrencies) | **Get** /cryptocurrencies | Get all supported cryptocurrencies
[**GetCryptoManualById**](CryptoManualAPI.md#GetCryptoManualById) | **Get** /crypto/manual/{id} | Get a single manual crypto balance
[**UpdateCryptoManual**](CryptoManualAPI.md#UpdateCryptoManual) | **Put** /crypto/manual/{id} | Update a manual crypto balance



## CreateCryptoManual

> CryptoManualObject CreateCryptoManual(ctx).CreateCryptoManualRequestObject(createCryptoManualRequestObject).Execute()

Create a manual crypto balance



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
	createCryptoManualRequestObject := *openapiclient.NewCreateCryptoManualRequestObject("Cold Wallet BTC", openapiclient.createCryptoManualRequestObject_balance{Float64: new(float64)}, "btc") // CreateCryptoManualRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoManualAPI.CreateCryptoManual(context.Background()).CreateCryptoManualRequestObject(createCryptoManualRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.CreateCryptoManual``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCryptoManual`: CryptoManualObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.CreateCryptoManual`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCryptoManualRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCryptoManualRequestObject** | [**CreateCryptoManualRequestObject**](CreateCryptoManualRequestObject.md) |  | 

### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCryptocurrency

> CryptoCurrencyObject CreateCryptocurrency(ctx).CreateCryptocurrencyRequestObject(createCryptocurrencyRequestObject).Execute()

Add a new supported cryptocurrency



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
	createCryptocurrencyRequestObject := *openapiclient.NewCreateCryptocurrencyRequestObject("https://www.coingecko.com/en/coins/cardano") // CreateCryptocurrencyRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoManualAPI.CreateCryptocurrency(context.Background()).CreateCryptocurrencyRequestObject(createCryptocurrencyRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.CreateCryptocurrency``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCryptocurrency`: CryptoCurrencyObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.CreateCryptocurrency`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCryptocurrencyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCryptocurrencyRequestObject** | [**CreateCryptocurrencyRequestObject**](CreateCryptocurrencyRequestObject.md) |  | 

### Return type

[**CryptoCurrencyObject**](CryptoCurrencyObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCryptoManual

> DeleteCryptoManual(ctx, id).KeepHistory(keepHistory).Execute()

Delete a manual crypto balance



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
	id := int32(22001) // int32 | ID of the manual crypto balance to delete
	keepHistory := true // bool | Explicitly set to `true` to preserve balance history, or `false` to remove associated history during deletion. This must be set if the account has a balance history. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CryptoManualAPI.DeleteCryptoManual(context.Background(), id).KeepHistory(keepHistory).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.DeleteCryptoManual``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual crypto balance to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCryptoManualRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **keepHistory** | **bool** | Explicitly set to &#x60;true&#x60; to preserve balance history, or &#x60;false&#x60; to remove associated history during deletion. This must be set if the account has a balance history. | 

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


## GetAllCryptoManual

> CryptoManualListResponseObject GetAllCryptoManual(ctx).Execute()

Get all manual crypto balances



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
	resp, r, err := apiClient.CryptoManualAPI.GetAllCryptoManual(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.GetAllCryptoManual``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllCryptoManual`: CryptoManualListResponseObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.GetAllCryptoManual`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllCryptoManualRequest struct via the builder pattern


### Return type

[**CryptoManualListResponseObject**](CryptoManualListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllCryptocurrencies

> CryptoCurrencyResponseObject GetAllCryptocurrencies(ctx).Execute()

Get all supported cryptocurrencies



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
	resp, r, err := apiClient.CryptoManualAPI.GetAllCryptocurrencies(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.GetAllCryptocurrencies``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllCryptocurrencies`: CryptoCurrencyResponseObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.GetAllCryptocurrencies`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllCryptocurrenciesRequest struct via the builder pattern


### Return type

[**CryptoCurrencyResponseObject**](CryptoCurrencyResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCryptoManualById

> CryptoManualObject GetCryptoManualById(ctx, id).Execute()

Get a single manual crypto balance



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
	id := int32(22001) // int32 | ID of the manual crypto balance to retrieve

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoManualAPI.GetCryptoManualById(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.GetCryptoManualById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCryptoManualById`: CryptoManualObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.GetCryptoManualById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual crypto balance to retrieve | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCryptoManualByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCryptoManual

> CryptoManualObject UpdateCryptoManual(ctx, id).UpdateCryptoManualRequestObject(updateCryptoManualRequestObject).Execute()

Update a manual crypto balance



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
	id := int32(22001) // int32 | ID of the manual crypto balance to update
	updateCryptoManualRequestObject := *openapiclient.NewUpdateCryptoManualRequestObject() // UpdateCryptoManualRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CryptoManualAPI.UpdateCryptoManual(context.Background(), id).UpdateCryptoManualRequestObject(updateCryptoManualRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CryptoManualAPI.UpdateCryptoManual``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateCryptoManual`: CryptoManualObject
	fmt.Fprintf(os.Stdout, "Response from `CryptoManualAPI.UpdateCryptoManual`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the manual crypto balance to update | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCryptoManualRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateCryptoManualRequestObject** | [**UpdateCryptoManualRequestObject**](UpdateCryptoManualRequestObject.md) |  | 

### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

