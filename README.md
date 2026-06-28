# Docuparse

[![CI](https://github.com/itacentury/docuparse/actions/workflows/ci.yml/badge.svg)](https://github.com/itacentury/docuparse/actions/workflows/ci.yml)

AI-powered bill parser that extracts structured data from PDF receipts using Claude and optionally uploads them to Paperless-ngx.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [Anthropic API Key](https://console.anthropic.com/)
- (Optional) Paperless-ngx instance

## Installation

```bash
uv sync
```

## Configuration

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your-api-key

# Optional: Paperless-ngx integration
PAPERLESS_URL=https://your-paperless-instance.com
PAPERLESS_API_TOKEN=your-paperless-token
```

To disable Paperless upload, set `PAPERLESS_UPLOAD_ENABLE = False` in `docuparse/config.py`.

## Usage

```bash
uv run docuparse
```

Or run as module:

```bash
uv run python -m docuparse
```

A file dialog opens to select PDF bills. The extracted data is saved to `~/Downloads/bills-YYYY-MM-DD.json`.

## Development

```bash
uv sync
```

The `dev` dependency group is installed automatically.

Lint and format:

```bash
uv run ruff check docuparse/
uv run ruff format docuparse/
```

Type checking:

```bash
uv run mypy docuparse/
```

Run tests:

```bash
uv run pytest
```
