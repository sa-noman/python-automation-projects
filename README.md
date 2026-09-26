# Python Automation Projects

A compact collection of practical Python automation tools for everyday file management, website checks, RSS collection, and public API data retrieval.

## Projects

| Project | What it does |
|---|---|
| **01. File Organizer** | Sorts files into category folders and supports safe dry-run previews. |
| **02. Website Status Checker** | Reports HTTP status, redirects, reachability, and response time. |
| **03. RSS News Collector** | Reads RSS/Atom feeds and prints recent headlines with links and dates. |
| **04. API Data Fetcher** | Fetches JSON from a public API and prints clean, readable output. |

## Tech Stack

- Python 3.10+
- `requests`
- Standard library modules such as `pathlib`, `argparse`, `json`, and `shutil`

## Getting Started

```bash
git clone https://github.com/sa-noman/python-automation-projects.git
cd python-automation-projects
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Quick Examples

```bash
python 01-file-organizer/app.py ~/Downloads --dry-run
python 02-website-status-checker/app.py example.com
python 03-rss-news-collector/app.py https://example.com/feed.xml --limit 5
python 04-api-data-fetcher/app.py https://api.github.com/repos/python/cpython
```

## Safety

The file organizer supports `--dry-run` so moves can be reviewed first. None of these tools require secrets or store credentials.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Future Ideas

- Duplicate file finder
- Scheduled website monitor
- CSV report generator
- Batch image renamer
