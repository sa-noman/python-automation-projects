from __future__ import annotations
import argparse
import json
import requests


def fetch_json(url: str, timeout: float = 10.0):
    response = requests.get(url, timeout=timeout, headers={'Accept':'application/json','User-Agent':'python-automation-projects/1.0'})
    response.raise_for_status()
    try:
        return response.json()
    except ValueError as exc:
        raise ValueError('Response was not valid JSON') from exc

def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch JSON from a public API endpoint.')
    parser.add_argument('url')
    parser.add_argument('--timeout', type=float, default=10.0)
    parser.add_argument('--indent', type=int, default=2)
    args = parser.parse_args()
    try:
        data = fetch_json(args.url, args.timeout)
    except (requests.RequestException, ValueError) as exc:
        raise SystemExit(f"Request failed: {exc}")
    print(json.dumps(data, indent=args.indent, ensure_ascii=False, sort_keys=True))

if __name__ == '__main__':
    main()
