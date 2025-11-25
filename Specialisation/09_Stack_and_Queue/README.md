# Links

Stacks and quese and deques (deque explained as its own data structure): https://www.youtube.com/watch?v=A3ZUpyrnCbM
Deques used for stacks and queues: https://www.youtube.com/watch?v=xz4-VroRCso


# Lesson Review

## STACK IMPLEMENTATION USING A LIST
class StackList:
    """
    Stack Implementation using a List
    """

    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1

Explanation

container is a list of fixed size to hold stack elements.

capacity defines how many items the stack can hold.

top keeps track of the current top index — starts at -1 to indicate an empty stack.

The top pointer moves upward (incremented) each time an element is added and downward (decremented) when removed.

This pointer movement mimics how stacks behave in low-level memory (like array-based stacks in C).

    def push(self, x):
        if self.is_full():
            print("Stack is full! Calling exit()…")
            exit(1)

        print("Inserting", x, "into the stack…")
        self.top = self.top + 1
        self.container[self.top] = x

Explanation

push() adds an element on top of the stack.

Before adding, it checks if the stack is already full using is_full().

self.top = self.top + 1 moves the pointer one step up.

Then the new element x is placed at that index.

The stack grows upward, so top always points to the newest element.

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Calling exit()…")
            exit(1)

        print("Removing", self.peek(), "from the stack")
        top = self.container[self.top]
        self.top = self.top - 1
        return top

Explanation

pop() removes and returns the element at the top.

Checks if the stack is empty first (to avoid “underflow”).

Uses peek() to show what’s being removed.

After removing, decreases top by 1 — moving the pointer down to the previous element.

The removed slot remains in memory but is now “inactive.”

    def peek(self):
        if self.is_empty():
            exit(1)
        return self.container[self.top]

Explanation

Returns the current top element without removing it.

Useful to check the “next” element that would be popped next.

    def size(self):
        return self.top + 1

Explanation

Since top starts at -1, the size is always one more than the top index.

Example: if top = 2 → size = 3.

    def is_empty(self):
        return self.size() == 0

Explanation

Checks whether stack has zero elements.

Returns True when top = -1.

    def is_full(self):
        return self.size() == self.capacity

Explanation

Returns True if number of elements equals total capacity — meaning no more push() allowed.

stack = StackList(3)
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.push(3)

print("Top element is", stack.peek())
print("The stack size is", stack.size())
stack.pop()

if stack.is_empty():
    print("The stack is empty")
else:
    print("The stack is not empty")

Explanation

Demonstrates a full cycle: push → pop → check top → check size → check emptiness.

The top pointer moves up and down with each operation, maintaining the LIFO (Last In, First Out) behavior.

## STACK IMPLEMENTATION USING deque
from collections import deque

stack = deque()
stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4')

print("Top element is", stack[-1])
print("Removing", stack.pop(), "from the stack")
print("Removing", stack.pop(), "from the stack")
print("Stack size is", len(stack))
print("Removing", stack.pop(), "from the stack")
print("Removing", stack.pop(), "from the stack")

if len(stack) == 0:
    print("The stack is empty")
else:
    print("The stack is not empty")

Explanation

deque (from the collections module) is a double-ended queue, ideal for stacks.

.append() adds items to the top.

.pop() removes items from the top — automatically providing LIFO functionality.

stack[-1] gives the top item.

len(stack) gives the current number of elements.

Faster and cleaner than manual list manipulation — Python manages pointers internally.

## QUEUE IMPLEMENTATION USING A LIST
class MyQueue:

    def __init__(self, size):
        self.q = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

Explanation

Sets up a queue with a fixed size.

front points to the first element to be removed next.

rear points to the last inserted element.

count keeps track of total active elements.

The (index + 1) % capacity pattern in later functions creates a circular queue:

It allows wrapping around the list when you reach the end, preventing wasted space.

    def pop(self):
        if self.is_empty():
            print("Queue Underflow!! Terminating process.")
            exit(1)

        print("Removing element…", self.q[self.front])
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

Explanation

pop() removes an element from the front (FIFO behavior).

The front pointer moves forward using modular arithmetic:

(self.front + 1) % self.capacity ensures that when you reach the end of the list, it loops back to 0.

This is why it’s called a circular queue — efficient reuse of space.

Decreasing count keeps track of the current queue size.

    def append(self, value):
        if self.is_full():
            print("Queue is full! Terminating process.")
            exit(1)

        print("Inserting element…", value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

Explanation

append() adds a new element to the rear.

Similar modular pointer logic ensures wrapping.

rear keeps track of where the newest element goes.

Increasing count tracks the new queue size.

    def peek(self):
        if self.is_empty():
            print("Queue is empty!! Terminating process.")
            exit(1)
        return self.q[self.front]

Explanation

Returns the front element without removing it.

Useful for checking which item will leave the queue next.

    def size(self):
        return self.count

Explanation

Simply returns how many active items are in the queue.

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

Explanation

Boolean checks for the queue’s current state.

is_full() helps prevent overflow; is_empty() prevents underflow.

q = MyQueue(5)
q.append(1)
q.append(2)
q.append(3)

print("The queue size is", q.size())
print("The front element is", q.peek())
q.pop()
print("The front element is", q.peek())

q.pop()
q.pop()

if q.is_empty():
    print("The queue is empty")
else:
    print("The queue is not empty")

Explanation

Demonstrates basic queue operations:

Items enter from the rear (append()).

Items leave from the front (pop()).

The order of removal matches the order of insertion — FIFO behavior.

## QUEUE IMPLEMENTATION USING deque
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("The front element is", queue[0])
queue.popleft()
queue.popleft()
print("The front element is", queue[0])
print("The queue size is", len(queue))

if len(queue) == 0:
    print("The queue is empty")
else:
    print("The queue is not empty")

Explanation

deque again provides a simpler, efficient alternative.

.append() adds to the rear.

.popleft() removes from the front.

Automatically manages internal pointers and resizing.

This perfectly fits FIFO behavior — no need for manual pointer math.

Summary of Pointer Movements
Structure    	Pointer	       Moves On	         Moves Direction	    Purpose
Stack	        top	           push() / pop()	 Up and down	        Tracks last inserted element
Queue	        front	       pop()	         Forward (modulo)	    Points to oldest element
Queue	        rear/back	       append()	         Forward (modulo)	    Points to newest element

Why use modulo (%) arithmetic?

To make the queue circular, avoiding wasted space at the start of the list.

Once rear or front reach the end, (index + 1) % capacity wraps it back to 0.

Real-world analogy:

Stack = A pile of plates (add/remove from top).

Queue = A line of people waiting (first person in line is served first).