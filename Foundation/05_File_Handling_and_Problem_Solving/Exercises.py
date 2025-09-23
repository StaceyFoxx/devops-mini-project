"""
EXAMPLE 2

(!!! use file: 5.3_example_two.txt, save this file in the same folder as your Python program! )

We need to demonstrate that our first solution would not work with a file that has any punctuation.
So try running file No 2 with our code to demonstrate that the result is wrong.

Now we need to modify our solution to make it compatible with ANY file with or without punctuation.

NB: there are two examples on how to solve EXAMPLE 2. Let's work with both of them.

Create a program that meets the requirements above - think creatively!

OPTIONAL - Extra credit: refine your solution above by using a translator instead:
e.g. line = line.translate(line.maketrans("", "", string.punctuation))
we will review this solution example in the drop in session on Thrusday
"""


#  SOLUTION 1 -- it is OK
#  file with punctuation (use file: 5.3_example_two.txt)
#  ------------------------------------------------------------

# fname = input("Enter file name: ")
# search_word = input("Enter word to be searched:").lower()
#
# count = 0
#
# with open(fname, 'r') as text:
#     for line in text:
#         # Remove the leading spaces and newline character
#         line = line.strip()
#
#         # Convert the characters in line to  lowercase to avoid case mismatch
#         line = line.lower()
#
#         # NB: 'clean up' each word from the punctuation
#         for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
#             line = line.replace(char, "")
#
#         # Split the line into words
#         words = line.split()
#
#         for word in words:
#             if (word == search_word):
#                 count = count + 1
#
# print("Occurrences of the word: " + search_word)
# print(count)


#  SOLUTION 2 -- MUCH BETTER
#  file with punctuation (use file: 5.3_example_two.txt)
#  ------------------------------------------------------------

# import string
#
# fname = input("Enter file name: ")
# search_word = input("Enter word to be searched:").lower()
#
# count = 0
#
# with open(fname, 'r') as text:
#     for line in text:
#         # Remove the leading spaces and newline character
#         line = line.strip()
#
#         # Convert the characters in line to  lowercase to avoid case mismatch
#         line = line.lower()
#
#         # Remove the punctuation marks from the line
#         line = line.translate(line.maketrans("", "", string.punctuation))  # much cleaner solution (we review this next)
#
#         # Split the line into words
#         words = line.split()
#
#         for word in words:
#             if (word == search_word):
#                 count = count + 1
#
# print("Occurrences of the word: " + search_word)
# print(count)