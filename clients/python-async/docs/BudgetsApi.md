# lunchmoney.BudgetsApi

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_budget**](BudgetsApi.md#delete_budget) | **DELETE** /budgets | Delete budget
[**get_budget_settings**](BudgetsApi.md#get_budget_settings) | **GET** /budgets/settings | Get budget period settings
[**upsert_budget**](BudgetsApi.md#upsert_budget) | **PUT** /budgets | Upsert budget


# **delete_budget**
> delete_budget(category_id, start_date)

Delete budget

Removes the budget for the given category and period. If there already is no budget set for that period, the request still succeeds (idempotent).<p> Note that `start_date` **must** be a valid budget period start for the account (based on the account's budget period settings). If an invalid `start_date` is provided, the request will fail with an error that indicates what the previous and next valid start dates are.<p> Use the [/budgets/settings](#tag/budgets/GET/budgets/settings) endpoint to view the account's budget settings.<br> To view details for existing budgets, use the [summary](#tag/summary) endpoint.

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
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.BudgetsApi(api_client)
    category_id = 56 # int | Category ID of the budget to delete
    start_date = '2013-10-20' # date | Start date of the budget period in ISO 8601 date format (YYYY-MM-DD)

    try:
        # Delete budget
        await api_instance.delete_budget(category_id, start_date)
    except Exception as e:
        print("Exception when calling BudgetsApi->delete_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID of the budget to delete | 
 **start_date** | **date**| Start date of the budget period in ISO 8601 date format (YYYY-MM-DD) | 

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
**204** | Budget deleted (or no budget existed for the given category and period) |  -  |
**400** | Bad Request (invalid period start, invalid category, or validation failure) |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_settings**
> BudgetSettingsResponseObject get_budget_settings()

Get budget period settings

Returns budget period and display settings for the budget
associated with this API token.<p> These control how budget **periods** are calculated
(granularity, anchor date, rollover, and related options).

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.budget_settings_response_object import BudgetSettingsResponseObject
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
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.BudgetsApi(api_client)

    try:
        # Get budget period settings
        api_response = await api_instance.get_budget_settings()
        print("The response of BudgetsApi->get_budget_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BudgetSettingsResponseObject**](BudgetSettingsResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget period settings for the current budget |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_budget**
> BudgetUpsertResponseObject upsert_budget(upsert_budget_request_object)

Upsert budget

Create or update a budget for a category and period.<p>
If a budget already exists for the specified `start_date` and `category_id`, the `amount` (and optional `currency` and `notes`) are updated; otherwise a new budget entry is created.<p>

Note that `start_date` **must** be a valid budget period start for the account (based on the account's
budget period settings). If an invalid `start_date` is provided, the request will fail with an error that indicates what the previous and next valid start dates are.<p>

Use the [/budgets/settings](#tag/budgets/GET/budgets/settings) endpoint to view the budget period settings for the account.<br>
To view details for existing budgets, use the [summary](#tag/summary) endpoint.

### Example

* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchmoney
from lunchmoney.models.budget_upsert_response_object import BudgetUpsertResponseObject
from lunchmoney.models.upsert_budget_request_object import UpsertBudgetRequestObject
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
async with lunchmoney.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchmoney.BudgetsApi(api_client)
    upsert_budget_request_object = {"start_date":"2025-01-01","category_id":315177,"amount":500,"currency":"usd","notes":"Monthly groceries"} # UpsertBudgetRequestObject | 

    try:
        # Upsert budget
        api_response = await api_instance.upsert_budget(upsert_budget_request_object)
        print("The response of BudgetsApi->upsert_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->upsert_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_budget_request_object** | [**UpsertBudgetRequestObject**](UpsertBudgetRequestObject.md)|  | 

### Return type

[**BudgetUpsertResponseObject**](BudgetUpsertResponseObject.md)

### Authorization

[bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget upserted successfully |  -  |
**400** | Bad Request (invalid period start, invalid category, or validation failure) |  -  |
**401** | Unauthorized. This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

