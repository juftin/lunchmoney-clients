# \BudgetsAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteBudget**](BudgetsAPI.md#DeleteBudget) | **Delete** /budgets | Delete budget
[**GetBudgetSettings**](BudgetsAPI.md#GetBudgetSettings) | **Get** /budgets/settings | Get budget period settings
[**UpsertBudget**](BudgetsAPI.md#UpsertBudget) | **Put** /budgets | Upsert budget



## DeleteBudget

> DeleteBudget(ctx).CategoryId(categoryId).StartDate(startDate).Execute()

Delete budget



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
	categoryId := int32(56) // int32 | Category ID of the budget to delete
	startDate := time.Now() // string | Start date of the budget period in ISO 8601 date format (YYYY-MM-DD)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BudgetsAPI.DeleteBudget(context.Background()).CategoryId(categoryId).StartDate(startDate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BudgetsAPI.DeleteBudget``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteBudgetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryId** | **int32** | Category ID of the budget to delete | 
 **startDate** | **string** | Start date of the budget period in ISO 8601 date format (YYYY-MM-DD) | 

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


## GetBudgetSettings

> BudgetSettingsResponseObject GetBudgetSettings(ctx).Execute()

Get budget period settings



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
	resp, r, err := apiClient.BudgetsAPI.GetBudgetSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BudgetsAPI.GetBudgetSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBudgetSettings`: BudgetSettingsResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BudgetsAPI.GetBudgetSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetBudgetSettingsRequest struct via the builder pattern


### Return type

[**BudgetSettingsResponseObject**](BudgetSettingsResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpsertBudget

> BudgetUpsertResponseObject UpsertBudget(ctx).UpsertBudgetRequestObject(upsertBudgetRequestObject).Execute()

Upsert budget



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
	upsertBudgetRequestObject := *openapiclient.NewUpsertBudgetRequestObject(time.Now(), int32(123), openapiclient.upsertBudgetRequestObject_amount{Float64: new(float64)}) // UpsertBudgetRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BudgetsAPI.UpsertBudget(context.Background()).UpsertBudgetRequestObject(upsertBudgetRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BudgetsAPI.UpsertBudget``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpsertBudget`: BudgetUpsertResponseObject
	fmt.Fprintf(os.Stdout, "Response from `BudgetsAPI.UpsertBudget`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpsertBudgetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsertBudgetRequestObject** | [**UpsertBudgetRequestObject**](UpsertBudgetRequestObject.md) |  | 

### Return type

[**BudgetUpsertResponseObject**](BudgetUpsertResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

