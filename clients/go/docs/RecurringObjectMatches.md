# RecurringObjectMatches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RequestStartDate** | Pointer to **string** | The beginning of the date range that this request used to find matching transactions. | [optional] 
**RequestEndDate** | Pointer to **string** | The beginning of the date range that this request used to find matching transactions. | [optional] 
**ExpectedOccurrenceDates** | Pointer to **[]string** | A list of dates within the specified range where a recurring transactions is expected. | [optional] 
**FoundTransactions** | Pointer to [**[]RecurringObjectMatchesFoundTransactionsInner**](RecurringObjectMatchesFoundTransactionsInner.md) | A list with the dates and IDs of matching transactions | [optional] 
**MissingTransactionDates** | Pointer to **[]string** | A list of dates within the range of where a recurring transaction was expected but none was found. | [optional] 

## Methods

### NewRecurringObjectMatches

`func NewRecurringObjectMatches() *RecurringObjectMatches`

NewRecurringObjectMatches instantiates a new RecurringObjectMatches object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRecurringObjectMatchesWithDefaults

`func NewRecurringObjectMatchesWithDefaults() *RecurringObjectMatches`

NewRecurringObjectMatchesWithDefaults instantiates a new RecurringObjectMatches object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRequestStartDate

`func (o *RecurringObjectMatches) GetRequestStartDate() string`

GetRequestStartDate returns the RequestStartDate field if non-nil, zero value otherwise.

### GetRequestStartDateOk

`func (o *RecurringObjectMatches) GetRequestStartDateOk() (*string, bool)`

GetRequestStartDateOk returns a tuple with the RequestStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestStartDate

`func (o *RecurringObjectMatches) SetRequestStartDate(v string)`

SetRequestStartDate sets RequestStartDate field to given value.

### HasRequestStartDate

`func (o *RecurringObjectMatches) HasRequestStartDate() bool`

HasRequestStartDate returns a boolean if a field has been set.

### GetRequestEndDate

`func (o *RecurringObjectMatches) GetRequestEndDate() string`

GetRequestEndDate returns the RequestEndDate field if non-nil, zero value otherwise.

### GetRequestEndDateOk

`func (o *RecurringObjectMatches) GetRequestEndDateOk() (*string, bool)`

GetRequestEndDateOk returns a tuple with the RequestEndDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestEndDate

`func (o *RecurringObjectMatches) SetRequestEndDate(v string)`

SetRequestEndDate sets RequestEndDate field to given value.

### HasRequestEndDate

`func (o *RecurringObjectMatches) HasRequestEndDate() bool`

HasRequestEndDate returns a boolean if a field has been set.

### GetExpectedOccurrenceDates

`func (o *RecurringObjectMatches) GetExpectedOccurrenceDates() []string`

GetExpectedOccurrenceDates returns the ExpectedOccurrenceDates field if non-nil, zero value otherwise.

### GetExpectedOccurrenceDatesOk

`func (o *RecurringObjectMatches) GetExpectedOccurrenceDatesOk() (*[]string, bool)`

GetExpectedOccurrenceDatesOk returns a tuple with the ExpectedOccurrenceDates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpectedOccurrenceDates

`func (o *RecurringObjectMatches) SetExpectedOccurrenceDates(v []string)`

SetExpectedOccurrenceDates sets ExpectedOccurrenceDates field to given value.

### HasExpectedOccurrenceDates

`func (o *RecurringObjectMatches) HasExpectedOccurrenceDates() bool`

HasExpectedOccurrenceDates returns a boolean if a field has been set.

### GetFoundTransactions

`func (o *RecurringObjectMatches) GetFoundTransactions() []RecurringObjectMatchesFoundTransactionsInner`

GetFoundTransactions returns the FoundTransactions field if non-nil, zero value otherwise.

### GetFoundTransactionsOk

`func (o *RecurringObjectMatches) GetFoundTransactionsOk() (*[]RecurringObjectMatchesFoundTransactionsInner, bool)`

GetFoundTransactionsOk returns a tuple with the FoundTransactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFoundTransactions

`func (o *RecurringObjectMatches) SetFoundTransactions(v []RecurringObjectMatchesFoundTransactionsInner)`

SetFoundTransactions sets FoundTransactions field to given value.

### HasFoundTransactions

`func (o *RecurringObjectMatches) HasFoundTransactions() bool`

HasFoundTransactions returns a boolean if a field has been set.

### GetMissingTransactionDates

`func (o *RecurringObjectMatches) GetMissingTransactionDates() []string`

GetMissingTransactionDates returns the MissingTransactionDates field if non-nil, zero value otherwise.

### GetMissingTransactionDatesOk

`func (o *RecurringObjectMatches) GetMissingTransactionDatesOk() (*[]string, bool)`

GetMissingTransactionDatesOk returns a tuple with the MissingTransactionDates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMissingTransactionDates

`func (o *RecurringObjectMatches) SetMissingTransactionDates(v []string)`

SetMissingTransactionDates sets MissingTransactionDates field to given value.

### HasMissingTransactionDates

`func (o *RecurringObjectMatches) HasMissingTransactionDates() bool`

HasMissingTransactionDates returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


