# Python Automation Projects

[![Tests](https://github.com/sa-noman/python-automation-projects/actions/workflows/tests.yml/badge.svg)](https://github.com/sa-noman/python-automation-projects/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Focus-Automation-6C63FF)

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
- Standard library modules including `pathlib`, `argparse`, `json`, `urllib`, and `shutil`
- GitHub Actions for automated testing

## Getting Started

```bash
git clone https://github.com/sa-noman/python-automation-projects.git
cd python-automation-projects
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Quick Examples

```bash
python 01-file-organizer/app.py ~/Downloads --dry-run
python 02-website-status-checker/app.py example.com
python 03-rss-news-collector/app.py https://example.com/feed.xml --limit 5
python 04-api-data-fetcher/app.py https://api.github.com/repos/python/cpython
```

## Tests

The repository is automatically tested on Python 3.10, 3.11, and 3.12 with GitHub Actions.

Run the same test suite locally:

```bash
python -m unittest discover -s tests -v
```

## Safety

- The File Organizer supports `--dry-run` so changes can be reviewed before files are moved.
- No passwords, API keys, tokens, or credentials are required or stored.
- Network tools use timeouts and basic error handling.

## Repository Structure

```text
python-automation-projects/
├── 01-file-organizer/
├── 02-website-status-checker/
├── 03-rss-news-collector/
├── 04-api-data-fetcher/
├── tests/
├── .github/workflows/tests.yml
├── .gitignore
├── requirements.txt
└── README.md
```

## Future Ideas

- Duplicate File Finder
- Scheduled Website Monitor
- CSV Report Generator
- Batch Image Renamer
