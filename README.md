# The Syndicate Loop

A turn-based terminal roguelite where you fight your way up a mafia family, floor by floor.

## How to run
- Requires Python 3.10+
- Clone or download the repo, then run `python main.py` in the project folder

## How to play
- Press 1 to attack the enemy
- Press 2 to defend: the enemy's next hit is halved, but you don't attack that turn
- Press 3 to patch up with meds (painkillers or whiskey). Find them in treasure rooms
- Watch for enemies winding up: their next hit is a critical hit, so that's the moment to defend

## Example
```
The Syndicate Loop!
No best run yet.
1. Start a new game
2. Exit
Enter your choice: 1

--- Floor 1 ---

You enter a shipping container.
You encounter: Soldier!
Soldier has 25 health and 3 damage.

Amanda 100/100 | Soldier 25 Choose an action: (1) Attack (2) Defend (3) Patch up: 1
Amanda attacks Soldier for 11!
Soldier has 14 health remaining.
Soldier attacks Amanda for 5!
Amanda has 95 health remaining.
Soldier is winding up for a critical hit!

Amanda 95/100 | Soldier 14 Choose an action: (1) Attack (2) Defend (3) Patch up: 2
Soldier lands a critical hit!
Amanda blocks! Soldier's hit is reduced to 4.
Amanda has 91 health remaining.
Soldier is winding up for a critical hit!

Amanda 91/100 | Soldier 14 Choose an action: (1) Attack (2) Defend (3) Patch up: 2
Soldier lands a critical hit!
Amanda blocks! Soldier's hit is reduced to 2.
Amanda has 89 health remaining.

Amanda 89/100 | Soldier 14 Choose an action: (1) Attack (2) Defend (3) Patch up: 1
Amanda attacks Soldier for 10!
Soldier has 4 health remaining.
Soldier attacks Amanda for 5!
Amanda has 84 health remaining.

Amanda 84/100 | Soldier 4 Choose an action: (1) Attack (2) Defend (3) Patch up: 1
Amanda attacks Soldier for 11!
Amanda defeated Soldier!
```

## Features
- 3 floors of 5 - 8 randomized rooms, weighted toward fights
- Enemies scale per floor, with a boss at the end of each floor: the Capo, the Consigliere and the Underboss
- Telegraphed enemy critical hits that reward defending at the right moment
- Weapons, armor and meds, with weighted drop chances
- Run summary, best run shown on the menu, and every run saved to a SQLite history (`runs.db`)
- All tuning numbers in `config.py`

## Running tests
1. Install the dev tools (pytest, ruff and pre-commit): `python -m pip install -r requirements-dev.txt`
2. From the project folder, run: `python -m pytest`
3. Format and lint: `python -m ruff format . && python -m ruff check .`
4. Optional: run ruff automatically on every commit with `python -m pre_commit install`

Tests cover healing, meds, armor's damage floor, blocking, enemy scaling, attack results, and loading old save files.

## Known issues
- Defending is still weaker than attacking in most fights. Telegraphed crits give it a purpose; a grudge meter that rewards blocking is planned.
- Weapon and armor bonuses stack with no limit.

## What I learned
- I used to write the same code in several places. Now I look for repeated blocks and turn them into one function (`run_encounter` replaced two copies of the fight logic), so a change only has to happen in one place.
- Leftover code from refactors caused bugs twice, including a whole extra fight running after the menu loop. Now I check `git diff` after every change to make sure the old version is really gone.
- I turned playtest feedback into an `ideas.md` backlog split into Balance, Features and Cleanup, then worked through it in small, focused commits.
- A passing test isn’t proof on its own. My no-painkillers test passed because the hero was at full health, so it never reached the code it was meant to check. Now I break the code on purpose to confirm each test can actually fail.

## What's next
- The grudge meter and a simulation script to measure each strategy's win rate
- A web version with Flask and an online leaderboard (my CS50 final project)
- More test coverage (every enemy type, the run history)