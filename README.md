# Holiday Feast Marketplace

One plugin, **madison-park-holiday-feast**, packaged for **Claude**, **ChatGPT/Codex** and **Gemini CLI**: eight skills and a 19-file knowledge base for cooking a Thanksgiving or holiday turkey or ham, timing the meal, food safety and leftovers, and using Madison Park Foods products. A Custom GPT version is included for one-link sharing and the GPT Store.

| | Claude | ChatGPT / Codex | Gemini CLI |
|---|---|---|---|
| Skills | `skills/<name>/SKILL.md` (shared) | same files | same files |
| Per-skill UI metadata | — | `skills/<name>/agents/openai.yaml` | — |
| Plugin manifest | `plugins/madison-park-holiday-feast/.claude-plugin/plugin.json` | `plugins/madison-park-holiday-feast/.codex-plugin/plugin.json` | `plugins/madison-park-holiday-feast/gemini-extension.json` |
| Always-loaded context | — | — | `plugins/madison-park-holiday-feast/GEMINI.md` |
| Marketplace | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` | Extension gallery (GitHub release + repo topic) |
| Single-assistant alternative | — | Custom GPT in `custom-gpt/` (GPT Store) | — |
| Single-skill uploads | `dist/skills/<name>.zip` | `dist/skills/<name>.zip` | — |
| Directory upload archive | — (submit the GitHub repo) | `dist/plugin/madison-park-holiday-feast.zip` | `dist/gemini/madison-park-holiday-feast.zip` (release asset) |

```
holiday-feast-marketplace/
├── .claude-plugin/marketplace.json        # Claude marketplace
├── .agents/plugins/marketplace.json       # ChatGPT / Codex marketplace
├── plugins/madison-park-holiday-feast/
│   ├── .claude-plugin/plugin.json
│   ├── .codex-plugin/plugin.json
│   ├── gemini-extension.json              # Gemini CLI extension manifest
│   ├── GEMINI.md                          # Gemini CLI context (skill list, guardrails)
│   ├── README.md                          # also the directory listing description
│   ├── LICENSE                            # copy of the root LICENSE
│   ├── assets/                            # logo and composer icon (Madison Park Foods emblem)
│   ├── knowledge/                         # canonical knowledge base (19 files, start at 00-index.md)
│   └── skills/<8 skills>/
│       ├── SKILL.md
│       ├── agents/openai.yaml             # ChatGPT/Codex display name, starter prompt
│       └── references/                    # copy of knowledge/, generated
├── custom-gpt/                            # Custom GPT instructions + setup guide
├── scripts/
│   ├── sync_knowledge.py                  # copy knowledge/ into every skill's references/
│   └── build_dist.py                      # build dist/ and check limits
├── dist/                                  # generated upload files
├── LICENSE
└── PUBLISHING.md                          # directory submission checklist
```

**Why each skill carries its own `references/` copy:** platforms load a skill as a single folder, and ChatGPT doesn't document reading files outside it. Self-contained skills work everywhere, including as single-skill uploads. Edit only `plugins/madison-park-holiday-feast/knowledge/`, then run `python3 scripts/sync_knowledge.py`.

## Claude Code

From the folder that contains `holiday-feast-marketplace/`:

```bash
claude plugin validate ./holiday-feast-marketplace
claude plugin marketplace add ./holiday-feast-marketplace
claude plugin install madison-park-holiday-feast@holiday-feast-marketplace
```

In a session: `/plugin marketplace add ./holiday-feast-marketplace`, then `/plugin install madison-park-holiday-feast@holiday-feast-marketplace`. Skills appear as `/madison-park-holiday-feast:<skill>`.

From GitHub ([madisonparkfoods/turkey_ham_knowledge_base](https://github.com/madisonparkfoods/turkey_ham_knowledge_base)):

```bash
claude plugin marketplace add madisonparkfoods/turkey_ham_knowledge_base
claude plugin install madison-park-holiday-feast@holiday-feast-marketplace
```

The contents of this folder must be the repository root (so `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` sit at the top level), or the GitHub install won't find the marketplace.

**Claude.ai (single skills):** upload a zip from `dist/skills/` in Claude.ai's skills settings.

## Codex and ChatGPT

```bash
codex plugin marketplace add ./holiday-feast-marketplace     # or madisonparkfoods/turkey_ham_knowledge_base
codex plugin add madison-park-holiday-feast@holiday-feast-marketplace
codex plugin list
```

- **ChatGPT desktop app:** plugins from a repo marketplace (`.agents/plugins/marketplace.json`) or a personal one (`~/.agents/plugins/marketplace.json`) show up in the Plugins Directory after restarting the app. Skills bundled in plugins are also available in Chat and Work on ChatGPT web, desktop and mobile, per OpenAI's docs; availability varies by surface and plan.
- **Workspace:** ChatGPT workspace admins can publish the plugin to selected roles from ChatGPT Plugins.
- **Public:** OpenAI's universal plugin directory (shared by ChatGPT and Codex) takes submissions through a review process. Upload `dist/plugin/madison-park-holiday-feast.zip` in the OpenAI plugin portal; see [`PUBLISHING.md`](PUBLISHING.md) for what to finish first.

## Gemini CLI

Gemini CLI has no marketplace file. It installs an extension from a local folder or a GitHub repository, and its public gallery at geminicli.com/extensions indexes GitHub repositories on its own. The plugin folder doubles as the extension: `gemini-extension.json` and `GEMINI.md` sit next to the shared `skills/`, which Gemini CLI loads as agent skills.

```bash
gemini extensions install ./holiday-feast-marketplace/plugins/madison-park-holiday-feast
gemini extensions list
```

Gemini CLI wants `gemini-extension.json` at the root of the repository or of a release archive, and here it is one folder down. So for a GitHub install, attach `dist/gemini/madison-park-holiday-feast.zip` to a GitHub release, which has the manifest at its root:

```bash
gemini extensions install https://github.com/madisonparkfoods/turkey_ham_knowledge_base
```

Gemini CLI uses the Latest release's archive. Install a specific version with `--ref <tag>`. See [`PUBLISHING.md`](PUBLISHING.md) for gallery listing.

## Custom GPT (GPT Store)

See [`custom-gpt/README.md`](custom-gpt/README.md): paste `custom-gpt/instructions.md` (5,592 of 8,000 characters), upload the 19 knowledge files, add the four conversation starters. Share by link or publish to the GPT Store.

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

- Food-safety numbers follow USDA FSIS guidance (see `plugins/madison-park-holiday-feast/knowledge/sources.md`).
- Madison Park Foods product details were checked 2026-11-01. This is Madison Park Foods' official holiday cooking plugin.
- Thanksgiving dates in the knowledge base are for 2026.
- Bump `version` in all three plugin manifests (Claude, Codex, Gemini) and the Claude marketplace entry when publishing changes. `build_dist.py` fails if they differ.
- License: proprietary, free to use. See [`LICENSE`](LICENSE) (a copy sits in the plugin folder, where both directories look for it).
- Before submitting to the Claude, OpenAI or Gemini directory, work through [`PUBLISHING.md`](PUBLISHING.md).
