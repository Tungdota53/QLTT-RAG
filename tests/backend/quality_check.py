#!/usr/bin/env python3
"""Dependency-free, reproducible quality gate for Model 1 foundation artifacts."""

from __future__ import annotations

import argparse
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
OWNED_PATHS = (
    ROOT / "packages" / "contracts",
    ROOT / "packages" / "sdk-typescript",
    ROOT / "tests" / "backend",
    ROOT / "tests" / "integration",
)
TEXT_SUFFIXES = {".json", ".js", ".mjs", ".py", ".ts"}
IGNORED_PARTS = {"__pycache__", "dist", "node_modules"}
SECRET_ASSIGNMENT = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|private[_-]?key)"
    r"\s*[=:]\s*['\"][^'\"]+['\"]"
)
SENSITIVE_JSON_KEYS = {
    "email_address", "health_detail", "latitude", "longitude", "phone_number",
    "precise_user_location", "resident_list",
}


def files(suffixes: set[str] | None = None) -> Iterable[Path]:
    for base in OWNED_PATHS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and not IGNORED_PARTS.intersection(path.parts):
                if suffixes is None or path.suffix in suffixes:
                    yield path


def resolve_json_pointer(document: object, fragment: str, reference: str) -> None:
    current = document
    if fragment:
        if not fragment.startswith("/"):
            raise ValueError(f"unsupported JSON reference fragment: {reference}")
        for raw_token in fragment[1:].split("/"):
            token = unquote(raw_token).replace("~1", "/").replace("~0", "~")
            if not isinstance(current, dict) or token not in current:
                raise ValueError(f"unresolved JSON reference: {reference}")
            current = current[token]


def walk_refs(value: object) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                yield child
            yield from walk_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_refs(child)


def check_python() -> None:
    for path in files({".py"}):
        py_compile.compile(str(path), doraise=True)


def check_json_and_refs() -> None:
    cache: dict[Path, object] = {}
    json_paths = list(files({".json"}))
    for path in json_paths:
        cache[path.resolve()] = json.loads(path.read_text(encoding="utf-8"))
    for source in json_paths:
        document = cache[source.resolve()]
        for reference in walk_refs(document):
            file_part, marker, fragment = reference.partition("#")
            if "://" in file_part:
                continue
            target = (source.parent / unquote(file_part)).resolve() if file_part else source.resolve()
            if target not in cache:
                raise ValueError(f"missing local JSON reference target: {source}: {reference}")
            if marker:
                resolve_json_pointer(cache[target], fragment, reference)


def check_safety_and_hygiene() -> None:
    for path in files(TEXT_SUFFIXES):
        display_path = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise ValueError(f"UTF-8 BOM is not allowed: {display_path}")
        text = raw.decode("utf-8")
        if SECRET_ASSIGNMENT.search(text):
            raise ValueError(f"possible hard-coded secret: {display_path}")
        if any(line.rstrip("\r\n").endswith((" ", "\t")) for line in text.splitlines(keepends=True)):
            raise ValueError(f"trailing whitespace: {display_path}")
    fixture = ROOT / "packages" / "sdk-typescript" / "fixtures" / "mock-data.json"
    payload = json.loads(fixture.read_text(encoding="utf-8"))
    serialized = json.dumps(payload).lower()
    for key in SENSITIVE_JSON_KEYS:
        if f'"{key}"' in serialized:
            raise ValueError(f"sensitive fixture key is prohibited: {key}")
    identifiers = re.findall(r'"(?:[a-z_]+_id)"\s*:\s*"([^"]+)"', serialized)
    if identifiers and not all("synthetic" in value for value in identifiers):
        raise ValueError("fixture identifiers must be explicitly synthetic")


def run(command: list[str], cwd: Path = ROOT) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def typescript_compiler() -> str:
    override = os.environ.get("SAFEZONE_TSC")
    candidates = [
        Path(override) if override else None,
        ROOT / "node_modules" / ".bin" / ("tsc.cmd" if os.name == "nt" else "tsc"),
        ROOT / "packages" / "sdk-typescript" / "node_modules" / ".bin" / ("tsc.cmd" if os.name == "nt" else "tsc"),
    ]
    for candidate in candidates:
        if candidate and candidate.is_file():
            return str(candidate)
    available = shutil.which("tsc")
    if available:
        return available
    raise RuntimeError(
        "TypeScript compiler unavailable. Restore the pinned workspace dependencies or set "
        "SAFEZONE_TSC to an existing tsc executable; this check never downloads packages."
    )


def run_all() -> None:
    print("[quality] Python compile")
    check_python()
    print("[quality] JSON parse and local references")
    check_json_and_refs()
    print("[quality] synthetic/secret/sensitive scan and hygiene")
    check_safety_and_hygiene()
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests/backend", "-v"])
    sdk = ROOT / "packages" / "sdk-typescript"
    run([shutil.which("node") or "node", "scripts/generate.mjs", "--check"], sdk)
    node_tests = sorted((sdk / "test").glob("*.test.mjs")) + sorted((ROOT / "tests/integration").glob("*.test.mjs"))
    run([shutil.which("node") or "node", "--test", *map(str, node_tests)])
    compiler = typescript_compiler()
    run([compiler, "-p", "tsconfig.json", "--noEmit"], sdk)
    run([compiler, "-p", "tsconfig.build.json", "--noEmit"], sdk)
    print("[quality] PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true", help="run dependency-free static checks only")
    args = parser.parse_args()
    try:
        if args.self_check:
            check_python()
            check_json_and_refs()
            check_safety_and_hygiene()
            print("[quality] self-check PASS")
        else:
            run_all()
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f"[quality] FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
