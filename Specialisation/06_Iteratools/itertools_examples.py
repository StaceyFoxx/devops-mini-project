import itertools

"""
Hamed's Q and A:

Q: What is "itertools" actually?
A: It's a build-in library, full of fast, highly memory-efficient tools for dealing with iterators.

Q: What is an "iterator" in Python?
A: It's a ONE-TIME-USE object the lets you traverse through all its elements sequentially (one at a time). 
   It is particularly useful since it allows you to do so WITHOUT loading the entire 
   collection (elements) into memory! Thus making it excellent for LARGE DATA SETS.

"""

#################################
# Infinite
#################################
# 1. Count: This function takes two optional arguments and returns an iterator.
# print the first four even numbers

result = itertools.count(start=0, step=2)

"""
Note about -> print(result)
if you run the print you get
>>> count(0, 2)

The reason being is that count has a customized __repr__() method that outputs its parameters 
in a readable format, like count(0, 2) instead of something like iterator object at memory. 
This is by design.

"""

for number in result:

    if number < 8:
        print(number)
    else:
        break

#################################
# 2. Cycle: This function takes in an iterable and goes over it indefinitely.
# print 2 three times

result = itertools.cycle('12345')
counter = 0

for number in result:
    if counter < 10:
        print(number)
        counter = counter + 1
    else:
        break

###################################
# 3. Repeat: Takes an optional times parameter that can be used as a termination condition.
# print CodeFirstGirls two times

result = itertools.repeat('CodeFirstGirls', times=2)

for word in result:
    print(word)

###################################
# Terminating
###################################


# 4. Chain: This function accepts a variable number of iterables and loops through all of them, one by one.
# iterate over three lists

list_one = ['a', 'b', 'c']
list_two = ['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)

for element in result:
    print(element)

###################################

# 5. Compress: This function takes in an iterable and a selector,
# and returns an iterable with only those items for which the corresponding selector value is true.

# find the names of people who have the COVID-19

names = ['Alice', 'Raja', 'Fatima']
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)

for element in result:
    print(element)

###################################

# 6. DropWhile: An iterable and a function (predefined or lambda) is passed to it.
# Based on the condition inside the function, dropwhile keeps on dropping values from the iterable
# until it encounters the FIRST element that evaluates to false.

my_list = [5, 5, 1, 2, 5]


def _func(item):
    return item == 0


# NOTE that _func is being passed a reference below and not actually being invoked/called
result = itertools.dropwhile(_func, my_list)
# Note to students: Can you write above with a lambda?

for elements in result:
    print(elements)

#####################################

# 8. iSlice: works much the same way as slicing a list or tuple.
# You pass it an iterable, a starting, and stopping point, and, just like slicing a list,
# the slice returned stops at the index just before the stopping point.

# Slice from index 2 to 4
result = itertools.islice('CodeFirstGirls', 2, 5)
print(list(result))

######################################

# 9. GroupBy: groups objects in an iterable.
# Example 1: group numbers

for key, grp in itertools.groupby([1, 1, 2, 2, 2, 3]):
    print('{}: {}'.format(key, list(grp)))

# group people by their age
# Example 2: group dictionaries

data = [
    {'name': 'Soujanya', 'age': 20, 'pet': 'dog'},
    {'name': 'Elena', 'age': 19, 'pet': 'cat'},
    {'name': 'Betsy', 'age': 19, 'pet': 'cat'},
    {'name': 'Ling', 'age': 23, 'pet': 'cat'}
]

grouped_data = itertools.groupby(data, key=lambda x: x['age'])

for key, grp in grouped_data:
    print('{}: {}'.format(key, list(grp)))

######################################

# 10. Tee: used to create any number of independent iterators from a single iterable.

iterator1, iterator2 = itertools.tee([1, 2, 3, 4, 5], 2)
print(list(iterator1))

# print again to see that iterator1 is now exhausted
print(list(iterator1))

# iterator2 works independently of iterator1
print(list(iterator2))

######################################

# 11. Zip Longest: advanced zip elements function

x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']

# we lose elements from x, as we can only have 3 matches with y
print(list(zip(x, y)))

# zip_longest allows all items
print(list(itertools.zip_longest(x, y)))


# create our own grouper utility function

def grouper(inputs, n, fill_value=None):
    iters = [iter(inputs)] * n
    return itertools.zip_longest(*iters, fillvalue=fill_value)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(grouper(nums, 4))

print(result)

######################################
# Combinatoric
######################################
# 7. Product: iterate over the Cartesian product of a list of iterables

a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

result = itertools.product(a, b)
print(result)

for i in result:
    print(i)

######################################

# 12. Permutation: all the possible combinations in which a set or string can be ordered or arranged.

word = 'CFG'

# no length entered so default length
# taken as 3(the length of string CFG)
result = itertools.permutations(word)

for p in list(result):
    print(p)
