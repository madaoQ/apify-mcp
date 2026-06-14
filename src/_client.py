# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Direct API testing client for Apify MCP.

This module is used for local testing without going through the MCP server.
"""

from __future__ import annotations

import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_list_actors() -> None:
    """Test list_actors endpoint."""
    print("Testing apify_list_actors...")

    api_key = os.getenv("APIFY_API_KEY")
    if not api_key:
        print("Error: APIFY_API_KEY not found in environment")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.apify.com/v2/acts",
            headers=headers,
            params={"limit": 10},
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ List actors successful")
        print(f"  Total: {data.get('data', []).__len__() if isinstance(data.get('data'), list) else 'N/A'}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def main() -> None:
    """Run all direct API tests."""
    print("=" * 50)
    print("Apify Direct API Tests")
    print("=" * 50)
    print()

    await test_list_actors()

    print()
    print("=" * 50)
    print("Tests completed!")


if __name__ == "__main__":
    asyncio.run(main())