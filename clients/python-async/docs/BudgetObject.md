# BudgetObject

A budget object represents a budgeted amount for a specific category and budget period. Each budget entry is tied to a specific time period defined by its `start_date`. The budget object includes information about the budget amount, currency, period settings, and how future periods will be automatically calculated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System created unique identifier for the budget entry. | 
**category_id** | **int** | The ID of the category this budget applies to. | 
**amount** | **float** | The budgeted amount for this period. | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | The currency of the budgeted amount in ISO 4217 format. | 
**start_date** | **date** | The start date of the budget period in ISO 8601 format (YYYY-MM-DD). This represents the beginning of the period for which this budget applies. | 
**next_start_date** | **date** | The calculated start date of the next budget period based on the category&#39;s period settings (granularity, quantity, and anchor_date). This is useful for determining when the next budget period begins. | [readonly] 
**notes** | **str** | Optional notes associated with this budget period. | [optional] 
**auto_budget_type** | **str** | The budget preset type that determines how future periods will be automatically calculated. &#x60;nothing&#x60; means no automatic calculation (budgets must be set manually for each period). &#x60;fixed&#x60; uses a fixed amount for all future periods. &#x60;spend&#x60; uses the previous period&#39;s spending amount. &#x60;budget&#x60; uses the previous period&#39;s budgeted amount. | [readonly] 
**auto_budget_amount** | **float** | If &#x60;auto_budget_type&#x60; is &#x60;fixed&#x60;, this is the fixed amount that will be used for future periods. | [optional] [readonly] 
**auto_budget_currency** | [**CurrencyEnum**](CurrencyEnum.md) | If &#x60;auto_budget_type&#x60; is &#x60;fixed&#x60;, this is the currency of the fixed amount. | [optional] [readonly] 
**rollover_option** | **str** | The rollover setting for this category. &#x60;same category&#x60; means unspent funds roll over to the next period for this category. &#x60;available funds&#x60; means unspent funds are added to the available funds pool. &#x60;null&#x60; means rollover is disabled. | [optional] [readonly] 
**granularity** | **str** | The granularity of the budget period (e.g., monthly, weekly, twice a month). This is determined by the category&#39;s custom budget settings or the account&#39;s default budget period settings. | [readonly] 
**quantity** | **int** | The quantity of granularity units that make up each budget period. For example, if granularity is &#x60;week&#x60; and quantity is &#x60;2&#x60;, each budget period is 2 weeks. | [readonly] 
**is_group** | **bool** | Whether the category is a category group. Category groups can have their own budgets that apply to all subcategories, or subcategories can have individual budgets. | [readonly] 
**group_id** | **int** | If this budget is for a subcategory, this is the ID of the parent category group. &#x60;null&#x60; if this is not a subcategory. | [optional] [readonly] 
**created_at** | **datetime** | The date and time when this budget entry was created (in ISO 8601 extended format). | 
**updated_at** | **datetime** | The date and time when this budget entry was last updated (in ISO 8601 extended format). | 

## Example

```python
from lunchmoney.models.budget_object import BudgetObject

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetObject from a JSON string
budget_object_instance = BudgetObject.from_json(json)
# print the JSON string representation of the object
print(BudgetObject.to_json())

# convert the object into a dict
budget_object_dict = budget_object_instance.to_dict()
# create an instance of BudgetObject from a dict
budget_object_from_dict = BudgetObject.from_dict(budget_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


