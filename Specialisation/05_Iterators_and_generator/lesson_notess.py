"""
Intro Iterator
"""

nums = [2, 4, 1, 9 ,6]
# print(type(nums))

# convert collection object list into an iterator object
nums_iter = iter(nums)
# print(type(nums_iter))

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))


"""
Create our own iterator
"""

class EvenNumbers:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        next_num = self.num
        self.num += 2
        return next_num

# this is just a EvenNumbers object i.e. using the init method behind the scenes
evens = EvenNumbers()
# use the EvenNumbers version of the iter method to turn it into an iterator object
evens_iter = iter(evens)
# print(next(evens_iter))
# print(next(evens_iter))
# print(next(evens_iter))
# print(next(evens_iter))
# print(next(evens_iter))


class EvenNumbers2:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num < 10:
            next_num = self.num
            self.num += 2
            return next_num
        else:
            raise StopIteration


evens2 = EvenNumbers2()
evens_iter2 = iter(evens2)
#
# for n in evens_iter2:
#     print(n)
#
# print(next(evens_iter2))




"""
Circle sequence example
"""
#  0   1  2  3  4  5  6  7  8  9  10  11
# [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

class CircleSequenceIterator:

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        # if i have reached the predefined max times value then stop iterating!
        if self.index >= self.max_times:
            raise StopIteration

        # get the next value in a circular way i.e. think clocks!
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value



class CircleSequence:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CircleSequenceIterator(self.data, self.max_times)


c = CircleSequence('xyz', 5)
# print(list(c))

c2 = CircleSequence(range(1, 13), 13)
# print(list(c2))

# c3 = CircleSequence([[1, 2], [3, 4]], 10)
# print(list(c3))





""""
GENERATATORS

"""

def my_gen():
    n = 1
    print('This is printed first')
    # generator functions contain YIELD statements not RETURNS
    yield n
    # checkpoint 1 <- state

    n += 1
    print('This is printed second')
    yield n
    # checkpoint 2 <- state

    n += 1
    print('This is printed third')
    yield n
#    third next() call stops here

g = my_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))



"""
Generator expressions
"""

my_list= [1, 3, 6, 10]

# we can square each term using list comprehension
new_list = [x**2 for x in my_list]

# could do the same things using a generator expression
# generators expressions are surrounded by () instead of [] seen in list comprehension
gen = (x**2 for x in my_list)

# print('Original List', my_list)
# print('List comprehension', new_list)
# print('Generator object', gen)
# print('Generator Object List', list(gen))

#  use next() to go over ever item in the generator object
# OR i can also iterate over it using a for loop BC an iterator object is iterable

# [1, 9, 36, 100]
# print(next(gen))
# for i in gen:
#     print(i)



"""
Generator VS Iterator
generators are easier to implement
rule of thumb - iterators create classes and generators to create functions
"""

# Iterator

class PowerThreeSequence:

    def __init__(self, max_times):
        self.max_times = max_times
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max_times:
            raise StopIteration

        res = 3 ** self.n
        self.n += 1
        return res

# obj = PowerThreeSequence(5)
# print(obj.__next__())
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

#  next() only works on iterable objects
# print(next(range(1, 11)))


# this will not work bc i is the value returend i.e. 1 and that is not an iterabtle value
# for i in obj:
#     print(i)
#     print(next(i))



# Generator

def power_three_seq(max_time=0):
    n = 0

    while n < max_time:
        yield 3 ** n
        n += 1

# generator example
my_gen = power_three_seq(5)
for i in my_gen:
    print(i)

print('-'*5)

# iterator example
my_iter = PowerThreeSequence(5)
for i in my_iter:
    print(i)











