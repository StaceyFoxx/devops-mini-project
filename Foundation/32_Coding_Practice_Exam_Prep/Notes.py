"""
Challenges:
Data Structures

"""

#  INPUTS
# pay attention to input type and what is represent
#  and whether you need to perform any operations on it within your function
code, acc, id = "1234,578,9".split(',')

# OUTPUS
#  check what data type is expected as an output
#  e.g. 'True' and True are different

# Deciding which data structure to use within your solution?
"""
First understand what the challenge is looking for you to do, i.e. what operation?
e.g. Searching, sorting, counting, or grouping?

ordering/iterating over a sequence - List 
unique checking/ distinction - set 
key value mapping - dictionary
counting or frequency - list/dictionary 
fixed size unchanging group of values - tuple

Do I need order?
→ Use a list or tuple.

Do I need uniqueness?
→ Use a set.

Do I need to map keys to values?
→ Use a dictionary.

"""


"""
Challenge 1 

Prompt:
You are given a list of numbers. Return the first value that appears more than once.
If there are no duplicates, return None.

Example:

nums = [4, 1, 2, 3, 2, 5]
# Expected output: 2


solution approach:
input is a list, i will be iterating over

steps -
create an empty set (placeholder)
loop through the list
update the set with that number
    - if the number i try to add already exists in the set, then break bc that is my duplicate and return the number
otherwise continue adding

by the end of the loop, not duplicates were found, i return None

"""

# # FUNCTIONS - are resuable pieces of code
# #  something may go in, something will process and something may go out
# def first_dup(nums):
#     #  a set is a data structure that allows for unique values only
#     seen = set()
#     for n in nums:
#         if n in seen:
#             return n
#         seen.add(n)
#     return None
#
# # the function call will return something and THEN you print it if you are checking your own work etc
# print(first_dup([4, 2, 1, 2, 3, 5]))




"""
Challenge 2 - word frequency counter

Prompt:
Given a string of text, return a dictionary showing how many times each word appears.
Ignore case and punctuation for simplicity.

Example:

text = "Code First Girls code first future future future"
# Expected output: {'code': 2, 'first': 2, 'girls': 1, 'future': 3}

steps:

first i get all the words - .split() to get a list of words and convert to lower

create an empty dictionary to hold the words and the counts against each of them

loop through every word in my list
    - if the word is in the dict then add one
    - else create new entry in dict and set it to count one

return a dictionary 

"""


def word_freq(text):
    #  convert to lowercase
    text = text.lower()
#      split the words
    words = text.split(' ')
#     create result dictionary
    counts = {}
#     loop over words and count every instance seen
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
#     return the counts list
    return counts

print(word_freq("Code First Girls code first future future future"))

















