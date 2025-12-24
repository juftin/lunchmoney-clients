# \TransactionsBulkAPI

All URIs are relative to *https://api.lunchmoney.dev/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateNewTransactions**](TransactionsBulkAPI.md#CreateNewTransactions) | **Post** /transactions | Insert one or more transactions.
[**DeleteTransactions**](TransactionsBulkAPI.md#DeleteTransactions) | **Delete** /transactions | Bulk delete existing transactions
[**GetAllTransactions**](TransactionsBulkAPI.md#GetAllTransactions) | **Get** /transactions | Get all transactions
[**UpdateTransactions**](TransactionsBulkAPI.md#UpdateTransactions) | **Put** /transactions | Update multiple transactions



## CreateNewTransactions

> InsertTransactionsResponseObject CreateNewTransactions(ctx).CreateNewTransactionsRequest(createNewTransactionsRequest).Execute()

Insert one or more transactions.



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
	createNewTransactionsRequest := *openapiclient.NewCreateNewTransactionsRequest([]openapiclient.InsertTransactionObject{*openapiclient.NewInsertTransactionObject(time.Now(), openapiclient.insertTransactionObject_amount{Float64: new(float64)})}) // CreateNewTransactionsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsBulkAPI.CreateNewTransactions(context.Background()).CreateNewTransactionsRequest(createNewTransactionsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsBulkAPI.CreateNewTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateNewTransactions`: InsertTransactionsResponseObject
	fmt.Fprintf(os.Stdout, "Response from `TransactionsBulkAPI.CreateNewTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateNewTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createNewTransactionsRequest** | [**CreateNewTransactionsRequest**](CreateNewTransactionsRequest.md) |  | 

### Return type

[**InsertTransactionsResponseObject**](InsertTransactionsResponseObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteTransactions

> DeleteTransactions(ctx).DeleteTransactionsRequest(deleteTransactionsRequest).Execute()

Bulk delete existing transactions



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
	deleteTransactionsRequest := *openapiclient.NewDeleteTransactionsRequest([]int64{int64(123)}) // DeleteTransactionsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TransactionsBulkAPI.DeleteTransactions(context.Background()).DeleteTransactionsRequest(deleteTransactionsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsBulkAPI.DeleteTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiDeleteTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deleteTransactionsRequest** | [**DeleteTransactionsRequest**](DeleteTransactionsRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAllTransactions

> GetAllTransactions200Response GetAllTransactions(ctx).StartDate(startDate).EndDate(endDate).ManualAccountId(manualAccountId).PlaidAccountId(plaidAccountId).RecurringId(recurringId).CategoryId(categoryId).TagId(tagId).IsGroup(isGroup).Status(status).IsPending(isPending).IncludePending(includePending).IncludeMetadata(includeMetadata).IncludeSplitParents(includeSplitParents).IncludeChildren(includeChildren).IncludeFiles(includeFiles).Limit(limit).Offset(offset).Execute()

Get all transactions



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
	startDate := time.Now() // string | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. See `limit`. Required if end_date exists. <br> (optional)
	endDate := time.Now() // string | Denotes the end of the time period you'd like to get transactions for. Required if start_date exists.  (optional)
	manualAccountId := int32(219909) // int32 | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and `plaid_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
	plaidAccountId := int32(119807) // int32 | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and `manual_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
	recurringId := int32(994069) // int32 | Filter transactions to those associated with specified Recurring  Item ID  (optional)
	categoryId := int32(83) // int32 | Filter transactions to those associated with the specified category ID. Will also match category groups.  Set this to 0 to return only un-categorized transactions (optional)
	tagId := int32(56) // int32 | Filter transactions to those that have a tag with the specified Tag ID (optional)
	isGroup := true // bool | Filter by group (returns only transaction groups if `true`) (optional)
	status := "unreviewed" // string | Filter transactions to those with the specified status:<br> - `reviewed`: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic<br> - `unreviewed`: Only transactions that need to be reviewed<br> - `delete_pending`: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. (optional)
	isPending := true // bool | Filter transactions by pending status. Set to `true` to return only pending transactions, or `false` to return only non-pending transactions. When this parameter is set, it takes precedence over `include_pending`. Note: Pending transactions always have a status of `unreviewed`, so when setting this parameter to `true`, either omit the `status` parameter or set it to `unreviewed`.  (optional)
	includePending := true // bool | By default, pending transactions are excluded from results. Set to `true` to include imported transactions with a pending status in the results. This query param is ignored if the `is_pending` query param is also set.  (optional) (default to false)
	includeMetadata := true // bool | By default, custom and plaid metadata are not included in the response.  Set to true if you'd like the returned transactions objects to include any  metadata associated with the transactions. (optional) (default to false)
	includeSplitParents := true // bool | By default, transactions that were split into multiple transactions are not included in the response. Set to true if you'd like the returned transactions objects to include any  transactions that were split into multiple transactions.  Use with caution as this data is normally not exposed after the split transactions are created. (optional) (default to false)
	includeChildren := true // bool | By default, the `children` property is not included in the response. Set to true if you'd like the children property to be populated with the transactions that  make up a transaction group, or, if the `include_split_parents` query param is also set,  the transactions that were split from a parent transaction. (optional) (default to false)
	includeFiles := true // bool | By default, the `files` property is not included in the response. Set to true if you'd like the responses to include a list of of  objects that describe any files attached to the transactions. (optional) (default to false)
	limit := int32(56) // int32 | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a `has_more` attribute set to `true`. See [Pagination](https://alpha.lunchmoney.dev/v2/pagination) (optional) (default to 1000)
	offset := int32(56) // int32 | Sets the offset for the records returned. This is typically set automatically in the header. See [Pagination](https://alpha.lunchmoney.dev/v2/pagination) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsBulkAPI.GetAllTransactions(context.Background()).StartDate(startDate).EndDate(endDate).ManualAccountId(manualAccountId).PlaidAccountId(plaidAccountId).RecurringId(recurringId).CategoryId(categoryId).TagId(tagId).IsGroup(isGroup).Status(status).IsPending(isPending).IncludePending(includePending).IncludeMetadata(includeMetadata).IncludeSplitParents(includeSplitParents).IncludeChildren(includeChildren).IncludeFiles(includeFiles).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsBulkAPI.GetAllTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAllTransactions`: GetAllTransactions200Response
	fmt.Fprintf(os.Stdout, "Response from `TransactionsBulkAPI.GetAllTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetAllTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **string** | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. See &#x60;limit&#x60;. Required if end_date exists. &lt;br&gt; | 
 **endDate** | **string** | Denotes the end of the time period you&#39;d like to get transactions for. Required if start_date exists.  | 
 **manualAccountId** | **int32** | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and &#x60;plaid_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI. | 
 **plaidAccountId** | **int32** | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and &#x60;manual_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI. | 
 **recurringId** | **int32** | Filter transactions to those associated with specified Recurring  Item ID  | 
 **categoryId** | **int32** | Filter transactions to those associated with the specified category ID. Will also match category groups.  Set this to 0 to return only un-categorized transactions | 
 **tagId** | **int32** | Filter transactions to those that have a tag with the specified Tag ID | 
 **isGroup** | **bool** | Filter by group (returns only transaction groups if &#x60;true&#x60;) | 
 **status** | **string** | Filter transactions to those with the specified status:&lt;br&gt; - &#x60;reviewed&#x60;: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic&lt;br&gt; - &#x60;unreviewed&#x60;: Only transactions that need to be reviewed&lt;br&gt; - &#x60;delete_pending&#x60;: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. | 
 **isPending** | **bool** | Filter transactions by pending status. Set to &#x60;true&#x60; to return only pending transactions, or &#x60;false&#x60; to return only non-pending transactions. When this parameter is set, it takes precedence over &#x60;include_pending&#x60;. Note: Pending transactions always have a status of &#x60;unreviewed&#x60;, so when setting this parameter to &#x60;true&#x60;, either omit the &#x60;status&#x60; parameter or set it to &#x60;unreviewed&#x60;.  | 
 **includePending** | **bool** | By default, pending transactions are excluded from results. Set to &#x60;true&#x60; to include imported transactions with a pending status in the results. This query param is ignored if the &#x60;is_pending&#x60; query param is also set.  | [default to false]
 **includeMetadata** | **bool** | By default, custom and plaid metadata are not included in the response.  Set to true if you&#39;d like the returned transactions objects to include any  metadata associated with the transactions. | [default to false]
 **includeSplitParents** | **bool** | By default, transactions that were split into multiple transactions are not included in the response. Set to true if you&#39;d like the returned transactions objects to include any  transactions that were split into multiple transactions.  Use with caution as this data is normally not exposed after the split transactions are created. | [default to false]
 **includeChildren** | **bool** | By default, the &#x60;children&#x60; property is not included in the response. Set to true if you&#39;d like the children property to be populated with the transactions that  make up a transaction group, or, if the &#x60;include_split_parents&#x60; query param is also set,  the transactions that were split from a parent transaction. | [default to false]
 **includeFiles** | **bool** | By default, the &#x60;files&#x60; property is not included in the response. Set to true if you&#39;d like the responses to include a list of of  objects that describe any files attached to the transactions. | [default to false]
 **limit** | **int32** | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a &#x60;has_more&#x60; attribute set to &#x60;true&#x60;. See [Pagination](https://alpha.lunchmoney.dev/v2/pagination) | [default to 1000]
 **offset** | **int32** | Sets the offset for the records returned. This is typically set automatically in the header. See [Pagination](https://alpha.lunchmoney.dev/v2/pagination) | 

### Return type

[**GetAllTransactions200Response**](GetAllTransactions200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateTransactions

> UpdateTransactions200Response UpdateTransactions(ctx).UpdateTransactionsRequest(updateTransactionsRequest).Execute()

Update multiple transactions



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
	updateTransactionsRequest := *openapiclient.NewUpdateTransactionsRequest([]openapiclient.UpdateTransactionsRequestTransactionsInner{*openapiclient.NewUpdateTransactionsRequestTransactionsInner(int64(123))}) // UpdateTransactionsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TransactionsBulkAPI.UpdateTransactions(context.Background()).UpdateTransactionsRequest(updateTransactionsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TransactionsBulkAPI.UpdateTransactions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateTransactions`: UpdateTransactions200Response
	fmt.Fprintf(os.Stdout, "Response from `TransactionsBulkAPI.UpdateTransactions`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateTransactionsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateTransactionsRequest** | [**UpdateTransactionsRequest**](UpdateTransactionsRequest.md) |  | 

### Return type

[**UpdateTransactions200Response**](UpdateTransactions200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

