# Ideas

## Defend rework: telegraphed crits + grudge meter
Done: crit settings and wind-up flag, telegraphed enemy crits.
- Crit tests: a crit multiplies damage, a blocked crit is halved (seeded)
- Grudge meter: blocking fills it by damage absorbed (cap GRUDGE_MAX), resets each fight, shown in the fight prompt
- "(4) Settle the Score": only at full grudge, GRUDGE_MULTIPLIER x damage, resets the meter
- `sim.py`: bots play thousands of seeded fights per strategy and print win rates
- Tune config until smart play beats mashing 1, then update the README's known issues
- Option: let enemies open a fight already winding up

## Balance
- Items stack: decide whether a new weapon replaces the old one

## Features
- Status line at each room: HP, damage, defense, meds
- Show when armor absorbs damage
- Per-enemy wind-up and crit lines stored in config (template strings filled with `.format`)
- Choose which med to use when carrying more than one kind
- More weapons and armor tiers (switchblade, leather jacket, padded vest)
- Enemy drops: money for a shop room, better weapons and armor
- Shop room: buy meds, armor and weapons
- Boss intro lines
- Seeded runs to share with friends
- Endless mode, with the floor reached as the score

## Roguelite progression (v2.0 idea)
- Runs earn a currency you keep (cash in empty rooms, favors from bosses)
- A safehouse between runs to spend it on permanent upgrades
- Saved to disk (JSON or the runs database)

## Cleanup
- `enemy_turn` returns whether a wind-up started instead of printing it
- Item names: drop the article from "an Overcoat" so messages read naturally
- Status strings in `use_potion` ("used", "full", "none") become an Enum

## Tests
- Floor scaling test checks every enemy type, not one random pick
- `save_run` test using pytest's `tmp_path`, so tests never write to the real `runs.db`

## The Syndicate Loop (Web): CS50 final project
Play the game in a browser with Flask, reusing the existing game logic. Same repo: `app.py` + `templates/` next to `main.py`.

### Must-haves
- Start page: enter player name, start a run
- Game page: floor, room, hero health, enemy; Attack / Defend / Patch Up buttons; this turn's messages
- Same rules as terminal: floors, rooms, items, rests, a boss per floor, telegraphed crits
- End page: run summary, saved to the leaderboard
- Leaderboard page: top 10 runs from SQLite (won, then floor, then enemies)
- Deployed online, playable from a link

### Stretch
- Ajax: buttons update the page without reloading
- Styling and layout

### Out of scope
- Accounts and passwords, graphics

### Expected challenges
- Store game state in Flask `session` between clicks (convert objects to and from dicts)
- Combat/report functions return message strings instead of printing

### Done
- Enemies wind up (telegraphed), next hit is a crit
- Menu best run
- Add Bosses Defeated in stats
- Weighted items
- Weight enemy encounters