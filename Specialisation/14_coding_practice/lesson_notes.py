"""
FIND THE THREE LARGEST NUMBERS
Given a list of integers, return the three largest numbers in ascending order
(smallest → largest).
CANNOT use sorting!

E.G.

# Case 1, result = [18, 141, 541]

# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# print(find_3_largest_nums(array))

Brainstorm:
inp = [1, 2, 3, 49, 1, 23, 7, 18]
tracker list = [None, None, None]

for every num in the input list:
    compare and update for every position in the tracker list
                - add to the lst if the placeholder is there or update the num
                - mindful of the index position, we want it in ascending order
                   - compare against every num in tracker, if it's smaller? only add if its
                        bigger than value in tracker position

return tracker list
"""


def find_3_largest_nums(nums):
    # Initialise with very small values
    first = second = third = float('-inf')

    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return [third, second, first]



####################################################
"""
CFG Solution
"""

# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

def find_3_largest_nums(arr):
    three_largest = [None, None, None]

    for num in arr:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_n_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_n_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_n_update(three_largest, num, 0)


# idx =>   0      1     2
# nums => max2   max1   max1_new

def shift_n_update(three_largest, num, idx):
    for i in range(idx + 1):
        if i == idx:
            three_largest[i] = num
        else:
            three_largest[i] = three_largest[i + 1]
















# Case 1, result = [18, 141, 541]

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(find_3_largest_nums(array))

####################################################

# Case 2, result = [8, 8, 10]
array = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
print(find_3_largest_nums(array))

####################################################

# Case 3, result = [1, 1, 1]
array = [1, 1, 1, 1, 1, 1, 1, 1]
print(find_3_largest_nums(array))

###################################################

# Case 4, result = [-2, -1, 7]
array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
print(find_3_largest_nums(array))

####################################################







