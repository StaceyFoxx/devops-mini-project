from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass


class Character(Entity):

    def __init__(self, name, hp, strength, defence):
        super().__init__(name)
        self.hp = hp
        self.strength = strength
        self.defence = defence

    def attack(self, target):
        dmg = self.strength - target.defence
        target.hp -= dmg
        print(f"{self.name} attacks {target.name} dealing {dmg} dmg")

    def __str__(self):
        return f"Name: {self.name}, hp: {self.hp}, " f"str: {self.strength}, def: {self.defence}"


class Fighter(Character):

    def attack(self, target):
        extra_fighter_combat_skill_addon = 18
        dmg = (self.strength + extra_fighter_combat_skill_addon) - target.defence
        target.hp -= dmg
        print(f"{self.name} attacks {target.name} dealing {dmg} dmg")


class Archer(Character):
    def __init__(self, name, hp, strength, defence, arrows):
        super().__init__(name, hp, strength, defence)
        self.arrows = arrows

    def shoot_arrow(self, target):
        arrow_perc_dmg = 3
        dmg = (self.strength * arrow_perc_dmg) - target.defence
        target.hp -= dmg
        print(f"{self.name} ({self.__class__.__name__}) attacks {target.name} with arrow dealing {dmg} dmg")

    def attack(self, target):
        if self.arrows > 0:
            self.shoot_arrow(target)
            self.arrows -= 1
            print(f"total {self.arrows} arrows remaining")
        else:
            print(f"{self.name} is out of arrows! Can't shoot")


class Wizard(Character):
    def __init__(self, name, hp, strength, defence, mana):
        super().__init__(name, hp, strength, defence)
        self.mana = mana
        self.spellbook = {
            "Fireball": {"cost": 15, "dmg": 30},
            "Ice Shard": {"cost": 10, "dmg": 20},
            "Lightning Bolt": {"cost": 20, "dmg": 40}
        }

    def attack(self, target, spell="Fireball"):
        self.cast_spell(target, spell)

    def cast_spell(self, target, spell):
        if spell in self.spellbook:
            spell_cost = self.spellbook[spell]["cost"]
            spell_dmg = self.spellbook[spell]["dmg"]

            if self.mana >= spell_cost:
                self.mana -= spell_cost
                target.hp -= spell_dmg
                print(f"{self.name} ({self.__class__.__name__}) casts {spell} on {target.name}, "
                      f"dealing {spell_dmg} dmg. Mana remaining: {self.mana}")
            else:
                print(f"{self.name} does not have enough mana to cast {spell}.")
        else:
            print(f"{self.name} does not know the spell {spell}.")


def main():
    aragorn = Fighter("Aragorn", 100, 20, 15)
    orc1 = Character("orc1", 140, 15, 10)
    lagolas = Archer("Lagolas", 80, 10, 20, 30)
    gandolf = Wizard("Gandolf", 60, 15, 40, 50)

    gandolf.attack(orc1)
    print(orc1)


if __name__ == "__main__":
    main()
