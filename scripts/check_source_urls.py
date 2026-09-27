#!/usr/bin/env python3
"""Check canonical source URLs without mutating analytical data."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = [ROOT / "sources.csv", ROOT / "data" / "source_registry.csv"]
USER_AGENT = "Mozilla/5.0 (compatible; SEGSourceCheck/1.0; +https://selguetagodoy.github.io/)"
TIMEOUT = 20


def find_registry() -> Path:
    for path in CANDIDATES:
        if path.exists():
            return path
    raise FileNotFoundError("No canonical source registry found (sources.csv or data/source_registry.csv)")


def check(url: str) -> tuple[str, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return "OK", str(response.status)
    except HTTPError as exc:
        if exc.code == 405 or exc.code >= 500:
            try:
                request = Request(
                    url,
                    headers={"User-Agent": USER_AGENT, "Range": "bytes=0-1023"},
                    method="GET",
                )
                with urlopen(request, timeout=TIMEOUT) as response:
                    return "OK", str(response.status)
            except HTTPError as fallback:
                exc = fallback
            except URLError as fallback:
                return "DEAD", f"network: {fallback.reason}"
        if 400 <= exc.code < 500:
            return "WARN", f"HTTP {exc.code}"
        return "DEAD", f"HTTP {exc.code}"
    except URLError as exc:
        return "DEAD", f"network: {exc.reason}"
    except Exception as exc:  # noqa: BLE001
        return "DEAD", str(exc)


def main() -> int:
    registry = find_registry()
    with registry.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if not rows:
        print(f"ERROR: {registry.relative_to(ROOT)} is empty")
        return 2

    dead = 0
    warn = 0
    checked = 0
    print(f"# Source URL Liveness — {registry.relative_to(ROOT)}\n")

    for row in rows:
        url = (row.get("url") or row.get("official_url") or "").strip()
        source_id = (row.get("source_id") or row.get("id") or "source").strip()
        publisher = (row.get("publisher") or row.get("institution") or "").strip()
        if not url:
            print(f"- SKIP {source_id} {publisher} — no URL (composite or non-URL source)")
            continue
        checked += 1
        label, detail = check(url)
        print(f"- {label} {source_id} {publisher} — {detail} — {url}")
        if label == "DEAD":
            dead += 1
        elif label == "WARN":
            warn += 1

    print(f"\nSummary: {checked} checked · {checked-dead-warn} OK · {warn} WARN · {dead} DEAD")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
