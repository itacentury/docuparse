# Docuparse

AI-powered bill parser that extracts structured data from PDF receipts using Claude and optionally uploads them to Paperless-ngx.

## Requirements

- Python 3.10+
- [Anthropic API Key](https://console.anthropic.com/)
- (Optional) Paperless-ngx instance

## Installation

```bash
pip install -e .
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
docuparse
```

Or run as module:

```bash
python -m docuparse
```

A file dialog opens to select PDF bills. The extracted data is saved to `~/Downloads/bills-YYYY-MM-DD.json`.

## Development

```bash
pip install -e ".[dev]"
```

Run checks:

```bash
black docuparse/
isort docuparse/
mypy docuparse/
```
