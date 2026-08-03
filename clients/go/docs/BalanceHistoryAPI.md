# \BalanceHistoryAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteBalanceHistoryEntry**](BalanceHistoryAPI.md#DeleteBalanceHistoryEntry) | **Delete** /balance_history/entries/{id} | Delete a balance history entry
[**DeleteBalanceHistoryForAccount**](BalanceHistoryAPI.md#DeleteBalanceHistoryForAccount) | **Delete** /balance_history/{account_type}/{account_id} | Delete all balance history for an account
[**DeleteBalanceHistoryForCryptoSynced**](BalanceHistoryAPI.md#DeleteBalanceHistoryForCryptoSynced) | **Delete** /balance_history/crypto_synced/{account_id}/{symbol} | Delete all balance history for a synced crypto symbol
[**GetBalanceHistory**](BalanceHistoryAPI.md#GetBalanceHistory) | **Get** /balance_history | Get balance history
[**GetBalanceHistoryForAccount**](BalanceHistoryAPI.md#GetBalanceHistoryForAccount) | **Get** /balance_history/{account_type}/{account_id} | Get balance history for an account
[**GetBalanceHistoryForCryptoSynced**](BalanceHistoryAPI.md#GetBalanceHistoryForCryptoSynced) | **Get** /balance_history/crypto_synced/{account_id}/{symbol} | Get balance history for a synced crypto symbol
[**UpdateBalanceHistoryDetails**](BalanceHistoryAPI.md#UpdateBalanceHistoryDetails) | **Put** /balance_history/deleted/{account_id}/details | Update details for a deleted account
[**UpsertBalanceHistoryForAccount**](BalanceHistoryAPI.md#UpsertBalanceHistoryForAccount) | **Put** /balance_history/{account_type}/{account_id} | Upsert balance history for an account
[**UpsertBalanceHistoryForCryptoSynced**](BalanceHistoryAPI.md#UpsertBalanceHistoryForCryptoSynced) | **Put** /balance_history/crypto_synced/{account_id}/{symbol} | Upsert balance history for a synced crypto symbol



## DeleteBalanceHistoryEntry

> DeleteBalanceHistoryEntry(ctx, id).Execute()

Delete a balance history entry



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
	id := int32(56) // int32 | Historical balance entry identifier to delete.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BalanceHistoryAPI.DeleteBalanceHistoryEntry(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.DeleteBalanceHistoryEntry``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | Historical balance entry identifier to delete. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteBalanceHistoryEntryRequest struct via the builder pattern


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


## DeleteBalanceHistoryForAccount

> DeleteBalanceHistoryForAccount(ctx, accountType, accountId).Execute()

Delete all balance history for an account



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
	accountType := "accountType_example" // string | Account family to delete. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
	accountId := int32(56) // int32 | Account or deleted-source identifier within the selected `account_type`.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BalanceHistoryAPI.DeleteBalanceHistoryForAccount(context.Background(), accountType, accountId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.DeleteBalanceHistoryForAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountType** | **string** | Account family to delete. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
**accountId** | **int32** | Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteBalanceHistoryForAccountRequest struct via the builder pattern


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


## DeleteBalanceHistoryForCryptoSynced

> DeleteBalanceHistoryForCryptoSynced(ctx, accountId, symbol).Execute()

Delete all balance history for a synced crypto symbol



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
	accountId := int32(56) // int32 | Synced crypto account identifier.
	symbol := "symbol_example" // string | Crypto symbol identifying one balance stream within the synced crypto account.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BalanceHistoryAPI.DeleteBalanceHistoryForCryptoSynced(context.Background(), accountId, symbol).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.DeleteBalanceHistoryForCryptoSynced``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | Synced crypto account identifier. | 
**symbol** | **string** | Crypto symbol identifying one balance stream within the synced crypto account. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteBalanceHistoryForCryptoSyncedRequest struct via the builder pattern


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


## GetBalanceHistory

> BalanceHistoryListResponseObject GetBalanceHistory(ctx).StartMonth(startMonth).EndMonth(endMonth).Execute()

Get balance history



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
	startMonth := "2026-01" // string | Optional start of the requested history range as a calendar month in YYYY-MM format (for example `2026-06`). If set, `end_month` is also required. The range is inclusive. `start_month` must not be in the future. A full date such as `2026-06-01` is invalid. (optional)
	endMonth := "2026-03" // string | Optional end of the requested history range as a calendar month in YYYY-MM format (for example `2026-06`). If set, `start_month` is also required. The range is inclusive. `end_month` may not be earlier than `start_month` and must not be in the future. A full date such as `2026-06-01` is invalid. For a single month, set this to the same value as `start_month`. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.GetBalanceHistory(context.Background()).StartMonth(startMonth).EndMonth(endMonth).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.GetBalanceHistory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBalanceHistory`: BalanceHistoryListResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.GetBalanceHistory`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetBalanceHistoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startMonth** | **string** | Optional start of the requested history range as a calendar month in YYYY-MM format (for example &#x60;2026-06&#x60;). If set, &#x60;end_month&#x60; is also required. The range is inclusive. &#x60;start_month&#x60; must not be in the future. A full date such as &#x60;2026-06-01&#x60; is invalid. | 
 **endMonth** | **string** | Optional end of the requested history range as a calendar month in YYYY-MM format (for example &#x60;2026-06&#x60;). If set, &#x60;start_month&#x60; is also required. The range is inclusive. &#x60;end_month&#x60; may not be earlier than &#x60;start_month&#x60; and must not be in the future. A full date such as &#x60;2026-06-01&#x60; is invalid. For a single month, set this to the same value as &#x60;start_month&#x60;. | 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBalanceHistoryForAccount

> BalanceHistoryListResponseObject GetBalanceHistoryForAccount(ctx, accountType, accountId).StartMonth(startMonth).EndMonth(endMonth).Execute()

Get balance history for an account



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
	accountType := "accountType_example" // string | Account family to retrieve. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
	accountId := int32(56) // int32 | Account or deleted-source identifier within the selected `account_type`.
	startMonth := "startMonth_example" // string | Optional. Same format and constraints as `start_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)
	endMonth := "endMonth_example" // string | Optional. Same format and constraints as `end_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.GetBalanceHistoryForAccount(context.Background(), accountType, accountId).StartMonth(startMonth).EndMonth(endMonth).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.GetBalanceHistoryForAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBalanceHistoryForAccount`: BalanceHistoryListResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.GetBalanceHistoryForAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountType** | **string** | Account family to retrieve. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
**accountId** | **int32** | Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBalanceHistoryForAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **startMonth** | **string** | Optional. Same format and constraints as &#x60;start_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | 
 **endMonth** | **string** | Optional. Same format and constraints as &#x60;end_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetBalanceHistoryForCryptoSynced

> BalanceHistoryListResponseObject GetBalanceHistoryForCryptoSynced(ctx, accountId, symbol).StartMonth(startMonth).EndMonth(endMonth).Execute()

Get balance history for a synced crypto symbol



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
	accountId := int32(56) // int32 | Synced crypto account identifier.
	symbol := "symbol_example" // string | Crypto symbol identifying one balance stream within the synced crypto account.
	startMonth := "startMonth_example" // string | Optional. Same format and constraints as `start_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)
	endMonth := "endMonth_example" // string | Optional. Same format and constraints as `end_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.GetBalanceHistoryForCryptoSynced(context.Background(), accountId, symbol).StartMonth(startMonth).EndMonth(endMonth).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.GetBalanceHistoryForCryptoSynced``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBalanceHistoryForCryptoSynced`: BalanceHistoryListResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.GetBalanceHistoryForCryptoSynced`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | Synced crypto account identifier. | 
**symbol** | **string** | Crypto symbol identifying one balance stream within the synced crypto account. | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetBalanceHistoryForCryptoSyncedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **startMonth** | **string** | Optional. Same format and constraints as &#x60;start_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | 
 **endMonth** | **string** | Optional. Same format and constraints as &#x60;end_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateBalanceHistoryDetails

> UpdateBalanceHistoryDetailsResponseObject UpdateBalanceHistoryDetails(ctx, accountId).UpdateBalanceHistoryDetailsRequestObject(updateBalanceHistoryDetailsRequestObject).Execute()

Update details for a deleted account



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
	accountId := int32(56) // int32 | Deleted account history source identifier to update.
	updateBalanceHistoryDetailsRequestObject := *openapiclient.NewUpdateBalanceHistoryDetailsRequestObject() // UpdateBalanceHistoryDetailsRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.UpdateBalanceHistoryDetails(context.Background(), accountId).UpdateBalanceHistoryDetailsRequestObject(updateBalanceHistoryDetailsRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.UpdateBalanceHistoryDetails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateBalanceHistoryDetails`: UpdateBalanceHistoryDetailsResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.UpdateBalanceHistoryDetails`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | Deleted account history source identifier to update. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateBalanceHistoryDetailsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateBalanceHistoryDetailsRequestObject** | [**UpdateBalanceHistoryDetailsRequestObject**](UpdateBalanceHistoryDetailsRequestObject.md) |  | 

### Return type

[**UpdateBalanceHistoryDetailsResponseObject**](UpdateBalanceHistoryDetailsResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpsertBalanceHistoryForAccount

> BalanceHistoryAccountObject UpsertBalanceHistoryForAccount(ctx, accountType, accountId).UpsertBalanceHistoryRequestObject(upsertBalanceHistoryRequestObject).Execute()

Upsert balance history for an account



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
	accountType := "accountType_example" // string | Account family to update. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
	accountId := int32(56) // int32 | Account or deleted-source identifier within the selected `account_type`.
	upsertBalanceHistoryRequestObject := *openapiclient.NewUpsertBalanceHistoryRequestObject([]openapiclient.BalanceHistoryUpdateItemObject{*openapiclient.NewBalanceHistoryUpdateItemObject("2026-06", openapiclient.balanceHistoryUpdateItemObject_balance{Float64: new(float64)})}) // UpsertBalanceHistoryRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.UpsertBalanceHistoryForAccount(context.Background(), accountType, accountId).UpsertBalanceHistoryRequestObject(upsertBalanceHistoryRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.UpsertBalanceHistoryForAccount``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpsertBalanceHistoryForAccount`: BalanceHistoryAccountObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.UpsertBalanceHistoryForAccount`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountType** | **string** | Account family to update. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
**accountId** | **int32** | Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpsertBalanceHistoryForAccountRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **upsertBalanceHistoryRequestObject** | [**UpsertBalanceHistoryRequestObject**](UpsertBalanceHistoryRequestObject.md) |  | 

### Return type

[**BalanceHistoryAccountObject**](BalanceHistoryAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpsertBalanceHistoryForCryptoSynced

> BalanceHistoryAccountObject UpsertBalanceHistoryForCryptoSynced(ctx, accountId, symbol).UpsertBalanceHistoryRequestObject(upsertBalanceHistoryRequestObject).Execute()

Upsert balance history for a synced crypto symbol



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
	accountId := int32(56) // int32 | Synced crypto account identifier to update.
	symbol := "symbol_example" // string | Crypto symbol identifying one balance stream within the synced crypto account.
	upsertBalanceHistoryRequestObject := *openapiclient.NewUpsertBalanceHistoryRequestObject([]openapiclient.BalanceHistoryUpdateItemObject{*openapiclient.NewBalanceHistoryUpdateItemObject("2026-06", openapiclient.balanceHistoryUpdateItemObject_balance{Float64: new(float64)})}) // UpsertBalanceHistoryRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BalanceHistoryAPI.UpsertBalanceHistoryForCryptoSynced(context.Background(), accountId, symbol).UpsertBalanceHistoryRequestObject(upsertBalanceHistoryRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BalanceHistoryAPI.UpsertBalanceHistoryForCryptoSynced``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpsertBalanceHistoryForCryptoSynced`: BalanceHistoryAccountObject
	fmt.Fprintf(os.Stdout, "Response from `BalanceHistoryAPI.UpsertBalanceHistoryForCryptoSynced`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**accountId** | **int32** | Synced crypto account identifier to update. | 
**symbol** | **string** | Crypto symbol identifying one balance stream within the synced crypto account. | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpsertBalanceHistoryForCryptoSyncedRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **upsertBalanceHistoryRequestObject** | [**UpsertBalanceHistoryRequestObject**](UpsertBalanceHistoryRequestObject.md) |  | 

### Return type

[**BalanceHistoryAccountObject**](BalanceHistoryAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

