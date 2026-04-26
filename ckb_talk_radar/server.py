from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class RadarRequestHandler(SimpleHTTPRequestHandler):
    def rewrite_path(self) -> None:
        if self.path in {"", "/"}:
            self.path = "/latest/index.html"
        elif self.path == "/rss.xml":
            self.path = "/latest/rss.xml"
        elif self.path == "/report.md":
            self.path = "/latest/report.md"
        elif self.path == "/snapshot.json":
            self.path = "/latest/snapshot.json"

    def do_GET(self) -> None:
        self.rewrite_path()
        super().do_GET()

    def do_HEAD(self) -> None:
        self.rewrite_path()
        super().do_HEAD()


def serve_output_dir(output_dir: str | Path, *, host: str, port: int) -> None:
    directory = str(Path(output_dir).resolve())
    handler = partial(RadarRequestHandler, directory=directory)
    httpd = ThreadingHTTPServer((host, port), handler)
    print(f"Serving CKB Talk Radar at http://{host}:{port}")
    print(f"Dashboard: http://{host}:{port}/")
    print(f"RSS: http://{host}:{port}/rss.xml")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        httpd.server_close()
