# lunchmoney.CryptoSyncedApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_crypto_synced**](CryptoSyncedApi.md#get_all_crypto_synced) | **GET** /crypto/synced | Get all synced crypto accounts
[**get_crypto_synced_balance_by_symbol**](CryptoSyncedApi.md#get_crypto_synced_balance_by_symbol) | **GET** /crypto/synced/{id}/{symbol} | Get a synced crypto balance by symbol
[**get_crypto_synced_by_id**](CryptoSyncedApi.md#get_crypto_synced_by_id) | **GET** /crypto/synced/{id} | Get a single synced crypto account
[**refresh_crypto_synced**](CryptoSyncedApi.md#refresh_crypto_synced) | **POST** /crypto/synced/{id}/refresh | Refresh balances for a synced crypto account


# **get_all_crypto_synced**
> CryptoSyncedListResponseObject get_all_crypto_synced()

Get all synced crypto accounts

Retrieves all synced crypto accounts associated with the user's account.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_synced_list_response_object import CryptoSyncedListResponseObject
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
    api_instance = lunchmoney.CryptoSyncedApi(api_client)

    try:
        # Get all synced crypto accounts
        api_response = api_instance.get_all_crypto_synced()
        print("The response of CryptoSyncedApi->get_all_crypto_synced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoSyncedApi->get_all_crypto_synced: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CryptoSyncedListResponseObject**](CryptoSyncedListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of synced crypto accounts |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_synced_balance_by_symbol**
> CryptoSyncedBalance get_crypto_synced_balance_by_symbol(id, symbol)

Get a synced crypto balance by symbol

Retrieves a single balance from the specified synced crypto account using the crypto symbol.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.crypto_synced_balance import CryptoSyncedBalance
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
    api_instance = lunchmoney.CryptoSyncedApi(api_client)
    id = 56 # int | Synced crypto account ID
    symbol = 'symbol_example' # str | Crypto symbol within the synced account

    try:
        # Get a synced crypto balance by symbol
        api_response = api_instance.get_crypto_synced_balance_by_symbol(id, symbol)
        print("The response of CryptoSyncedApi->get_crypto_synced_balance_by_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoSyncedApi->get_crypto_synced_balance_by_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Synced crypto account ID | 
 **symbol** | **str**| Crypto symbol within the synced account | 

### Return type

[**CryptoSyncedBalance**](CryptoSyncedBalance.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synced crypto balance object |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_synced_by_id**
> SyncedCryptoAccount get_crypto_synced_by_id(id)

Get a single synced crypto account

Retrieves the synced crypto account and all nested balances for the specified synced crypto account ID.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.synced_crypto_account import SyncedCryptoAccount
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
    api_instance = lunchmoney.CryptoSyncedApi(api_client)
    id = 33004 # int | Synced crypto account ID

    try:
        # Get a single synced crypto account
        api_response = api_instance.get_crypto_synced_by_id(id)
        print("The response of CryptoSyncedApi->get_crypto_synced_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoSyncedApi->get_crypto_synced_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Synced crypto account ID | 

### Return type

[**SyncedCryptoAccount**](SyncedCryptoAccount.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synced crypto account object |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_crypto_synced**
> SyncedCryptoAccount refresh_crypto_synced(id)

Refresh balances for a synced crypto account

Trigger a balance refresh for the specified synced crypto account. Returns the refreshed synced crypto account.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.synced_crypto_account import SyncedCryptoAccount
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
    api_instance = lunchmoney.CryptoSyncedApi(api_client)
    id = 33004 # int | Synced crypto account ID

    try:
        # Refresh balances for a synced crypto account
        api_response = api_instance.refresh_crypto_synced(id)
        print("The response of CryptoSyncedApi->refresh_crypto_synced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoSyncedApi->refresh_crypto_synced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Synced crypto account ID | 

### Return type

[**SyncedCryptoAccount**](SyncedCryptoAccount.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refreshed synced crypto account |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

