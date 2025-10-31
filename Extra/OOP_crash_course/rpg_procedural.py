def create_character(name, hp, strength, mana):
    return {
        "name": name,
        "hp": hp,
        "strength": strength,
        "mana": mana
    }


def attack(attacker, defender):
    dmg = attacker["strength"]
    defender["hp"] -= dmg
    print(f"{attacker['name']} attacks {defender['name']} for {dmg} damage!")
    print(f"{defender['name']} has {defender['hp']} HP remaining.")


def main():
    print("Welcome to the game")

    hero = create_character("Hero", 100, 15, 0)
    orc1 = create_character("Orc1", 140, 10, 0)
    wizard1 = create_character("Wiz", 140, 10, 100)

    attack(hero, orc1)
    attack(orc1, hero)


if __name__ == "__main__":
    main()
