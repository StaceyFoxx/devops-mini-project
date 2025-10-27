"""
Note from Hamed - BOTH solutions below are correct. HOWEVER, the one that uses "set" is more
optimised and works better/faster for large inputs of data. That's the only difference.
"""

def remove_duplicates(s):
    result = []
    for char in s:
        if char not in result:
            result.append(char)

    return ''.join(result)


def remove_duplicates(s):
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)