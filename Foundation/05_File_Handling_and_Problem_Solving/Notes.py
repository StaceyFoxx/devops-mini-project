"""
FILE HANDLING - OPEN()
"""

# file = open("test.txt", 'r')
# open() will create the file object we can use to interact with the file in python
# print(file)

"""
READ()
"""

# read() will read ALL content from a file and pop that into a variable
# content = file.read()
# print(content)
# print(type(content))


"""
READLINE()
"""
# readline() will read only the first line of a file - \n <- new line in a file
# content = file.readline()
# print(content)


"""
READLINES()
"""

# content = file.readlines()
# print(content)
# print(type(content))

# file.close()


"""
FILE HANDLING - WRITE TO FILE
- write to an existing file
- append to an existing file
"""

"""
WRITE()
"""
# # OPEN() a file to create the file object - use 'w' for write mode
# file = open("test.txt", 'w')
#
# # WRITE a line into the file object
# file.write("Frankly, my dear, I don't give a damn. (GONE WITH THE WIND)")
#
# # CLOSE() the file after all operations are done
# file.close()


"""
APPEND()

"""

# # first open the file
# file = open("test.txt", "a")
#
# # setup lines to write into a file
# movie_quotes = [
#     "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
#     "\nMay the Force be with you. (START WARS)",
#     "\nThere's no place like home. (THE WIZARD OF OZ)"
# ]
#
# # write the lines into the file
# file.writelines(movie_quotes)
#
# # close the file
# file.close()


"""
WITH BLOCK
Context manager to handle open() and close() of a file during file handling in python
"""

# # setup the lines to write into a file
# movie_quotes = [
#     "\nThis is second randomly generated new line"
# ]
#
# # use with block to open a file
# with open("test.txt", 'a') as file:
#     # write the movie quote lines into a file object
#     file.writelines(movie_quotes)


### EXERCISE 1 ###
"""
Create a to-do list program that writes user input to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items

NB: You will need to manually create a new file called todo.txt in the same folder 
as your program before you start.
"""

# # Ask the user to input a new to-do item
# new_item = input('Enter a to-do item: ')
#
# # Read the contents of the existing to-do items
# with open('todo.txt', 'r') as todo_file:
#     content = todo_file.read()
# # WITH() block automatically CLOSE() the file
#
# # Add the new to do item to the existing to-do items
# todos = content + '\n' + new_item
#
# # Save the updated to-do items into the file
# with open('todo.txt', 'w+') as todo_file:
#     todo_file.write(todos)



"""
CSV
file operations through the csv library in python
- writing to a CSV file
- reading data from a CSV file
"""

import csv

# define the header names
field_names = ['name', 'age']

# setup the data values as a list of rows and k:v pairs, where key is a header and a value is the row value
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28}
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    print(type(spreadsheet))
    #  use writeheader to write out the fieldnames we passed when creating a csv object
    spreadsheet.writeheader()
    # use writerows to write out data rows into the csv
    spreadsheet.writerows(data)
















