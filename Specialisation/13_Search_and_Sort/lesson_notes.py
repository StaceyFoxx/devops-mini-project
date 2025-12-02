"""
BUBBLE SORT
"""

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            [1, 2, 3, 8]
            prev = arr[i - 1]
            curr = arr[i]
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr


# print(bubble_sort([2, 3, 1, 8]))




"""
SELECTION SORT
"""
 # 0  1  2  3
# [1, 2, 4, 6]

def select_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            curr_min = arr[min]
            # values from the unordered group
            value_j = arr[j]
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

arr= [2, 6, 4, 1]
# print(select_sort(arr))


"""
INSERTION SORT
"""
#      0  1  2  3  4  5
arr = [2, 5, 6, 9, 8, 1]

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr


# print(insertion_sort(arr))



"""
EXTRA
"""


######### QUICK SORT ##########


# helper function No 1
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


# helper function No 2
def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)


# main function No 1
def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


######### MERGE SORT ##########


# main function
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


# helper function
def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged



#######################################################################################

# Timing Experiment

#######################################################################################
import sys
import timeit
import random

# generate an array of random numbers. The len of array is 1000 and numbers vary in the range 100 - 10,000
array = random.sample(range(100, 10000), 1000)

"""
Let's profile performance of our sorting functions. 
We run all sort functions with the same array 100 times each
and see what the average execution time per sorting method is. 

NB: the time return value is  *seconds as float*
"""

print("Bubble sort run 100 times in: ",
      timeit.timeit(
          stmt='bubble_sort(array)',
          setup='from __main__ import bubble_sort, array',
          number=100),
      " seconds.\n"
      )

# this one is going to be pretty slow, be patient!
print("Selection sort run 100 times in: ",
      timeit.timeit(
          stmt='selection_sort(array)',
          setup='from __main__ import selection_sort, array',
          number=100),
      " seconds.\n"
      )


print("Insertion sort run 100 times in: ",
      timeit.timeit(
          stmt='insertion_sort(array)',
          setup='from __main__ import insertion_sort, array',
          number=100),
      " seconds.\n"
      )


########## PROFILE QUICK AND MERGE SORTS ONLY IF YOU IMPLEMENTED THEM ##############


print("Merge sort run 100 times in: ",
      timeit.timeit(
          stmt='merge_sort(array)',
          setup='from __main__ import merge_sort, array',
          number=100),
      " seconds.\n"
      )

"""
NB: Quick sort is also going to be very slow and it uses lots of recursion.
There is a danger that it would exceed the depths of recursion and will throw an error.

We need to set the recursion limit to a higher number when running Quick sort. 
Also we need to use CONTEXT MANAGER, so that value gets reset once the function executed 
and we do not clutter our stack!
"""


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


with recursionlimit(5000):
    print("Quick sort run 100 times in: ",
          timeit.timeit(
              stmt='quick_sort(array)',
              setup='from __main__ import quick_sort, array',
              number=100),
          " seconds.\n"
          )





