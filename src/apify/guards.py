# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for Apify API parameters."""

from __future__ import annotations

import re


# Apify actor ID: alphanumeric with hyphens, underscores, dots
_ACTOR_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]*$")

# Apify run ID: alphanumeric with hyphens
_RUN_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-]*$")

# Dataset ID: alphanumeric with hyphens, underscores
_DATASET_ID_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$")


def validate_actor_id(actor_id: str) -> None:
    """Validate an actor ID."""
    if not actor_id or not _ACTOR_ID_RE.match(actor_id):
        msg = f"Invalid actor ID: {actor_id!r}"
        raise ValueError(msg)


def validate_run_id(run_id: str) -> None:
    """Validate a run ID."""
    if not run_id or not _RUN_ID_RE.match(run_id):
        msg = f"Invalid run ID: {run_id!r}"
        raise ValueError(msg)


def validate_dataset_id(dataset_id: str) -> None:
    """Validate a dataset ID."""
    if not dataset_id or not _DATASET_ID_RE.match(dataset_id):
        msg = f"Invalid dataset ID: {dataset_id!r}"
        raise ValueError(msg)


def validate_limit(limit: int) -> None:
    """Validate pagination limit."""
    if limit < 1 or limit > 10000:
        msg = f"Limit must be between 1 and 10000, got {limit}"
        raise ValueError(msg)


def validate_offset(offset: int) -> None:
    """Validate pagination offset."""
    if offset < 0:
        msg = f"Offset must be non-negative, got {offset}"
        raise ValueError(msg)