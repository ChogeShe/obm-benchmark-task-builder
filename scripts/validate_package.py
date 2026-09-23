#!/usr/bin/env python3
"""Dependency-free validation for the public OBM benchmark task builder bundle."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "skills" / "benchmark-task-wizard" / "SKILL.md"
HUMANIZER = ROOT / "skills" / "humanizer"
MANIFEST = ROOT / "bundle-manifest.json"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")


def read_text(path: Path) -> str:
    require_file(path)
    return path.read_text(encoding="utf-8")


def main() -> int:
    for path in (MAIN, PLUGIN, MANIFEST, HUMANIZER / "SKILL.md", HUMANIZER / "README.md", HUMANIZER / "LICENSE"):
        require_file(path)

    main_text = read_text(MAIN)
    if not main_text.startswith("---\n") or "name: benchmark-task-wizard" not in main_text:
        fail("main Skill frontmatter is missing or has the wrong name")
    if "[TODO" in main_text or "<your" in main_text.lower():
        fail("main Skill contains an unfinished placeholder")

    plugin = json.loads(read_text(PLUGIN))
    if plugin.get("name") != "obm-benchmark-task-builder":
        fail("plugin name does not match the repository")
    if plugin.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")

    bundle = json.loads(read_text(MANIFEST))
    if bundle.get("name") != plugin.get("name"):
        fail("bundle manifest name does not match plugin name")
    if len(bundle.get("components", [])) != 2:
        fail("bundle manifest should list the wizard and humanizer components")

    # Do not let obvious private or generated artifacts enter the public bundle.
    forbidden_names = {".env", ".DS_Store", "credentials.json", "api_keys.local.json"}
    forbidden_parts = {"__pycache__", ".git", "harbor_validation", "trae_validation"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        # Repository metadata belongs to the source checkout, not the Skill bundle.
        if ".git" in rel.parts:
            continue
        if path.name in forbidden_names or any(part in forbidden_parts for part in rel.parts):
            fail(f"forbidden private/generated file: {rel}")
        if path.name.startswith("._"):
            fail(f"macOS metadata file must not be published: {rel}")

    # Keep the vendored version explicit and preserve its attribution.
    humanizer_text = read_text(HUMANIZER / "SKILL.md")
    if 'metadata:\n  version: "2.9.1"' not in humanizer_text:
        fail("vendored Humanizer version is not 2.9.1")
    if "MIT License" not in read_text(HUMANIZER / "LICENSE"):
        fail("vendored Humanizer license is missing")
    if "https://github.com/blader/humanizer" not in read_text(ROOT / "THIRD_PARTY_NOTICES.md"):
        fail("Humanizer source attribution is missing")

    print("OK: plugin bundle structure, attribution, placeholders, and private-file scan passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
