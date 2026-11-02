#!/usr/bin/env python3
"""Build upload-ready artifacts in dist/.

    python3 scripts/build_dist.py

Produces:
  dist/skills/<skill>.zip     one zip per skill (SKILL.md + references/ + agents/),
                              for uploading a single skill to Claude.ai or ChatGPT
  dist/custom-gpt/knowledge/  the knowledge files to upload to a Custom GPT
  dist/custom-gpt/instructions.md
  dist/plugin/<plugin>.zip    the whole plugin folder, for the OpenAI plugin portal

Also checks that skill references are in sync, the Custom GPT
instructions fit the 8,000-character limit, the plugin's LICENSE copy
matches the root one, and the plugin folder has no OS junk files. Warns
about TODO placeholders that must be filled in before directory submission.
"""
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "madison-park-holiday-feast"
DIST = ROOT / "dist"
GPT_LIMIT = 8000
GPT_FILE_LIMIT = 20
JUNK = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}


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

    if (PLUGIN / "LICENSE").read_bytes() != (ROOT / "LICENSE").read_bytes():
        print("plugins/*/LICENSE differs from the root LICENSE; copy it over.", file=sys.stderr)
        return 1

    junk = [p for p in PLUGIN.rglob("*") if p.name in JUNK]
    if junk:
        print("Remove OS files from the plugin folder:\n  " + "\n  ".join(str(p.relative_to(ROOT)) for p in junk), file=sys.stderr)
        return 1

    todos = [p for p in PLUGIN.rglob("*") if p.is_file() and p.suffix in {".json", ".md"}
             and "/references/" not in p.as_posix() and "TODO-replace" in p.read_text()]
    for p in todos:
        print(f"WARNING: placeholder to fill in before submission: {p.relative_to(ROOT)}")

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "skills").mkdir(parents=True)
    for skill in sorted(p for p in (PLUGIN / "skills").iterdir() if (p / "SKILL.md").exists()):
        out = DIST / "skills" / f"{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, Path(skill.name) / f.relative_to(skill))
            z.write(PLUGIN / "LICENSE", Path(skill.name) / "LICENSE")
        print(f"dist/skills/{out.name}")

    (DIST / "plugin").mkdir()
    out = DIST / "plugin" / f"{PLUGIN.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(PLUGIN.rglob("*")):
            if f.is_file():
                z.write(f, Path(PLUGIN.name) / f.relative_to(PLUGIN))
    print(f"dist/plugin/{out.name}")

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
