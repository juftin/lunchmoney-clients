# lunchmoney.BalanceHistoryApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_balance_history_entry**](BalanceHistoryApi.md#delete_balance_history_entry) | **DELETE** /balance_history/entries/{id} | Delete a balance history entry
[**delete_balance_history_for_account**](BalanceHistoryApi.md#delete_balance_history_for_account) | **DELETE** /balance_history/{account_type}/{account_id} | Delete all balance history for an account
[**delete_balance_history_for_crypto_synced**](BalanceHistoryApi.md#delete_balance_history_for_crypto_synced) | **DELETE** /balance_history/crypto_synced/{account_id}/{symbol} | Delete all balance history for a synced crypto symbol
[**get_balance_history**](BalanceHistoryApi.md#get_balance_history) | **GET** /balance_history | Get balance history
[**get_balance_history_for_account**](BalanceHistoryApi.md#get_balance_history_for_account) | **GET** /balance_history/{account_type}/{account_id} | Get balance history for an account
[**get_balance_history_for_crypto_synced**](BalanceHistoryApi.md#get_balance_history_for_crypto_synced) | **GET** /balance_history/crypto_synced/{account_id}/{symbol} | Get balance history for a synced crypto symbol
[**update_balance_history_details**](BalanceHistoryApi.md#update_balance_history_details) | **PUT** /balance_history/deleted/{account_id}/details | Update details for a deleted account
[**upsert_balance_history_for_account**](BalanceHistoryApi.md#upsert_balance_history_for_account) | **PUT** /balance_history/{account_type}/{account_id} | Upsert balance history for an account
[**upsert_balance_history_for_crypto_synced**](BalanceHistoryApi.md#upsert_balance_history_for_crypto_synced) | **PUT** /balance_history/crypto_synced/{account_id}/{symbol} | Upsert balance history for a synced crypto symbol


# **delete_balance_history_entry**
> delete_balance_history_entry(id)

Delete a balance history entry

Delete a single stored (`type: historical`) monthly balance history entry by its id. Ephemeral `current` entries cannot be deleted this way.

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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    id = 56 # int | Historical balance entry identifier to delete.

    try:
        # Delete a balance history entry
        api_instance.delete_balance_history_entry(id)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->delete_balance_history_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Historical balance entry identifier to delete. | 

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
**204** | The balance history entry was deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balance_history_for_account**
> delete_balance_history_for_account(account_type, account_id)

Delete all balance history for an account

Delete all historical balance entries for a single manual, Plaid, manual crypto, or deleted account. For synced crypto symbol streams, use [DELETE /balance_history/crypto_synced/{account_id}/{symbol}](#tag/balance-history/DELETE/balance_history/crypto_synced/{account_id}/{symbol}).

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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_type = 'account_type_example' # str | Account family to delete. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
    account_id = 56 # int | Account or deleted-source identifier within the selected `account_type`.

    try:
        # Delete all balance history for an account
        api_instance.delete_balance_history_for_account(account_type, account_id)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->delete_balance_history_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| Account family to delete. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
 **account_id** | **int**| Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 

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
**204** | All history for the account/source was deleted |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balance_history_for_crypto_synced**
> delete_balance_history_for_crypto_synced(account_id, symbol)

Delete all balance history for a synced crypto symbol

Delete all historical balance entries for a single synced crypto symbol stream.<br><br>
The path identifies both the synced crypto account and the symbol whose history should be deleted.

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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_id = 56 # int | Synced crypto account identifier.
    symbol = 'symbol_example' # str | Crypto symbol identifying one balance stream within the synced crypto account.

    try:
        # Delete all balance history for a synced crypto symbol
        api_instance.delete_balance_history_for_crypto_synced(account_id, symbol)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->delete_balance_history_for_crypto_synced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Synced crypto account identifier. | 
 **symbol** | **str**| Crypto symbol identifying one balance stream within the synced crypto account. | 

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
**204** | All history for the synced crypto symbol stream was deleted |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history**
> BalanceHistoryListResponseObject get_balance_history(start_month=start_month, end_month=end_month)

Get balance history

Retrieve monthly balance history for all account sources.<br><br>
Balance history is monthly. Each entry represents the account balance at or around the end of the specified month. System-generated entries are generally captured near the boundary between months.<br><br>
Query with optional `start_month` and `end_month` in YYYY-MM format. The range is inclusive. If either parameter is provided, both are required. `start_month` must not be in the future. `end_month` may not be earlier than `start_month` and must not be in the future. Values must be valid calendar months in exact YYYY-MM format. A full date such as `2026-06-01` is invalid. If neither is provided, all available balance history is returned, including an ephemeral `current` entry for the current month when applicable.<br><br>
The response groups entries by source account. Each item in `balance_history` contains a `source` object plus a `balances` array. Within a requested range (or across all history when no range is provided), the array includes only months that have data — months with no data are omitted. A `current` entry is also included when the requested range includes the current month.<br><br>
Each balance entry has a `type`:<br>
- `historical`: stored snapshot of a past month for an active or deleted account. Includes an `id` that can be used with balance history entry endpoints<br>
- `current`: snapshot based on the account's current balances. It is ephemeral and may change between requests. To inspect the underlying account, use the type-specific source id for the `source.type` values:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- `manual`: `source.manual_account_id` with [GET /manual_accounts/{id}](#tag/manual-accounts/GET/manual_accounts/{id})<br>
&nbsp;&nbsp;&nbsp;&nbsp;- `plaid`: `source.plaid_account_id` with [GET /plaid_accounts/{id}](#tag/plaid-accounts/GET/plaid_accounts/{id})<br>
&nbsp;&nbsp;&nbsp;&nbsp;- `crypto_manual`: `source.crypto_manual_id` with [GET /crypto/manual/{id}](#tag/crypto-manual/GET/crypto/manual/{id})<br>
&nbsp;&nbsp;&nbsp;&nbsp;- `crypto_synced`: `source.crypto_synced_id` and `source.symbol` with [GET /crypto/synced/{id}/{symbol}](#tag/crypto-synced/GET/crypto/synced/{id}/{symbol})

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.balance_history_list_response_object import BalanceHistoryListResponseObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    start_month = '2026-01' # str | Optional start of the requested history range as a calendar month in YYYY-MM format (for example `2026-06`). If set, `end_month` is also required. The range is inclusive. `start_month` must not be in the future. A full date such as `2026-06-01` is invalid. (optional)
    end_month = '2026-03' # str | Optional end of the requested history range as a calendar month in YYYY-MM format (for example `2026-06`). If set, `start_month` is also required. The range is inclusive. `end_month` may not be earlier than `start_month` and must not be in the future. A full date such as `2026-06-01` is invalid. For a single month, set this to the same value as `start_month`. (optional)

    try:
        # Get balance history
        api_response = api_instance.get_balance_history(start_month=start_month, end_month=end_month)
        print("The response of BalanceHistoryApi->get_balance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->get_balance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_month** | **str**| Optional start of the requested history range as a calendar month in YYYY-MM format (for example &#x60;2026-06&#x60;). If set, &#x60;end_month&#x60; is also required. The range is inclusive. &#x60;start_month&#x60; must not be in the future. A full date such as &#x60;2026-06-01&#x60; is invalid. | [optional] 
 **end_month** | **str**| Optional end of the requested history range as a calendar month in YYYY-MM format (for example &#x60;2026-06&#x60;). If set, &#x60;start_month&#x60; is also required. The range is inclusive. &#x60;end_month&#x60; may not be earlier than &#x60;start_month&#x60; and must not be in the future. A full date such as &#x60;2026-06-01&#x60; is invalid. For a single month, set this to the same value as &#x60;start_month&#x60;. | [optional] 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monthly balance history for the requested month range |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history_for_account**
> BalanceHistoryListResponseObject get_balance_history_for_account(account_type, account_id, start_month=start_month, end_month=end_month)

Get balance history for an account

Retrieve monthly balance history for one manual, Plaid, manual crypto, or deleted account. For synced crypto symbol streams, use [GET /balance_history/crypto_synced/{account_id}/{symbol}](#tag/balance-history/GET/balance_history/crypto_synced/{account_id}/{symbol}).<br><br>
The `account_type` path parameter identifies the account family (`manual`, `plaid`, `crypto_manual`, or `deleted`) and `account_id` identifies the account within that family.<br><br>
`start_month`, `end_month`, and current-month entries behave as described in [GET /balance_history](#tag/balance-history/GET/balance_history).

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.balance_history_list_response_object import BalanceHistoryListResponseObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_type = 'account_type_example' # str | Account family to retrieve. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
    account_id = 56 # int | Account or deleted-source identifier within the selected `account_type`.
    start_month = 'start_month_example' # str | Optional. Same format and constraints as `start_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)
    end_month = 'end_month_example' # str | Optional. Same format and constraints as `end_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)

    try:
        # Get balance history for an account
        api_response = api_instance.get_balance_history_for_account(account_type, account_id, start_month=start_month, end_month=end_month)
        print("The response of BalanceHistoryApi->get_balance_history_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->get_balance_history_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| Account family to retrieve. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
 **account_id** | **int**| Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 
 **start_month** | **str**| Optional. Same format and constraints as &#x60;start_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | [optional] 
 **end_month** | **str**| Optional. Same format and constraints as &#x60;end_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | [optional] 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monthly balance history for the requested source |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_history_for_crypto_synced**
> BalanceHistoryListResponseObject get_balance_history_for_crypto_synced(account_id, symbol, start_month=start_month, end_month=end_month)

Get balance history for a synced crypto symbol

Retrieve monthly balance history for a single synced crypto symbol stream.<br><br>
The path selects one balance stream with a synced crypto account id and `symbol`.<br><br>
`start_month`, `end_month`, and current-month entries behave as described in [GET /balance_history](#tag/balance-history/GET/balance_history).

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.balance_history_list_response_object import BalanceHistoryListResponseObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_id = 56 # int | Synced crypto account identifier.
    symbol = 'symbol_example' # str | Crypto symbol identifying one balance stream within the synced crypto account.
    start_month = 'start_month_example' # str | Optional. Same format and constraints as `start_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)
    end_month = 'end_month_example' # str | Optional. Same format and constraints as `end_month` on [GET /balance_history](#tag/balance-history/GET/balance_history). (optional)

    try:
        # Get balance history for a synced crypto symbol
        api_response = api_instance.get_balance_history_for_crypto_synced(account_id, symbol, start_month=start_month, end_month=end_month)
        print("The response of BalanceHistoryApi->get_balance_history_for_crypto_synced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->get_balance_history_for_crypto_synced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Synced crypto account identifier. | 
 **symbol** | **str**| Crypto symbol identifying one balance stream within the synced crypto account. | 
 **start_month** | **str**| Optional. Same format and constraints as &#x60;start_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | [optional] 
 **end_month** | **str**| Optional. Same format and constraints as &#x60;end_month&#x60; on [GET /balance_history](#tag/balance-history/GET/balance_history). | [optional] 

### Return type

[**BalanceHistoryListResponseObject**](BalanceHistoryListResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monthly balance history for the synced crypto symbol stream |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_history_details**
> UpdateBalanceHistoryDetailsResponseObject update_balance_history_details(account_id, update_balance_history_details_request_object)

Update details for a deleted account

Update archived metadata for a deleted balance history source.<br><br>
Pass the `deleted_account_id` from a `source.type: deleted` entry. The update applies to all historical entries associated with that deleted source.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.update_balance_history_details_request_object import UpdateBalanceHistoryDetailsRequestObject
from lunchmoney.models.update_balance_history_details_response_object import UpdateBalanceHistoryDetailsResponseObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_id = 56 # int | Deleted account history source identifier to update.
    update_balance_history_details_request_object = {"name":"Savings","institution_name":"Old Bank","display_name":"Old Savings Account","account_type":"savings","subtype":"savings","mask":"1234"} # UpdateBalanceHistoryDetailsRequestObject | 

    try:
        # Update details for a deleted account
        api_response = api_instance.update_balance_history_details(account_id, update_balance_history_details_request_object)
        print("The response of BalanceHistoryApi->update_balance_history_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->update_balance_history_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Deleted account history source identifier to update. | 
 **update_balance_history_details_request_object** | [**UpdateBalanceHistoryDetailsRequestObject**](UpdateBalanceHistoryDetailsRequestObject.md)|  | 

### Return type

[**UpdateBalanceHistoryDetailsResponseObject**](UpdateBalanceHistoryDetailsResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated deleted source details |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_balance_history_for_account**
> BalanceHistoryAccountObject upsert_balance_history_for_account(account_type, account_id, upsert_balance_history_request_object)

Upsert balance history for an account

Upsert one or more historical balance entries for a single manual, Plaid, manual crypto, or deleted account. For synced crypto symbol streams, use [PUT /balance_history/crypto_synced/{account_id}/{symbol}](#tag/balance-history/PUT/balance_history/crypto_synced/{account_id}/{symbol}).<br><br>
The `account_type` path parameter identifies the account family (`manual`, `plaid`, `crypto_manual`, or `deleted`) and `account_id` identifies the account within that family.<br><br>
Submit one or more entries in the `balances` array. Each entry must specify a `month` (YYYY-MM) and `balance` value. `month` must be a past calendar month. The current month cannot be written through this endpoint.<br><br>
`currency` may be provided for any balance entry. If omitted, it defaults to the account currency for manual/Plaid accounts, or the user's primary currency for crypto/deleted accounts.<br><br>
`symbol` may be set for `crypto_manual` (optional) and `deleted` (tolerated) accounts. Do not provide it for `manual` or `plaid` accounts.<br><br>
`crypto_balance` may be provided for `crypto_manual` and `deleted` accounts. It is invalid for `manual` or `plaid` accounts.<br><br>
The response contains only the `type: historical` balance entries that were submitted in this request.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.balance_history_account_object import BalanceHistoryAccountObject
from lunchmoney.models.upsert_balance_history_request_object import UpsertBalanceHistoryRequestObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_type = 'account_type_example' # str | Account family to update. Use `manual`, `plaid`, `crypto_manual`, or `deleted`.
    account_id = 56 # int | Account or deleted-source identifier within the selected `account_type`.
    upsert_balance_history_request_object = {"balances":[{"month":"2026-03","balance":"41500.0000"},{"month":"2026-04","balance":"41625.5000"}]} # UpsertBalanceHistoryRequestObject | 

    try:
        # Upsert balance history for an account
        api_response = api_instance.upsert_balance_history_for_account(account_type, account_id, upsert_balance_history_request_object)
        print("The response of BalanceHistoryApi->upsert_balance_history_for_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->upsert_balance_history_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| Account family to update. Use &#x60;manual&#x60;, &#x60;plaid&#x60;, &#x60;crypto_manual&#x60;, or &#x60;deleted&#x60;. | 
 **account_id** | **int**| Account or deleted-source identifier within the selected &#x60;account_type&#x60;. | 
 **upsert_balance_history_request_object** | [**UpsertBalanceHistoryRequestObject**](UpsertBalanceHistoryRequestObject.md)|  | 

### Return type

[**BalanceHistoryAccountObject**](BalanceHistoryAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns only the &#x60;type: historical&#x60; entries modified by this request. Other historical entries for the account are omitted from &#x60;balances&#x60;. |  -  |
**400** | Bad Request. If any entry in &#x60;balances&#x60; fails validation, the entire request is rejected and no entries are updated. |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_balance_history_for_crypto_synced**
> BalanceHistoryAccountObject upsert_balance_history_for_crypto_synced(account_id, symbol, upsert_balance_history_request_object)

Upsert balance history for a synced crypto symbol

Upsert one or more historical balance entries for a single synced crypto symbol stream.<br><br>
The path identifies both the synced crypto account and the symbol being updated.<br><br>
Submit one or more entries in the `balances` array. Each entry must specify a `month` (YYYY-MM) and `balance` value. `month` must be a past calendar month. The current month cannot be written through this endpoint.<br><br>
The request body may include an optional `symbol` on each balance entry. If provided, it must match the `symbol` path parameter. Omit `symbol` to use the path value.<br><br>
`currency` may be provided for any balance entry. If omitted, it defaults to the user's primary currency for synced crypto balances.<br><br>
`crypto_balance` may be provided for synced crypto balances.<br><br>
The response contains only the `type: historical` balance entries that were submitted in this request.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.balance_history_account_object import BalanceHistoryAccountObject
from lunchmoney.models.upsert_balance_history_request_object import UpsertBalanceHistoryRequestObject
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
    api_instance = lunchmoney.BalanceHistoryApi(api_client)
    account_id = 56 # int | Synced crypto account identifier to update.
    symbol = 'symbol_example' # str | Crypto symbol identifying one balance stream within the synced crypto account.
    upsert_balance_history_request_object = {"balances":[{"month":"2026-03","balance":"6400.0000","crypto_balance":"0.100020003000400050"},{"month":"2026-04","balance":"6500.0000","crypto_balance":"0.100020003000400050"}]} # UpsertBalanceHistoryRequestObject | 

    try:
        # Upsert balance history for a synced crypto symbol
        api_response = api_instance.upsert_balance_history_for_crypto_synced(account_id, symbol, upsert_balance_history_request_object)
        print("The response of BalanceHistoryApi->upsert_balance_history_for_crypto_synced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceHistoryApi->upsert_balance_history_for_crypto_synced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Synced crypto account identifier to update. | 
 **symbol** | **str**| Crypto symbol identifying one balance stream within the synced crypto account. | 
 **upsert_balance_history_request_object** | [**UpsertBalanceHistoryRequestObject**](UpsertBalanceHistoryRequestObject.md)|  | 

### Return type

[**BalanceHistoryAccountObject**](BalanceHistoryAccountObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns only the &#x60;type: historical&#x60; entries modified by this request. Other historical entries for the symbol stream are omitted from &#x60;balances&#x60;. |  -  |
**400** | Bad Request. If any entry in &#x60;balances&#x60; fails validation, the entire request is rejected and no entries are updated. |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

