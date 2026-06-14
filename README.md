# Apify MCP Server

A Type 3 DAuth MCP server for [Apify API](https://apify.com). Provides web scraping, browser automation, and dataset management through Apify's actor platform.

## Features

- **List Actors** — View all available actors
- **Run Actor** — Execute an actor with custom input
- **Get Run** — Check actor run status
- **Get Dataset Items** — Retrieve scraped data
- **Abort Run** — Stop a running actor
- **List Tasks** — View all tasks

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your Apify API Key

1. Go to https://console.apify.com/account/integrations
2. Find your API token
3. Copy the token

## Installation

```bash
git clone https://github.com/dedalus-labs/apify-mcp.git
cd apify-mcp
pip install -e .
cp .env.example .env
# Edit .env and add APIFY_API_KEY
```

## Available Tools

### `apify_list_actors`

List all actors in your account.

```python
apify_list_actors(limit=20, offset=0)
```

### `apify_run_actor`

Run an actor.

```python
apify_run_actor(
    actor_id="apify/web-scraper",
    run_input={"startUrls": [{"url": "https://example.com"}]},
    timeout=60,
    memory_mbytes=512,
)
```

### `apify_get_run`

Get run details.

```python
apify_get_run(
    actor_id="apify/web-scraper",
    run_id="run-id-here",
)
```

### `apify_get_dataset_items`

Get items from a dataset.

```python
apify_get_dataset_items(
    dataset_id="dataset-id-here",
    limit=100,
    clean=True,
)
```

### `apify_abort_run`

Abort a running actor.

```python
apify_abort_run(
    actor_id="apify/web-scraper",
    run_id="run-id-here",
)
```

### `apify_list_tasks`

List all tasks.

```python
apify_list_tasks(limit=20, offset=0)
```

## Pricing

Apify uses a credit-based system. Check https://apify.com/pricing for details.

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `APIFY_API_KEY` as Required Credential
5. Deploy

## License

MIT