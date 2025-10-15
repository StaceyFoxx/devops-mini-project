"""
Phone Number Validator

Write a function called validate_phone that checks if a string is a valid phone number
according to the following rules:

1. The phone number must be in the format: XXX-XXX-XXXX (3 digits, hyphen, 3 digits, hyphen, 4 digits)
2. All characters except hyphens must be digits
3. The first digit cannot be 0 or 1 (US area codes don't start with these)
4. The first three digits (area code) cannot be 911
5. The middle three digits cannot be all the same digit (e.g., 555)

Your function should return True if all conditions are met, and False otherwise.


"""


def validate_phone(phone_number):
    pass


# Test cases
print(validate_phone("212-4567890"))  # False (wrong format)
print(validate_phone("123-456-7890"))  # False (area code starts with 1)
print(validate_phone("911-456-7890"))  # False (area code is 911)
print(validate_phone("212-555-3456"))  # False (middle section has all same digits)
print(validate_phone("212-456-7890"))  # True
