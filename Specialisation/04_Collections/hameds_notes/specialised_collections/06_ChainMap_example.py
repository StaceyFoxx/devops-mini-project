"""
ChainMap provides a convenient way  to manage multiple dictionaries as a single unit.
It allows you to create a chain of dictionaries and perform lookups and updates in the
order they are chained together. The dictionaries are treated as a single view,
making it easier to work with a collection of dictionaries as if they were a
merged or concatenated dictionary.
"""

from collections import ChainMap

# Imagine you're building a game with settings
default_settings = {
    "difficulty": "medium",
    "sound": "on",
    "graphics": "high"
}

# User changed some settings
user_settings = {
    "difficulty": "hard"
}

# Combine them with ChainMap (user settings take priority)
settings = ChainMap(user_settings, default_settings)

# print(settings["difficulty"])  # Outputs: "hard" (found in user_settings)
# print(settings["sound"])       # Outputs: "on" (found in default_settings)
# print(settings["graphics"])    # Outputs: "high" (found in default_settings)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

# Using dictionary unpacking operator (**)
normal_decomposition_way = {**dict1, **dict2, **dict3}
# NOTE what happens to "b"
# print("decomposition: ", normal_decomposition_way)


# Using ChainMap
chain = ChainMap(dict1, dict2, dict3)
# print(chain)

# for key, value in chain.items():
#     print(f"{key}: {value}", end=" ")

"""
student question:
how is it different to : list = [dict1,dict2,dict3]


Answer according to the internet:
The key difference between using ChainMap and a simple list of dictionaries is that ChainMap 
provides a unified view of the dictionaries, allowing for direct lookups across all of them 
as if they were a single dictionary, while a list does not offer this behavior. 

"""


# Further discussion on ChainMap in the wild:
# https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap