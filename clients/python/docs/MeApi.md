# lunchmoney.MeApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_settings**](MeApi.md#get_account_settings) | **GET** /me/account/settings | Get account settings
[**get_me**](MeApi.md#get_me) | **GET** /me | Get current user
[**get_user_account_settings**](MeApi.md#get_user_account_settings) | **GET** /me/user/account/settings | Get user account settings
[**get_user_settings**](MeApi.md#get_user_settings) | **GET** /me/user/settings | Get user settings
[**update_account_settings**](MeApi.md#update_account_settings) | **PUT** /me/account/settings | Update account settings
[**update_user_account_settings**](MeApi.md#update_user_account_settings) | **PUT** /me/user/account/settings | Update user account settings
[**update_user_settings**](MeApi.md#update_user_settings) | **PUT** /me/user/settings | Update user settings


# **get_account_settings**
> AccountSettingsObject get_account_settings()

Get account settings

Returns settings for the current budgeting account. These settings apply regardless of which user is accessing the account.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.account_settings_object import AccountSettingsObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)

    try:
        # Get account settings
        api_response = api_instance.get_account_settings()
        print("The response of MeApi->get_account_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_account_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountSettingsObject**](AccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account settings for the current budgeting account |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> UserObject get_me()

Get current user

Get details about the user associated with the supplied authorization
token.<p> Use [/me/user/settings](#tag/me/GET/me/user/settings) for
user-wide preferences,
[/me/account/settings](#tag/me/GET/me/account/settings) for account-wide
preferences, and
[/me/user/account/settings](#tag/me/GET/me/user/account/settings) for
preferences specific to the current user and budgeting account.
Properties such as `primary_currency` and `budget_name` remain on this
response for backwards compatibility.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.user_object import UserObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)

    try:
        # Get current user
        api_response = api_instance.get_me()
        print("The response of MeApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserObject**](UserObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The User Object associated with the authorized token. |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_account_settings**
> UserAccountSettingsObject get_user_account_settings()

Get user account settings

Returns settings specific to the authorized user within the current budgeting account. These settings do not affect other users or the authorized user's settings in other budgeting accounts.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.user_account_settings_object import UserAccountSettingsObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)

    try:
        # Get user account settings
        api_response = api_instance.get_user_account_settings()
        print("The response of MeApi->get_user_account_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_user_account_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserAccountSettingsObject**](UserAccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings for the authorized user in the current budgeting account |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings**
> UserSettingsObject get_user_settings()

Get user settings

Returns display and formatting preferences for the authorized user. These settings apply across every budgeting account the user owns or collaborates on.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.user_settings_object import UserSettingsObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)

    try:
        # Get user settings
        api_response = api_instance.get_user_settings()
        print("The response of MeApi->get_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_user_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserSettingsObject**](UserSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User settings for the authorized user |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_settings**
> AccountSettingsObject update_account_settings(update_account_settings_request_object)

Update account settings

Updates account-level settings for the budgeting account
associated with the authorized API token. Submit the full response from
`GET /me/account/settings` with one or more properties changed, or
provide only the properties to update. The request body must include at
least one property.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.account_settings_object import AccountSettingsObject
from lunchmoney.models.update_account_settings_request_object import UpdateAccountSettingsRequestObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)
    update_account_settings_request_object = {"display_name":"Travel budget"} # UpdateAccountSettingsRequestObject | 

    try:
        # Update account settings
        api_response = api_instance.update_account_settings(update_account_settings_request_object)
        print("The response of MeApi->update_account_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->update_account_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_account_settings_request_object** | [**UpdateAccountSettingsRequestObject**](UpdateAccountSettingsRequestObject.md)|  | 

### Return type

[**AccountSettingsObject**](AccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account settings updated successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_account_settings**
> UserAccountSettingsObject update_user_account_settings(update_user_account_settings_request_object)

Update user account settings

Updates settings specific to the authorized user within the current
budgeting account. Submit the full response from
`GET /me/user/account/settings` with one or more properties changed, or
provide only the properties to update. The request body must include at
least one property.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.update_user_account_settings_request_object import UpdateUserAccountSettingsRequestObject
from lunchmoney.models.user_account_settings_object import UserAccountSettingsObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)
    update_user_account_settings_request_object = {"auto_review_transaction_on_creation":false} # UpdateUserAccountSettingsRequestObject | 

    try:
        # Update user account settings
        api_response = api_instance.update_user_account_settings(update_user_account_settings_request_object)
        print("The response of MeApi->update_user_account_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->update_user_account_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_account_settings_request_object** | [**UpdateUserAccountSettingsRequestObject**](UpdateUserAccountSettingsRequestObject.md)|  | 

### Return type

[**UserAccountSettingsObject**](UserAccountSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User account settings updated successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_settings**
> UserSettingsObject update_user_settings(update_user_settings_request_object)

Update user settings

Updates user-level display and formatting preferences for the user
associated with the authorized API token. Submit the full response from
`GET /me/user/settings` with one or more properties changed, or provide
only the properties to update. The request body must include at least
one property.<p> Updating
`show_debits_as_negative` affects display in the Lunch Money app only.
Amount fields in API responses always use positive values for debits and
negative values for credits.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.update_user_settings_request_object import UpdateUserSettingsRequestObject
from lunchmoney.models.user_settings_object import UserSettingsObject
from lunchmoney.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lunchmoney.dev/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchmoney.Configuration(
    host = "https://api.lunchmoney.dev/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.MeApi(api_client)
    update_user_settings_request_object = {"month_year_format":"YYYY-MM","month_day_year_format":"YYYY-MM-DD","month_day_format":"MM-DD"} # UpdateUserSettingsRequestObject | 

    try:
        # Update user settings
        api_response = api_instance.update_user_settings(update_user_settings_request_object)
        print("The response of MeApi->update_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->update_user_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_settings_request_object** | [**UpdateUserSettingsRequestObject**](UpdateUserSettingsRequestObject.md)|  | 

### Return type

[**UserSettingsObject**](UserSettingsObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User settings updated successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

