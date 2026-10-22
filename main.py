from combat import run_encounter
from dungeon import BOSS_ROOMS, generate_floor
from entities import Character, create_boss, random_enemy
from items import random_item
import json


def play_run():
    stats = {"Floors": 1, "Enemies Defeated": 0, "Items Found": 0, "Won": False}
    hero = Character("Amanda", 100, 10)
    for floor_number in range(1, 4):
        stats["Floors"] = floor_number
        print(f"\n--- Floor {floor_number} ---")
        rooms = generate_floor()
        for room in rooms:

            print(f"\nYou enter {room.place}.")
            if room.room_type == "enemy":
                enemy = random_enemy(floor_number)
                if not run_encounter(hero, enemy):
                    return stats
                stats["Enemies Defeated"] += 1
            elif room.room_type == "treasure":
                item = random_item()
                hero.pick_up(item)
                stats["Items Found"] += 1

            elif room.room_type == "rest":
                print("You find a safe place to rest.")
                hero.heal()
            else:
                print("The room is empty. Nothing happens.")
        print("You have cleared the floor! Congratulations!")
    boss = create_boss()
    print(
        f"\n{hero.name} is taking the elevator to {BOSS_ROOMS[0]} to face the {boss.name}!"
    )
    hero.heal()
    print(f"\nYou enter {BOSS_ROOMS[0]}.")
    if not run_encounter(hero, boss):
        return stats
    stats["Enemies Defeated"] += 1
    stats["Won"] = True
    return stats


def show_summary(stats):
    if stats["Won"]:
        print("\n--- Game Summary ---")
        print(f"Floor Reached: {stats['Floors']}")
        print(f"Enemies Defeated: {stats['Enemies Defeated']}")
        print(f"Items Found: {stats['Items Found']}")
    else:
        print("\n--- Game Summary ---")
        print(f"Floor Reached: {stats['Floors']}")
        print(f"Enemies Defeated: {stats['Enemies Defeated']}")
        print(f"Items Found: {stats['Items Found']}")


def load_best_run():
    try:
        with open("best_run.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_best_run(stats):
    with open("best_run.json", "w") as f:
        json.dump(stats, f)


def run_score(run):
    return (run["Won"], run["Floors"], run["Enemies Defeated"])


def main():
    while True:
        print("\nThe Syndicate Loop!")
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
                print(
                    f"Best run: Reached floor {best['Floors']} and defeated "
                    f"{best['Enemies Defeated']} enemies."
                )
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
