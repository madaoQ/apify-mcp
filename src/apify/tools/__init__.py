# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for apify-mcp.

Modules:
  actors   -- apify_list_actors, apify_run_actor, apify_get_run, apify_abort_run
  datasets -- apify_get_dataset_items
  tasks    -- apify_list_tasks
"""

from __future__ import annotations

from apify.tools.actors import actor_tools
from apify.tools.datasets import dataset_tools
from apify.tools.tasks import task_tools

apify_tools = [
    *actor_tools,
    *dataset_tools,
    *task_tools,
]