"""
CREATE & INSTANTIATE A CLASS
"""

# class Cat:
#
#     def __init__(self):
#         pass
#
# jake = Cat()
# print(jake)


class Cat:

    def __init__(self, name, age, breed):
        # Define characteristics of a class
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('meow meow')

    def get_info(self):
        print(f"{self.name} is {self.age} years old")
#
# jake = Cat("Jake", 4, 'Maine Coon')
# print(jake.name)
# print(jake.age)
# print(jake.breed)
# jake.meow()
# jake.get_info()
#
# snowball = Cat(name="Snowball", age=2, breed='Tabby')
# Paw = Cat("Paw", 2, 'Sphynx')
#
# Paw.meow()
#
# snowball.get_info()


# assign new value to the attribute in the class
# we can also link objects together
class Cat:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('meow meow')

    def get_info(self):
        print(f"{self.name} is {self.age} years old")

    def birthday(self):
#         add one year to the objects age
        self.age += 1

    def set_friend(self, friend):
#         link a friend (another cat object) to this cat and set the other cat as friends
        self.friend = friend
        friend.friend = self


jake = Cat("Jake", 2, "Tabby")
snowball = Cat("Snowball", 3, "British Shorthair")

# # links the two objects together via each friend attribute
# jake.set_friend(snowball)
#
# print(jake.friend.name)
# print(snowball.friend.name)
#
# print(jake.friend.age)
# print(snowball.friend.breed)







""""
INHERITANCE 
"""

# class Vehicle:
#
#     def vehicle_method(self):
#         print("This is a parent Vehicle class method")
#
#
# class Car(Vehicle):
#
#     def car_method(self):
#         print("This is a child Car class method")


# child classes have access to parents methods and attributes
# car_a = Car()
# car_a.vehicle_method()


class Camera:
    def camera_method(self):
        print("This is a parent Camera class method")

class Radio:
    def radio_method(self):
        print("This is a parent Radio class method")


class MobilePhone(Camera, Radio):
     def mobile_phone_method(self):
         print("This is a child Mobile Phone class method")

#
# cell_phone_a = MobilePhone()
#
# cell_phone_a.mobile_phone_method()
# cell_phone_a.radio_method()
# cell_phone_a.camera_method()
#



"""
POLYMORPHISM
"""


# class Vehicle:
#     def print_details(self):
#         print("This is the details of the Parent Vehicle Class")
#
# class Car(Vehicle):
#     def print_details(self):
#         print("This is the details of the Child Car Class")
#
# class Cycle(Vehicle):
#     def print_details(self):
#         print("This is the details of the Child Cycle Class")


# car_a = Car()
# cycle_a = Cycle()
#
# car_a.print_details()
# cycle_a.print_details()



""""
ENCAPSULATION
"""


class Car:
    def __init__(self, model):
        self.model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2021:
            self.__model = 2021
        else:
            self.__model = model

    def get_car_model(self):
        return f"The car model is {self.model}"


#
# my_car = Car(2025)
# print(my_car.model)
# print(my_car.get_car_model())


""""
ABSTRACTION
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calc_perimeter(self):
        pass


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
#
# triangle_a = Triangle(1, 2, 3)
# print(triangle_a.calc_perimeter())
#
# circle_a = Circle(2)
# print(circle_a)


from datetime import date

class Person:
    variable = "class variable example"

    def __init__(self, name, age):
        # instance attributes - Person('Fatma', 31)
        self.name = name
        self.age = age

    def speak(self):
        # Instance method
        print('Hello!')

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def check_age(age):
        # does NOT rely on object creation but can be used by class or objects
        return age > 18

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")




# normal instantiation of an object
person1 = Person('Fatma', 31)

print(person1)
person1.get_details()
# run instance method - a method only ran AFTER an object is created
person1.speak()
# Person.speak() <- this would fail as NO object has been created i.e. there is NO self

# create object using class method directly
# e.g. creating a class method from_json within a web app to create new person -> Person(data_json)
person2 = Person.details('Fatma', 1994)
print(person2)
person2.get_details()

# static methods can be used by class or objects
print(person2.check_age(31))
print(Person.check_age(31))