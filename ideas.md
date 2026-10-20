# Ideas

## Balance
- Weight room types so empty rooms are rarer (random.choices with weights)
- Items stack: decide whether a new weapon replaces the old one
- Check the Underboss is beatable after three floors
- Make blocking meaningful (Counter-attack, "Grudge meter")

## Features
- Status line at each room: HP, damage, defense, painkillers
- Show when armor absorbs damage
- Don't let painkillers be used at full health
- Seeded runs to share with friends
- Endless mode, with the floor reached as the score
- More weapons and armor tiers (switchblade, leather jacket, padded vest)
- Shop Room (potions, armor, weapons)
- Enemy Drops (Money for shop room, better weapon's/armor)
- Add Bosses Defeated in stats
- Add Menu best-run display
- Crit damage for characters
## Cleanup
- heal() takes an amount so painkillers can reuse it
- attack() returns damage and blocked instead of printing (keep armor defense); combat.py handles messages (prep for graphics)