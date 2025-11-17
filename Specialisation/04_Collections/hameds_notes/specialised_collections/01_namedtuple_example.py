"""
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of
position index.
"""

point = (1, 2, 3)

print("point x", point[0])

# Now look at how namedtuple does it

from collections import namedtuple

Point = namedtuple("Point", "x y z")
# Point = namedtuple("Point", ["x", "y", "z"]) # Pretty much the same thing as above

new_point = Point(1, 2, 3)

print(new_point.x)

#  Same thing but with Normal Dic - BUT MUTABLE
dict_point = {'x': 255, 'y': 0, 'z': 0}
print("x:", dict_point['x'])
