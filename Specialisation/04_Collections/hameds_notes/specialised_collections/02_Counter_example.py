"""
Counter is used to count the occurrences of elements in a collection, such as a list or a
string. It's essentially a specialized dictionary where elements are stored as keys,
and their counts as values. The Counter class provides a convenient and
efficient way to perform counting operations on iterable objects


It's a powerful tool for data analysis, statistics, and various scenarios where you
need to quickly determine the frequency of elements in a collection.
"""

from collections import Counter

elements = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

element_counter = Counter(elements)

print(element_counter)
print(element_counter['a'])
print(element_counter.most_common(1))

### Same thing but done using normal dictionary

element_counts = {}

for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1

# print("Count of 'a':", element_counts.get('a', 0))
