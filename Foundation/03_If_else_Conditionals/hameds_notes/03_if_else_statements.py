"""
IF-ELSE Statements:

If-else handles two possibilities:
- Run one block of code when condition is True
- Run another block when condition is False

Syntax:
    if condition:
        code to run if True
    else:
        code to run if False
"""

# beach example
temperature = 2
is_sunny = False

if (temperature > 25) or is_sunny:
    print("Go to Beach")
else:
    print("Go read a book inside")
