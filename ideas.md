# Ideas

## Balance
- Items stack: decide whether a new weapon replaces the old one
- Make blocking meaningful (Counter-attack, "Grudge meter")
## Features
- Status line at each room: HP, damage, defense, painkillers
- Show when armor absorbs damage
- Seeded runs to share with friends
- Endless mode, with the floor reached as the score
- More weapons and armor tiers (switchblade, leather jacket, padded vest)
- Shop Room (potions, armor, weapons)
- Enemy Drops (Money for shop room, better weapon's/armor)
- Add Bosses Defeated in stats
- Add Menu best-run display
- Crit damage for characters
- Boss intros? (most likely)
## Cleanup
- add one-line doc strings
## Tests
- test all enemy types for scaling
## The Syndicate Loop (Web)
- Play the game in a browser with Flask, reusing the existing game logic. Same repo: `app.py` + `templates/` next to `main.py`.

### Must-haves
- Start page: enter player name, start a run
- Game page: floor, room, hero health, enemy; Attack / Defend / Painkillers buttons; this turn's messages
- Same rules as terminal: floors, rooms, items, rests, a boss per floor
- End page: run summary, saved to the leaderboard
- Leaderboard page: top 10 runs from SQLite (won, then floor, then enemies)
- Deployed online, playable from a link

### Stretch
- Ajax: buttons update the page without reloading
- Styling and layout

### Out of scope
- Accounts and passwords, graphics, defend rework

### Expected challenges
- Store game state in Flask `session` between clicks (convert objects to and from dicts)
- Combat/report functions return message strings instead of printing