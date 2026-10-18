#!/usr/bin/env python3
"""Minimal offline research integrity checker: local Markdown links and study evidence fields."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINKS = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
errors = []
checked = 0

for doc in sorted(ROOT.rglob("*.md")):
    if ".git" in doc.parts or "node_modules" in doc.parts:
        continue
    content = doc.read_text(encoding="utf-8")
    for target in LINKS.findall(content):
        target = target.strip().split(" ", 1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#") or not parsed.path:
            continue
        resolved = (doc.parent / unquote(parsed.path)).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            errors.append(f"{doc.relative_to(ROOT)}: broken local link: {target}")
        checked += 1
    if "studies/" in doc.relative_to(ROOT).as_posix():
        if "来源" not in content and "Source" not in content:
            errors.append(f"{doc.relative_to(ROOT)}: no source field")
        if "Verified" not in content:
            errors.append(f"{doc.relative_to(ROOT)}: missing Verified section")
        if "Inferred" not in content:
            errors.append(f"{doc.relative_to(ROOT)}: missing Inferred section")

print(f"Checked {checked} relative Markdown links across research files.")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Research integrity check passed.")
