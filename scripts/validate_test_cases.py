from __future__ import annotations

import re
import sys
from pathlib import Path

case_files = sorted(Path("test-cases").glob("*.md"))
case_pattern = re.compile(r"^## (TC-[A-Z0-9]+-\d{3}) — .+$", re.MULTILINE)
required_markers = (
    "- **Requirement:** REQ-",
    "- **Priority:**",
    "- **Type:**",
    "### Preconditions",
    "### Steps",
    "### Expected result",
)

found: dict[str, Path] = {}
errors: list[str] = []

for path in case_files:
    text = path.read_text(encoding="utf-8")
    matches = list(case_pattern.finditer(text))

    if not matches:
        errors.append(f"{path}: no test cases found")
        continue

    for index, match in enumerate(matches):
        case_id = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end]

        if case_id in found:
            errors.append(f"{case_id}: duplicate in {found[case_id]} and {path}")
        else:
            found[case_id] = path

        for marker in required_markers:
            if marker not in block:
                errors.append(f"{case_id}: missing {marker}")

        steps = re.findall(r"^\d+\. .+", block, re.MULTILINE)
        if not steps:
            errors.append(f"{case_id}: no numbered steps found")

if errors:
    print("Test-case validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Validated {len(found)} test cases across {len(case_files)} suites.")
