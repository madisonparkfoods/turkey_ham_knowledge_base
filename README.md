# Holiday Feast Marketplace

One plugin, **holiday-feast**, packaged for both **Claude** and **ChatGPT/Codex**: eight skills and a 19-file knowledge base for cooking a Thanksgiving or holiday turkey or ham, timing the meal, food safety and leftovers, and using Madison Park Foods products. A Custom GPT version is included for one-link sharing and the GPT Store.

| | Claude | ChatGPT / Codex |
|---|---|---|
| Skills | `skills/<name>/SKILL.md` (shared) | same files |
| Per-skill UI metadata | — | `skills/<name>/agents/openai.yaml` |
| Plugin manifest | `plugins/holiday-feast/.claude-plugin/plugin.json` | `plugins/holiday-feast/.codex-plugin/plugin.json` |
| Marketplace | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` |
| Single-assistant alternative | — | Custom GPT in `custom-gpt/` (GPT Store) |
| Single-skill uploads | `dist/skills/<name>.zip` | `dist/skills/<name>.zip` |

```
holiday-feast-marketplace/
├── .claude-plugin/marketplace.json        # Claude marketplace
├── .agents/plugins/marketplace.json       # ChatGPT / Codex marketplace
├── plugins/holiday-feast/
│   ├── .claude-plugin/plugin.json
│   ├── .codex-plugin/plugin.json
│   ├── README.md
│   ├── knowledge/                         # canonical knowledge base (19 files, start at 00-index.md)
│   └── skills/<8 skills>/
│       ├── SKILL.md
│       ├── agents/openai.yaml             # ChatGPT/Codex display name, starter prompt
│       └── references/                    # copy of knowledge/, generated
├── custom-gpt/                            # Custom GPT instructions + setup guide
├── scripts/
│   ├── sync_knowledge.py                  # copy knowledge/ into every skill's references/
│   └── build_dist.py                      # build dist/ and check limits
└── dist/                                  # generated upload files
```

**Why each skill carries its own `references/` copy:** platforms load a skill as a single folder, and ChatGPT doesn't document reading files outside it. Self-contained skills work everywhere, including as single-skill uploads. Edit only `plugins/holiday-feast/knowledge/`, then run `python3 scripts/sync_knowledge.py`.

## Claude Code

From the folder that contains `holiday-feast-marketplace/`:

```bash
claude plugin validate ./holiday-feast-marketplace
claude plugin marketplace add ./holiday-feast-marketplace
claude plugin install holiday-feast@holiday-feast-marketplace
```

In a session: `/plugin marketplace add ./holiday-feast-marketplace`, then `/plugin install holiday-feast@holiday-feast-marketplace`. Skills appear as `/holiday-feast:<skill>`.

From GitHub ([madisonparkfoods/turkey_ham_knowledge_base](https://github.com/madisonparkfoods/turkey_ham_knowledge_base)):

```bash
claude plugin marketplace add madisonparkfoods/turkey_ham_knowledge_base
claude plugin install holiday-feast@holiday-feast-marketplace
```

The contents of this folder must be the repository root (so `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` sit at the top level), or the GitHub install won't find the marketplace.

**Claude.ai (single skills):** upload a zip from `dist/skills/` in Claude.ai's skills settings.

## Codex and ChatGPT

```bash
codex plugin marketplace add ./holiday-feast-marketplace     # or madisonparkfoods/turkey_ham_knowledge_base
codex plugin add holiday-feast@holiday-feast-marketplace
codex plugin list
```

- **ChatGPT desktop app:** plugins from a repo marketplace (`.agents/plugins/marketplace.json`) or a personal one (`~/.agents/plugins/marketplace.json`) show up in the Plugins Directory after restarting the app. Skills bundled in plugins are also available in Chat and Work on ChatGPT web, desktop and mobile, per OpenAI's docs; availability varies by surface and plan.
- **Workspace:** ChatGPT workspace admins can publish the plugin to selected roles from ChatGPT Plugins.
- **Public:** OpenAI's universal plugin directory (shared by ChatGPT and Codex) takes submissions through a review process. Before submitting, check OpenAI's current requirements: allowed `category` values, logo and icon assets, privacy and terms URLs, and a license.

## Custom GPT (GPT Store)

See [`custom-gpt/README.md`](custom-gpt/README.md): paste `custom-gpt/instructions.md` (5,357 of 8,000 characters), upload the 19 knowledge files, add the four conversation starters. Share by link or publish to the GPT Store.

## Build

```bash
python3 scripts/sync_knowledge.py    # after editing knowledge/
python3 scripts/build_dist.py        # rebuild dist/ and check limits
```

## Try it

- "I'm hosting 12 people for Thanksgiving, first time. Plan it."
- "I have a 14 lb frozen turkey and the Chairman of the Bird rub. Walk me through it."
- "Build me a timeline for dinner at 4 PM with one oven, turkey plus a spiral ham."
- "The skin is getting too dark and the thighs are only at 150."
- "How long is leftover stuffing good for?"

## Notes

- Food-safety numbers follow USDA FSIS guidance (see `plugins/holiday-feast/knowledge/sources.md`).
- Madison Park Foods product details were checked 2026-11-01. This is Madison Park Foods' official holiday cooking plugin.
- Thanksgiving dates in the knowledge base are for 2026.
- Bump `version` in both plugin manifests and the Claude marketplace entry when publishing changes.
- No license is set. Add one before submitting to either public directory.
