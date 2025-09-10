# String Interpolation in Python
"""
String Interpolation in Python:

String interpolation means inserting variables into strings.
There are two main ways to do this in modern Python:
1. f-strings (formatted string literals) - introduced in Python 3.6
2. The format() method - an older but still useful approach
"""

# ----- Using f-strings -----
"""
f-strings:

Start a string with the letter 'f' before the quotes: f"text here"
Put variables or expressions inside curly braces: {variable}
Very easy to read and use
"""
name = "Maria"
age = 28
language = "Python"

# Basic f-string usage
greeting = f"Hello, my name is {name}!"
print(greeting)  # Output: Hello, my name is Maria!

# Including multiple variables
intro = f"I am {name}, I am {age} years old, and I am learning {language}."
print(intro)  # Output: I am Maria, I am 28 years old, and I am learning Python.

# Using expressions inside f-strings
price = 49.99
quantity = 3
total = f"Total cost: ${price * quantity}"
print(total)  # Output: Total cost: $149.97

# ----- Using format() method -----
"""
format() method:

Use curly braces {} as placeholders in the string
Call .format() on the string and pass the values to be inserted
Works in all Python 3 versions
"""
# Basic format() usage
greeting2 = "Hello, my name is {}.".format(name)
print(greeting2)  # Output: Hello, my name is Maria.

# Including multiple variables
intro2 = "I am {}, I am {} years old, and I am learning {}.".format(name, age, language)
print(intro2)  # Output: I am Maria, I am 28 years old, and I am learning Python.

# Using positions to specify order
positions = "{2} is being learned by {0}, who is {1} years old.".format(name, age, language)
print(positions)  # Output: Python is being learned by Maria, who is 28 years old.

# Using named placeholders
named = "The price of {item} is ${cost}.".format(item="bananas", cost=1.99)
print(named)  # Output: The price of bananas is $1.99.

