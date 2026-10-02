#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import os


class CleanURLHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        prefix = getattr(self.server, "url_prefix", "")
        if prefix and (path == prefix or path.startswith(prefix + "/")):
            path = path[len(prefix):] or "/"

        translated = Path(super().translate_path(path))
        appended_html = Path(str(translated) + ".html")
        if appended_html.exists():
            return str(appended_html)

        if translated.suffix == "":
            sibling_html = translated.with_suffix(".html")
            if sibling_html.exists():
                return str(sibling_html)

        if translated.exists():
            return str(translated)

        root = Path(self.directory).resolve()
        rel = translated.resolve().relative_to(root) if root in translated.resolve().parents or translated.resolve() == root else None
        if rel is None:
            return str(translated)

        html = Path(str(root / rel) + ".html")
        if html.exists():
            return str(html)

        if translated.suffix == "":
            index = root / rel / "index.html"
            if index.exists():
                return str(index)

        return str(translated)


def main():
    parser = argparse.ArgumentParser(description="Serve Quartz public output with clean URL support.")
    parser.add_argument("--bind", default="100.89.89.46")
    parser.add_argument("--port", type=int, default=8081)
    parser.add_argument("--directory", default="/home/pi/quartz/public")
    parser.add_argument("--prefix", default="/quartz")
    args = parser.parse_args()

    os.chdir(args.directory)
    handler = lambda *a, **kw: CleanURLHandler(*a, directory=args.directory, **kw)
    server = ThreadingHTTPServer((args.bind, args.port), handler)
    server.url_prefix = args.prefix.rstrip("/")
    print(f"Serving {args.directory} on http://{args.bind}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
