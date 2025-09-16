### EXERCISE 3 ###
"""
PROBLEM SOLVING WITH PYTHON -->

Write a Python program to count the occurrences of a word in a text file.
Your program will take a word from the user and count the number of occurrences of that word in a file.

(use file: 5.3_example_one.txt, save this file in the same folder as your Python program! )
"""
# take the file name and the word to be counted from the user
fname = input('Enter file name: ')
serach_word = input('Enter word to be searched: ').lower()
count  = 0
# read each line from the file and split each line to get the words
with open(fname, 'r') as text:
    content = text.readlines()
    #  loop through the list and split each row to get the words
    for row in content:
        words = row.split(' ')

#         evaluate every word in words to check if it is the searched_word
        for word in words:
            word = word.rstrip('\n')
            if word == serach_word:
                count += 1


print(f'Occurrences of the word {serach_word} is {count}')