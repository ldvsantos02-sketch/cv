"""Deduplicate embedded resources in the generated GitHub Pages output.

Run after Quarto and the book outputs have been copied to _site. Original
self-contained lecture downloads in aulas/ are never modified.
"""

import argparse
import base64
import binascii
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import unicodedata
from urllib.parse import quote, unquote, unquote_to_bytes, urlsplit


DATA_URI = re.compile(
    r"data:([\w.+/-]+)(?:;charset=[\w-]+)?;base64,([A-Za-z0-9+/]+={0,2})",
    re.IGNORECASE,
)
EXTENSIONS = {
    "image/png": "png", "image/jpeg": "jpg", "image/gif": "gif",
    "image/webp": "webp", "image/svg+xml": "svg", "image/avif": "avif",
    "image/x-icon": "ico", "font/woff": "woff", "font/woff2": "woff2",
    "font/ttf": "ttf", "font/otf": "otf", "application/font-woff": "woff",
    "application/x-font-woff": "woff", "application/x-font-ttf": "ttf",
    "application/x-font-opentype": "otf", "application/vnd.ms-fontobject": "eot",
    "text/javascript": "js", "application/javascript": "js", "text/css": "css",
}
JAVASCRIPT_TYPES = {"", "text/javascript", "application/javascript", "module"}


class Assets:
    def __init__(self, output, base_path, asset_base_url=None):
        self.directory = output / "_pages-assets"
        self.url_prefix = (asset_base_url or base_path).rstrip("/") + "/_pages-assets/"
        self.created = 0
        self.references = 0

    def save(self, content, extension):
        name = hashlib.sha256(content).hexdigest() + "." + extension
        target = self.directory / name
        if not target.exists():
            self.directory.mkdir(exist_ok=True)
            target.write_bytes(content)
            self.created += 1
        self.references += 1
        return self.url_prefix + name

    def replace_data_uris(self, text):
        def replace(match):
            extension = EXTENSIONS.get(match[1].lower())
            if not extension:
                return match[0]
            try:
                content = base64.b64decode(match[2], validate=True)
            except (ValueError, binascii.Error):
                return match[0]
            return self.save(content, extension)

        return DATA_URI.sub(replace, text)

    def stylesheet_url(self, value):
        # Quarto also writes percent-encoded CSS links containing complete font
        # families. Sharing these saves several megabytes per presentation.
        header, separator, payload = value.partition(",")
        if not separator or not re.fullmatch(r"data:text/css(?:;charset=[\w-]+)?", header, re.I):
            return value
        try:
            css = unquote_to_bytes(payload).decode("utf-8")
        except (UnicodeError, ValueError):
            return value
        css = self.replace_data_uris(css)
        if not safe_style(css):
            return value
        return self.save(css.encode("utf-8"), "css")


def safe_script(body):
    # These APIs depend on an inline script's location or its element contents.
    if re.search(r"document\s*\.\s*currentScript|import\s*\.\s*meta", body):
        return False
    if re.search(r"\bimport\s*(?:\(\s*)?['\"]\.{1,2}/", body):
        return False
    if re.search(r"\b(?:from|import)\s*['\"]\.{1,2}/", body):
        return False
    return True


def safe_style(body):
    for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", body, re.I):
        if not re.match(r"(?:/|data:|https?:|//)", match[2], re.I):
            return False
    return not re.search(r"@import\s+['\"](?!/|https?:)", body, re.I)


class ResourceParser(HTMLParser):
    def __init__(self, assets):
        super().__init__(convert_charrefs=False)
        self.assets = assets
        self.parts = []
        self.capture = None
        self.svg_depth = 0

    def handle_starttag(self, tag, attrs):
        raw = self.get_starttag_text()
        attributes = dict(attrs)
        if tag == "link" and attributes.get("href", "").lower().startswith("data:text/css,"):
            url = self.assets.stylesheet_url(attributes["href"])
            if url != attributes["href"]:
                raw = re.sub(r"(\bhref\s*=\s*)([\"'])(.*?)\2", lambda match: match[1] + match[2] + url + match[2], raw, count=1, flags=re.I | re.S)
        if tag == "svg":
            self.svg_depth += 1
        is_script = (
            tag == "script" and "src" not in attributes
            and attributes.get("type", "").lower() in JAVASCRIPT_TYPES
            and not self.svg_depth
        )
        is_style = tag == "style" and not self.svg_depth
        if is_script or is_style:
            self.capture = (tag, attributes, raw, [])
        else:
            self.parts.append(raw)

    def handle_startendtag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.capture and tag == self.capture[0]:
            kind, attrs, raw, pieces = self.capture
            body = "".join(pieces)
            # Preserve styles/scripts addressed by id: other code may read them.
            eligible = len(body) >= 4096 and "id" not in attrs
            eligible = eligible and (safe_script(body) if kind == "script" else safe_style(body))
            if eligible:
                url = self.assets.save(body.encode("utf-8"), "js" if kind == "script" else "css")
                if kind == "script":
                    # async/defer do not apply to classic inline scripts. Removing
                    # them preserves execution order after adding a src.
                    if attrs.get("type") != "module":
                        raw = re.sub(r"\s+(?:async|defer)(?:\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+))?(?=\s|>)", "", raw, flags=re.I)
                    self.parts.append(raw[:-1] + ' src="' + url + '"></script>')
                else:
                    media = attrs.get("media")
                    media_attr = ' media="' + html.escape(media, quote=True) + '"' if media else ""
                    self.parts.append('<link rel="stylesheet" href="' + url + '"' + media_attr + '>')
            else:
                self.parts.extend((raw, body, "</" + tag + ">"))
            self.capture = None
        else:
            self.parts.append("</" + tag + ">")
        if tag == "svg":
            self.svg_depth -= 1

    def append(self, text):
        (self.capture[3] if self.capture else self.parts).append(text)

    def handle_data(self, data):
        self.append(data)

    def handle_entityref(self, name):
        self.append("&" + name + ";")

    def handle_charref(self, name):
        self.append("&#" + name + ";")

    def handle_comment(self, data):
        self.append("<!--" + data + "-->")

    def handle_decl(self, decl):
        self.append("<!" + decl + ">")

    def handle_pi(self, data):
        self.append("<?" + data + ">")

    def unknown_decl(self, data):
        self.append("<![" + data + "]>")

    def result(self):
        if self.capture:
            self.parts.extend((self.capture[2], "".join(self.capture[3])))
        return "".join(self.parts)


def remove_nested_book_outputs(output):
    books = output / "books"
    if not books.is_dir():
        return 0
    removed = 0
    for book in books.iterdir():
        duplicate = book / "_book"
        if book.is_dir() and (book / "index.html").is_file() and duplicate.is_dir():
            # Only generated duplicates inside _site/books may be removed.
            if duplicate.is_symlink() or not duplicate.resolve().is_relative_to(books.resolve()):
                raise ValueError("Unexpected book output location: " + str(duplicate))
            shutil.rmtree(duplicate)
            removed += 1
    return removed


def output_size(output):
    return sum(path.stat().st_size for path in output.rglob("*") if path.is_file())


def report_output_size(output):
    groups = {}
    largest = []
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        size = path.stat().st_size
        relative = path.relative_to(output)
        key = "/".join(relative.parts[:2]) if relative.parts[0] == "books" else relative.parts[0]
        groups[key] = groups.get(key, 0) + size
        largest.append((size, relative.as_posix()))
    for name, size in sorted(groups.items(), key=lambda item: item[1], reverse=True)[:20]:
        print(f"Directory: {name}: {size / 1024**2:.1f} MiB", flush=True)
    for size, name in sorted(largest, reverse=True)[:20]:
        print(f"Largest: {name}: {size / 1024**2:.1f} MiB", flush=True)


IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}
TEXT_TYPES = {".html", ".css", ".js", ".json", ".svg", ".xml", ".csv", ".mtl", ".gltf", ".map"}


def share_copied_images(output, assets, base_path="/", source_base_url=None):
    """Reuse identical extracted images and serve large originals from Git.

    Only delete a published copy after rewriting its static URLs and checking
    that no other text resource still mentions its filename. Original repository
    files and PDFs are never changed. Source URLs must identify an immutable
    public repository revision in the publication workflow.
    """
    replacements = {}
    source_root = output.parent
    for path in output.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_TYPES or assets.directory in path.parents:
            continue
        relative = path.relative_to(output)
        extension = path.suffix.lower().replace(".jpeg", ".jpg")
        content = path.read_bytes()
        name = hashlib.sha256(content).hexdigest() + extension
        if (assets.directory / name).is_file():
            replacements[path.resolve()] = assets.url_prefix + name
        elif source_base_url and relative.parts[0] == "img" and len(content) >= 8_000_000:
            source = source_root / relative
            if source.is_file() and source.read_bytes() == content:
                replacements[path.resolve()] = source_base_url.rstrip("/") + "/" + quote(relative.as_posix(), safe="/")
    if not replacements:
        return 0, 0

    def replace_url(value, document):
        parsed = urlsplit(html.unescape(value))
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("#"):
            return value
        path = unquote(parsed.path)
        if path.startswith("/"):
            if base_path != "/" and path.startswith(base_path.rstrip("/") + "/"):
                path = path[len(base_path.rstrip("/")):]
            target = output / path.lstrip("/")
        else:
            target = document.parent / path
        url = replacements.get(target.resolve())
        if not url:
            return value
        return url + ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")

    attributes = re.compile(r"(\b(?:src|href|poster|data-src|data-background-image)\s*=\s*)([\"'])(.*?)\2", re.I | re.S)
    srcsets = re.compile(r"(\bsrcset\s*=\s*)([\"'])(.*?)\2", re.I | re.S)
    css_urls = re.compile(r"(url\(\s*)([\"']?)([^)\s\"']+)\2(\s*\))", re.I)
    documents = [path for path in output.rglob("*") if path.is_file() and path.suffix.lower() in TEXT_TYPES]
    texts = []
    for document in documents:
        original = document.read_text(encoding="utf-8", errors="replace")
        result = original
        if document.suffix.lower() in {".html", ".css", ".svg"}:
            result = attributes.sub(lambda m: m[1] + m[2] + replace_url(m[3], document) + m[2], result)
            result = srcsets.sub(lambda m: m[1] + m[2] + re.sub(r"(^|,)(\s*)([^\s,]+)", lambda item: item[1] + item[2] + replace_url(item[3], document), m[3]) + m[2], result)
            result = css_urls.sub(lambda m: m[1] + m[2] + replace_url(m[3], document) + m[2] + m[4], result)
            if result != original:
                document.write_text(result, encoding="utf-8", newline="")
        texts.append(result)
    text = unicodedata.normalize("NFC", unquote(html.unescape("\n".join(texts))))
    # A rewritten raw GitHub URL contains the original filename. It is remote
    # and therefore must not count as a reference to the local published copy.
    for url in set(replacements.values()):
        text = text.replace(unicodedata.normalize("NFC", unquote(url)), "")
    removed = removed_bytes = 0
    for path in replacements:
        name = unicodedata.normalize("NFC", path.name)
        variants = (name, quote(name), json.dumps(name, ensure_ascii=True)[1:-1])
        if any(variant in text for variant in variants):
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(output):
            raise ValueError("Unexpected published image location: " + str(path))
        removed_bytes += path.stat().st_size
        path.unlink()
        removed += 1
    return removed, removed_bytes


def remove_unreferenced_book_images(output):
    """Drop copied book image sources that no published text resource uses.

    Match filenames across the whole site, including CSS, JSON and SVG. This
    deliberately keeps duplicate copies whenever their basename is referenced.
    Original source images and downloadable PDFs are outside this cleanup.
    """
    books = output / "books"
    if not books.is_dir():
        return 0, 0
    if not books.resolve().is_relative_to(output.resolve()):
        raise ValueError("Unexpected books directory: " + str(books))
    text_types = {".html", ".css", ".js", ".json", ".svg", ".xml", ".csv", ".mtl", ".gltf", ".map"}
    text = "\n".join(path.read_text(encoding="utf-8", errors="replace")
                     for path in output.rglob("*") if path.is_file() and path.suffix.lower() in text_types)
    text = unicodedata.normalize("NFC", unquote(html.unescape(text))).replace("\\ ", " ")
    image_types = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}
    unused = []
    for book in books.iterdir():
        directory = book / "img"
        if not (book / "index.html").is_file() or not directory.is_dir():
            continue
        for image_path in directory.rglob("*"):
            if not image_path.is_file() or image_path.suffix.lower() not in image_types:
                continue
            name = unicodedata.normalize("NFC", image_path.name)
            variants = (name, quote(name), json.dumps(name, ensure_ascii=True)[1:-1])
            if not any(variant in text for variant in variants):
                if image_path.is_symlink() or not image_path.resolve().is_relative_to(books.resolve()):
                    raise ValueError("Unexpected book image location: " + str(image_path))
                unused.append(image_path)
    removed_bytes = sum(path.stat().st_size for path in unused)
    for path in unused:
        path.unlink()
    return len(unused), removed_bytes


def prepare(output, base_path="/", max_bytes=1_000_000_000, asset_base_url=None, source_base_url=None):
    output = Path(output).resolve()
    if not output.is_dir() or not (output / "index.html").is_file():
        raise ValueError("Expected a rendered website containing index.html: " + str(output))
    if not base_path.startswith("/") or ".." in base_path or "?" in base_path or "#" in base_path:
        raise ValueError("base-path must be an absolute site path, for example / or /cv/")
    if asset_base_url:
        url = urlsplit(asset_base_url)
        if url.scheme not in {"https", "http"} or not url.netloc or url.query or url.fragment or url.username or url.password:
            raise ValueError("asset-base-url must be a public HTTP(S) site URL without credentials, query or fragment")
    if source_base_url:
        url = urlsplit(source_base_url)
        if url.scheme != "https" or url.hostname != "raw.githubusercontent.com" or url.query or url.fragment or url.username or url.password or not re.fullmatch(r"/[^/]+/[^/]+/[0-9a-f]{40}/?", url.path):
            raise ValueError("source-base-url must identify an immutable public GitHub repository revision")
    before = output_size(output)
    removed = remove_nested_book_outputs(output)
    assets = Assets(output, base_path, asset_base_url)
    changed = 0
    for number, path in enumerate(sorted(output.rglob("*.html")), start=1):
        if assets.directory in path.parents:
            continue
        original = path.read_text(encoding="utf-8")
        text = assets.replace_data_uris(original)
        parser = ResourceParser(assets)
        parser.feed(text)
        parser.close()
        result = parser.result()
        if result != original:
            path.write_text(result, encoding="utf-8", newline="")
            changed += 1
        if number % 50 == 0:
            print(f"Prepared {number} HTML files...", flush=True)
    shared_images, shared_bytes = share_copied_images(output, assets, base_path, source_base_url)
    unused_images, unused_bytes = remove_unreferenced_book_images(output)
    after = output_size(output)
    print(f"Pages: {before / 1024**2:.1f} -> {after / 1024**2:.1f} MiB; "
          f"{changed} HTML files; {assets.created} shared assets; "
          f"{removed} duplicate book outputs removed.", flush=True)
    print(f"Books: removed {unused_images} unreferenced image copies "
          f"({unused_bytes / 1024**2:.1f} MiB).", flush=True)
    print(f"Images: shared {shared_images} published copies "
          f"({shared_bytes / 1024**2:.1f} MiB); original bytes preserved.", flush=True)
    report_output_size(output)
    if after > max_bytes:
        raise ValueError(f"Pages output is {after:,} bytes; limit is {max_bytes:,} bytes")
    return after


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("output", type=Path)
    argument_parser.add_argument("--base-path", default="/")
    argument_parser.add_argument("--asset-base-url", help="Canonical Pages URL; its redirects keep assets working when a custom domain is attached")
    argument_parser.add_argument("--source-base-url", help="Immutable raw GitHub revision URL for large original images already tracked in the repository")
    argument_parser.add_argument("--max-bytes", type=int, default=1_000_000_000)
    options = argument_parser.parse_args()
    prepare(options.output, options.base_path, options.max_bytes, options.asset_base_url, options.source_base_url)
