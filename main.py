from entities import Character, random_enemy
from combat import fight
from dungeon import generate_floor


def main():
    hero = Character("Amanda", 100, 10)
    rooms = generate_floor()
    for room in rooms:
        print(f"\nYou enter {room.place}.")
        if room.room_type == "enemy":
            enemy = random_enemy()
            print(f"You encounter: {enemy.name}!")
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


if __name__ == "__main__":
    main()
