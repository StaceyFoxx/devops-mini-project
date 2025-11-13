
# 📘 Python Glossary for Beginners

A quick reference to help you understand common Python and programming terms that appear in lessons on **functions**, **OOP (Object-Oriented Programming)**, and **decorators**.

---

## 🔤 Core Python Terms

| Term                                         | Beginner-Friendly Explanation                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Function**                                 | A reusable block of code that performs a task when called. You define it using `def`.              |
| **Parameter**                                | A variable name inside a function definition — acts like a placeholder for inputs.                 |
| **Argument**                                 | The actual data you pass into a function when you call it.                                         |
| **Return Value**                             | The result a function gives back using `return`.                                                   |
| **Class**                                    | A blueprint that defines what an object is and how it behaves (its attributes and methods).        |
| **Object / Instance**                        | A specific “thing” created from a class (e.g., `cat1 = Cat()`).                                    |
| **Instantiate**                              | The act of creating an object from a class. Example: `my_car = Car()`.                             |
| **Attribute**                                | A piece of data stored inside an object, like `self.name`.                                         |
| **Method**                                   | A function defined inside a class that operates on its data.                                       |
| **Decorator**                                | A function or class that wraps another function to modify or enhance its behaviour.                |
| **Wrapper Function**                         | The inner function inside a decorator that adds extra logic before or after the original function. |
| **Argument Unpacking (`*args`, `**kwargs`)** | Special syntax that lets a function accept any number of arguments.                                |
| **Encapsulation**                            | Hiding internal details within a class to protect its data.                                        |
| **Polymorphism**                             | Using one method name for multiple behaviours depending on the object.                             |
| **Inheritance**                              | A way for one class to inherit attributes and methods from another.                                |
| **Abstraction**                              | Simplifying complexity by exposing only what’s necessary to the user.                              |
| **Scope**                                    | Where a variable can be accessed in your code (local or global).                                   |
| **Keyword Argument**                         | Passing an argument by name, e.g. `print(name="Fatma")`.                                           |
| **Docstring**                                | A triple-quoted string that explains what a function or class does.                                |
| **Call Stack**                               | The order in which Python executes and returns function calls — important for debugging.           |




# EXTRA:  Visual Class Decorator guide
                 +--------------------------+
                 |        CLASS             |
                 |--------------------------|
                 |  defines structure       |
                 |  and behaviour (methods) |
                 +------------+-------------+
                              |
               instantiate -> |  (creates)
                              v
                        +------------+
                        |   OBJECT   |
                        +------------+
                        | attributes |
                        | methods    |
                        +------------+
                              |
                              v
                calls methods / functions
                              |
                              v
                 +---------------------------+
                 |      Function Flow        |
                 |---------------------------|
                 |  Inp→func→output(return)  |
                 |  wrapped by → @decorator  |
                 |  Decorator adds behaviour | 
                 +------------+--------------+


Example:
@SquaredDecorator
def multiply():
    ...
→ “multiply()” gets wrapped to measure execution time
