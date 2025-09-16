"""
INPUT
A way to get data from the user during program execution
"""
## use input() function with message prompt - also remember any value returned from user is a STRING
# animal = input('Do you like dogs or cats more? ')
# pet_name = input('What would you name your pet? ')
## You can use f'{}' f string to add varaibels directly into your string
# print(f'You like {animal} and you would name your pet {pet_name}')

## becuase the return of input if string, make sure to convert to int() if used in int calculation
# apples_string = input('How many apples did you buy? ')
# total_apples = int(apples_string) + 5
# print(total_apples)

"""
You have friends at your house for dinner and you've accidentally burnt the lasagne. 
Time to order pizza.
Write a program calculate how many pizzas you need to feed you and your friends
"""

# friends = input('How many friends are at your house? ')
# pizzas = int(friends) * 0.5
# print(f'You need {pizzas} for {friends} friends')

"""
MODULES
Import modules using the import or import from keywords
"""

## you can import multiple ways, either from <module> or from <module> import <function/modudle>
import datetime

# x = datetime.datetime.now()
# print(x)

## use datetime.date to create a date time object of the date you give, it expected YYYY, MM, DD
# my_date = datetime.date(2022, 12, 31)

## you can use strftime() on a datetime object to convert it to a formatted string version of the datetime
# formatted_date = my_date.strftime("%d-%b-%Y")
# print(formatted_date)


### EXERCISE 2 ###
"""
Write a program that issues notifications to drivers about PCN (Penalty Charge Notice) 
for £130. 
If a person pays within 14 days, then the amount will be reduced to £65.

Pseudo-code Example:

- Accept the PCN date as an input
- Calculate the deadline date, which is 14 days from the PCT issue date.
- Print the message informing the driver about the deadline date, so that they only 
need to pay £65.

Example solution below.
"""


# from datetime import datetime, timedelta
#
# pcn_date = input('Please enter the PCN issue date in the following format DDMMYYYY: ')

## use the strptime() function to parse a string date into a datetime
# date_obj = datetime.strptime(pcn_date, '%d%m%Y')

## we can use the timedelta() function to add or subtract time, specifying what time/date type
## e.g. days=14
# deadline = date_obj + timedelta(days=14)

## use strftime() to format a datetime object to specific format as string
# formatted_deadline = deadline.strftime("%d-%b-%Y")
#
# print(f'Of you pay PCN penalty by {formatted_deadline}, the amount will be reduced to £65')
#


"""
FOR LOOPS
Use the for <var> in <collection>: keywords and make sure to indent the for loop body
"""

# total = 0
#
# for num in range(3): # remember that range is zero indexed so - 0, 1, 2 in this example
#     print('----')
#     print("Total value is: " + str(total))
#     print("This is run no " + str(num) + " inside the loop")
#     total = total + 10 # we are updating the variable by re-assining it to the value of itself plus 10
#     print('---')
#
# print(f'Total value is: {total}')


"""
WHIlE LOOPS
use a condition to keep iterations going 
IMPORTANT - use a condition that will be false and make sure its changing within the while body
"""

#
# store_capacity = 10
#
# while store_capacity > 0: # use the while keyword and a condition that evaluates to True or False
#     print(f'Please come in, Space Available: {str(store_capacity)}')
#     store_capacity  = store_capacity - 1 # this ensures that tht condition variable is changing
      # once it reaches 0 then it will break the condition to False and exit the while loop
#
# print('Please wait for someone to exit the store')


"""
Functions
use def to start creating a function with function name then brackets with none or some arguments defined
"""
## no argument example
# def hello():
#     print('Hello class!')

## single argument example
# def hello(name):
#     print('Hello', name)

## multipe argument example
# def hello(name, job):
#     print(f'Hello {name}, your job is {job}')

# default argument example - if job is not defined during function call then this value is used
# def hello(name, job='Developer'):
#     print(f'Hello {name}, your job is {job}')

# *args will allow for any number of arguments to be passed during function call and accepted into the func
# def hello(*args):
#     print(args)

# **kwargs will allow for any number of keyword arguments to be accepted and used within the func
# def hello(**kwargs):
#     print(kwargs)

# hello(name='Fatma', course='CFG', year=2025)

"""
FUNCTION - return
"""

## return is used to allow function to output a value after its function call
## any function without a return, will automatically return a None
# def sumx_y(x, y):
#     # print(x+y)
#     return x + y


# summed_values = sumx_y(x=10, y=20)
# print(summed_values)
# print(sumx_y(100, 20))
# print(sumx_y(10, 40))
