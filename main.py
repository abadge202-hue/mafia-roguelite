import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.defending = False

    def attack(self, target):
        damage_dealt = random.randint(self.damage - 2, self.damage + 2)
        if target.defending:
            print(f"{self.name} attacks {target.name} for {damage_dealt}!")
            damage_dealt = damage_dealt // 2
            print(f"{target.name} is defending! Damage is reduced to {damage_dealt}.")
            target.defending = False
        target.health = max(0, target.health - damage_dealt)
        print(f"{self.name} hits {target.name} for {damage_dealt}")

        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{target.name} has been defeated!")


def main():
    hero = Character("Amanda", 100, 10)
    enemy = Character("Theodore", 80, 8)
    while True:
        print()
        action = input("Choose an action: (1) Attack (2) Defend: ")
        if action == "1":
            hero.attack(enemy)
            if enemy.health <= 0:
                break
            enemy.attack(hero)
            if hero.health <= 0:
                break
        elif action == "2":
            hero.defending = True
            enemy.attack(hero)
            if hero.health <= 0:
                break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
