import json
from pathlib import Path

from combat import run_encounter
from config import (
    HERO_DAMAGE,
    HERO_HEALTH,
    HERO_NAME,
    NUM_FLOORS,
    REST_HEAL_FRACTION,
    RoomType,
)
from dungeon import BOSS_ROOMS, generate_floor
from entities import Character, create_boss, random_enemy
from items import random_item

BEST_RUN_FILE = Path(__file__).parent / "best_run.json"


def play_run():
    """Play one full run from the first floor; return the run's stats when the hero dies or beats the final boss."""
    stats = {"Floors": 1, "Enemies Defeated": 0, "Items Found": 0, "Won": False}
    hero = Character(HERO_NAME, HERO_HEALTH, HERO_DAMAGE)
    for floor_number in range(1, NUM_FLOORS + 1):
        stats["Floors"] = floor_number
        print(f"\n--- Floor {floor_number} ---")
        rooms = generate_floor()
        for room in rooms:
            print(f"\nYou enter {room.place}.")
            if room.room_type == RoomType.ENEMY:
                enemy = random_enemy(floor_number)
                if not run_encounter(hero, enemy):
                    return stats
                stats["Enemies Defeated"] += 1
            elif room.room_type == RoomType.TREASURE:
                item = random_item()
                hero.pick_up(item)
                if item.item_type == "potion":
                    print(f"{hero.name} picked up {item.name}!")
                elif item.item_type == "armor":
                    print(
                        f"{hero.name} picked up {item.name}! Defense increased by {item.value}."
                    )
                elif item.item_type == "weapon":
                    print(
                        f"{hero.name} picked up {item.name}! Damage increased by {item.value}."
                    )
                stats["Items Found"] += 1

            elif room.room_type == RoomType.REST:
                print("You find a safe place to rest.")
                rest_amount = int(hero.max_health * REST_HEAL_FRACTION)
                gained = hero.heal(rest_amount)
                if gained == 0:
                    print(f"{hero.name} is already at full health!")
                else:
                    print(
                        f"{hero.name} heals for {gained}. Current health: {hero.health}/{hero.max_health}"
                    )
            elif room.room_type == RoomType.EMPTY:
                print("The room is empty. Nothing happens.")
        boss = create_boss(floor_number)
        print(
            f"\n{hero.name} heads to {BOSS_ROOMS[floor_number - 1]} to face the {boss.name}!"
        )
        print(f"\nYou arrive at {BOSS_ROOMS[floor_number - 1]}.")
        if not run_encounter(hero, boss):
            return stats
        stats["Enemies Defeated"] += 1
        print("You have cleared the floor! Congratulations!")

    stats["Won"] = True
    return stats


def show_summary(stats):
    """Print the run summary: result, floor reached, enemies defeated and items found."""
    print("\n--- Game Summary ---")
    result = "Won" if stats["Won"] else "Lost"
    print(f"Result: {result}")
    print(f"Floor Reached: {stats['Floors']}")
    print(f"Enemies Defeated: {stats['Enemies Defeated']}")
    print(f"Items Found: {stats['Items Found']}")


def load_best_run():
    """Return the saved best run as a dict, or None if there is no save file yet."""
    try:
        with open(BEST_RUN_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_best_run(stats):
    """Write the run's stats to the best-run file."""
    with open(BEST_RUN_FILE, "w") as f:
        json.dump(stats, f)


def run_score(run):
    """Return a (won, floor, enemies defeated) tuple used to rank runs, best first."""
    return (run["Won"], run["Floors"], run["Enemies Defeated"])

def describe_best(best: dict) -> str:
    """Return a one-line description of the best run."""
    if best["Won"]:
        return f"Best run: Defeated the Family, {best['Enemies Defeated']} enemies defeated"
    return f"Best run: floor {best['Floors']}, {best['Enemies Defeated']} enemies defeated"


def main():
    """Show the main menu in a loop: play a run, print its summary and save new bests, until the player exits."""
    while True:
        print("\nThe Syndicate Loop!")
        best = load_best_run()
        if best is None:
            print("No best run yet.")
        else:
            print(describe_best(best))    
        print("1. Start a new game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stats = play_run()
            show_summary(stats)
            best = load_best_run()
            if best is None or run_score(stats) > run_score(best):
                save_best_run(stats)
                print("New best run!")
            else:
                print(describe_best(best))
        elif choice == "2":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nThanks for playing!")
