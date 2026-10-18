"""Print the CHANGELOG.md section for one version (used by the release workflow).

Usage: python3 .github/scripts/changelog_section.py 0.7.2
Exits non-zero if the section is missing or empty, so a release is never
published without notes.
"""
import re
import sys

version = sys.argv[1]
lines = open("CHANGELOG.md", encoding="utf-8").read().splitlines()
start = next(
    (i for i, line in enumerate(lines) if re.match(rf"^## \[{re.escape(version)}\]", line)),
    None,
)
if start is None:
    sys.exit(f"No '## [{version}]' section in CHANGELOG.md")
end = next(
    (i for i in range(start + 1, len(lines)) if lines[i].startswith("## [")),
    len(lines),
)
body = "\n".join(lines[start + 1 : end]).strip()
if not body:
    sys.exit(f"The '## [{version}]' section in CHANGELOG.md is empty")
print(body)
