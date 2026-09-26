from __future__ import annotations
import argparse
import time
import requests


def normalize_url(url: str) -> str:
    return url if url.startswith(('http://', 'https://')) else 'https://' + url

def check(url: str, timeout: float = 10.0) -> dict:
    url = normalize_url(url.strip())
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True, headers={'User-Agent':'python-automation-projects/1.0'})
        elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
        return {'url': url, 'final_url': response.url, 'status': response.status_code, 'ok': response.ok, 'response_ms': elapsed_ms, 'error': None}
    except requests.RequestException as exc:
        elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
        return {'url': url, 'final_url': None, 'status': None, 'ok': False, 'response_ms': elapsed_ms, 'error': str(exc)}

def main() -> None:
    parser = argparse.ArgumentParser(description='Check a website status code and response time.')
    parser.add_argument('url')
    parser.add_argument('--timeout', type=float, default=10.0)
    args = parser.parse_args()
    result = check(args.url, args.timeout)
    print(f"URL: {result['url']}")
    print(f"Status: {result['status'] if result['status'] is not None else 'ERROR'}")
    print(f"Reachable: {'yes' if result['ok'] else 'no'}")
    print(f"Response time: {result['response_ms']} ms")
    if result['final_url'] and result['final_url'] != result['url']:
        print(f"Final URL: {result['final_url']}")
    if result['error']:
        print(f"Error: {result['error']}")

if __name__ == '__main__':
    main()
