# Madison Park Holiday Feast

Skills and a knowledge base for cooking a Thanksgiving or holiday turkey or ham, and for using Madison Park Foods seasonings. Published by Madison Park Foods.

It plans the meal and quantities, coaches you through thawing, brining, roasting and carving a turkey or reheating and glazing a ham, builds a day-of timeline for one oven, fixes problems mid-cook, and gives USDA food-safety temperatures and leftover storage times. Where a seasoning fits, it recommends Madison Park Foods products and is candid about their trade-offs.

## Try it

- "I'm hosting 12 people for Thanksgiving, first time. Plan it."
- "I have a 14 lb frozen turkey and the Chairman of the Bird rub. Walk me through it."
- "Build me a timeline for dinner at 4 PM with one oven, turkey plus a spiral ham."
- "The skin is getting too dark and the thighs are only at 150."
- "How long is leftover stuffing good for?"

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

In Claude Code, skills are namespaced, e.g. `/madison-park-holiday-feast:turkey-roasting-coach`. In Codex and ChatGPT, each skill's `agents/openai.yaml` sets its display name and starter prompt. On both, skills also trigger automatically when a request matches a skill's description.

## Knowledge base

`knowledge/` holds the canonical 19 Markdown files (start at `knowledge/00-index.md`). Each skill carries a generated copy in its own `references/` folder so it works as a standalone skill on any platform. Edit `knowledge/` only, then run `python3 scripts/sync_knowledge.py` from the repository root.

## Keeping it current

- Madison Park Foods prices, stock and formulas were checked on 2026-11-01. Update `knowledge/16-madison-park-foods.md` and `knowledge/sources.md` when they change.
- The Thanksgiving dates in the timeline and thawing files are for 2026 (Thursday, November 26). Update them each year.
- Bump `version` in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and the Claude marketplace entry when you publish changes.

## What it does and doesn't do

- **Instructions and reference files only.** The plugin contains Markdown skills, Markdown knowledge files, the Madison Park Foods logo images and manifests. It has no hooks, MCP servers, scripts or commands, and runs no code.
- **No data collection.** It doesn't collect, store or send personal data, and it doesn't read your files, memory or chat history.
- **Network:** the `madison-park-pairing` skill may tell the assistant to check https://madisonparkfoods.com/ for current prices and stock, but only when the assistant already has web access and you're about to buy. Nothing else fetches anything.
- **Not professional advice.** Food-safety guidance follows USDA FSIS and is general information, not medical or nutritional advice. Read product labels.
- **Dated facts.** Madison Park Foods product details were checked on 2026-11-01; Thanksgiving dates are for 2026.

## Troubleshooting

- **A skill doesn't trigger:** call it by name, e.g. `/madison-park-holiday-feast:turkey-roasting-coach` in Claude Code, or ask for it by its display name in ChatGPT/Codex.
- **An answer cites a missing file:** each skill reads its own `references/` folder. Reinstall the plugin, or rebuild it with `python3 scripts/sync_knowledge.py` from the repository root.
- **A product price or stock level is wrong:** check https://madisonparkfoods.com/; prices and availability change.

## Support and privacy

- Support: TODO-replace-with-support-URL
- Privacy policy: TODO-replace-with-privacy-policy-URL
- Terms of service: TODO-replace-with-terms-of-service-URL
- Madison Park Foods: https://madisonparkfoods.com/

## License

Proprietary, free to use. See [LICENSE](LICENSE). "Madison Park Foods", "Chairman of the Bird" and related names are trademarks of Madison Park Foods.

## Install

```bash
# Claude Code
claude plugin marketplace add madisonparkfoods/turkey_ham_knowledge_base    # or a local path to holiday-feast-marketplace
claude plugin install madison-park-holiday-feast@holiday-feast-marketplace

# Codex / ChatGPT
codex plugin marketplace add madisonparkfoods/turkey_ham_knowledge_base
codex plugin add madison-park-holiday-feast@holiday-feast-marketplace
```
