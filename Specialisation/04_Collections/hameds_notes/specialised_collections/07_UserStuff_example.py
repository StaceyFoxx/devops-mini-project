"""
UserDict provides a dictionary-like wrapper around a regular dictionary.
It's designed to make it easier to create custom dictionary-like classes by providing
a simple way to subclass and extend the behavior of dictionaries
"""
from collections import UserDict, UserList


class CustomDictionaryWithoutPop(UserDict):
    def pop(self, s=None):
        return "No Pop Today!"


a_dict = CustomDictionaryWithoutPop({"A": 666, "B": 777})


# print(a_dict)
# print(a_dict.pop("A"))
# print(a_dict)


# USER LIST

class MyUniqueList(UserList):

    def add_in_middle(self, item):
        if len(self) == 0:
            self.append(item)
        else:
            middle_index = len(self) // 2
            self[middle_index] = item


my_list = MyUniqueList([1, 2, 3, 4, 5])
print(my_list)
#
my_list.add_in_middle("CFG")
print(my_list)
