import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_site", ROOT / "scripts/build_site.py")
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = site.read_catalog()

    def test_every_markdown_entry_has_a_source_record(self):
        expected = set()
        for path in (ROOT / "papers").glob("*.md"):
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if re.match(r"\| \[.+\]\(https?://", line):
                    expected.add((str(path.relative_to(ROOT)), number))
        actual = [(s["path"], s["line"]) for p in self.catalog["papers"] for s in p["sources"]]
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(expected, set(actual))

    def test_cross_listed_papers_keep_all_topics_and_sources(self):
        papers = self.catalog["papers"]
        self.assertLess(len(papers), self.catalog["source_entries"])
        self.assertEqual(len({p["id"] for p in papers}), len(papers))
        for paper in papers:
            for source in paper["sources"]:
                line = (ROOT / source["path"]).read_text().splitlines()[source["line"] - 1]
                title, url, year = re.fullmatch(r"\|\s*\[(.+)\]\((https?://.+)\)\s*\|\s*(\d{4})\s*\|", line).groups()
                self.assertIn(url, paper["urls"])
                self.assertEqual(int(year), paper["year"])
                self.assertIn(site.html.unescape(title), paper["title_variants"])

    def test_all_topics_and_collections_are_searchable(self):
        used_topics = {t for p in self.catalog["papers"] for t in p["topics"]}
        used_sections = {s for p in self.catalog["papers"] for s in p["sections"]}
        self.assertEqual(set(self.catalog["topics"]), used_topics)
        self.assertEqual(set(self.catalog["sections"]), used_sections)
        for paper in self.catalog["papers"]:
            for topic in paper["topics"]:
                self.assertIn(self.catalog["topics"][topic]["section"], paper["sections"])

    def test_build_contains_all_papers_without_javascript(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            data = site.build(output)
            page = (output / "index.html").read_text()
            self.assertEqual(page.count('class="paper-card"'), len(data["papers"]))
            embedded = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>', page, re.S)
            self.assertEqual(json.loads(embedded.group(1)), data)
            self.assertEqual(json.loads((output / "papers.json").read_text()), data)
            self.assertNotRegex(page, r"\{\{[A-Z_]+\}\}")
            for asset in ("app.js", "styles.css", "favicon.svg", "sitemap.xml", "figs/overview.png"):
                self.assertTrue((output / asset).is_file(), asset)

    def test_markup_escapes_external_titles_and_urls(self):
        data = self.catalog.copy()
        data["papers"] = [{**self.catalog["papers"][0], "title": '<script>alert("x")</script>',
                           "urls": ['https://example.org/?q=" onload="alert(1)']}]
        markup = site.cards(data)
        self.assertNotIn('<script>', markup)
        self.assertIn('&lt;script&gt;', markup)
        self.assertNotIn('" onload="', markup)


if __name__ == "__main__":
    unittest.main()
