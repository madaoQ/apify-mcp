# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Task management tools for Apify."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from apify_mcp.guards import validate_limit, validate_offset
from apify_mcp.request import request
from apify_mcp.types import JSONObject


@tool(
    description="List all Apify tasks.",
    tags=["tasks", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def apify_list_tasks(
    limit: int = 20,
    offset: int = 0,
) -> JSONObject:
    """List tasks.

    Args:
        limit: Number of results.
        offset: Pagination offset.

    Returns:
        List of tasks.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_limit(limit)
    validate_offset(offset)

    result = await request(
        HttpMethod.GET, "/tasks", params={"limit": limit, "offset": offset}
    )
    return result


task_tools = [apify_list_tasks]