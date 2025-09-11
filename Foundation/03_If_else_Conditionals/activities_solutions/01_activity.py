"""
Movie Age Check

Write a program that asks the user for their age and checks if they
are old enough to watch a PG-13 movie.

"""

# Instructions for students:
# 1. Ask the user for their age (convert input to an integer)
# 2. Check if they are 13 or older
# 3. If they are 13 or older, print a message saying they can watch the movie


age = int(input("What is your age? "))


if age >= 13:
    print("You are old enough to watch a PG-13 movie.")
else:
    print("You are NOT old enough to watch a PG-13 movie.")


