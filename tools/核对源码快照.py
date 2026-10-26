#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""核对 CK3 Mod 源码的字节、BOM、换行与 SHA-256；不验证游戏行为。"""
import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath


def run(repo: Path, manifest_file: Path) -> int:
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    errors = []
    warnings = []
    paths_seen = set()
    files = manifest["files"]
    for item in files:
        name = item["path"]
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or name in paths_seen:
            errors.append(f"INVALID_PATH_OR_DUPLICATE: {name}")
            continue
        paths_seen.add(name)
        file_path = repo.joinpath(*path.parts)
        if not file_path.is_file():
            errors.append(f"MISSING: {name}")
            continue
        data = file_path.read_bytes()
        if len(data) != item["bytes"]:
            errors.append(f"SIZE_MISMATCH: {name}: {len(data)} != {item['bytes']}")
        digest = hashlib.sha256(data).hexdigest()
        if digest != item["sha256"]:
            errors.append(f"SHA256_MISMATCH: {name}")
        if data.startswith(b"\xef\xbb\xbf") != bool(item["bom"]):
            errors.append(f"BOM_MISMATCH: {name}")
        if data.count(b"\r\n") != item["crlf"]:
            errors.append(f"CRLF_MISMATCH: {name}")
        try:
            data.decode("utf-8-sig")
        except UnicodeDecodeError:
            errors.append(f"INVALID_UTF8: {name}")

    for name in manifest.get("known_exclusions", []):
        if not (repo / name).is_file():
            warnings.append(f"EXCLUDED_GUI_REQUIRES_SEPARATE_REVIEW: {name}")

    verified_count = len(files) - sum(e.startswith("MISSING:") for e in errors)
    print(f"Snapshot: {manifest['source_snapshot']}")
    print(f"Present: {verified_count}/{len(files)}")
    for w in warnings:
        print(f"WARN {w}")
    for e in errors:
        print(f"FAIL {e}")
    if errors:
        print("RESULT: INCOMPLETE_OR_CHANGED (not release-ready)")
        return 2
    print("RESULT: BYTE_CHECK_PASS (not engine/game validation)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    return run(args.repo, args.manifest or args.repo / "docs" / "源码清单_20261017.json")


if __name__ == "__main__":
    sys.exit(main())
