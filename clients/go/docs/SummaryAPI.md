# \SummaryAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetBudgetSummary**](SummaryAPI.md#GetBudgetSummary) | **Get** /summary | Get summary



## GetBudgetSummary

> GetBudgetSummary200Response GetBudgetSummary(ctx).StartDate(startDate).EndDate(endDate).IncludeExcludeFromBudgets(includeExcludeFromBudgets).IncludeOccurrences(includeOccurrences).IncludePastBudgetDates(includePastBudgetDates).IncludeTotals(includeTotals).IncludeRolloverPool(includeRolloverPool).Execute()

Get summary



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
	startDate := time.Now() // string | Start of date range in ISO 8601 date format (YYYY-MM-DD).
	endDate := time.Now() // string | End of date range in ISO 8601 date format (YYYY-MM-DD).
	includeExcludeFromBudgets := true // bool | Enable to include categories that have the 'Exclude from Budgets' flag set in the returned `categories` array. (optional) (default to false)
	includeOccurrences := true // bool | Enable to include an `occurrences` array for each category in an aligned response. Each array will include an object for each budget period that falls within the specified date range which includes details on the activity for the budget period. (optional) (default to false)
	includePastBudgetDates := true // bool | Enable to include the three budget occurrences prior to the start date in the `occurrences` array for each category in an aligned response. This property is ignored if `include_occurrences` is not also set to `true`. (optional) (default to false)
	includeTotals := true // bool | Enable to include a top-level `totals` section that summarizes the inflow and outflow across all transactions for the specified date range. (optional) (default to false)
	includeRolloverPool := true // bool | Enable to include a `rollover_pool` section that summarizes the current rollover pool balance and all previous adjustments. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SummaryAPI.GetBudgetSummary(context.Background()).StartDate(startDate).EndDate(endDate).IncludeExcludeFromBudgets(includeExcludeFromBudgets).IncludeOccurrences(includeOccurrences).IncludePastBudgetDates(includePastBudgetDates).IncludeTotals(includeTotals).IncludeRolloverPool(includeRolloverPool).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SummaryAPI.GetBudgetSummary``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetBudgetSummary`: GetBudgetSummary200Response
	fmt.Fprintf(os.Stdout, "Response from `SummaryAPI.GetBudgetSummary`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetBudgetSummaryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **string** | Start of date range in ISO 8601 date format (YYYY-MM-DD). | 
 **endDate** | **string** | End of date range in ISO 8601 date format (YYYY-MM-DD). | 
 **includeExcludeFromBudgets** | **bool** | Enable to include categories that have the &#39;Exclude from Budgets&#39; flag set in the returned &#x60;categories&#x60; array. | [default to false]
 **includeOccurrences** | **bool** | Enable to include an &#x60;occurrences&#x60; array for each category in an aligned response. Each array will include an object for each budget period that falls within the specified date range which includes details on the activity for the budget period. | [default to false]
 **includePastBudgetDates** | **bool** | Enable to include the three budget occurrences prior to the start date in the &#x60;occurrences&#x60; array for each category in an aligned response. This property is ignored if &#x60;include_occurrences&#x60; is not also set to &#x60;true&#x60;. | [default to false]
 **includeTotals** | **bool** | Enable to include a top-level &#x60;totals&#x60; section that summarizes the inflow and outflow across all transactions for the specified date range. | [default to false]
 **includeRolloverPool** | **bool** | Enable to include a &#x60;rollover_pool&#x60; section that summarizes the current rollover pool balance and all previous adjustments. | [default to false]

### Return type

[**GetBudgetSummary200Response**](GetBudgetSummary200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

