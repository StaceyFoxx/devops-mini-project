import itertools

#################################
# Infinite
#################################
# 1. Count:

# result = itertools.count(start=0, step=2)
#
# for number in result:
#
#     if number < 8:
#         print(number)
#     else:
#         break

#################################
# 2. Cycle:

# result = itertools.cycle('12345')
# counter = 0
#
# for number in result:
#     if counter < 10:
#         print(number)
#         counter = counter + 1
#     else:
#         break

###################################
# 3. Repeat:

# result = itertools.repeat('CodeFirstGirls', times=2)
#
# for word in result:
#     print(word)


###################################
# Terminating
###################################


# 4. Chain:

# list_one = ['a', 'b', 'c']
# list_two = ['d', 'e', 'f']
# list_three = ['1', '2', '3']
#
# result = itertools.chain(list_one, list_two, list_three)
#
# for element in result:
#     print(element)


###################################

# 5. Compress:

# names = ['Alice', 'Raja', 'Fatima']
# have_cat = [True, True, False]
#
# result = itertools.compress(names, have_cat)
#
# for element in result:
#     print(element)

###################################

# 6. DropWhile:

my_list = [1, 2, 3, 5, 1, 4, 7, 2, 8, 3]

# def _func(item):
#     # print(item, item < 5) # this might help
#     return item < 5
#
# result = itertools.dropwhile(_func, my_list)
#
# for elements in result:
#     print(elements)

# Hamed's 2nd example for DropWhile

# def is_odd(x):
#     # print(x, x % 2 != 0) # this might help
#     return x % 2 != 0
#
# numbers = [1, 1, 1, 3, 5, 2, 4, 6]
#
# result = itertools.dropwhile(is_odd, numbers)
#
# for num in result:
#     print(num)


#####################################

# 8. iSlice:

# result = itertools.islice('CodeFirstGirls', 2, 5)
# print(list(result))

######################################

# 9. GroupBy:

# Example 1

# for key, grp in itertools.groupby([1, 1, 2, 2, 2, 3]):
#     print('{}: {}'.format(key, list(grp)))

# Example 2 - pay attention to the dict keys

# data = [{'name': 'Soujanya', 'age': 20, 'pet': 'dog'},
#         {'name': 'Elena', 'age': 19, 'pet': 'cat'},
#         {'name': 'Betsy', 'age': 19, 'pet': 'cat'},
#         {'name': 'Ling', 'age': 23, 'pet': 'cat'}]
#
# grouped_data = itertools.groupby(data, key=lambda x: x['age'])
#
# for key, grp in grouped_data:
#     print('{}: {}'.format(key, list(grp)))

######################################
# 10. Tee

# iterator1, iterator2 = itertools.tee([1, 2, 3, 4, 5], 2)
# print(list(iterator1))
#
# # print again to see that iterator1 is now exhausted
# print(list(iterator1))
#
# # iterator2 works independently of iterator1
# print(list(iterator2))

######################################

# 11. Zip and Zip Longest:

# x = [1, 2, 3, 4, 5]
# y = ['a', 'b', 'c']
#
# print(list(zip(x, y)))
#
# print(list(itertools.zip_longest(x, y)))


######################################
# Combinatoric
######################################
# 7. Product:

# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
#
# result = itertools.product(a, b)
# print(result)
#
# for i in result:
#     print(i)


######################################

# 12. Permutation:

# word = 'CFG'
#
# result = itertools.permutations(word)
#
# for p in list(result):
#     print(p)
