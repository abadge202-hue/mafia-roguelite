def report_attack(attacker, target, damage, blocked):
    if blocked:
        print(f"{target.name} blocks! {attacker.name}'s hit is reduced to {damage}.")
    else:
        print(f"{attacker.name} attacks {target.name} for {damage}!")
    if target.health > 0:
        print(f"{target.name} has {target.health} health remaining.")


def fight(hero, enemy):
    while True:
        print()

        action = input(
            f"{hero.name} {hero.health}/{hero.max_health} | {enemy.name} {enemy.health} "
            "Choose an action: (1) Attack (2) Defend (3) Painkillers: "
        )
        if action == "1":
            damage, blocked = hero.attack(enemy)
            report_attack(hero, enemy, damage, blocked)
            if enemy.health <= 0:
                break
            damage, blocked = enemy.attack(hero)
            report_attack(enemy, hero, damage, blocked)
            if hero.health <= 0:
                break
        elif action == "2":
            hero.defending = True
            damage, blocked = enemy.attack(hero)
            report_attack(enemy, hero, damage, blocked)
            if hero.health <= 0:
                break
        elif action == "3":
            if hero.use_painkillers():
                damage, blocked = enemy.attack(hero)
                report_attack(enemy, hero, damage, blocked)
                if hero.health <= 0:
                    break
        else:
            print("Invalid choice. Please choose again.")
    return hero.health > 0


def run_encounter(hero, enemy):
    print(f"You encounter: {enemy.name}!")
    print(f"{enemy.name} has {enemy.health} health and {enemy.damage} damage.")
    fight(hero, enemy)
    if hero.health <= 0:
        print(f"{hero.name} was defeated by {enemy.name}.")
    else:
        print(f"{hero.name} defeated {enemy.name}!")
    return hero.health > 0
