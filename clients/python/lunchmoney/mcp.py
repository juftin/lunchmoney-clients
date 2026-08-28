"""
MCP Server for LunchMoney API.

Provides read-only tools to interact with LunchMoney data via the Model Context Protocol.
"""

from __future__ import annotations

import datetime
import logging
from typing import Any

try:
    from fastmcp import FastMCP
except ImportError as e:
    raise ImportError(
        "fastmcp is required for the MCP server. "
        "Install it with: pip install lunchmoney-python[mcp]"
    ) from e

from lunchmoney.app import LunchMoneyApp
from lunchmoney.models import (
    CategoryObject,
    ManualAccountObject,
    PlaidAccountObject,
    RecurringObject,
    TagObject,
    TransactionObject,
    UserObject,
)

logger = logging.getLogger(__name__)

app = LunchMoneyApp()
"""Shared app instance providing client and data access."""

mcp = FastMCP(name="LunchMoney")


@mcp.tool
def get_categories() -> list[CategoryObject]:
    """Get all categories from LunchMoney."""
    categories = app.refresh(app.models.CategoryObject)
    result = list(categories.values())
    app.data.categories.clear()
    return result


@mcp.tool
def get_tags() -> list[TagObject]:
    """Get all tags from LunchMoney."""
    tags = app.refresh(app.models.TagObject)
    result = list(tags.values())
    app.data.tags.clear()
    return result


@mcp.tool
def get_plaid_accounts() -> list[PlaidAccountObject]:
    """Get all Plaid (synced) accounts from LunchMoney."""
    accounts = app.refresh(app.models.PlaidAccountObject)
    result = list(accounts.values())
    app.data.plaid_accounts.clear()
    return result


@mcp.tool
def get_manual_accounts() -> list[ManualAccountObject]:
    """Get all manual accounts from LunchMoney."""
    accounts = app.refresh(app.models.ManualAccountObject)
    result = list(accounts.values())
    app.data.manual_accounts.clear()
    return result


@mcp.tool
def get_accounts() -> list[ManualAccountObject | PlaidAccountObject]:
    """Get all accounts from LunchMoney."""
    app.refresh_data(
        models=[app.models.ManualAccountObject, app.models.PlaidAccountObject]
    )
    result = list(app.data.asset_map.values())
    app.data.manual_accounts.clear()
    app.data.plaid_accounts.clear()
    return result


@mcp.tool
def get_user() -> UserObject:
    """Get the current LunchMoney user profile."""
    user = app.refresh(app.models.UserObject)
    app.data.user = None
    return user


@mcp.tool
def get_recurring_items() -> list[RecurringObject]:
    """Get all recurring items from LunchMoney."""
    response = app.client.recurring_items.get_all_recurring()
    return response.recurring_items or []


@mcp.tool
def get_budget_summary(
    start_date: str,
    end_date: str,
) -> Any:  # noqa: ANN401
    """Get budget summary for a date range.

    Parameters
    ----------
    start_date : str
        Start date in YYYY-MM-DD format.
    end_date : str
        End date in YYYY-MM-DD format.
    """
    return app.client.summary.get_budget_summary(
        start_date=datetime.date.fromisoformat(start_date),
        end_date=datetime.date.fromisoformat(end_date),
    )


@mcp.tool
def get_transactions(
    start_date: str | None = None,
    end_date: str | None = None,
    tag_id: int | None = None,
    category_id: int | None = None,
    plaid_account_id: int | None = None,
    manual_account_id: int | None = None,
    status: str | None = None,
    is_pending: bool | None = None,
) -> list[TransactionObject]:
    """Get transactions from LunchMoney with optional filters.

    Parameters
    ----------
    start_date : str | None
        Beginning of date range (YYYY-MM-DD).
    end_date : str | None
        End of date range (YYYY-MM-DD).
    tag_id : int | None
        Filter by tag ID.
    category_id : int | None
        Filter by category ID.
    plaid_account_id : int | None
        Filter by Plaid account ID. Set to 0 to omit Plaid transactions.
    manual_account_id : int | None
        Filter by manual account ID. Set to 0 to omit manual transactions.
    status : str | None
        Filter by status: 'reviewed', 'unreviewed', or 'delete_pending'.
    is_pending : bool | None
        Filter by pending status.
    """
    start = datetime.date.fromisoformat(start_date) if start_date else None
    end = datetime.date.fromisoformat(end_date) if end_date else None
    transactions = app.refresh_transactions(
        start_date=start,
        end_date=end,
        tag_id=tag_id,
        category_id=category_id,
        plaid_account_id=plaid_account_id,
        manual_account_id=manual_account_id,
        status=status,
        is_pending=is_pending,
    )
    result = list(transactions.values())
    app.data.transactions.clear()
    return result


@mcp.tool
def get_spending_summary(
    start_date: str | None = None,
    end_date: str | None = None,
    tag_id: int | None = None,
    category_id: int | None = None,
    plaid_account_id: int | None = None,
    manual_account_id: int | None = None,
    status: str | None = None,
    is_pending: bool | None = None,
) -> dict[str, float]:
    """Summarize Spending Per Category.

    Parameters
    ----------
    start_date : str | None
        Beginning of date range (YYYY-MM-DD).
    end_date : str | None
        End of date range (YYYY-MM-DD).
    tag_id : int | None
        Filter by tag ID.
    category_id : int | None
        Filter by category ID.
    plaid_account_id : int | None
        Filter by Plaid account ID. Set to 0 to omit Plaid transactions.
    manual_account_id : int | None
        Filter by manual account ID. Set to 0 to omit manual transactions.
    status : str | None
        Filter by status: 'reviewed', 'unreviewed', or 'delete_pending'.
    is_pending : bool | None
        Filter by pending status.

    Returns
    --------
    dict[str, float]
        A dictionary where the keys are category names and the values are
        the respective category's spend
    """
    start = datetime.date.fromisoformat(start_date) if start_date else None
    end = datetime.date.fromisoformat(end_date) if end_date else None
    app.refresh_transactions(
        start_date=start,
        end_date=end,
        tag_id=tag_id,
        category_id=category_id,
        plaid_account_id=plaid_account_id,
        manual_account_id=manual_account_id,
        status=status,
        is_pending=is_pending,
    )
    app.refresh(app.models.CategoryObject)
    category_map = app.data.category_map.copy()
    summary: dict[str, float] = {"Uncategorized": 0}
    for category in category_map.values():
        summary[category.name] = 0
    for transaction in app.data.transactions.values():
        if transaction.category_id:
            category_name = category_map[transaction.category_id].name
        else:
            category_name = "Uncategorized"
        summary[category_name] += float(transaction.amount)
    normalized_summary: dict[str, float] = {
        key: round(value, 2) for key, value in summary.items()
    }
    app.data.transactions.clear()
    app.data.categories.clear()
    return normalized_summary


def main() -> None:
    """Entry point for the ``lunchable-mcp`` console script."""
    mcp.run()


__all__ = ["main", "mcp"]

if __name__ == "__main__":
    main()
