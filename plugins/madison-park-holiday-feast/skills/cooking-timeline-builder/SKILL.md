---
name: cooking-timeline-builder
description: Build a reverse-scheduled cooking timeline for a holiday meal - a multi-day countdown (thawing, brining, make-ahead dishes) and a minute-by-minute day-of schedule that fits turkey, ham and sides into the available oven, stovetop and slow cookers. Use when someone asks when to start the turkey, how to time dinner, or how to fit everything into one oven.
---

# Cooking Timeline Builder

## Knowledge base

In `references/` inside this skill's folder:

- `10-day-of-timeline.md` — method, sample schedules, one-oven strategy, recovery
- `01-quick-reference.md` — thaw times, roast and ham times, rest times
- `04-thawing.md` — thaw start dates
- `06-roasting-turkey.md`, `07-ham.md` — main-dish methods
- `09-stuffing-and-sides.md` — side-dish oven temps, times and make-ahead options
- `08-gravy.md` — make-ahead gravy

## Inputs

Get (or assume and state): serving time and date; main(s) with weight and method; list of sides; equipment (ovens, burners, slow cookers, grill, toaster oven); what's already made ahead; and whether the turkey is frozen.

## Method

1. **Work backward from serving time** for each main: serving − carve (15 min) − rest (30–45 min turkey, 10–20 ham) − cook time (upper end of the estimate) − 45–60 min buffer − 1 h tempering.
2. **Assign every side to a resource** (oven, stovetop, slow cooker, make-ahead, guest). Put high-heat oven sides in the turkey's rest window.
3. **Check for conflicts**: two dishes at different oven temperatures at the same time, too many burners, too many dishes on one rack. Resolve by moving dishes to make-ahead, slow cooker, stovetop or guests, or by baking at a compromise temperature with adjusted times.
4. **Multi-day countdown** if the meal is days away: frozen-turkey thaw date (fridge ~1 day per 4–5 lb + 1 day cushion), dry-brine start (1–3 days before), make-ahead items (cranberry sauce, gravy, pies, potatoes, assembled casseroles), shopping, table setting.
5. **Add checkpoints**: first thermometer check, oven temperature changes, "put leftovers away by" (2 hours after serving).

## Output

- A countdown table by date (if multi-day).
- A day-of table: time | task | resource (oven/stove/slow cooker/counter).
- A short "if the turkey is early / late" note from `10-day-of-timeline.md`.

If the user wants reminders, offer to set scheduled reminders for key steps (thaw start, brine start, turkey in, temperature check) using whatever scheduling tool is available in the session; otherwise suggest phone alarms. Offer to save the timeline as a document if they'll print it.

## Guardrails

- Time estimates are estimates. Always say the turkey is done by thermometer, not clock.
- Include the 2-hour leftover rule at the end of the day.
