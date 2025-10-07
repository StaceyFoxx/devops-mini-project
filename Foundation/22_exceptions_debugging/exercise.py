"""
Create a program that will:
- validate an input name
- validate an input age
- raise error if any fail
- or if passed, then
    - open registration file, enter the person details
    - if any error here, handle the error
- always end the script
"""

def name_validated(name):
    # validate that a comma is in the name
    if "," not in name:
        raise ValueError('Incorrect input, expected a comma between name and surname')

    name, surname = name.split(',')

    #  check that the first and last name exist and are not empty
    if not len(name) or not len(surname):
        raise ValueError('Incorrect input, missing a name or surname')


def age_validated(age):
    # check valid age, i.e. not under 0
    if age < 0:
        raise ValueError('Incorrect input, age cannot be negative')

    # check that it is a teenage between 13 - 19
    assert 13 <= age <= 19

    return True


if_successful = False

try:
    #  accept name and surname from a user separated by comma
    #  accept an age from the user
    # save them into variables
    full_name = input('Please enter your name and surname separated by a comma e.g "John,Smith": ')
    #  run validations ont he name
    name_validated(full_name)
    age = int(input('Please enter your age: '))
    #  run validations on the age
    age_validated(age)

except ValueError as exc:
    print('Invalid Input: %s' % exc)

except AssertionError as exc:
    print("The age is not within the 'teenager' category")
else:
#     if all validations have run and NO errors were ran, then write into the registration file
    try:
       with open('register.txt', 'a+') as fn:
           fn.write(f'New member name {full_name} and age {age}.\n')
       if_successful = True
    except Exception as exc:
        print('Error with writing into the file! %s' % exc)
finally:
    # always run whether an error was raised or not
    if if_successful:
        print('Registatration complete.')
    else:
        print('Could not complete registration. Please try again.')



def readFile(file_name):
    """
    write a function that accepts a name and checks if it already is registered and print out their details
    :param file_name:
    :return:
    """