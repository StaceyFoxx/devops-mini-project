"""
Note from Hamed
I've added examples from BEST to WORSE time complexity
"""


# O(1) - Constant Time
# constant time does not care about the input at all
def get_first_element(nums):
    return nums[0]



# O(log n) - Logarithmic Time
# Usually for solutions that divide the input size in half repeatedly like the below binary tree
# (which we'll teach later)
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# O(n): Linear
# Traversing all elements of a list
def find_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


# O(n log n) - Log Linear, aka Linearithmic
# Very common in effective (good) sorting algos (Will teach more sorting this week)
def sort_nums(nums):
    # Note python uses Timsort for its sorting needs which is also O(n log n)
    # We wont cover Timsort itself this week but we will look at other sorting examples.
    # https://en.wikipedia.org/wiki/Timsort
    return sorted(nums)


# O(n^2) - Quadratic
# nested for loops are usually this
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates


# O(2^n) - Exponential Time
# Recursive solutions where the input size doubles the computation, e.g., Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# O(n!) - Factorial Time
# for example an algo that generates ALL permutations of a list
def generate_permutations(nums):
    if len(nums) == 0:
        return [[]]
    permutations = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i + 1:]
        for perm in generate_permutations(rest):
            permutations.append([nums[i]] + perm)
    return permutations



# O(n + m)
# This really only happens if your dealing with 2 SEPARATE datasets.
# for example

def has_common_element(list1, list2):
    set1 = set(list1)  # Here for list1, adding all elements to a set is order n operation O(n)

    # Check each element of list2 against the set (O(m))
    for elem in list2:  # Here we have a for loop for list2 which is order m operation O(m)
        if elem in set1:  # Note here that SET LOOKUPS are O(1) in time
            return True
    return False
