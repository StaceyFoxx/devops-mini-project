from hamed_logger import performance_logger


@performance_logger
def find_duplicates_inefficient(nums):
    """
    Find duplicates in a list using a nested loop approach.
    Time -> O(n2)
    """
    duplicates = []

    for i in range(len(nums)):
        for j in range(len(nums)):

            if i != j and nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
                break

    return duplicates


@performance_logger
def find_duplicates_efficient(nums):
    """
    Find duplicates in a list using a hash set approach.
    """
    seen = set()  # O(1) - Creating an empty set, constant time
    duplicates = []  # O(1) - Creating an empty list, constant time

    for num in nums:  # O(n) - Loop that runs n times
        if num in seen and num not in duplicates:  # O(1)
            duplicates.append(num)  # O(1) - Appending to a list is constant time
        else:  # O(1) - Condition evaluation is constant time
            seen.add(num)  # O(1) - Adding to a hash set is constant time

    return duplicates  # O(1) - Returning a reference is constant time


if __name__ == "__main__":
    tiny_list = [1, 2, 3]
    # find_duplicates_inefficient(tiny_list)
    # find_duplicates_efficient(tiny_list)

