#!/usr/bin/env python3
"""Check basic Markdown link integrity, research evidence structure and English-only policy."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINKS = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
errors = []
checked = 0
documents = 0

for doc in sorted(ROOT.rglob("*.md")):
    if ".git" in doc.parts or "node_modules" in doc.parts:
        continue
    documents += 1
    content = doc.read_text(encoding="utf-8")
    if CJK.search(content):
        errors.append(f"{doc.relative_to(ROOT)}: contains CJK characters (English-only policy)")
    for target in LINKS.findall(content):
        target = target.strip().split(" ", 1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#") or not parsed.path:
            continue
        resolved = (doc.parent / unquote(parsed.path)).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            errors.append(f"{doc.relative_to(ROOT)}: broken local link: {target}")
        checked += 1
    if doc.relative_to(ROOT).parts[0] == "studies":
        if not ("Source" in content or "source" in content):
            errors.append(f"{doc.relative_to(ROOT)}: missing source description")
        if "Verified" not in content:
            errors.append(f"{doc.relative_to(ROOT)}: missing Verified section")
        if "Inferred" not in content:
            errors.append(f"{doc.relative_to(ROOT)}: missing Inferred section")

must_exist = [
    "domains/README.md",
    "docs/RESEARCH_FRAMEWORK.md",
    "observations/anthropic/2026-09-18_to_2026-10-18.md",
    "observations/openai/2026-09-18_to_2026-10-18.md",
]
for required in must_exist:
    if not (ROOT / required).is_file():
        errors.append(f"Missing research foundation: {required}")

print(f"Validated {documents} Markdown files and {checked} relative links.")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Research checks passed.")
