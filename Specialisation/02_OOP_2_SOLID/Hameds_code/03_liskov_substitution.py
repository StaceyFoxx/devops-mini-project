"""
LISKOV SUBSTITUTION PRINCIPLE

If we have a base class A (SUPER CLASS) and subclass B (SUB CLASS),
we should be able to substitute the main class A with the subclass B without breaking the code.
"""


# BAD EXAMPLE FIRST

class Parent:
    def eat(self):
        print("Eating food.")

    def sleep(self):
        print("Sleeping.")

    def work(self):
        print("Working a job.")

    def pay_taxes(self):
        print("Paying taxes.")


class Child(Parent):
    def work(self):
        # Violates LSP. Kids can't work!
        print("Playing with toys instead of working.")

    def pay_taxes(self):
        # Violates LSP as it makes no sense for a child to pay taxes.
        print("Children don't pay taxes.")


"""
### WHY IS IT BAD?
In this example, Child is a subclass of Parent. However, it violates the Liskov Substitution
 Principle because the behavior of work and pay_taxes methods in Child are not
  consistent with the behavior of the same methods in the base class Parent.
"""

#############################################################################################
#############################################################################################
# GOOD EXAMPLE NOW
#############################################################################################
#############################################################################################

from abc import ABC, abstractmethod


class Human(ABC):
    def eat(self):
        print("Eating food.")

    def sleep(self):
        print("Sleeping.")

    @abstractmethod
    def activity(self):
        pass


class Adult(Human):
    def activity(self):
        print("Working a job and paying taxes.")


class Child(Human):
    def activity(self):
        print("Playing and going to school.")


"""
### WHY IS IT GOOD?
In this improved example,Here, Adult and Child both inherit from Human but implement activity() in ways 
that are appropriate to their roles. 
Now, we avoid the need for inappropriate method overrides
"""
