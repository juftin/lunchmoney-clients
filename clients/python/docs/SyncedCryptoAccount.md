# SyncedCryptoAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System defined unique ID for the synced crypto connection | 
**provider** | **str** | Provider used for the synced crypto connection | 
**status** | **str** | Status of the synced crypto account. If not &#x60;active&#x60;, see the [Knowledge Base](https://support.lunchmoney.app/setup/crypto#why-is-my-synced-crypto-account-showing-not-supported) for details. | 
**created_by_name** | **str** | Name of the user who created the crypto connection | 
**created_at** | **datetime** | Date/time the synced crypto connection was created in ISO 8601 extended format | 
**updated_at** | **datetime** | Date/time the synced crypto connection was last updated in ISO 8601 extended format | 
**last_import** | **datetime** | System defined timestamp in ISO 8601 extended format of the last successful import. | [optional] 
**display_name** | **str** | Optional display name for the synced crypto connection | 
**balances** | [**List[CryptoSyncedBalance]**](CryptoSyncedBalance.md) | Balances currently held in the synced crypto connection | 

## Example

```python
from lunchmoney.models.synced_crypto_account import SyncedCryptoAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SyncedCryptoAccount from a JSON string
synced_crypto_account_instance = SyncedCryptoAccount.from_json(json)
# print the JSON string representation of the object
print(SyncedCryptoAccount.to_json())

# convert the object into a dict
synced_crypto_account_dict = synced_crypto_account_instance.to_dict()
# create an instance of SyncedCryptoAccount from a dict
synced_crypto_account_from_dict = SyncedCryptoAccount.from_dict(synced_crypto_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


