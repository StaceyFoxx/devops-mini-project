# 💻 CFG OOP REVISION PACK
## 📘 Session Topics Covered:

Object-Oriented Programming (OOP)

Classes & Objects

Inheritance

Polymorphism

Encapsulation

Abstraction

Static & Class Methods

### 🧩 1️⃣ Object-Oriented Programming (OOP)
🧠 What It Is

OOP is a way to structure programs so that code is grouped into objects — like mini self-contained systems that have:

Attributes (data) — what an object knows

Methods (functions) — what an object does

💬 Example
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says meow!")

jake = Cat("Jake", 5)
jake.meow()

🧭 Analogy

Think of a blueprint (class) and a house (object).
You can build many houses from the same blueprint, each with unique paint, rooms, and furniture.

💡 Why We Use OOP

Keeps code organised and modular

Makes it easier to reuse logic

Allows us to model real-world systems directly in code

🧩 Quick Check

What’s the difference between a class and an object?

Why is self used inside methods?

How do attributes and methods differ?

### 🏗️ 2️⃣ Classes & Objects
🧠 What It Is

A class is like a plan that defines what data and actions an object should have.
An object is one specific thing created from that plan.

💬 Example
class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def get_info(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed} cat.")

snowy = Cat("Snowy", 8, "Siamese")
snowy.get_info()

🧩 Key Ideas

Every time you call Cat(...), you create a new object.

Each object has its own data.

Methods can interact with that data safely.

🧭 Analogy

Think of a template for a form — every user fills in their own details but follows the same structure.

🧩 Quick Check

What happens when you create two different objects from the same class?

What’s the purpose of __init__?

What does self do in a method?

### 🚗 3️⃣ Inheritance
🧠 What It Is

Inheritance allows one class to reuse or extend the behaviour of another.
A child class inherits from a parent class.

💬 Example
class Vehicle:
    def vehicle_method(self):
        print("This is the parent Vehicle class")

class Car(Vehicle):
    def car_method(self):
        print("This is the child Car class")

car_a = Car()
car_a.vehicle_method()

🧭 Analogy

Think of a family tree — children inherit characteristics from parents, but can add their own traits.

💡 Why It Matters

Reuse existing logic (avoid rewriting code).

Add new behaviour while keeping shared rules.

Create logical hierarchies like:
Vehicle → Car → ElectricCar

🌍 Real-World Use

A User class might have child classes like:

AdminUser

GuestUser

PremiumUser

All share login logic but differ in permissions.

🧩 Quick Check

What is the relationship between parent and child classes?

Why is inheritance better than copying code?

### 🌀 4️⃣ Polymorphism
🧠 What It Is

“Poly” = many, “morph” = forms.
Polymorphism lets different classes use the same method name but behave differently.

💬 Example
class Vehicle:
    def start(self):
        print("Starting a generic vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting a car engine...")

class Bike(Vehicle):
    def start(self):
        print("Starting a bike engine...")

for v in [Car(), Bike()]:
    v.start()

🧭 Analogy

Think of a “Play” button:

On Spotify, it plays music.

On Netflix, it plays a video.
Same button → different actions depending on context.

💡 Why It Matters

Reduces complexity — one interface, many outcomes.

Enables flexible, extendable designs (common in APIs).

🧩 Quick Check

What does “many forms” mean in code?

How can the same method name produce different results?

### 🧱 5️⃣ Encapsulation

⚠️ This was the most confusing topic for many students — so this section has extra notes and examples.

🧠 What It Is

Encapsulation means protecting an object’s data and only allowing controlled access to it.
It helps you hide internal details and enforce rules when that data changes.

💬 Example
class Car:
    def __init__(self, model):
        self.model = model  # triggers setter

    @property
    def model(self):
        return self.__model   # private variable

    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2021:
            self.__model = 2021
        else:
            self.__model = model

🟨 Pause & Recap

@property lets you read the value like a variable (car.model).

@model.setter lets you validate the input before saving it.

__model is private (Python renames it internally to _Car__model).

🧭 Analogy

Think of encapsulation like an ATM.
You can’t directly touch the bank’s database — you must go through safe access points (buttons/methods).

💡 Why It Matters

Prevents invalid data (e.g. a car model in the year 3000).

Keeps logic consistent — you can change rules inside the setter without breaking code elsewhere.

Improves maintainability in larger systems.

🌍 Real-World Use

Password verification and hashing.

Validating age, price, or score before saving.

Banking systems preventing direct balance edits.

🧩 Quick Check

Why do we use __model with double underscores?

How does encapsulation make code safer?

What happens if someone tries to bypass it?

### 🎨 6️⃣ Abstraction
🧠 What It Is

Abstraction hides unnecessary details and focuses on what something does, not how it does it.

💬 Example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calc_perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a; self.b = b; self.c = c

    def calc_perimeter(self):
        return self.a + self.b + self.c

🧭 Analogy

Think of a TV remote: you only care about the buttons, not the circuitry inside.
You just press “Power,” “Volume,” or “Channel.”

💡 Why It Matters

Keeps code simple to use but flexible underneath.

Ensures subclasses follow the same design (every Shape must have calc_perimeter()).

🌍 Real-World Use

Defining base “interface” classes for plugins or APIs.

Payment systems (every payment type must have a process_payment() method).

Data pipelines with consistent input/output rules.

🧩 Quick Check

Why does Shape not implement calc_perimeter()?

What happens if a subclass forgets to define it?

### ⚙️ 7️⃣ Static & Class Methods

⚠️ These were tricky for several learners — here’s an expanded recap.

🧠 What They Are
Type	Access	Purpose
Instance Method	Works on one object (self)	Change or read that object’s data
Class Method	Works on the whole class (cls)	Create or modify class-wide data
Static Method	Doesn’t use self or cls	Utility or validation function
💬 Example
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    @staticmethod
    def is_adult(age):
        return age >= 18

🟨 Pause & Recap

from_birth_year() → class method that creates a person from birth year.

is_adult() → static method that just checks an age — no object needed.

🧭 Analogy

Class Method = 🏭 Factory — builds objects from different materials (data).

Static Method = 🧰 Toolbox — helper logic that belongs with the class but works independently.

💡 Why It Matters

Keeps code organised — related tools live inside the same class.

Makes it easier to create objects from multiple data sources (files, APIs, forms).

Simplifies validation and data conversion.

🌍 Real-World Use

User.from_json() → create user from API data

Payment.validate_amount() → check transaction amount

Order.from_csv() → create orders from file rows

🧩 Try It

Create a Book class:

@classmethod from_string(cls, "Title-Author") → returns a Book object

@staticmethod validate_title(title) → returns False if title is empty

### 🧭 8️⃣ How They Connect
Concept	How It Links to Others
Classes & Objects	Foundation — every concept builds from here
Inheritance	Reuses and extends class logic
Polymorphism	Uses shared method names for flexible design
Encapsulation	Protects data in those objects
Abstraction	Hides unnecessary detail from the user
Class & Static Methods	Support encapsulation and abstraction — adding structure and utilities
🧠 Revision Strategy

Rewatch the session recording with your code open.

Run each example one at a time.

After each concept, pause and explain it aloud as if teaching it — this strengthens recall.

Recreate examples from memory, then modify them slightly (change data, names, or values).

### 🧰 Helpful Practice Prompts

✏️ Write a BankAccount class with encapsulated balance, and deposit/withdraw methods.

✏️ Create a Vehicle base class and two child classes using polymorphism.

✏️ Build a User class with a class method that constructs from an email address.

💬 Final Tip

Don’t worry if these ideas take time to click — OOP is learned through repetition.
Focus on understanding why each tool exists rather than memorising syntax.
Once you start building mini-projects (like your Flask Library API), you’ll see them all working together naturally.