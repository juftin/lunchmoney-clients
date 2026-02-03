# lunchmoney.TagsApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create a new tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a tag
[**get_all_tags**](TagsApi.md#get_all_tags) | **GET** /tags | Get All Tags
[**get_tag_by_id**](TagsApi.md#get_tag_by_id) | **GET** /tags/{id} | Get a single tag
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tags/{id} | Update an existing tag


# **create_tag**
> TagObject create_tag(create_tag_request_object)

Create a new tag

Creates a new tag with the given name

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.create_tag_request_object import CreateTagRequestObject
from lunchmoney.models.tag_object import TagObject
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.TagsApi(api_client)
    create_tag_request_object = {"name":"API Created Tag with no description"} # CreateTagRequestObject | 

    try:
        # Create a new tag
        api_response = await api_instance.create_tag(create_tag_request_object)
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request_object** | [**CreateTagRequestObject**](CreateTagRequestObject.md)|  | 

### Return type

[**TagObject**](TagObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag Object with the successfully created tag |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(id, force=force)

Delete a tag

Deletes the tag with the ID specified on the path.<br>
If transaction or rules exist with the tag a dependents object is returned and the tag is not deleted. This behavior can be overridden by setting the `force` param to `true`.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.TagsApi(api_client)
    id = 94319 # int | ID of the tag to delete
    force = False # bool | Set to true to force deletion even if there are dependencies (optional) (default to False)

    try:
        # Delete a tag
        await api_instance.delete_tag(id, force=force)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the tag to delete | 
 **force** | **bool**| Set to true to force deletion even if there are dependencies | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> GetAllTags200Response get_all_tags()

Get All Tags

Retrieve a list of all tags associated with the user's account.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.get_all_tags200_response import GetAllTags200Response
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.TagsApi(api_client)

    try:
        # Get All Tags
        api_response = await api_instance.get_all_tags()
        print("The response of TagsApi->get_all_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_all_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllTags200Response**](GetAllTags200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of tags |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> TagObject get_tag_by_id(id)

Get a single tag

Retrieve the details of a specific tag with the specified ID.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.tag_object import TagObject
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.TagsApi(api_client)
    id = 94319 # int | ID of the tag to retrieve

    try:
        # Get a single tag
        api_response = await api_instance.get_tag_by_id(id)
        print("The response of TagsApi->get_tag_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the tag to retrieve | 

### Return type

[**TagObject**](TagObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag Object with the requested Tag ID |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> TagObject update_tag(id, update_tag_request_object)

Update an existing tag

Updates an existing tag.<br><br>
You may submit the response from a `GET /tags/{id}` as the request body, however only certain properties can be updated using this API. The following system set properties are accepted in the request body but their values will be ignored: `id`, `updated_at`, `created_at`, and `archived_at`.<br><br>
It is also possible to provide only the properties to be updated in the request body, as long as the request includes at least one of the properties that is not listed above. For example a request body that contains only a `name` attribute is valid.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.tag_object import TagObject
from lunchmoney.models.update_tag_request_object import UpdateTagRequestObject
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.TagsApi(api_client)
    id = 94319 # int | ID of the tag to update
    update_tag_request_object = {"name":"Updated Tag Name"} # UpdateTagRequestObject | 

    try:
        # Update an existing tag
        api_response = await api_instance.update_tag(id, update_tag_request_object)
        print("The response of TagsApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the tag to update | 
 **update_tag_request_object** | [**UpdateTagRequestObject**](UpdateTagRequestObject.md)|  | 

### Return type

[**TagObject**](TagObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category or Category Group updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

