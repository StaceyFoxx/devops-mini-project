def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in s:
        if counts[char] == 1:
            return char

    return None