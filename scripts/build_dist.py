#!/usr/bin/env python3
"""Build upload-ready artifacts in dist/.

    python3 scripts/build_dist.py

Produces:
  dist/skills/<skill>.zip     one zip per skill (SKILL.md + references/ + agents/),
                              for uploading a single skill to Claude.ai or ChatGPT
  dist/custom-gpt/knowledge/  the knowledge files to upload to a Custom GPT
  dist/custom-gpt/instructions.md

Also checks that skill references are in sync and the Custom GPT
instructions fit the 8,000-character limit.
"""
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "holiday-feast"
DIST = ROOT / "dist"
GPT_LIMIT = 8000
GPT_FILE_LIMIT = 20


def main() -> int:
    sync = subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_knowledge.py"), "--check"])
    if sync.returncode:
        print("Run scripts/sync_knowledge.py first.", file=sys.stderr)
        return 1

    instructions = (ROOT / "custom-gpt" / "instructions.md").read_text()
    print(f"Custom GPT instructions: {len(instructions):,} / {GPT_LIMIT:,} characters")
    if len(instructions) > GPT_LIMIT:
        print("Instructions exceed the Custom GPT limit.", file=sys.stderr)
        return 1

    knowledge = sorted((PLUGIN / "knowledge").glob("*.md"))
    print(f"Custom GPT knowledge files: {len(knowledge)} / {GPT_FILE_LIMIT}")
    if len(knowledge) > GPT_FILE_LIMIT:
        print("Too many knowledge files for a Custom GPT.", file=sys.stderr)
        return 1

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "skills").mkdir(parents=True)
    for skill in sorted(p for p in (PLUGIN / "skills").iterdir() if (p / "SKILL.md").exists()):
        out = DIST / "skills" / f"{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, Path(skill.name) / f.relative_to(skill))
        print(f"dist/skills/{out.name}")

    gpt = DIST / "custom-gpt"
    (gpt / "knowledge").mkdir(parents=True)
    for f in knowledge:
        shutil.copy2(f, gpt / "knowledge" / f.name)
    shutil.copy2(ROOT / "custom-gpt" / "instructions.md", gpt / "instructions.md")
    shutil.copy2(ROOT / "custom-gpt" / "README.md", gpt / "README.md")
    print("dist/custom-gpt/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
