from entities import Character
from combat import fight


def main():
    hero = Character("Amanda", 100, 10)
    enemy = Character("Theodore", 80, 8)
    fight(hero, enemy)


if __name__ == "__main__":
    main()
