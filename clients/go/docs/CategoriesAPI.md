# \CategoriesAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCategory**](CategoriesAPI.md#CreateCategory) | **Post** /categories | Create a new category or category group
[**DeleteCategory**](CategoriesAPI.md#DeleteCategory) | **Delete** /categories/{id} | Delete a category or category group
[**GetAllCategories**](CategoriesAPI.md#GetAllCategories) | **Get** /categories | Get all categories
[**GetCategoryById**](CategoriesAPI.md#GetCategoryById) | **Get** /categories/{id} | Get a single category
[**UpdateCategory**](CategoriesAPI.md#UpdateCategory) | **Put** /categories/{id} | Update an existing category or category group



## CreateCategory

> CategoryObject CreateCategory(ctx).CreateCategoryRequestObject(createCategoryRequestObject).Execute()

Create a new category or category group



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
	createCategoryRequestObject := *openapiclient.NewCreateCategoryRequestObject("Name_example") // CreateCategoryRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CategoriesAPI.CreateCategory(context.Background()).CreateCategoryRequestObject(createCategoryRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CategoriesAPI.CreateCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCategory`: CategoryObject
	fmt.Fprintf(os.Stdout, "Response from `CategoriesAPI.CreateCategory`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCategoryRequestObject** | [**CreateCategoryRequestObject**](CreateCategoryRequestObject.md) |  | 

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteCategory

> DeleteCategory(ctx, id).Force(force).Execute()

Delete a category or category group



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
	id := int32(83) // int32 | ID of the category to delete
	force := true // bool | Set to `true` to force deletion even if there are dependencies (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.CategoriesAPI.DeleteCategory(context.Background(), id).Force(force).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CategoriesAPI.DeleteCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the category to delete | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **force** | **bool** | Set to &#x60;true&#x60; to force deletion even if there are dependencies | [default to false]

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


## GetAllCategories

> GetAllCategories200Response GetAllCategories(ctx).Format(format).IsGroup(isGroup).Execute()

Get all categories



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
	format := "format_example" // string | If `nested`, returns top-level categories (either category groups or categories not part of a category group) in alphabetical order. Grouped categories are nested within the category group under the property `children`. A `flattened`, response is similar but it includes grouped categories at the top level.<br/><br/> Categories are sorted by their `order`. When `order` is null, they are listed in alphabetical order below other categories with an `order`. (optional) (default to "nested")
	isGroup := true // bool | If `false`, only categories not part of a category group are returned.<br> If `true`, only category groups are returned.<br> When set, the `format` parameter is ignored. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CategoriesAPI.GetAllCategories(context.Background()).Format(format).IsGroup(isGroup).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CategoriesAPI.GetAllCategories``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllCategories`: GetAllCategories200Response
	fmt.Fprintf(os.Stdout, "Response from `CategoriesAPI.GetAllCategories`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllCategoriesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **string** | If &#x60;nested&#x60;, returns top-level categories (either category groups or categories not part of a category group) in alphabetical order. Grouped categories are nested within the category group under the property &#x60;children&#x60;. A &#x60;flattened&#x60;, response is similar but it includes grouped categories at the top level.&lt;br/&gt;&lt;br/&gt; Categories are sorted by their &#x60;order&#x60;. When &#x60;order&#x60; is null, they are listed in alphabetical order below other categories with an &#x60;order&#x60;. | [default to &quot;nested&quot;]
 **isGroup** | **bool** | If &#x60;false&#x60;, only categories not part of a category group are returned.&lt;br&gt; If &#x60;true&#x60;, only category groups are returned.&lt;br&gt; When set, the &#x60;format&#x60; parameter is ignored. | 

### Return type

[**GetAllCategories200Response**](GetAllCategories200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetCategoryById

> CategoryObject GetCategoryById(ctx, id).Execute()

Get a single category



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
	id := int32(315174) // int32 | ID of the category to retrieve

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CategoriesAPI.GetCategoryById(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CategoriesAPI.GetCategoryById``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCategoryById`: CategoryObject
	fmt.Fprintf(os.Stdout, "Response from `CategoriesAPI.GetCategoryById`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the category to retrieve | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetCategoryByIdRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCategory

> CategoryObject UpdateCategory(ctx, id).UpdateCategoryRequestObject(updateCategoryRequestObject).Execute()

Update an existing category or category group



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
	id := int32(83) // int32 | ID of the category to update
	updateCategoryRequestObject := *openapiclient.NewUpdateCategoryRequestObject() // UpdateCategoryRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.CategoriesAPI.UpdateCategory(context.Background(), id).UpdateCategoryRequestObject(updateCategoryRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CategoriesAPI.UpdateCategory``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateCategory`: CategoryObject
	fmt.Fprintf(os.Stdout, "Response from `CategoriesAPI.UpdateCategory`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **int32** | ID of the category to update | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCategoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateCategoryRequestObject** | [**UpdateCategoryRequestObject**](UpdateCategoryRequestObject.md) |  | 

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

