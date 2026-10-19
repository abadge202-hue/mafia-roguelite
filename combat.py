def fight(hero, enemy):
    while True:
        print()
        print(f"inventory: {[item.name for item in hero.inventory]}")
        action = input("Choose an action: (1) Attack (2) Defend (3) Use Painkillers: ")
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
        elif action == "3":
            if hero.use_painkillers():
                enemy.attack(hero)
                if hero.health == hero.max_health:

                    print(f"{hero.name} is already at full health!")
                    return False
                if hero.health <= 0:
                    break
        else:
            print("Invalid choice. Please choose again.")
