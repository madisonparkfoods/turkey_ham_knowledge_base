---
name: holiday-meal-planner
description: Plan a Thanksgiving or holiday dinner from a headcount - choose turkey, ham or both, size the main and sides, handle dietary needs, assign guest dishes, and produce a combined shopping list and make-ahead plan. Use when someone is planning a holiday meal, asks how much food to buy, or is hosting for the first time.
---

# Holiday Meal Planner

Turn "I'm hosting N people" into a concrete menu, quantities, shopping list and prep plan.

## Knowledge base

The knowledge base is in `references/` inside this skill's folder. Read what you need:

- `01-quick-reference.md` — per-person quantities, temperatures, thaw times
- `02-planning-and-quantities.md` — menu size, dietary needs, guest assignments
- `03-buying-turkey-and-ham.md` — sizes, labels, when to buy
- `09-stuffing-and-sides.md` — side recipes and make-ahead notes
- `10-day-of-timeline.md` — countdown schedule
- `16-madison-park-foods.md` — product options, if the user wants them

Use the knowledge base's numbers rather than memory, so answers stay consistent across skills.

## Gather (ask only what's missing, in one message)

1. Number of guests (adults / kids) and the date
2. Turkey, ham, both, or undecided
3. Dietary needs (vegetarian, gluten-free, allergies, low sodium)
4. Oven situation (one oven? second oven, grill, slow cookers?)
5. Whether guests will bring dishes
6. Whether they want to use Madison Park Foods products

If the user just wants a quick answer, make reasonable assumptions (one oven, no restrictions, leftovers wanted), state them in one line, and proceed.

## Produce

1. **Main(s)** with size, using 1–1½ lb per person for whole turkey, ¾ lb bone-in ham, ⅓–½ lb boneless ham. Above ~18 lb, suggest two smaller birds or a bird plus a breast.
2. **Menu**: one starch, one stuffing, one or two vegetables, cranberry sauce, gravy, rolls, dessert; adjust for headcount and dietary needs. Balance oven use (see `10-day-of-timeline.md`).
3. **Quantities table** for each dish, from the per-person table.
4. **Guest assignments**: oven-free dishes (pies, salads, rolls, drinks, ice); keep the main and gravy for the host.
5. **Shopping list**, combined across recipes and split into *buy now* and *buy 1–3 days before*. Include commonly forgotten items (thermometer, foil, stock, butter, flour/cornstarch, ice, containers).
6. **Key dates**: thaw start date for a frozen turkey (refrigerator, ~1 day per 4–5 lb, plus a day of cushion), dry-brine start, make-ahead days.
7. **Madison Park options** (only if wanted): default recommendation is the salt-free Chairman of the Bird rub with a salt dry brine; the EASYBRINE kit only as a wet-brine alternative, never combined with a dry brine.

## Output format

Use short sections with tables for quantities and the shopping list. If the user wants to keep the plan, offer to save it as a document or file. Finish by offering the next step: a day-of timeline (`cooking-timeline-builder` skill) or turkey/ham method (`turkey-roasting-coach` / `holiday-ham-guide`).

## Guardrails

- Food-safety numbers come from `01-quick-reference.md` and `12-food-safety.md` (USDA). Don't loosen them.
- Flag kosher/enhanced turkeys: no brining.
- Don't invent Madison Park product details; use `16-madison-park-foods.md` and note that products and prices were checked on its stated date.
