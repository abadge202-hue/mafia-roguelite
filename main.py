from entities import Character, create_boss, random_enemy
from combat import fight
from dungeon import BOSS_ROOMS, generate_floor


def main():
    hero = Character("Amanda", 100, 10)
    for floor_number in range(1, 4):
        print(f"\n--- Floor {floor_number} ---")
        rooms = generate_floor()
        for room in rooms:
            print(f"\nYou enter {room.place}.")
            if room.room_type == "enemy":
                enemy = random_enemy(floor_number)
                print(f"You encounter: {enemy.name}!")
                print(
                    f"{enemy.name} has {enemy.health} health and {enemy.damage} damage."
                )
                print(f"{hero.name} has {hero.health} health")
                fight(hero, enemy)
                if hero.health <= 0:
                    print("You have been defeated! Game over.")
                    return
            elif room.room_type == "treasure":
                print("You find a black book!")
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
    print(f"\nYou encounter the first boss: {boss.name}!")
    print(f"{boss.name} has {boss.health} health and {boss.damage} damage.")
    fight(hero, boss)
    if hero.health <= 0:
        print(f"\nYou have been defeated by {boss.name}! Game over.")
        return
    print(f"\nCongratulations! You have defeated {boss.name} and completed the game!") 
    


if __name__ == "__main__":
    main()
