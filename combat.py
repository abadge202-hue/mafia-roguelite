import random

from config import CRIT_CHANCE
from entities import Character


def report_attack(
    attacker: Character, target: Character, damage: int, blocked: bool, crit: bool
) -> None:
    """Print one attack's result: the hit or block, then remaining health if the target survived."""
    if crit:
        print(f"{attacker.name} lands a critical hit!")
    if blocked:
        print(f"{target.name} blocks! {attacker.name}'s hit is reduced to {damage}.")
    else:
        print(f"{attacker.name} attacks {target.name} for {damage}!")
    if target.health > 0:
        print(f"{target.name} has {target.health} health remaining.")


def enemy_turn(enemy: Character, hero: Character) -> None:
    damage, blocked, crit = enemy.attack(hero)
    report_attack(enemy, hero, damage, blocked, crit)
    if hero.health > 0 and random.random() < CRIT_CHANCE:
        enemy.winding_up = True
        print(f"{enemy.name} is winding up for a critical hit!")


def fight(hero: Character, enemy: Character) -> bool:
    """Run turn-by-turn combat with player input until one side falls; return True if the hero survived."""
    while True:
        print()

        action = input(
            f"{hero.name} {hero.health}/{hero.max_health} | {enemy.name} {enemy.health} "
            "Choose an action: (1) Attack (2) Defend (3) Painkillers: "
        )
        if action == "1":
            damage, blocked, crit = hero.attack(enemy)
            report_attack(hero, enemy, damage, blocked, crit)
            if enemy.health <= 0:
                break
            enemy_turn(enemy, hero)
            if hero.health <= 0:
                break
        elif action == "2":
            hero.defending = True
            enemy_turn(enemy, hero)
            if hero.health <= 0:
                break
        elif action == "3":
            status, gained, item_name = hero.use_painkillers()
            if status == "used":
                print(
                    f"{hero.name} uses {item_name} and heals for {gained}. Current health: {hero.health}/{hero.max_health}"
                )
                enemy_turn(enemy, hero)
                if hero.health <= 0:
                    break
            elif status == "full":
                print(f"{hero.name} is already at full health!")
            elif status == "none":
                print(f"{hero.name} has no Painkillers to use!")
        else:
            print("Invalid choice. Please choose again.")
    return hero.health > 0


def run_encounter(hero: Character, enemy: Character) -> bool:
    """Announce the enemy, run the fight, and print who won; return True if the hero survived."""
    print(f"You encounter: {enemy.name}!")
    print(f"{enemy.name} has {enemy.health} health and {enemy.damage} damage.")
    fight(hero, enemy)
    if hero.health <= 0:
        print(f"{hero.name} was defeated by {enemy.name}.")
    else:
        print(f"{hero.name} defeated {enemy.name}!")
    return hero.health > 0
