"""
Longest Word Challenge

Challenge:
    Write a function longest_word(sentence) that finds and returns the largest
    word in a string.

Requirements:
    1. Return the longest word in the string
    2. If multiple words have the same length, return the FIRST one encountered
    3. Ignore all punctuation (keep only letters a-z, A-Z, and spaces)
    4. Assume the input string will not be empty
    5. Words are separated by spaces

Return Value:
    - Return the longest word as a string (without punctuation)

Examples:
    longest_word("fun&!! time")                    # → "time"
    longest_word("I love dogs")                    # → "love" (first of equal length)
    longest_word("a beautiful sentence^&!")       # → "beautiful"
    longest_word("letter after letter!!")         # → "letter" (first occurrence)
    longest_word("confusing /:sentence:/[ this is not!!!!!!!~")  # → "confusing"

"""


def longest_word(sentence):
    # Clean the sentence; remove none alpha word
    clean_sentence = ""
    for char in sentence:
        if char.isalpha() or char == " ":
            clean_sentence += char

    # split sentence into words
    words = clean_sentence.split()

    # find the longest word - itself an easy challenge in some places
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("fun&!! time"))                    # → "time"
# longest_word("I love dogs")                    # → "love" (first of equal length)
# longest_word("a beautiful sentence^&!")       # → "beautiful"
# longest_word("letter after letter!!")         # → "letter" (first occurrence)
# longest_word("confusing /:sentence:/[ this is not!!!!!!!~")  # → "confusing"
