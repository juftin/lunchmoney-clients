# lunchmoney.CryptoManualApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crypto_manual**](CryptoManualApi.md#create_crypto_manual) | **POST** /crypto/manual | Create a manual crypto balance
[**create_cryptocurrency**](CryptoManualApi.md#create_cryptocurrency) | **POST** /cryptocurrencies | Add a new supported cryptocurrency
[**delete_crypto_manual**](CryptoManualApi.md#delete_crypto_manual) | **DELETE** /crypto/manual/{id} | Delete a manual crypto balance
[**get_all_crypto_manual**](CryptoManualApi.md#get_all_crypto_manual) | **GET** /crypto/manual | Get all manual crypto balances
[**get_all_cryptocurrencies**](CryptoManualApi.md#get_all_cryptocurrencies) | **GET** /cryptocurrencies | Get all supported cryptocurrencies
[**get_crypto_manual_by_id**](CryptoManualApi.md#get_crypto_manual_by_id) | **GET** /crypto/manual/{id} | Get a single manual crypto balance
[**update_crypto_manual**](CryptoManualApi.md#update_crypto_manual) | **PUT** /crypto/manual/{id} | Update a manual crypto balance


# **create_crypto_manual**
> CryptoManualObject create_crypto_manual(create_crypto_manual_request_object)

Create a manual crypto balance

Create a manually managed crypto asset.<br><br>
If `display_name` is `null`, clients may derive one from `institution_name` + `name`.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.create_crypto_manual_request_object import CreateCryptoManualRequestObject
from lunchmoney.models.crypto_manual_object import CryptoManualObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)
    create_crypto_manual_request_object = {"name":"Cold Wallet BTC","balance":"0.852341920145782301","symbol":"btc"} # CreateCryptoManualRequestObject | 

    try:
        # Create a manual crypto balance
        api_response = api_instance.create_crypto_manual(create_crypto_manual_request_object)
        print("The response of CryptoManualApi->create_crypto_manual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->create_crypto_manual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_crypto_manual_request_object** | [**CreateCryptoManualRequestObject**](CreateCryptoManualRequestObject.md)|  | 

### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Manual crypto balance created successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cryptocurrency**
> CryptoCurrencyObject create_cryptocurrency(create_cryptocurrency_request_object)

Add a new supported cryptocurrency

Adds a new cryptocurrency to the supported manual-crypto list.<br><br>
Lunch Money uses [CoinGecko](https://www.coingecko.com/us/coins/ethereum) to convert crypto balances to the user's primary currency. Users add a new supported cryptocurrency by submitting a CoinGecko coin-page URL. The server validates the URL, extracts the id from `/coins/{id}`, checks for an existing supported `coingecko_id`, validates the id against CoinGecko, then confirms the resolved symbol is not already supported before creating the new entry.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.create_cryptocurrency_request_object import CreateCryptocurrencyRequestObject
from lunchmoney.models.crypto_currency_object import CryptoCurrencyObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)
    create_cryptocurrency_request_object = {"coingecko_url":"https://www.coingecko.com/fr/coins/cardano"} # CreateCryptocurrencyRequestObject | 

    try:
        # Add a new supported cryptocurrency
        api_response = api_instance.create_cryptocurrency(create_cryptocurrency_request_object)
        print("The response of CryptoManualApi->create_cryptocurrency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->create_cryptocurrency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cryptocurrency_request_object** | [**CreateCryptocurrencyRequestObject**](CreateCryptocurrencyRequestObject.md)|  | 

### Return type

[**CryptoCurrencyObject**](CryptoCurrencyObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Supported cryptocurrency created successfully |  -  |
**400** | Invalid request body |  -  |
**422** | Request validation failure |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crypto_manual**
> delete_crypto_manual(id, keep_history=keep_history)

Delete a manual crypto balance

Delete a single manually managed crypto asset by ID.<p> If this crypto asset has a balance history, and you do not explicitly set the query parameter`keep_history`, a 422 response will be returned requesting you to explicitly set `keep_history` to `true` or `false`.

### Example

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

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchmoney.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.CryptoManualApi(api_client)
    id = 22001 # int | ID of the manual crypto balance to delete
    keep_history = True # bool | Explicitly set to `true` to preserve balance history, or `false` to remove associated history during deletion. This must be set if the account has a balance history. (optional)

    try:
        # Delete a manual crypto balance
        api_instance.delete_crypto_manual(id, keep_history=keep_history)
    except Exception as e:
        print("Exception when calling CryptoManualApi->delete_crypto_manual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual crypto balance to delete | 
 **keep_history** | **bool**| Explicitly set to &#x60;true&#x60; to preserve balance history, or &#x60;false&#x60; to remove associated history during deletion. This must be set if the account has a balance history. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content. The crypto asset has been deleted. |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_crypto_manual**
> CryptoManualListResponseObject get_all_crypto_manual()

Get all manual crypto balances

Retrieve all manually managed crypto balances associated with the user's account.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_manual_list_response_object import CryptoManualListResponseObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)

    try:
        # Get all manual crypto balances
        api_response = api_instance.get_all_crypto_manual()
        print("The response of CryptoManualApi->get_all_crypto_manual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->get_all_crypto_manual: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CryptoManualListResponseObject**](CryptoManualListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of manual crypto balances |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cryptocurrencies**
> CryptoCurrencyResponseObject get_all_cryptocurrencies()

Get all supported cryptocurrencies

Retrieve the list of cryptocurrencies currently supported for manual tracking.<p>
When creating a new manual crypto balance via `POST /crypto/manual`, the `symbol` you specify must match the `symbol` of one of the entries returned by this endpoint.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_currency_response_object import CryptoCurrencyResponseObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)

    try:
        # Get all supported cryptocurrencies
        api_response = api_instance.get_all_cryptocurrencies()
        print("The response of CryptoManualApi->get_all_cryptocurrencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->get_all_cryptocurrencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CryptoCurrencyResponseObject**](CryptoCurrencyResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported cryptocurrencies |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_manual_by_id**
> CryptoManualObject get_crypto_manual_by_id(id)

Get a single manual crypto balance

Retrieve a single manually managed crypto balance by ID.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_manual_object import CryptoManualObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)
    id = 22001 # int | ID of the manual crypto balance to retrieve

    try:
        # Get a single manual crypto balance
        api_response = api_instance.get_crypto_manual_by_id(id)
        print("The response of CryptoManualApi->get_crypto_manual_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->get_crypto_manual_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual crypto balance to retrieve | 

### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manual crypto balance object |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crypto_manual**
> CryptoManualObject update_crypto_manual(id, update_crypto_manual_request_object)

Update a manual crypto balance

Modify a manually managed crypto balance.<br><br>
You may submit the response from `GET /crypto/manual/{id}` as the request body. System-defined properties are accepted according to the `x-updatable` metadata in the update schema.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_manual_object import CryptoManualObject
from lunchmoney.models.update_crypto_manual_request_object import UpdateCryptoManualRequestObject
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
    api_instance = lunchmoney.CryptoManualApi(api_client)
    id = 22001 # int | ID of the manual crypto balance to update
    update_crypto_manual_request_object = {"balance":"0.900000000000000000"} # UpdateCryptoManualRequestObject | 

    try:
        # Update a manual crypto balance
        api_response = api_instance.update_crypto_manual(id, update_crypto_manual_request_object)
        print("The response of CryptoManualApi->update_crypto_manual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoManualApi->update_crypto_manual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual crypto balance to update | 
 **update_crypto_manual_request_object** | [**UpdateCryptoManualRequestObject**](UpdateCryptoManualRequestObject.md)|  | 

### Return type

[**CryptoManualObject**](CryptoManualObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manual crypto balance updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

