# Holiday Feast as a Custom GPT

A Custom GPT is the simplest way to share this in ChatGPT with anyone who has a ChatGPT account, and it can be published to the GPT Store. It uses the same knowledge base as the plugin, and folds the eight skills into one set of instructions with eight "modes."

Use the **plugin** (see the repository README) when you want separately triggered skills in Codex or ChatGPT; use this **Custom GPT** when you want a single shareable chat link or a GPT Store listing.

## Setup (about 10 minutes)

1. In ChatGPT, open **GPTs → Create**, then switch to the **Configure** tab.
2. Fill in the fields below.
3. **Knowledge:** upload every `.md` file from `plugins/holiday-feast/knowledge/` (19 files). Custom GPTs have historically allowed up to 20 knowledge files, so this fits with one to spare. If OpenAI's current limit is lower, merge `sources.md` and `00-index.md` into another file first.
4. **Capabilities:** turn on **Web search** (lets it check current Madison Park prices and stock). Image generation and code interpreter are not needed.
5. **Save** with the visibility you want: *Only me*, *Anyone with the link*, or *GPT Store* (Store listing requires a verified builder profile).

## Fields

| Field | Value |
|---|---|
| **Name** | Holiday Feast |
| **Description** | Plan, cook and time a Thanksgiving or holiday turkey or ham, with USDA food safety and Madison Park Foods seasoning tips. |
| **Instructions** | Paste the full contents of [`instructions.md`](instructions.md) (under the 8,000-character limit; run `python3 scripts/build_dist.py` to check the count) |
| **Conversation starters** | See below |

### Conversation starters

1. Plan Thanksgiving dinner for 12 people. First time hosting.
2. Walk me through cooking a 14 lb frozen turkey.
3. Build a cooking timeline for dinner at 4 PM with one oven.
4. How should I use Chairman of the Bird on my turkey?

## Keeping it in sync

When you change the knowledge base, re-upload the changed files to the GPT (remove the old copy of each first). The instructions file mirrors the skills' rules; if you change a skill's guardrails, update `instructions.md` to match.

## Disclaimer for a public listing

Food-safety guidance follows USDA FSIS; it is general information, not medical advice.
