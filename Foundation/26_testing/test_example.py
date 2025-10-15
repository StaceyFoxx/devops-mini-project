"""
Task:

Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
if x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

notes:
an input is always within the range of 1 to 100 inclusive
"""
from jedi.api import file_name

"""
BLUE
even  
above 20 OR is 2, 3, 4 or 5


RED
odd 
even and between 6 - 20
"""

def is_even(num):
    return num % 2 == 0


def is_within_range(num, min, max):
    if min <= num <= max:
        return True
    else:
        return False


def red_or_blue(num):
    if (not is_even(num)) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'
    if  is_even(num) and (is_within_range(num, 2, 5) or is_within_range(num, 20, 100)):
        return 'Blue'
    return 'Could not evaluate number'

# print(red_or_blue(10))
# print(red_or_blue(97))
# print(red_or_blue(4))
# print(red_or_blue(23))


"""

Task
Given a list of dictionaries where keys are student's  name and values are  student's mark.
calculate the average score for the exam.

If mark is not within the range 1 to 10, raise an error
Some mark values can be integers and some are strings, we need to process both
If mark is missing, use value 5

[
    {'name': 'Jane', 'mark' : 7},
    {'name': 'John', 'mark' : '8'},
    {'name': 'Joey', 'mark' : } # auto populate mark to a 5
]
"""

def average_exam_score(student_marks):
    denominator = len(student_marks)
    marks = []

    for result in student_marks:
        try:
            mark = result['mark']
        except KeyError:
            mark = 5

        if not 10 > mark > 1:
            raise ValueError("Mark value is not in the valid range")

        marks.append(mark)

    return sum(marks) / denominator









"""""
read a file line by line and check the number of the last line. 
Extract that number, increment by 1 and return the new number 

If you have a file example.txt like this:

1. Melon
2. Pear
3. Apple


[ '3', ' Apple' ]


Read the last line, extract number 3 and increment it by 1.  
returns 4

"""

def get_file_content(file_name):
    # open the file in read
    with open(file_name, 'r') as f:
        #  read lines
        content = f.readlines()

    # extract number from last line and  convert to int and return that number incremented
    num = int(content.pop().split('.')[0])
    return num + 1


# second mock function example
def get_item_price(item):
    """Pretend to fetch item price from a database or API"""
    print("Fetching real price...")  # we don't want this to run in tests
    prices = {"apple": 1.5, "banana": 2.0, "milk": 1.2}
    return prices.get(item, 0)

def calculate_total(item, quantity):
    """Calculate total cost of items"""
    price = get_item_price(item)
    total = price * quantity
    return total










