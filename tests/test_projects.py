import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]

def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

organizer = load('organizer', '01-file-organizer/app.py')
status = load('status', '02-website-status-checker/app.py')
rss = load('rss', '03-rss-news-collector/app.py')
api = load('api', '04-api-data-fetcher/app.py')

class ProjectTests(unittest.TestCase):
    def test_category(self):
        self.assertEqual(organizer.category_for(Path('photo.jpg')), 'Images')
        self.assertEqual(organizer.category_for(Path('unknown.xyz')), 'Other')

    def test_organizer_dry_run(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td); (p/'a.txt').write_text('x'); (p/'b.jpg').write_text('x')
            moves = organizer.organize(p, dry_run=True)
            self.assertEqual(len(moves), 2)
            self.assertTrue((p/'a.txt').exists())

    def test_url_normalize(self):
        self.assertEqual(status.normalize_url('example.com'), 'https://example.com')

    @patch.object(status.requests, 'get')
    def test_status_checker(self, get):
        r = Mock(status_code=200, ok=True, url='https://example.com')
        get.return_value = r
        out = status.check('example.com')
        self.assertTrue(out['ok']); self.assertEqual(out['status'], 200)

    def test_rss_parse(self):
        xml = b'<rss><channel><item><title>Hello</title><link>https://x</link><pubDate>Today</pubDate></item></channel></rss>'
        items=rss.parse_feed_xml(xml, 5)
        self.assertEqual(items[0]['title'], 'Hello')

    @patch.object(api.requests, 'get')
    def test_api_fetch(self, get):
        r=Mock(); r.raise_for_status=Mock(); r.json.return_value={'ok': True}; get.return_value=r
        self.assertEqual(api.fetch_json('https://api.example.com'), {'ok': True})

if __name__ == '__main__':
    unittest.main()
