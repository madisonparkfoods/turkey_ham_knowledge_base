# holiday-feast plugin

Skills and a knowledge base for cooking a Thanksgiving or holiday turkey or ham, and for using Madison Park Foods seasonings.

## Skills

| Skill | Use it for |
|---|---|
| `holiday-meal-planner` | Headcount → menu, quantities, guest assignments, shopping list, key dates |
| `turkey-roasting-coach` | Thawing, brining, seasoning, roasting (classic, spatchcock, breast, smoked, fried), doneness, carving |
| `holiday-ham-guide` | Identifying ham type, reheating or cooking, glazes, carving, leftovers |
| `cooking-timeline-builder` | Multi-day countdown and day-of schedule that fits one oven |
| `madison-park-pairing` | Which Madison Park product to use, how much, how it fits the salt plan, honest trade-offs |
| `holiday-kitchen-rescue` | Fast fixes when something goes wrong mid-cook |
| `food-safety-and-leftovers` | USDA temperatures, 2-hour rule, storage times, reheating, stock |
| `holiday-cooking-kb` | General lookups in the knowledge base and first-timer FAQs |

In Claude Code, skills are namespaced, e.g. `/holiday-feast:turkey-roasting-coach`. In Codex and ChatGPT, each skill's `agents/openai.yaml` sets its display name and starter prompt. On both, skills also trigger automatically when a request matches a skill's description.

## Knowledge base

`knowledge/` holds the canonical 19 Markdown files (start at `knowledge/00-index.md`). Each skill carries a generated copy in its own `references/` folder so it works as a standalone skill on any platform. Edit `knowledge/` only, then run `python3 scripts/sync_knowledge.py` from the repository root.

## Keeping it current

- Madison Park Foods prices, stock and formulas were checked on 2026-11-01. Update `knowledge/16-madison-park-foods.md` and `knowledge/sources.md` when they change.
- The Thanksgiving dates in the timeline and thawing files are for 2026 (Thursday, November 26). Update them each year.
- Bump `version` in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and the Claude marketplace entry when you publish changes.

## Install

```bash
# Claude Code
claude plugin marketplace add <owner>/<repo>    # or a local path to holiday-feast-marketplace
claude plugin install holiday-feast@holiday-feast-marketplace

# Codex / ChatGPT
codex plugin marketplace add <owner>/<repo>
codex plugin add holiday-feast@holiday-feast-marketplace
```
