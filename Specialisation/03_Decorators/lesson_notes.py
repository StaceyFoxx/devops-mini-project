""""
Decorator
demo 1 - accepting function as input
"""

def add_one(x):
    """
    add one to a value
    :param x: int
    :return: x plus 1
    """
    return x + 1

def subtract_one(x):
    """
    subtract one from a value
    :param x: int
    :return: x minus 1
    """
    return x - 1


def operate(func, x):
    """
    will run a function on value x and return the result
    :param func: a function object
    :param x: an int object
    :return: result of func(x)
    """
    # running the parameter name func as a function
    result = func(x)
    return result

# print(add_one(5))
# print(subtract_one(5))
# print(add_one)
# x = 5
# print(type(x))

# print(operate(add_one, x=5))
# print(operate(add_one, x=12))
# print(operate(subtract_one, 5))


"""
DEMO 2 
Returning functions from a function

"""


def outer_called():
    def inner_returned():
        print('Hello CFG!')
    return inner_returned

# functions can also be populated into a variable as they are first class citizens
# example_func = outer_called() # <- outer called returns a FUCNTION
# print(example_func)
# example_func() # <- the RETURNED function is now triggered here i.e. Hello CFG is triggered

"""
DEMO 3
accept an input allowing for flexibity
returning a function from anotehr function - demo2
"""

def pet_owner(num):
    def first_pet():
        return "Hi i am a cat called Tigger"

    def second_pet():
        return "Hi i am a dog called Butch"

    if num == 1:
        return first_pet
    else:
        return second_pet

# save the functions into variables
first = pet_owner(1)
second = pet_owner(2)

# the variables are function types and so they can be called!
# print(first)
# print(second)
#
# print(first())
# print(second())


"""
Demo 4
decorator example 1
"""

def enhance_my_function(func):
    def inner_wrapper():
        # logic to enhance func call (i.e. the function passed in (func))
        print('Something is happening BEFORE a simple function is called')
        func()
        print('Something is happening AFTER a simple function is called')
    return inner_wrapper

def simple_function():
    print("I am a simple function")

# simple_function()
# print('-'*10)
#
# def simple(func):
#     def inner_wrapper():
#         print('Before function call')
#         func()
#         print('After function call')
#     return inner_wrapper
#     return 5
#
# x = simple(simple_function)
# print(x)
# print(type(x))
# x()



# decorated = enhance_my_function(simple_function)
#
# # print(decorated)
# decorated()

"""
Demo 5
Syntantactical Sugar
"""

@enhance_my_function
def simple_function_2():
    print("I am a simple function")


# simple_function_2()

"""
Demo 6
Decorators and multiple parameters
"""



def clever_divide(func):
    def inner_wrapper(a, b):
        print('Lets divide ', a, ' and ', b)
        if b == 0:
            print('Whoops! Cannot divide by zero')
            # return early! why? bc a 0 was found in b and so to avoid the function call just end here
            return
        return func(a, b)
    return inner_wrapper

@clever_divide
def divide(a, b):
    return a / b

# print(divide(100, 10))

"""
Use UNIVERSAL decorators to capture any and all arguments
"""
"""
keyword arguments
  simple_function(a=1, b=2, c=3)
arguments
   simple_function(1, 2, 3)
"""
def universal_decorator(func):

    def inner_wrapper(*args, **kwargs):
        print('I can decorate a function')
        return func(*args, **kwargs)
    return inner_wrapper


"""
UNIVERSAL DECORATOR APPLIED
"""

def run_twice_decorator(func):
    def inner_wrapper(*args, **kwargs):
        print('I can run your function twice!')
        # print(*args)
        # print(**kwargs)
        print(func(*args, **kwargs))
        print(func(*args, **kwargs))
    return inner_wrapper

@run_twice_decorator
def divide_two(a, b):
    return a / b

@run_twice_decorator
def divide_three(a, b, c):
    return a / b / c

# print(divide_two(100, 2) <- ARGS
# divide_two(100, 2)
# print('-'*10)
# divide_three(a=100, b=2, c=2) # <- KEYWORD ARGS
# (a=100, b=2, c=2)

"""
Chaining Decorators
"""

def equal_sign(func):
    def inner_wrapper(*args, **kwargs):
        print('='*30)
        func(*args, **kwargs)
        print('='*30)
    return inner_wrapper

def pipe_sign(func):
    def inner_wrapper(*args, **kwargs):
        print('|'*30)
        func(*args, **kwargs)
        print('|'*30)
    return inner_wrapper

@equal_sign
@equal_sign
@pipe_sign
@pipe_sign
def display_message(msg):
    print(msg)

# display_message('Hello CFG Cohort!')

"""
DEMO 7
DECORATOR as a Class
"""

class SquareDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Something happens BEFORE function call')
        res = self.func(*args, **kwargs)
        print('Something happens AFTER function call')
        return res ** 2

# @SquareDecorator
# def multiply(a, b):
#     print('Your numbers are:', a, b)
#     return a * b
#
# print(f'Result with SquareDecorator {multiply(2, 3)}')

class SquareDecoratorWithMemory:

    def __init__(self, simple_function):
        self.function = simple_function
        self._memory = []

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs) ** 2
        self._memory.append(result)
        return result

    def memory(self):
        print('_' * 10)
        return self._memory


@SquareDecoratorWithMemory
def multiply(a, b):
    print("Your numbers are:", a, ' and ', b)
    return a * b


# print("Result with SquareDecoratorWithMemory is:", multiply(2, 3))
# print("Result with SquareDecoratorWithMemory is:", multiply(2, 2))
# print("Result with SquareDecoratorWithMemory is:", multiply(3, 3))
# print("Memory:", multiply.memory())

"""

Timer exercise
"""

import time


def timer(func):
    def inner_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('-' * 20)
        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value
    return inner_wrapper


@timer
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


@timer
def worker_function_strings(word):
    new_word = ''
    for char in word:
        new_word = new_word + ''.join('ZZZ-' + char + '-ZZZ-')
    return new_word.rstrip('-')


# print(worker_function_numbers(1))
# print(worker_function_numbers(80))
#
# print(worker_function_strings('CFG'))
# print(worker_function_strings('supercalifragilisticexpialidocious'))

############## CACHE EXERCISE ##############



"""
Challenge: Medium - Hard
Creating a @memoize decorator.
It will cache results of a function with specific parameters and would instantaneously provide an answer instead
hint:
    data structure for memory - think dictionary
    if i have the answer stored - do i need to recaclulate??
"""



