"""
MINI CHALLENGES
"""
"""
Challenge 1 — Match Items Between Two Lists

Approach:

Create an empty list to hold matches.
Loop through each item in the first list.
If it also exists in the second list and is not already in the results, append it.

"""

def find_common_ids(list_a, list_b):
    common = []
    for item in list_a:
        if item in list_b and item not in common:
            common.append(item)
    return common

# print(find_common_ids([101, 102, 103, 104], [103, 105, 106, 101]))  # ➜ [101, 103]


"""
Challenge 2 — Simple Student Directory

Approach:
Use a dictionary with the student ID as the key.
Store each student’s details as another dictionary.
Access data directly by ID.


"""

students = {
    1001: {"name": "Amira", "grade": "A"},
    1002: {"name": "Sofia", "grade": "B"}
}

# print(students[1001]["name"])   # ➜ 'Amira'
# print(students[1002]["grade"])  # ➜ 'B'



"""
Challenge 3 - sum of digits

Approach:

Convert the number to a string (or use integer division/modulus).
Loop through each character, convert to int, and add to total.

"""
def sum_of_digits(num):
    total = 0
    for ch in str(num):
        total += int(ch)
    return total

# Test
# print(sum_of_digits(12345))  # ➜ 15

"""
Challenge 4 - Factorial 

Approach:
Initialise result = 1.
Loop i from 1 to n.
Multiply result *= i.
Return result.

"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
# print(factorial(5))  # ➜ 120


"""
CHALLENGING QUESTIONS
"""

"""
Question 1 - StudentScoreBoard

def StudentScoreboard(strParam):
    
    Expected input: "Alice:85,Bob:90,Clara:78"
    Expected output: "Average:84.33, Top:Bob"

    Algorithm flow:
      1. Split by commas, then by ':'
      2. Build a dictionary {name: score}
      3. Compute average
      4. Find highest scoring student
      5. Return formatted string
      
    # code goes here
    return strParam

"""

def StudentScoreboard(strParam):
    entries = strParam.split(',')
    scores = {}
    for e in entries:
        name, val = e.split(':')
        scores[name] = int(val)
    avg = sum(scores.values()) / len(scores)
    top = max(scores, key=scores.get)
    return f"Average:{avg:.2f}, Top:{top}"


"""
question 2 - EvenDifference

Algorithm / Flow

Initialise an empty list evens.

Loop through all numbers in the list.

If a number is even (num % 2 == 0), append it to evens.

After the loop:

If len(evens) < 2, return 0.

Otherwise, return max(evens) - min(evens).
"""

def even_difference(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    if len(evens) < 2:
        return 0
    return max(evens) - min(evens)

# print(even_difference([3, 8, 2, 7, 10, 5]))  # ➜ 8


"""
Questoin 3 - Count Vowels

algorithm / Flow

Create a variable vowels = "aeiou".

Convert the input string to lowercase.

Initialise count = 0.

Loop through each character:

If it exists in vowels, increment count.

Return count.
"""

def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# print(count_vowels("Beautiful"))  # ➜ 5
