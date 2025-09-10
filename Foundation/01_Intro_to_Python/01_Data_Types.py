# STRING Data Type
"""
STRING Data Type in Python:

A string is a sequence of characters enclosed in quotes.
Strings can use single quotes ('') or double quotes ("").
Strings are used to represent text.
"""
# Creating strings
name = "Alex"
greeting = 'Hello'
sentence = "I'm learning Python"

# Displaying strings
print(name)  # Output: Alex
print(greeting)  # Output: Hello
print(sentence)  # Output: I'm learning Python

# Combining strings (concatenation)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# INT Data Type
"""
INT Data Type in Python:

An integer (int) is a whole number without a decimal point.
Integers can be positive or negative.
"""
# Creating integers
age = 25
temperature = -5
count = 100

# Displaying integers
print(age)  # Output: 25
print(temperature)  # Output: -5
print(count)  # Output: 100

# Simple calculations with integers
sum_result = 5 + 3
difference = 10 - 4
product = 6 * 7
division = 20 // 3  # Integer division (floor division)

print(sum_result)  # Output: 8
print(difference)  # Output: 6
print(product)  # Output: 42
print(division)  # Output: 6

# FLOAT Data Type
"""
FLOAT Data Type in Python:

A float is a number with a decimal point.
Floats are used to represent fractional values.
"""
# Creating floats
height = 1.75
price = 19.99
pi_value = 3.14159

# Displaying floats
print(height)  # Output: 1.75
print(price)  # Output: 19.99
print(pi_value)  # Output: 3.14159

# Simple calculations with floats
area = pi_value * 5 * 5  # Area of circle with radius 5
print(area)  # Output: 78.53975

# Converting between int and float
integer_value = 10
float_from_int = float(integer_value)
print(float_from_int)  # Output: 10.0

float_value = 7.8
int_from_float = int(float_value)  # Cuts off decimal part
print(int_from_float)  # Output: 7

# BOOL Data Type
"""
BOOL Data Type in Python:

A boolean (bool) can have only two values: True or False.
Booleans are used in conditions and logical operations.
"""
# Creating booleans
is_student = True
has_passed = False

# Displaying booleans
print(is_student)  # Output: True
print(has_passed)  # Output: False
