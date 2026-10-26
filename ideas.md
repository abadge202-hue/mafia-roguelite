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
- heal() takes an amount so painkillers can reuse it
- attack() returns damage and blocked instead of printing (keep armor defense); combat.py handles messages (prep for graphics)
- add one-line doc strings
- NamedTuples for ENEMY_TYPES, ITEM_TYPES (name the fields; unpacking still works)
- Enum for room types so a typo errors instead of becoming an empty room
- @dataclass for Room and Item (replaces hand-writtien __init__)
## Tests
- test all enemy types for scaling