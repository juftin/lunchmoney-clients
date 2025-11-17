# \RecurringItemsAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAllRecurring**](RecurringItemsAPI.md#GetAllRecurring) | **Get** /recurring_items | Get all recurring items
[**GetRecurringById**](RecurringItemsAPI.md#GetRecurringById) | **Get** /recurring_items/{id} | Get a single recurring item



## GetAllRecurring

> GetAllRecurring200Response GetAllRecurring(ctx).StartDate(startDate).EndDate(endDate).IncludeSuggested(includeSuggested).Execute()

Get all recurring items



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
	startDate := time.Now() // string | Denotes the beginning of the range used to populate the `matching` object in the recurring items. If omitted, the current month will be used as the range.<br> Required if end_date exists. (optional)
	endDate := time.Now() // string | Denotes the end of the the range used to populate the `matching` object in the recurring items. Required if start_date exists.  (optional)
	includeSuggested := true // bool |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RecurringItemsAPI.GetAllRecurring(context.Background()).StartDate(startDate).EndDate(endDate).IncludeSuggested(includeSuggested).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RecurringItemsAPI.GetAllRecurring``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllRecurring`: GetAllRecurring200Response
	fmt.Fprintf(os.Stdout, "Response from `RecurringItemsAPI.GetAllRecurring`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllRecurringRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **string** | Denotes the beginning of the range used to populate the &#x60;matching&#x60; object in the recurring items. If omitted, the current month will be used as the range.&lt;br&gt; Required if end_date exists. | 
 **endDate** | **string** | Denotes the end of the the range used to populate the &#x60;matching&#x60; object in the recurring items. Required if start_date exists.  | 
 **includeSuggested** | **bool** |  | 

### Return type

[**GetAllRecurring200Response**](GetAllRecurring200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRecurringById

> RecurringObject GetRecurringById(ctx, id).StartDate(startDate).EndDate(endDate).Execute()

Get a single recurring item



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
	id := int32(994069) // int32 | ID of the recurring item to retrieve
	startDate := time.Now() // string | Denotes the beginning of the range used to populate the `matching` object in the recurring items. If omitted, the current month will be used as the range.<br> Required if end_date exists. (optional)
	endDate := time.Now() // string | Denotes the end of the the range used to populate the `matching` object in the recurring items. Required if start_date exists.  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RecurringItemsAPI.GetRecurringById(context.Background(), id).StartDate(startDate).EndDate(endDate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RecurringItemsAPI.GetRecurringById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRecurringById`: RecurringObject
	fmt.Fprintf(os.Stdout, "Response from `RecurringItemsAPI.GetRecurringById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the recurring item to retrieve | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetRecurringByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startDate** | **string** | Denotes the beginning of the range used to populate the &#x60;matching&#x60; object in the recurring items. If omitted, the current month will be used as the range.&lt;br&gt; Required if end_date exists. | 
 **endDate** | **string** | Denotes the end of the the range used to populate the &#x60;matching&#x60; object in the recurring items. Required if start_date exists.  | 

### Return type

[**RecurringObject**](RecurringObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

