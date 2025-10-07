"""
ASSERTIONS
"""

def apply_discount(product, discount):
    """
    Add a discount to the product price
    :param product: dict obj, item specs incl. price
    :param discount: float, discount value
    :return: float new discounted price
    """
    # calculate the price
    price = round(product['price'] * (1.0 - (discount / 100)), 2)
    # asset that is within the bounds i expect i.e. not free and less that original price
    assert 0 <= price <= product['price']
    # return the new price
    return price

#### INVALID INPUT (comment / uncomment to use  as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 200 #(represents 200%) --> Assertion Error will be raised
# print(apply_discount(trainers, discount))

#### VALID INPUT (comment / uncomment  to use as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 25 #(represents 25%)
# print(apply_discount(trainers, discount))

"""
USER DEFINED EXCEPTIONS/ERRORS
example of how we verify data before running a function
"""
#
# class AuthorisationError(Exception):
#     pass
#
# gym_members = []
#
# def cancel_membership(membership_id, user):
#     """
#     cancel gym membership for an existing member
#     """
#     # verify that user is admin of this account
#     if not user.is_admin():
#         raise AuthorisationError("Must be a member to cancel.")
#
#     # verify that the memborship id exists
#     if not gym_members.membership_exists(membership_id):
#         raise ValueError('Unknown id.')
#
#     # If verified and passes checks, then we can delete the membership
#     gym_members.find_membership(membership_id).delete()









"""
TRY/EXCEPT
"""

# # Example 1 - try / except
# denominator = int(input("Please enter a number to divide by: "))
# try:
#     division_result = 100 / denominator
#     print("Division result:", division_result)
# except ZeroDivisionError:
#    print('You cannot divide by zero, please try again.')

# # Example 2 - try / except - multiple exceptions
# denominator = input("Please enter a number to divide by: ")
# try:
#     denominator = int(denominator)
#     division_result = 100 / denominator
#     print("Division result:", division_result)
# except ZeroDivisionError:
#    print('You cannot divide by zero, please try again.')
# except ValueError:
#     print('Wrong input! Please enter a number only')
# except Exception:
#     print('Something went wrong, please try again.')
# else:
#     # run ONLY when exceptions are NOT raised
#     print('All ran successfully')
# finally:
#     #  this will run no matter what
#     print('That is the end of the division script!')


# # example 3 - raise exception
# number = input('Enter a number in the range 5-10: ')
#
# try:
#
#     # validate that the input is numeric
#     if not number.isnumeric():
#         raise ValueError
#
#     # if it is numeric convert to an integer
#     number = int(number)
#
#     # validate that the number is within the expected range
#     if number < 5 or number > 10:
#         raise Exception
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
#
# except ValueError:
#     print('Numeric input expected between 5 and 10, please try again.')
# except Exception:
#     print("Error occurred. please try again: ")






# EXAMPLE 3 - user defined errors

# class ValueIsBelowHundredError(ValueError):
#     """Raised when value is below 100"""
#     pass

import pdb

# EXAMPLE 4 - debugging

# def debugging_n_breakpoints():
#     my_list = []
#     for i in range(10):
#         new_i = 10 + i
#
#
#         # pdb.set_trace()
#
#         print('new value is: ', i)
#         my_list.append((new_i))
#     return my_list
#
# debugging_n_breakpoints()














