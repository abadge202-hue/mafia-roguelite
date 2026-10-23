# The Syndicate Loop

A turn-based terminal roguelite where you fight your way up a mafia family, floor by floor.

## How to run
- Requires Python 3.10+
- Clone or download the repo, then run `python main.py` in the project folder

## How to play
- Press 1 to attack the enemy
- Press 2 to defend against the enemy attack
- Press 3 to use painkillers (heal). Find them in treasure rooms

## Example
```
The Syndicate Loop!
1. Start a new game
2. Exit
Enter your choice: 1

--- Floor 1 ---

You enter the back of a shipping warehouse.
You encounter: Soldier!
Soldier has 25 health and 3 damage.

Amanda 100/100 | Soldier 25 Choose an action: (1) Attack (2) Defend (3) Use Painkillers: 1 
Amanda hits Soldier for 10
Soldier has 15 health remaining.
Soldier hits Amanda for 1
Amanda has 99 health remaining.

Amanda 99/100 | Soldier 15 Choose an action: (1) Attack (2) Defend (3) Use Painkillers: 2 
Soldier attacks Amanda for 5!
Amanda is defending! Damage is reduced to 2.
Soldier hits Amanda for 2
Amanda has 97 health remaining.

Amanda 97/100 | Soldier 15 Choose an action: (1) Attack (2) Defend (3) Use Painkillers: 1 
Amanda hits Soldier for 12
Soldier has 3 health remaining.
Soldier hits Amanda for 5
Amanda has 92 health remaining.

Amanda 92/100 | Soldier 3 Choose an action: (1) Attack (2) Defend (3) Use Painkillers: 1
Amanda hits Soldier for 9
Amanda defeated Soldier!
```

## Features
- 3 floors of 5 - 8 randomized rooms
- Enemies scale per floor
- A boss at the end of each floor
- Items that increase damage, defense, and heal
- Saved best run


## Known issues
- Defending is underpowered (attacking almost always wins). A rework is planned.
- Weapon and armor bonuses stack with no limit.

## What I learned
- I used to write the same code in several places. Now I look for repeated blocks and turn them into one function (`run_encounter` replaced two copies of the fight logic), so a change only has to happen in one place.
- Leftover code from refactors caused bugs twice, including a whole extra fight running after the menu loop. Now I check `git diff` after every change to make sure the old version is really gone.
- I turned playtest feedback into an `ideas.md` backlog split into Balance, Features and Cleanup, then worked through it in small, focused commits.

## What's next
- Tests with pytest 
- Separating game logic from display 
- The defend rework