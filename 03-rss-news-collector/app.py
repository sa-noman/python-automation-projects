from __future__ import annotations
import argparse
from datetime import datetime
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET


def _text(node, names):
    for name in names:
        child = node.find(name)
        if child is not None and child.text:
            return child.text.strip()
    return ''


def parse_feed_xml(xml_bytes: bytes, limit: int = 10) -> list[dict]:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid RSS/Atom XML: {exc}") from exc

    items = []
    for item in root.findall('.//item')[:limit]:
        items.append({
            'title': _text(item, ['title']) or 'Untitled',
            'link': _text(item, ['link']),
            'published': _text(item, ['pubDate', 'date']) or 'Unknown',
        })

    if items:
        return items

    entries = [e for e in root.iter() if e.tag.split('}')[-1] == 'entry']
    for entry in entries[:limit]:
        title = next((c.text.strip() for c in entry if c.tag.split('}')[-1] == 'title' and c.text), 'Untitled')
        published = next((c.text.strip() for c in entry if c.tag.split('}')[-1] in {'published','updated'} and c.text), 'Unknown')
        link = ''
        for c in entry:
            if c.tag.split('}')[-1] == 'link':
                link = (c.attrib.get('href') or (c.text or '')).strip()
                if link:
                    break
        items.append({'title': title, 'link': link, 'published': published})
    return items


def collect(feed_url: str, limit: int = 10, timeout: float = 10.0) -> list[dict]:
    req = Request(feed_url, headers={'User-Agent': 'python-automation-projects/1.0'})
    try:
        with urlopen(req, timeout=timeout) as response:
            data = response.read()
    except Exception as exc:
        raise ValueError(f"Could not download feed: {exc}") from exc
    return parse_feed_xml(data, limit)


def main() -> None:
    parser = argparse.ArgumentParser(description='Collect recent headlines from an RSS/Atom feed.')
    parser.add_argument('feed_url')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--timeout', type=float, default=10.0)
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 100:
        raise SystemExit('--limit must be between 1 and 100')
    try:
        items = collect(args.feed_url, args.limit, args.timeout)
    except ValueError as exc:
        raise SystemExit(str(exc))
    print(f"Collected {len(items)} item(s) at {datetime.now().isoformat(timespec='seconds')}\n")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['title']}")
        print(f"   {item['published']}")
        if item['link']:
            print(f"   {item['link']}")

if __name__ == '__main__':
    main()
