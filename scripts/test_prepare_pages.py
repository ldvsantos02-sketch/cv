"""Checks that publication deduplication preserves resource semantics."""

import base64
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from urllib.parse import quote

from prepare_pages import prepare, remove_unreferenced_book_images


class PreparePagesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name)

    def write(self, name, text):
        target = self.site / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def run_prepare(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return prepare(self.site, **kwargs)

    def test_shares_exact_resource_bytes_and_preserves_script_order(self):
        image = b"same image bytes"
        uri = "data:image/png;base64," + base64.b64encode(image).decode()
        script = "window.example = '" + "x" * 5000 + "';"
        document = '<!DOCTYPE html><img src="' + uri + '"><script defer>' + script + '</script><script>window.next = example;</script>'
        first = self.write("index.html", document)
        second = self.write("nested/lesson.html", document)
        self.run_prepare()
        self.assertEqual(first.read_bytes(), second.read_bytes())
        result = first.read_text(encoding="utf-8")
        self.assertNotIn("data:image", result)
        self.assertNotIn("defer", result)
        self.assertLess(result.index(' src="/_pages-assets/', result.index("<script")), result.index("window.next"))
        contents = {path.read_bytes() for path in (self.site / "_pages-assets").iterdir()}
        self.assertEqual(contents, {image, script.encode()})

    def test_preserves_location_sensitive_scripts_json_and_svg_styles(self):
        padding = " " * 5000
        body = ('<script>document.currentScript;' + padding + '</script>'
                '<script type="module">import x from "./module.js";' + padding + '</script>'
                '<script type="application/json">{"value":"' + padding + '"}</script>'
                '<script id="config">window.example=1;' + padding + '</script>'
                '<svg><style>.a{fill:red;}' + padding + '</style></svg>'
                '<style>.a{background:url(../image.png);}' + padding + '</style>')
        source = self.write("index.html", body)
        self.run_prepare()
        self.assertEqual(source.read_text(encoding="utf-8"), body)

    def test_preserves_css_media_and_supports_site_prefix(self):
        css = ".print{color:green;}" + " " * 5000
        source = self.write("index.html", '<style media="print">' + css + '</style>')
        self.run_prepare(base_path="/cv/")
        result = source.read_text(encoding="utf-8")
        self.assertIn('href="/cv/_pages-assets/', result)
        self.assertIn('media="print"', result)
        self.assertEqual(next((self.site / "_pages-assets").glob("*.css")).read_text(), css)

    def test_keeps_pdf_data_urls_and_invalid_base64(self):
        body = '<a href="data:application/pdf;base64,YWJj">PDF</a><img src="data:image/png;base64,a">'
        source = self.write("index.html", body)
        self.run_prepare()
        self.assertEqual(source.read_text(encoding="utf-8"), body)

    def test_shares_percent_encoded_stylesheets_and_nested_fonts(self):
        font = b"same font bytes"
        css = '@font-face{font-family:Example;src:url(data:font/woff2;base64,' + base64.b64encode(font).decode() + ')}'
        document = '<link rel="stylesheet" href="data:text/css,' + quote(css, safe="") + '">'
        first = self.write("index.html", document)
        second = self.write("lesson.html", document)
        self.run_prepare()
        self.assertEqual(first.read_bytes(), second.read_bytes())
        self.assertNotIn("data:text/css", first.read_text())
        directory = self.site / "_pages-assets"
        self.assertEqual(len(list(directory.iterdir())), 2)
        self.assertEqual(next(directory.glob("*.woff2")).read_bytes(), font)
        self.assertIn("/_pages-assets/", next(directory.glob("*.css")).read_text())

    def test_only_removes_nested_book_output_after_flattening(self):
        self.write("index.html", "site")
        self.write("books/flat/index.html", "book")
        self.write("books/flat/book.pdf", "download")
        self.write("books/flat/_book/index.html", "duplicate")
        self.write("books/not-flat/_book/index.html", "keep")
        self.run_prepare()
        self.assertFalse((self.site / "books/flat/_book").exists())
        self.assertTrue((self.site / "books/flat/book.pdf").exists())
        self.assertTrue((self.site / "books/not-flat/_book/index.html").exists())

    def test_is_idempotent_and_reports_oversized_output(self):
        self.write("index.html", '<script>' + 'window.example="' + 'x' * 5000 + '";</script>')
        self.run_prepare()
        before = {path.relative_to(self.site): path.read_bytes() for path in self.site.rglob("*") if path.is_file()}
        self.run_prepare()
        after = {path.relative_to(self.site): path.read_bytes() for path in self.site.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        with self.assertRaisesRegex(ValueError, "limit"):
            self.run_prepare(max_bytes=1)

    def test_removes_only_unused_book_images_and_preserves_references(self):
        self.write("index.html", '<img src="books/example/img/caf%C3%A9.png">')
        self.write("books/example/index.html", '<img src="img/used.png">')
        self.write("books/example/style.css", '.figure{background:url(img/space\\ name.png)}')
        self.write("books/example/data.json", '{"image":"img/json\\u00e9.png"}')
        for name in ("used.png", "café.png", "space name.png", "jsoné.png", "unused.png"):
            self.write("books/example/img/" + name, "image")
        self.write("books/example/book.pdf", "download")
        self.write("books/example/img/source.pdf", "download")
        self.write("img/unused.png", "keep outside books")
        self.write("books/no-index/img/unused.png", "keep without a rendered book")
        self.assertEqual(remove_unreferenced_book_images(self.site), (1, 5))
        self.assertFalse((self.site / "books/example/img/unused.png").exists())
        for name in ("used.png", "café.png", "space name.png", "jsoné.png", "source.pdf"):
            self.assertTrue((self.site / "books/example/img" / name).exists())
        self.assertTrue((self.site / "books/example/book.pdf").exists())
        self.assertTrue((self.site / "img/unused.png").exists())
        self.assertTrue((self.site / "books/no-index/img/unused.png").exists())


if __name__ == "__main__":
    unittest.main()
