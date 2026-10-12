class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health = max(0, target.health - self.damage)
        print(f"{self.name} hits {target.name} for {self.damage}")
        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{target.name} has been defeated!")


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health = max(0, target.health - self.damage)
        print(f"{self.name} hits {target.name} for {self.damage}")
        if target.health > 0:
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{target.name} has been defeated!")


def main():
    hero = Hero("Amanda", 100, 10)
    enemy = Enemy("Theodore", 80, 8)
    while True:
        hero.attack(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(hero)
        if hero.health <= 0:
            break


if __name__ == "__main__":
    main()
