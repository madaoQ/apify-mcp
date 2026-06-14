# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Apify API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ActorInfo(BaseModel, frozen=True, slots=True):
    """Actor info."""

    id: str | None = None
    name: str | None = None
    description: str | None = None


class ActorList(BaseModel, frozen=True, slots=True):
    """List of actors."""

    data: list[ActorInfo] = Field(default_factory=list)
    total: int | None = None


class RunInfo(BaseModel, frozen=True, slots=True):
    """Actor run info."""

    id: str | None = None
    act_id: str | None = None
    status: str | None = None
    started_at: str | None = None
    finished_at: str | None = None


class DatasetItem(BaseModel, frozen=True, slots=True):
    """Dataset item."""

    # Dataset items are arbitrary JSON
    pass


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]