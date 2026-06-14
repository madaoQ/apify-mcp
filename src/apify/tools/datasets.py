# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Dataset tools for Apify."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from apify.guards import validate_dataset_id, validate_limit, validate_offset
from apify.request import request
from apify.types import JSONObject


@tool(
    description="Get items from a dataset.",
    tags=["datasets", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def apify_get_dataset_items(
    dataset_id: str,
    limit: int = 100,
    offset: int = 0,
    clean: bool = True,
) -> JSONObject:
    """Get dataset items.

    Args:
        dataset_id: Dataset ID.
        limit: Number of items.
        offset: Pagination offset.
        clean: Return clean data only.

    Returns:
        Dataset items.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_dataset_id(dataset_id)
    validate_limit(limit)
    validate_offset(offset)

    result = await request(
        HttpMethod.GET,
        f"/datasets/{dataset_id}/items",
        params={"limit": limit, "offset": offset, "clean": clean},
    )
    return result


dataset_tools = [apify_get_dataset_items]