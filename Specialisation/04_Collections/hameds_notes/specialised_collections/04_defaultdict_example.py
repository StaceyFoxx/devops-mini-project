"""
defaultdict is a subclass of the built-in dict class, and it overrides one method to
provide a default value for a nonexistent key. This makes it particularly useful when
dealing with dictionaries where you want to ensure that certain keys always have a default
value, even if they haven't been explicitly set.

NOTE!
By "override one method" it means that it overrides the __missing__ method of the
built-in dict class. The __missing__ method is called by the dict class when a key is
not found. defaultdict extends this method to provide a default value for the missing key
"""
from collections import defaultdict

# Look at this error for a normal dict
mydict = dict()
# print(mydict)
# mydict["age"] = 0  # what happens if you don't add this line before next?
# print(mydict["age"])
# mydict["age"] += 40
# print(mydict)

# instead look at this
# do above but with defaultdict

mydict = defaultdict(int)
# print(mydict)
# mydict["age"] += 40
# print(mydict)

#  REAL WORLD-ish example of usage
from collections import defaultdict

student_grades = [('Alice', 'A'), ('Charlie', 'B')]

# Create a defaultdict to store student grades with a default value of 'N/A'
grade_records = defaultdict(lambda: "Not Graded")

# Update the grades for each student
for student, grade in student_grades:
    grade_records[student] = grade

print("Grade for Alice:", grade_records['Alice'])
print("Grade for Charlie:", grade_records['Charlie'])
print("Grade for BOB:", grade_records['BOB'])
