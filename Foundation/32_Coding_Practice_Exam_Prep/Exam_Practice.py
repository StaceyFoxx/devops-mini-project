"""
Challenge 1 - SerialPlus

Input format: "XXX-YYY-ZZZ" (three groups separated by hyphens). Each group has exactly 3 digits (0–9 allowed).

Requirements:
Each group must be exactly 3 digits
Sum of digits of first group must be divisible by 3
Sum of digits of second group must be divisible by 5
The third group must contain at least one even digit
Return "true" if all constraints satisfied, otherwise "false".

Input: "123-555-246"
Output: "true"

Input: "111-222-333"
Output: "false"

steps:

first split the string on hyphen to get three groups leaving me with a list of strings
validate each group
    - check that three groups have been created, ie the split was successful
    - each group has 3 values

if blocks to check for every condition:
    - convert to int for each check before summing and dividing
    Sum of digits of first group must be divisible by 3
        if failed then exit early and return "false"
    Sum of digits of second group must be divisible by 5
        if failed then exit early and return "false"
    The third group must contain at least one even digit
        if failed then exit early and return "false"

if all have passed, ie i have reached this point of my code then return "true"

"""


def serial_plus(serial):
    if '-' not in serial:
        raise Exception

    parts = serial.split('-')

    if len(parts) != 3:
        raise Exception

    for p in parts:
#         "123" - check if the length is not 3 or it is not all digits
        if len(p) != 3 or not p.isdigit():
            return 'false'

    #   0      1      2
    # ['123', '555', '543']
    nums = [int(d) for d in parts[0]]
#     iterating over the string '123' using list comprehension to create [1, 2, 3]

#     nums = [1, 2, 3]
# Sum of digits of first group must be divisible by 3
    if sum(nums) % 3 != 0:
        return 'false'

# Sum of digits of second group must be divisible by 5
    if sum( int(d) for d in parts[1] ) % 5 != 0:
        return 'false'

    # if not any( int(d) % 2 == 0 for d in parts[2] ):
    #     return "false"

    nums = [int(d) for d in parts[2]]
    one_true_found = False
    #  [5, 4, 3]
    for n in nums:
         if n % 2 == 0:
            one_true_found = True
            break
    #  if not ONE of the numbers in my list is divisible by 2, then return false bc ONE number should be True
    if not one_true_found:
        return 'false'

    return 'true'

# print(serial_plus("123-555-246"))

"""
Challenge 2 - Sum of Two Targets

Prompt:
Given a list of numbers and a target value, return True if any two numbers sum to the target, otherwise False.

Example:


nums = [11, 2, 15, 7]
target = 9
# 2 + 7 = 9 ➜ True
9 - 2 = 7

steps:
create a list that acts as a placeholder for any number ive already evaluated

loop through every number in my list of numbers
    for current number im evaluating, find the difference between target and current num
        check if I have seen that number in my list, ie my placeholders
            if not then add to my list, and continue ahead
        if i do see the difference num in my placeholder list then return True
        
return false if nothing was found


"""


def has_pair_sum(nums, target):
    seen = list()

    for num in nums:
        diff = target - num
        if diff in seen:
                return True
        seen.append(num)

    return False

                    # 0    1  2  4
# print(has_pair_sum([11, 2, 15, 7], 9))



def has_pair_sum2(nums, target):
    """
        create combination by using two for loops and adding until you see a target
    """
    for idx, num in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if idx == idx2:
                continue
            if num + num2 == target:
                return True

    return False

print(has_pair_sum2([11,  2, 15, 7], 4))
