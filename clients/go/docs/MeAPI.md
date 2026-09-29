# \MeAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAccountSettings**](MeAPI.md#GetAccountSettings) | **Get** /me/account/settings | Get account settings
[**GetMe**](MeAPI.md#GetMe) | **Get** /me | Get current user
[**GetUserAccountSettings**](MeAPI.md#GetUserAccountSettings) | **Get** /me/user/account/settings | Get user account settings
[**GetUserSettings**](MeAPI.md#GetUserSettings) | **Get** /me/user/settings | Get user settings
[**UpdateAccountSettings**](MeAPI.md#UpdateAccountSettings) | **Put** /me/account/settings | Update account settings
[**UpdateUserAccountSettings**](MeAPI.md#UpdateUserAccountSettings) | **Put** /me/user/account/settings | Update user account settings
[**UpdateUserSettings**](MeAPI.md#UpdateUserSettings) | **Put** /me/user/settings | Update user settings



## GetAccountSettings

> AccountSettingsObject GetAccountSettings(ctx).Execute()

Get account settings



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
	resp, r, err := apiClient.MeAPI.GetAccountSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.GetAccountSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAccountSettings`: AccountSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.GetAccountSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetAccountSettingsRequest struct via the builder pattern


### Return type

[**AccountSettingsObject**](AccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetMe

> UserObject GetMe(ctx).Execute()

Get current user



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
	resp, r, err := apiClient.MeAPI.GetMe(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.GetMe``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetMe`: UserObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.GetMe`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetMeRequest struct via the builder pattern


### Return type

[**UserObject**](UserObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUserAccountSettings

> UserAccountSettingsObject GetUserAccountSettings(ctx).Execute()

Get user account settings



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
	resp, r, err := apiClient.MeAPI.GetUserAccountSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.GetUserAccountSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUserAccountSettings`: UserAccountSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.GetUserAccountSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetUserAccountSettingsRequest struct via the builder pattern


### Return type

[**UserAccountSettingsObject**](UserAccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUserSettings

> UserSettingsObject GetUserSettings(ctx).Execute()

Get user settings



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
	resp, r, err := apiClient.MeAPI.GetUserSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.GetUserSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUserSettings`: UserSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.GetUserSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetUserSettingsRequest struct via the builder pattern


### Return type

[**UserSettingsObject**](UserSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAccountSettings

> AccountSettingsObject UpdateAccountSettings(ctx).UpdateAccountSettingsRequestObject(updateAccountSettingsRequestObject).Execute()

Update account settings



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
	updateAccountSettingsRequestObject := *openapiclient.NewUpdateAccountSettingsRequestObject() // UpdateAccountSettingsRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MeAPI.UpdateAccountSettings(context.Background()).UpdateAccountSettingsRequestObject(updateAccountSettingsRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.UpdateAccountSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAccountSettings`: AccountSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.UpdateAccountSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAccountSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateAccountSettingsRequestObject** | [**UpdateAccountSettingsRequestObject**](UpdateAccountSettingsRequestObject.md) |  | 

### Return type

[**AccountSettingsObject**](AccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateUserAccountSettings

> UserAccountSettingsObject UpdateUserAccountSettings(ctx).UpdateUserAccountSettingsRequestObject(updateUserAccountSettingsRequestObject).Execute()

Update user account settings



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
	updateUserAccountSettingsRequestObject := *openapiclient.NewUpdateUserAccountSettingsRequestObject() // UpdateUserAccountSettingsRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MeAPI.UpdateUserAccountSettings(context.Background()).UpdateUserAccountSettingsRequestObject(updateUserAccountSettingsRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.UpdateUserAccountSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateUserAccountSettings`: UserAccountSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.UpdateUserAccountSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateUserAccountSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateUserAccountSettingsRequestObject** | [**UpdateUserAccountSettingsRequestObject**](UpdateUserAccountSettingsRequestObject.md) |  | 

### Return type

[**UserAccountSettingsObject**](UserAccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateUserSettings

> UserSettingsObject UpdateUserSettings(ctx).UpdateUserSettingsRequestObject(updateUserSettingsRequestObject).Execute()

Update user settings



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
	updateUserSettingsRequestObject := *openapiclient.NewUpdateUserSettingsRequestObject() // UpdateUserSettingsRequestObject | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.MeAPI.UpdateUserSettings(context.Background()).UpdateUserSettingsRequestObject(updateUserSettingsRequestObject).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MeAPI.UpdateUserSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateUserSettings`: UserSettingsObject
	fmt.Fprintf(os.Stdout, "Response from `MeAPI.UpdateUserSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateUserSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateUserSettingsRequestObject** | [**UpdateUserSettingsRequestObject**](UpdateUserSettingsRequestObject.md) |  | 

### Return type

[**UserSettingsObject**](UserSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

