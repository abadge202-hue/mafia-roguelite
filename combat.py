def fight(hero, enemy):
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
