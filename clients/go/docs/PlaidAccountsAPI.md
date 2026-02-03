# \PlaidAccountsAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAllPlaidAccounts**](PlaidAccountsAPI.md#GetAllPlaidAccounts) | **Get** /plaid_accounts | Get all accounts synced via Plaid
[**GetPlaidAccountById**](PlaidAccountsAPI.md#GetPlaidAccountById) | **Get** /plaid_accounts/{id} | Get a single account that is synced via Plaid
[**TriggerPlaidAccountFetch**](PlaidAccountsAPI.md#TriggerPlaidAccountFetch) | **Post** /plaid_accounts/fetch | Trigger Fetch from Plaid



## GetAllPlaidAccounts

> GetAllPlaidAccounts200Response GetAllPlaidAccounts(ctx).Execute()

Get all accounts synced via Plaid



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
	resp, r, err := apiClient.PlaidAccountsAPI.GetAllPlaidAccounts(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlaidAccountsAPI.GetAllPlaidAccounts``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllPlaidAccounts`: GetAllPlaidAccounts200Response
	fmt.Fprintf(os.Stdout, "Response from `PlaidAccountsAPI.GetAllPlaidAccounts`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAllPlaidAccountsRequest struct via the builder pattern


### Return type

[**GetAllPlaidAccounts200Response**](GetAllPlaidAccounts200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetPlaidAccountById

> PlaidAccountObject GetPlaidAccountById(ctx, id).Execute()

Get a single account that is synced via Plaid



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
	id := int32(119805) // int32 | ID of the plaid account to retrieve

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PlaidAccountsAPI.GetPlaidAccountById(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlaidAccountsAPI.GetPlaidAccountById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetPlaidAccountById`: PlaidAccountObject
	fmt.Fprintf(os.Stdout, "Response from `PlaidAccountsAPI.GetPlaidAccountById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the plaid account to retrieve | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetPlaidAccountByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PlaidAccountObject**](PlaidAccountObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TriggerPlaidAccountFetch

> TriggerPlaidAccountFetch(ctx).StartDate(startDate).EndDate(endDate).Id(id).Execute()

Trigger Fetch from Plaid



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
	startDate := time.Now() // string | Denotes the beginning of the time period to fetch transactions for If omitted, the most recent transactions will be returned. <br> Required if end_date exists. <br> (optional)
	endDate := time.Now() // string | Denotes the end of the time period you'd like to get transactions for. Required if start_date exists.  (optional)
	id := int32(119807) // int32 | Specific ID of a plaid account to fetch. If not set the endpoint will trigger a fetch for all eligible accounts. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PlaidAccountsAPI.TriggerPlaidAccountFetch(context.Background()).StartDate(startDate).EndDate(endDate).Id(id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PlaidAccountsAPI.TriggerPlaidAccountFetch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTriggerPlaidAccountFetchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **string** | Denotes the beginning of the time period to fetch transactions for If omitted, the most recent transactions will be returned. &lt;br&gt; Required if end_date exists. &lt;br&gt; | 
 **endDate** | **string** | Denotes the end of the time period you&#39;d like to get transactions for. Required if start_date exists.  | 
 **id** | **int32** | Specific ID of a plaid account to fetch. If not set the endpoint will trigger a fetch for all eligible accounts. | 

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

