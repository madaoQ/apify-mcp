# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Apify MCP server for Dedalus.

Provides web scraping, automation, and dataset access via Apify API.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from apify_mcp.config import create_apify_connection
from apify_mcp.tools import apify_tools

__all__ = ["create_apify_connection", "apify_tools"]