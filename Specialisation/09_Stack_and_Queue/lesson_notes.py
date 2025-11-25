"""
STACK
"""
class StackList:
    """
    Stack implementation using a list
    LIFO - last in first out
    """

    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1


    def push(self, x):
        """
        method to add items to a 'stack' and use self.top to always point to top of the 'stack'
        """
        if self.is_full():
            print("Stack is full! calling exit()...")
            exit(1)
        print('Inserting ', x, 'into the stack')
        self.top = self.top + 1
        self.container[self.top] = x

    def pop(self):
        """
        method to remove item from TOP of the stack using the self.top pointer
        """
        print('Removing top item from stack')
        top = self.container[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        """
        method to see what value is on top of the stack
        """
        if self.is_empty():
            exit(1)
        return self.container[self.top]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        """
        return the size of the stack
        """
        return self.top + 1

    def is_full(self):
        return self.size() == self.capacity


stack = StackList(3)
# stack.push('x')
# stack.push('y')
# #
# print('Whats at the top of my stack?', stack.peek())
# removed_item = stack.pop()
# print('last removed item: ', removed_item)
# print('whats at the top of my stack?', stack.peek())
# stack.push('z')
# print('Whats at the top of my stack?', stack.peek())


"""
Stack implementation using deque class in Python
"""

from collections import deque

# NB: module deque alredy has useful methods, so we don't need to re-implement them
# stack = deque()
#
#
# stack.append('1')
# stack.append('2')
# stack.append('3')
# stack.append('4')
#
# print("Top element is", stack[-1])  # prints the stack's top (4)
#
# print("Removing", stack.pop(), "from the stack")  # removing the top element (4)
# print("Removing", stack.pop(), "from the stack")  # removing the next top (3)
# #
# # returns the total number of elements present in the stack
# print("Stack size is", len(stack))
#
# print("Removing", stack.pop(), "from the stack")  # removing the top element (2)
# print("Removing", stack.pop(), "from the stack")  # removing the next top (1)
# #
# # check if the stack is empty
# if len(stack) == 0:
#     print("The stack is empty")
# else:
#     print("The stack is not empty")



"""
QUEUE 
LIST implementation
"""

class MyQueue:

    def __init__(self, size):
        self.q = [None] * size
        self.capacity = size
        # front points to the FRONT element in the queue
        self.front = 0
        # back points to the LAST element in the queue
        self.back = -1
        self.count = 0

    def pop(self):
        if self.is_empty():
            print('Queue Underflow! Terminating process')
            exit(1)
        print('Removing item from queue')
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def append(self, value):
        if self.is_full():
            print('Queue is full! Terminating process')
            exit(1)
        self.back = (self.back + 1) % self.capacity
        self.q[self.back] = value
        self.count = self.count + 1

    def peek(self):
        if self.is_empty():
            print('Queue is empty! Terminating process')
            exit(1)
        return self.q[self.front]

    def is_full(self):
        return self.size() == self.capacity

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.count


#
# q = MyQueue(5)
#
# q.append(1)
# q.append(2)
# q.append(3)
#
# print('Queue size is ', q.size())
# print('Queue front is ', q.peek())
#
# q.pop()
# q.pop()
# print('Queue size is ', q.size())
# print('Queue front is ', q.peek())
#
# q.append(8)
# q.pop()
# q.append(9)
# q.append(10)
# q.pop()




"""
Queue implementation using deque class in Python
"""

# NB: module deque alredy has useful methods, so we don't need to re-implement them
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("The front element is", queue[0])  # 1

queue.popleft()  # removing the front element (1)
queue.popleft()  # removing the front element (2)

# Print front item of the queue
print("The front element is", queue[0])  # 3

print("The queue size is", len(queue))  # 2

# check whether the queue is empty
if len(queue) == 0:
    print("The queue is empty")
else:
    print("The queue is not empty")








