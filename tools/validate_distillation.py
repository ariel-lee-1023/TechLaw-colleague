#!/usr/bin/env python3
"""Validate TechLaw cluster budgets and the runtime/documentation boundary.

The budget formula and script-density estimate mirror Books-to-Skill-Refs.
No third-party packages are required.
"""

from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 0.10
CAP = 8_500


@dataclass(frozen=True)
class Module:
    path: str
    sections: int

    @property
    def budget(self) -> int:
        # reference depth, text-heavy source
        return round(1_700 + (1_050 + 1_500 * math.sqrt(self.sections)) * 0.55)


MODULES = (
    Module("references/clusters/institutional-reflex.md", 18),
    Module("references/clusters/efficiency-refusal.md", 8),
    Module("references/clusters/doctrinal-mechanics.md", 20),
)

DENSE_RANGES = (
    (0x2E80, 0x2EFF), (0x3000, 0x303F), (0x3040, 0x309F),
    (0x30A0, 0x30FF), (0x3400, 0x4DBF), (0x4E00, 0x9FFF),
    (0xF900, 0xFAFF), (0xFF00, 0xFFEF), (0xAC00, 0xD7AF),
    (0x0E00, 0x0E7F), (0x20000, 0x2A6DF),
)


def is_dense(char: str) -> bool:
    point = ord(char)
    return any(low <= point <= high for low, high in DENSE_RANGES)


def estimate_tokens(text: str) -> int:
    dense = sum(is_dense(char) for char in text)
    return int(dense / 1.5 + (len(text) - dense) / 4.0)


def main() -> int:
    failures: list[str] = []
    print("module                                      tokens  target      band      cap")

    for module in MODULES:
        path = ROOT / module.path
        if not path.is_file():
            failures.append(f"missing runtime module: {module.path}")
            continue

        text = path.read_text(encoding="utf-8")
        tokens = estimate_tokens(text)
        budget = module.budget
        low = math.ceil(budget * (1 - TOLERANCE))
        high = math.floor(budget * (1 + TOLERANCE))
        print(f"{module.path:43} {tokens:6}  {budget:6}  {low:4}-{high:<4}  {CAP:6}")

        declared_sections = re.search(r"\*\*Coverage basis\*\*:\s*(\d+)", text)
        if not declared_sections or int(declared_sections.group(1)) != module.sections:
            failures.append(f"{module.path}: Coverage basis must declare {module.sections} sections")
        if tokens < low or tokens > high:
            failures.append(f"{module.path}: {tokens} tokens is outside {low}-{high}")
        if tokens > CAP:
            failures.append(f"{module.path}: {tokens} tokens exceeds the {CAP} hard cap")

    forbidden = ROOT / "references" / "provenance.md"
    if forbidden.exists():
        failures.append("maintainer provenance must live in fidelity-ledger/, not references/")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "fidelity-ledger/" in skill:
        failures.append("SKILL.md must not route runtime agents to maintainer-only fidelity-ledger files")
    for module in MODULES:
        if module.path not in skill:
            failures.append(f"SKILL.md does not route to {module.path}")

    if failures:
        print("\nFAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nPASS: all runtime modules satisfy the computed reference-depth budgets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
