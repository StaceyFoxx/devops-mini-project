"""
OrderedDict is a class that maintains the order of the items based on the order they
were added to the dictionary.

NOTE
Starting from Python 3.7, the standard dict type in Python also preserves the order
of insertion.

"""
from collections import OrderedDict

ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# print(ordered_dict)
# print(ordered_dict["one"])

# You can pass a dict in as well instead of a list of tuples
another_dict = {'one': 1, 'two': 2, 'three': 3}
ordered_dict = OrderedDict(another_dict.items())
# print(ordered_dict)
# print(ordered_dict["one"])


# An interesting thing about it though
ordered_dict.move_to_end("one")
# print(ordered_dict)
