# PlaidAccountObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | The unique identifier of this account | 
**PlaidItemId** | **NullableString** | The unique identifier of the Plaid connection that this account belongs to. Accounts with the same plaid_item_id usually belong to the same institution. | 
**DateLinked** | **string** | Date account was first linked in ISO 8601 format | 
**LinkedByName** | **string** | The name of the user who linked the account | 
**Name** | **string** | Name of the account. This field is set by Plaid and cannot be altered. | 
**DisplayName** | **NullableString** | Optional display name for the account set by the user. If not set, it will return a concatenated string of institution and account name. | 
**Type** | **string** | Primary type of the account, such as &#x60;credit&#x60;, &#x60;depository&#x60;, etc. This field is set by Plaid and cannot be altered. | 
**Subtype** | **string** | Optional account subtype. This field is set by Plaid and cannot be altered. | 
**Mask** | **string** | Mask (last 3 to 4 digits of account) of account. This field is set by Plaid and cannot be altered. | 
**InstitutionName** | **string** | Name of institution holding the account. This field is set by Plaid and cannot be altered. | 
**Status** | **string** | Denotes the current status of the account within Lunch Money. Must be one of&lt;br&gt; - active: Account is actively syncing transactions and/or balance&lt;br&gt; - inactive: Account marked inactive from user. Transaction imports and balance updates will not occur for this account.&lt;br&gt; - closed: Account is marked as closed&lt;br&gt; - deactivated: Account is marked deactivated during setup. The user must click &#x60;Add/Remove Accounts From This Bank&#x60; and manually re-select this account to activate it.&#39;&lt;br&gt; - not found: Account was once linked but can no longer be found with Plaid.&lt;br&gt; - not supported: Account is not supported by Plaid.&lt;br&gt; - relink: Account (and others with the same connection) need to be relinked with Plaid.&lt;br&gt; - syncing: Account is awaiting the first import of transactions.&lt;br&gt; - revoked: Account connection has been revoked by Plaid and syncing is no longer possible. A new connection needs to be set up again.&lt;br&gt; - error: Account (and others with the same connection) is in error with Plaid and requires intervention to re-activate it.&lt;br&gt; | 
**AllowTransactionModifications** | **bool** | If &#x60;false&#x60;, transactions imported for this synced account can have their properties (such as amount and account) be modified by the user. This option is managed in the web app. | 
**Limit** | **NullableFloat32** | Optional credit limit of the account. This field is set by Plaid and cannot be altered | 
**Balance** | **string** | Current balance of the account in numeric format to 4 decimal places. This field is set by Plaid and cannot be altered. | 
**Currency** | **string** | Three-letter lowercase currency code of the account balance | 
**ToBase** | **float32** | The account balance converted to the user&#39;s primary currency | 
**BalanceLastUpdate** | **NullableTime** | Date balance was last updated in ISO 8601 extended format. This field is set by Plaid and cannot be altered. | 
**ImportStartDate** | **NullableString** | Date of earliest date allowed for importing transactions. Transactions earlier than this date are not imported. | 
**LastImport** | **NullableTime** | Timestamp in ISO 8601 extended format of the last time Lunch Money imported new data from Plaid for this account. | 
**LastFetch** | **NullableTime** | Timestamp in ISO 8601 extended format of the last successful request from Lunch Money for updated data or timestamps from Plaid in ISO 8601 extended format (not necessarily date of last successful import) | 
**PlaidLastSuccessfulUpdate** | **NullableTime** | Timestamp in ISO 8601 extended format of the last time Plaid successfully connected with institution for new transaction updates, regardless of whether any new data was available in the update. | 

## Methods

### NewPlaidAccountObject

`func NewPlaidAccountObject(id int32, plaidItemId NullableString, dateLinked string, linkedByName string, name string, displayName NullableString, type_ string, subtype string, mask string, institutionName string, status string, allowTransactionModifications bool, limit NullableFloat32, balance string, currency string, toBase float32, balanceLastUpdate NullableTime, importStartDate NullableString, lastImport NullableTime, lastFetch NullableTime, plaidLastSuccessfulUpdate NullableTime, ) *PlaidAccountObject`

NewPlaidAccountObject instantiates a new PlaidAccountObject object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlaidAccountObjectWithDefaults

`func NewPlaidAccountObjectWithDefaults() *PlaidAccountObject`

NewPlaidAccountObjectWithDefaults instantiates a new PlaidAccountObject object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PlaidAccountObject) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PlaidAccountObject) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PlaidAccountObject) SetId(v int32)`

SetId sets Id field to given value.


### GetPlaidItemId

`func (o *PlaidAccountObject) GetPlaidItemId() string`

GetPlaidItemId returns the PlaidItemId field if non-nil, zero value otherwise.

### GetPlaidItemIdOk

`func (o *PlaidAccountObject) GetPlaidItemIdOk() (*string, bool)`

GetPlaidItemIdOk returns a tuple with the PlaidItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidItemId

`func (o *PlaidAccountObject) SetPlaidItemId(v string)`

SetPlaidItemId sets PlaidItemId field to given value.


### SetPlaidItemIdNil

`func (o *PlaidAccountObject) SetPlaidItemIdNil(b bool)`

 SetPlaidItemIdNil sets the value for PlaidItemId to be an explicit nil

### UnsetPlaidItemId
`func (o *PlaidAccountObject) UnsetPlaidItemId()`

UnsetPlaidItemId ensures that no value is present for PlaidItemId, not even an explicit nil
### GetDateLinked

`func (o *PlaidAccountObject) GetDateLinked() string`

GetDateLinked returns the DateLinked field if non-nil, zero value otherwise.

### GetDateLinkedOk

`func (o *PlaidAccountObject) GetDateLinkedOk() (*string, bool)`

GetDateLinkedOk returns a tuple with the DateLinked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDateLinked

`func (o *PlaidAccountObject) SetDateLinked(v string)`

SetDateLinked sets DateLinked field to given value.


### GetLinkedByName

`func (o *PlaidAccountObject) GetLinkedByName() string`

GetLinkedByName returns the LinkedByName field if non-nil, zero value otherwise.

### GetLinkedByNameOk

`func (o *PlaidAccountObject) GetLinkedByNameOk() (*string, bool)`

GetLinkedByNameOk returns a tuple with the LinkedByName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedByName

`func (o *PlaidAccountObject) SetLinkedByName(v string)`

SetLinkedByName sets LinkedByName field to given value.


### GetName

`func (o *PlaidAccountObject) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PlaidAccountObject) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PlaidAccountObject) SetName(v string)`

SetName sets Name field to given value.


### GetDisplayName

`func (o *PlaidAccountObject) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *PlaidAccountObject) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *PlaidAccountObject) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### SetDisplayNameNil

`func (o *PlaidAccountObject) SetDisplayNameNil(b bool)`

 SetDisplayNameNil sets the value for DisplayName to be an explicit nil

### UnsetDisplayName
`func (o *PlaidAccountObject) UnsetDisplayName()`

UnsetDisplayName ensures that no value is present for DisplayName, not even an explicit nil
### GetType

`func (o *PlaidAccountObject) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *PlaidAccountObject) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *PlaidAccountObject) SetType(v string)`

SetType sets Type field to given value.


### GetSubtype

`func (o *PlaidAccountObject) GetSubtype() string`

GetSubtype returns the Subtype field if non-nil, zero value otherwise.

### GetSubtypeOk

`func (o *PlaidAccountObject) GetSubtypeOk() (*string, bool)`

GetSubtypeOk returns a tuple with the Subtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubtype

`func (o *PlaidAccountObject) SetSubtype(v string)`

SetSubtype sets Subtype field to given value.


### GetMask

`func (o *PlaidAccountObject) GetMask() string`

GetMask returns the Mask field if non-nil, zero value otherwise.

### GetMaskOk

`func (o *PlaidAccountObject) GetMaskOk() (*string, bool)`

GetMaskOk returns a tuple with the Mask field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMask

`func (o *PlaidAccountObject) SetMask(v string)`

SetMask sets Mask field to given value.


### GetInstitutionName

`func (o *PlaidAccountObject) GetInstitutionName() string`

GetInstitutionName returns the InstitutionName field if non-nil, zero value otherwise.

### GetInstitutionNameOk

`func (o *PlaidAccountObject) GetInstitutionNameOk() (*string, bool)`

GetInstitutionNameOk returns a tuple with the InstitutionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstitutionName

`func (o *PlaidAccountObject) SetInstitutionName(v string)`

SetInstitutionName sets InstitutionName field to given value.


### GetStatus

`func (o *PlaidAccountObject) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PlaidAccountObject) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PlaidAccountObject) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetAllowTransactionModifications

`func (o *PlaidAccountObject) GetAllowTransactionModifications() bool`

GetAllowTransactionModifications returns the AllowTransactionModifications field if non-nil, zero value otherwise.

### GetAllowTransactionModificationsOk

`func (o *PlaidAccountObject) GetAllowTransactionModificationsOk() (*bool, bool)`

GetAllowTransactionModificationsOk returns a tuple with the AllowTransactionModifications field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAllowTransactionModifications

`func (o *PlaidAccountObject) SetAllowTransactionModifications(v bool)`

SetAllowTransactionModifications sets AllowTransactionModifications field to given value.


### GetLimit

`func (o *PlaidAccountObject) GetLimit() float32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *PlaidAccountObject) GetLimitOk() (*float32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *PlaidAccountObject) SetLimit(v float32)`

SetLimit sets Limit field to given value.


### SetLimitNil

`func (o *PlaidAccountObject) SetLimitNil(b bool)`

 SetLimitNil sets the value for Limit to be an explicit nil

### UnsetLimit
`func (o *PlaidAccountObject) UnsetLimit()`

UnsetLimit ensures that no value is present for Limit, not even an explicit nil
### GetBalance

`func (o *PlaidAccountObject) GetBalance() string`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *PlaidAccountObject) GetBalanceOk() (*string, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *PlaidAccountObject) SetBalance(v string)`

SetBalance sets Balance field to given value.


### GetCurrency

`func (o *PlaidAccountObject) GetCurrency() string`

GetCurrency returns the Currency field if non-nil, zero value otherwise.

### GetCurrencyOk

`func (o *PlaidAccountObject) GetCurrencyOk() (*string, bool)`

GetCurrencyOk returns a tuple with the Currency field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrency

`func (o *PlaidAccountObject) SetCurrency(v string)`

SetCurrency sets Currency field to given value.


### GetToBase

`func (o *PlaidAccountObject) GetToBase() float32`

GetToBase returns the ToBase field if non-nil, zero value otherwise.

### GetToBaseOk

`func (o *PlaidAccountObject) GetToBaseOk() (*float32, bool)`

GetToBaseOk returns a tuple with the ToBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToBase

`func (o *PlaidAccountObject) SetToBase(v float32)`

SetToBase sets ToBase field to given value.


### GetBalanceLastUpdate

`func (o *PlaidAccountObject) GetBalanceLastUpdate() time.Time`

GetBalanceLastUpdate returns the BalanceLastUpdate field if non-nil, zero value otherwise.

### GetBalanceLastUpdateOk

`func (o *PlaidAccountObject) GetBalanceLastUpdateOk() (*time.Time, bool)`

GetBalanceLastUpdateOk returns a tuple with the BalanceLastUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalanceLastUpdate

`func (o *PlaidAccountObject) SetBalanceLastUpdate(v time.Time)`

SetBalanceLastUpdate sets BalanceLastUpdate field to given value.


### SetBalanceLastUpdateNil

`func (o *PlaidAccountObject) SetBalanceLastUpdateNil(b bool)`

 SetBalanceLastUpdateNil sets the value for BalanceLastUpdate to be an explicit nil

### UnsetBalanceLastUpdate
`func (o *PlaidAccountObject) UnsetBalanceLastUpdate()`

UnsetBalanceLastUpdate ensures that no value is present for BalanceLastUpdate, not even an explicit nil
### GetImportStartDate

`func (o *PlaidAccountObject) GetImportStartDate() string`

GetImportStartDate returns the ImportStartDate field if non-nil, zero value otherwise.

### GetImportStartDateOk

`func (o *PlaidAccountObject) GetImportStartDateOk() (*string, bool)`

GetImportStartDateOk returns a tuple with the ImportStartDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImportStartDate

`func (o *PlaidAccountObject) SetImportStartDate(v string)`

SetImportStartDate sets ImportStartDate field to given value.


### SetImportStartDateNil

`func (o *PlaidAccountObject) SetImportStartDateNil(b bool)`

 SetImportStartDateNil sets the value for ImportStartDate to be an explicit nil

### UnsetImportStartDate
`func (o *PlaidAccountObject) UnsetImportStartDate()`

UnsetImportStartDate ensures that no value is present for ImportStartDate, not even an explicit nil
### GetLastImport

`func (o *PlaidAccountObject) GetLastImport() time.Time`

GetLastImport returns the LastImport field if non-nil, zero value otherwise.

### GetLastImportOk

`func (o *PlaidAccountObject) GetLastImportOk() (*time.Time, bool)`

GetLastImportOk returns a tuple with the LastImport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastImport

`func (o *PlaidAccountObject) SetLastImport(v time.Time)`

SetLastImport sets LastImport field to given value.


### SetLastImportNil

`func (o *PlaidAccountObject) SetLastImportNil(b bool)`

 SetLastImportNil sets the value for LastImport to be an explicit nil

### UnsetLastImport
`func (o *PlaidAccountObject) UnsetLastImport()`

UnsetLastImport ensures that no value is present for LastImport, not even an explicit nil
### GetLastFetch

`func (o *PlaidAccountObject) GetLastFetch() time.Time`

GetLastFetch returns the LastFetch field if non-nil, zero value otherwise.

### GetLastFetchOk

`func (o *PlaidAccountObject) GetLastFetchOk() (*time.Time, bool)`

GetLastFetchOk returns a tuple with the LastFetch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastFetch

`func (o *PlaidAccountObject) SetLastFetch(v time.Time)`

SetLastFetch sets LastFetch field to given value.


### SetLastFetchNil

`func (o *PlaidAccountObject) SetLastFetchNil(b bool)`

 SetLastFetchNil sets the value for LastFetch to be an explicit nil

### UnsetLastFetch
`func (o *PlaidAccountObject) UnsetLastFetch()`

UnsetLastFetch ensures that no value is present for LastFetch, not even an explicit nil
### GetPlaidLastSuccessfulUpdate

`func (o *PlaidAccountObject) GetPlaidLastSuccessfulUpdate() time.Time`

GetPlaidLastSuccessfulUpdate returns the PlaidLastSuccessfulUpdate field if non-nil, zero value otherwise.

### GetPlaidLastSuccessfulUpdateOk

`func (o *PlaidAccountObject) GetPlaidLastSuccessfulUpdateOk() (*time.Time, bool)`

GetPlaidLastSuccessfulUpdateOk returns a tuple with the PlaidLastSuccessfulUpdate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlaidLastSuccessfulUpdate

`func (o *PlaidAccountObject) SetPlaidLastSuccessfulUpdate(v time.Time)`

SetPlaidLastSuccessfulUpdate sets PlaidLastSuccessfulUpdate field to given value.


### SetPlaidLastSuccessfulUpdateNil

`func (o *PlaidAccountObject) SetPlaidLastSuccessfulUpdateNil(b bool)`

 SetPlaidLastSuccessfulUpdateNil sets the value for PlaidLastSuccessfulUpdate to be an explicit nil

### UnsetPlaidLastSuccessfulUpdate
`func (o *PlaidAccountObject) UnsetPlaidLastSuccessfulUpdate()`

UnsetPlaidLastSuccessfulUpdate ensures that no value is present for PlaidLastSuccessfulUpdate, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


