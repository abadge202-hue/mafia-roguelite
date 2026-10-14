from entities import Character, random_enemy
from combat import fight


def main():
    hero = Character("Amanda", 100, 10)
    enemy = random_enemy()
    fight(hero, enemy)


if __name__ == "__main__":
    main()
