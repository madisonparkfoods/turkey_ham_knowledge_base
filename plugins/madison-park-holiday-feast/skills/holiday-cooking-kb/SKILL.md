---
name: holiday-cooking-kb
description: Look up answers in the Holiday Feast knowledge base for any Thanksgiving or holiday cooking question not covered by a more specific skill - buying, thawing, brining, roasting, ham, gravy, stuffing and sides, timing, carving, hosting, equipment, food safety, leftovers and Madison Park Foods products. Use for general holiday-cooking questions and first-timer FAQs.
---

# Holiday Cooking Knowledge Base

## Where it is

The knowledge base is in `references/` inside this skill's folder. Start with `00-index.md` for the file map, or `17-first-timer-faq.md` for short answers with links.

## How to answer

1. Find the relevant file(s) from the index; read only what you need.
2. Answer directly, with the specific numbers from the knowledge base.
3. Keep the knowledge base's distinctions: USDA safety minimums vs. common cooking practice; label/product-page facts vs. reseller listings vs. serving suggestions.
4. If the question is better served by a dedicated skill, use it:
   - planning a whole meal → `holiday-meal-planner`
   - cooking a turkey → `turkey-roasting-coach`
   - ham → `holiday-ham-guide`
   - scheduling → `cooking-timeline-builder`
   - Madison Park products → `madison-park-pairing`
   - something going wrong now → `holiday-kitchen-rescue`
   - safety and leftovers → `food-safety-and-leftovers`
5. If the knowledge base doesn't cover it, say so and answer from general cooking knowledge, keeping food-safety rules intact. For anything that changes over time (prices, stock, current dates), check a current source if one is available.

## Updating the knowledge base

Product facts in `16-madison-park-foods.md` are dated. When the user provides newer information (a new label, price, product), suggest updating the canonical copy in the plugin's `knowledge/` folder and the date in `sources.md`, then running `python3 scripts/sync_knowledge.py` from the repository root to refresh every skill's `references/`.
