"""
BUBBLE SORT
"""

def bubble_sort(arr):
    # helper function to swap values at positions i and j
    # using a helper keeps the main code cleaner
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)

    # swapped starts as True so the loop runs at least once and only ends if no swaps are done within an iteration
    swapped = True

    # x counts how many items at the END are already in correct sorted position
    # we start with -1 so first cycle becomes -1 + 1 = 0
    # meaning: at the start, nothing is guaranteed sorted yet
    x = -1
    """ X -> keeps track of how many elements at the end are already sorted. We use it to create shrinking 
    sublists of what hasn't been sorted yet.
        More clearly:
        When x = 0 → 0 elements are guaranteed sorted
        When x = 1 → 1 element at the end is sorted
        When x = 2 → 2 elements at the end are sorted
        When x = 3 → 3 elements at the end are sorted
    """

    while swapped:
        swapped = False  # assume no swaps, will be checked each pass, if it remains False we can end i.e. no swaps needed anymore
        x = x + 1        # after each full pass, the largest element is at the end i.e. it has been BUBBLED up to the end

        # Loop goes from index 1 to the "unsorted" part n - x
        # Each cycle, we shrink the checking area because the last x elements are sorted
        for i in range(1, n - x):

            prev = arr[i - 1]
            curr = arr[i]

            # If two adjacent values are out of order, swap them
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True  # we made a swap → keep looping

    return arr


# print(bubble_sort([2, 3, 1, 8]))



"""
SELECTION SORT
"""

def select_sort(arr):
    # loop through each index of the list
    for i in range(len(arr)):

        # assume the current index i is the position of the smallest element
        # we will try to find a smaller one in the remaining unsorted portion
        min = i

        # check the rest of the list (the "unsorted group")
        for j in range(i + 1, len(arr)):
            curr_min = arr[min]
            value_j = arr[j]

            # if we find a smaller value, update min index
            if arr[j] < arr[min]:
                min = j

        # after scanning, min holds the index of the smallest value
        # swap it with the current i position
        arr[min], arr[i] = arr[i], arr[min]
        # NOTE for students:
        # If 'min' never changed (meaning the smallest value was already at position i),
        # then we are swapping the element with itself.
        # This does NOTHING — but it keeps the code simple and consistent.

    return arr


arr = [2, 6, 4, 1]
# print(select_sort(arr))



"""
INSERTION SORT
"""

# example array
# index: 0  1  2  3  4  5
arr = [2, 5, 6, 9, 8, 1]

def insertion_sort(arr):
    # start from i = 0 all the way to the end
    for i in range(len(arr)):
        # cursor temporarily stores the value we want to insert into sorted position
        cursor = arr[i]

        # pos tracks where the cursor needs to move to
        # this allows us to "shift" values right until the correct place is found
        pos = i

        # while cursor has not reached the beginning AND
        # the value before pos is bigger than cursor → shift it right
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]  # shift value right
            pos = pos - 1            # move left to keep checking

        # once the correct spot is found, place cursor there
        arr[pos] = cursor

    return arr

# print(insertion_sort(arr))


"""
EXTRA
"""


######### QUICK SORT ##########

# helper function No 1
def partition(array, begin, end):
    # We choose the first element as the pivot
    pivot_idx = begin

    # Loop through the sub-array (everything after the pivot)
    for i in range(begin + 1, end + 1):

        # If we find a value smaller than or equal to the pivot,
        # we move it towards the left "partition" area
        if array[i] <= array[begin]:
            pivot_idx += 1
            # Swap to expand the left partition
            array[i], array[pivot_idx] = array[pivot_idx], array[i]

    # Finally, swap pivot into its correct position
    # Everything left of pivot_idx is <= pivot
    # Everything right is > pivot
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]

    return pivot_idx  # return pivot's final position


# helper function No 2
def quick_sort_recursion(array, begin, end):
    # Base condition: if the sub-array has 0 or 1 elements, it's already sorted
    if begin >= end:
        return

    # Partition array: pivot placed in correct position
    pivot_idx = partition(array, begin, end)

    # Recursively sort the left side of the pivot
    quick_sort_recursion(array, begin, pivot_idx - 1)

    # Recursively sort the right side of the pivot
    quick_sort_recursion(array, pivot_idx + 1, end)


# main function No 1
def quick_sort(array, begin=0, end=None):
    # Default end index is last index of array
    if end is None:
        end = len(array) - 1

    # Kick off recursive quicksort
    return quick_sort_recursion(array, begin, end)


######### MERGE SORT ##########

# main function
def merge_sort(arr):
    # Base case: A list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # Find midpoint to split array into two halves
    mid = len(arr) // 2

    # Recursively break down left and right halves
    # This continues splitting until size reaches 1-element lists
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves back together
    return merge(left, right, arr.copy())


# helper function
def merge(left, right, merged):
    # Cursors (pointers) for each half
    left_cursor, right_cursor = 0, 0

    # Compare elements from both lists until one runs out
    while left_cursor < len(left) and right_cursor < len(right):

        # Take the smaller of the two values and put it in merged
        # This ensures the merged array is sorted
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    # If any elements remain in the LEFT half, copy them over
    # Only one of these loops will run — whichever side still has items
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # If any elements remain in the RIGHT half, copy them over
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # Return the fully merged, sorted array
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





