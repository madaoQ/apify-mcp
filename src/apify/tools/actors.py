# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Actor management tools for Apify."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from apify.guards import (
    validate_actor_id,
    validate_limit,
    validate_offset,
    validate_run_id,
)
from apify.request import request
from apify.types import JSONObject


@tool(
    description="List all actors in your Apify account.",
    tags=["actors", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def apify_list_actors(
    limit: int = 20,
    offset: int = 0,
) -> JSONObject:
    """List actors.

    Args:
        limit: Number of results (1-10000).
        offset: Pagination offset.

    Returns:
        List of actors.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_limit(limit)
    validate_offset(offset)

    result = await request(
        HttpMethod.GET, "/acts", params={"limit": limit, "offset": offset}
    )
    return result


@tool(
    description="Run an Apify actor.",
    tags=["actors", "write"],
    annotations=ToolAnnotations(readOnlyHint=False),
)
async def apify_run_actor(
    actor_id: str,
    run_input: dict[str, Any] | None = None,
    build: str | None = None,
    timeout: int | None = None,
    memory_mbytes: int | None = None,
) -> JSONObject:
    """Run an actor.

    Args:
        actor_id: Actor ID or name.
        run_input: Input data for the actor.
        build: Actor build tag or version.
        timeout: Timeout in seconds.
        memory_mbytes: Memory in MB.

    Returns:
        Run details with ID.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_actor_id(actor_id)

    body: JSONObject = {}

    if run_input is not None:
        body["input"] = run_input
    if build is not None:
        body["build"] = build
    if timeout is not None:
        body["timeout"] = timeout
    if memory_mbytes is not None:
        body["memoryMbytes"] = memory_mbytes

    result = await request(HttpMethod.POST, f"/acts/{actor_id}/runs", body)
    return result


@tool(
    description="Get details of an actor run.",
    tags=["actors", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def apify_get_run(
    actor_id: str,
    run_id: str,
) -> JSONObject:
    """Get run details.

    Args:
        actor_id: Actor ID.
        run_id: Run ID.

    Returns:
        Run details.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_actor_id(actor_id)
    validate_run_id(run_id)

    result = await request(HttpMethod.GET, f"/acts/{actor_id}/runs/{run_id}")
    return result


@tool(
    description="Abort a running actor.",
    tags=["actors", "write"],
    annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True),
)
async def apify_abort_run(
    actor_id: str,
    run_id: str,
) -> JSONObject:
    """Abort a run.

    Args:
        actor_id: Actor ID.
        run_id: Run ID.

    Returns:
        Abort confirmation.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_actor_id(actor_id)
    validate_run_id(run_id)

    result = await request(HttpMethod.POST, f"/acts/{actor_id}/runs/{run_id}/abort", {})
    return result


actor_tools = [apify_list_actors, apify_run_actor, apify_get_run, apify_abort_run]