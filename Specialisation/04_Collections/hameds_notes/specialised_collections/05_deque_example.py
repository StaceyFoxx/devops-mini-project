"""
A deque (pronounced "deck", like in deck of cards) in Python stands for "double-ended queue." It is a
versatile data structure that allows fast and efficient operations from both
ends — adding and removing elements from both the left and the right sides of the queue.

NOTE
We will get back to this when we're covering Stacks and Queues later
"""


from collections import deque


normal_List = [1, 2, 3, 4, 5]
# normal_List.append(6)
# print(normal_List)
normal_List.pop(0)
normal_List.insert(0, 666)
# print(normal_List)


# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])
# print("Before:", my_deque)

# Appending and popping from both ends
my_deque.append(6)          # Appending to the right
my_deque.appendleft(0)       # Appending to the left
right_pop = my_deque.pop()   # Popping from the right
left_pop = my_deque.popleft()  # Popping from the left

# print("After:", my_deque)