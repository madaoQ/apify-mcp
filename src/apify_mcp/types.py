# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Apify API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


# Reusable config: immutable, slotted.
_FROZEN_SLOT = ConfigDict(frozen=True, slots=True)


class ActorInfo(BaseModel):
    """Actor info."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    name: str | None = None
    description: str | None = None


class ActorList(BaseModel):
    """List of actors."""
    model_config = _FROZEN_SLOT


    data: list[ActorInfo] = Field(default_factory=list)
    total: int | None = None


class RunInfo(BaseModel):
    """Actor run info."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    act_id: str | None = None
    status: str | None = None
    started_at: str | None = None
    finished_at: str | None = None


class DatasetItem(BaseModel):
    """Dataset item."""
    model_config = _FROZEN_SLOT


    # Dataset items are arbitrary JSON
    pass


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]