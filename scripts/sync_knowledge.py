#!/usr/bin/env python3
"""Copy the canonical knowledge base into every skill's references/ folder.

Edit files in plugins/madison-park-holiday-feast/knowledge/, then run:

    python3 scripts/sync_knowledge.py          # copy
    python3 scripts/sync_knowledge.py --check  # exit 1 if any copy is stale

Each skill carries its own copy so it works on any platform that loads a
single skill folder (Claude Code, Claude.ai, Codex, ChatGPT), without relying
on paths outside the skill.
"""
import filecmp
import shutil
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent / "plugins" / "madison-park-holiday-feast"
KNOWLEDGE = PLUGIN / "knowledge"
SKILLS = PLUGIN / "skills"


def main() -> int:
    check = "--check" in sys.argv
    sources = sorted(KNOWLEDGE.glob("*.md"))
    if not sources:
        print(f"No knowledge files found in {KNOWLEDGE}", file=sys.stderr)
        return 1

    stale = []
    for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        refs = skill / "references"
        if check:
            for src in sources:
                dst = refs / src.name
                if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
                    stale.append(str(dst.relative_to(PLUGIN)))
            extra = {p.name for p in refs.glob("*.md")} - {s.name for s in sources} if refs.exists() else set()
            stale += [str((refs / n).relative_to(PLUGIN)) + " (extra)" for n in sorted(extra)]
            continue
        if refs.exists():
            shutil.rmtree(refs)
        refs.mkdir()
        for src in sources:
            shutil.copy2(src, refs / src.name)
        print(f"{skill.name}: {len(sources)} files")

    if check:
        if stale:
            print("Stale or missing reference copies:\n  " + "\n  ".join(stale))
            return 1
        print("All skill references are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
