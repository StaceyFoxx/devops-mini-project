"""
LISTS
Hold a collection of items - within  [  ] square brackets
"""
from traceback import print_tb

# important note - lists are 0 indexed
#                  0        1       2         3
# student_names = ["Fatma", "Sara", "Arthur", "Hamed"]
#
# print(student_names[1])
# student_names[1] = 'Rhian'
# print(student_names[1])
# print(student_names)


### EXERCISE 1 ###
"""
When I'm travelling in the winter I often forget to pack warm clothes. 
Let's write a program to help me to remember the right clothes.

The program should check if the first item in the clothes list is "shorts". 
If it is it should change the value to "warm coat".
"""

clothes = ['shorts', 'shoes', 't-shirts']

# print(clothes)
# if i have shorts as my first item, then i need to change it to warm coat
if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
# print(clothes)


"""
LISTS 
Common list functions
"""

#         0    1    2    3
# costs = [1.2, 4.3, 2.0, 0.5]
# student_names = [-50, "Abbie", "Sara", 120]

# # len = 4
# print(len(student_names))
# # max = 4.3
# print(max(student_names))
# #  min = 0.5
# print(min(student_names))



"""
LIST - APPEND & in
how do we add items to a list? use .append()
how do we search within an item for a value - in 
"""

# IN - search through list
# student_name = input('Which student are you looking for? ').lower()
#
# students = ['fatma', 'sara', 'arthur', 'hamed']
#
# if student_name in students:
#     print(f'{student_name} is in the class.')
# else:
#     print(f'{student_name} is not in the class.')

# APPEND - add to a list
# students = ['fatma', 'sara', 'arthur', 'hamed']
#
# student_name = input('what is the name of the new student? ')
#
# students.append(student_name)
#
# print(students)




"""
LISTS - FOR LOOP
Iterate over every item in a list
"""

students = ['fatma', 'sara', 'arthur', 'hamed']

# for student in students:
#     print(student)
#
# count = 0
# # print(student)
# for student in students:
#     #  ['fatma', 'sara', 'arthur', 'hamed']
#     count = count + 1
#
# print(count)
#
# for student in students:
#     print(student.upper())
#
# for x in students:
#     print(x)


# new_list = []
#
# for number in range(5):
#     new_list.append(number)
#
# print(new_list)
#


"""
LIST - COMPREHENSION
"""

# new_list = []
#
# for num in range(5):
#     new_list.append(num)
#
# # print(new_list)
#
# #  Simple list comprehension
# #  for every item in a list/collection
# new_list = [ num for num in range(5) ]
# # [ 0, 1, 2, 3, 4 ]
# print(new_list)
#
# # Simple list comprehention with a condition/conditions
# new_list = [ num for num in range(10) if (num % 2 == 0) and (num < 5 ) ]
# print(new_list)

# #  list comprehension example with string
# new_list = ['fatma', 'sara', 'arthur', 'hamed']
# upper_list = [ name.upper() for name in new_list ]
# print(upper_list)
#
# #  list comprehension example with string  WITH condition
# new_list = ['fatma', 'sara', 'arthur', 'hamed']
# m_name_list = [ name for name in new_list if 'm' in name ]
# print(m_name_list)
#




"""
DICTIONARIES
"""


#  Access a value in a dictionary using the 'KEY' and [] brackets e.e person['name']
# person = {
#     'name': 'Jessica',
#     'age': 23,
#     'height': 172
# }
#
# print(person['name'])



place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 54,
    }
}

# print(place['name'])
# print(place['post_code'])
# print(place['location'])
# print(place['location']['latitude'])

#  get list of all values in a dict
# print(place['location'].values())

#  get list of all keys in a diction
# print(place.keys())


# fruits = [
#      {'name': 'apple', 'colour': 'red', 'price': 0.12},
#      {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#      {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# for fruit in fruits:
#     print(fruit['name'])
#     print(fruit['colour'])
#     print(fruit['price'])


fruit =  {
    'name'    : 'apple',
    'colour'  : 'red',
    'price'   : 0.12
}

# how to loop over the items in a dictionary
# for key, value in fruit.items():
#     print(key)
#     print(value)
#     print('-')
#
# for key in fruit.keys():
#     print(key)
#
# for value in fruit.values():
#     print(value)



"""
RANDOM MODULE
random module helps provide and get random values
"""
# import random
#
# colors = ['red', 'green', 'blue']
# chosen_color = random.choice(colors)
# print(chosen_color)




"""
TUPLE
similar to a list - BUT it is immutable i.e. you cannot reassign or change any of the values
"""
#           0            1         2
# order = ('croissant', 'coffee', 'juice')

#  cannot add to a tuple or reassign values to it
# order.apenned('porridge')
# order[0] = 'porridge'

#  accessing a specific item location
# first_order = order[0]
# print(first_order)


"""
TUPLE & FOR LOOPS
"""

# order = ('croissant', 'coffee', 'juice')
# for item in order:
#     print(f'Order item: {item}')




"""
SETS
"""

my_set = {1, 2, 3, 4, 5, 'hi', 7}

# # how to add to a set
# my_set.add(6)
# print(my_set)


# #  if you add a value that already exist in the set - it will only show once i.e no duplicates allowed!
# my_set.add(6)
# print(my_set)

# words = ['hi', 'potato', 'car', 'hi', 'hi', 'car']
# result = set(words)
# print(result)












































