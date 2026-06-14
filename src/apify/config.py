# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Apify API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# Apify API base URL
APIFY_API_BASE = "https://api.apify.com/v2"


def create_apify_connection() -> Connection:
    """Create a DAuth connection to Apify API.

    Uses Bearer token authentication.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for Apify API.

    """
    return Connection(
        name="apify",
        secrets=SecretKeys(token="APIFY_API_KEY"),
        base_url=APIFY_API_BASE,
        auth_header_format="Bearer {api_key}",
    )