"""
INTERFACE SEGREGATION PRINCIPLE

A class should not be forced to implement interfaces it does not use.

In other words, a class should not be forced to implement methods it does not need.
"""


# BAD EXAMPLE FIRST - Using a single large interface

class Entity:
    def move(self):
        pass

    def attack(self):
        pass

    def spawn(self):
        pass


class Character(Entity):
    def move(self):
        print("Character is moving")

    def attack(self):
        print("Character is attacking")

    def spawn(self):
        print("Character is spawned")


class Turret(Entity):
    def move(self):
        pass  # Turret doesn't move, but forced to implement the method

    def attack(self):
        print("Turret is attacking")

    def spawn(self):
        pass  # Turret doesn't spawn, but forced to implement the method


"""
### WHY IS IT BAD?
In this example, the Entity interface is too broad, and both Character and Turret
 have to implement methods that are not relevant to them
"""


#############################################################################################
#############################################################################################
# GOOD EXAMPLE NOW
#############################################################################################
#############################################################################################

# Good Example - Using specific interfaces

class Moveable:
    def move(self):
        pass


class Attacker:
    def attack(self):
        pass


class Spawner:
    def spawn(self):
        pass


class Character(Moveable, Attacker, Spawner):
    def move(self):
        print("Character is moving")

    def attack(self):
        print("Character is attacking")

    def spawn(self):
        print("Character is spawned")


class Turret(Attacker):
    def attack(self):
        print("Turret is attacking")


"""
### WHY IS IT GOOD?
In this improved example, we have specific interfaces (Moveable, Attacker, Spawner) 
that are implemented by the classes that need them. Now, Character implements all three 
interfaces, while Turret only implements the Attacker interface, reflecting a more 
segregated and flexible design.

"""
