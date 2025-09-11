"""
IF-ELIF-ELSE Statements:

If-elif-else handles multiple conditions:
- Check first condition with 'if'
- Check additional conditions with 'elif'
- Optional 'else' for when no conditions are True

Syntax:
    if condition1:
        code for condition1
    elif condition2:
        code for condition2
    elif condition3:
        code for condition3
    else:
        code when no conditions match
"""

temp = 15


if 0 <= temp < 10:
    print("Its VERY cold outside")
elif 10 <= temp < 20:
    print("It's fairly cold but you're fine")
elif 20 <= temp < 30:
    print("ITs pretty warm")
elif 30 <= temp < 40:
    print("It's Very warm")
elif 40 <= temp < 50:
    print("DO GO OUT - ITS TOOO HOT")
else:
    print("I dont know what temp it really is!!!! its probably over 50")

