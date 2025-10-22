# Heads up that this is just my solutions. There are more ways to do this
"""
Challenge:
    Have the function bracket_matcher(a_string) take the a_string parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if a_string is "(hello (world))", then the output should be 1, but if a_string is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If a_string contains no brackets return 1

Requirements:
    Function name: bracket_matcher(a_string)
    Return 1 if brackets are correctly matched, 0 otherwise
    Only parentheses ( and ) are used as brackets
    Must handle nested brackets correctly
    If no brackets exist in the string, return 1
    Must ensure brackets are in correct order (opening before closing)

Test Cases:
    # print(bracket_matcher("(hello (world))")) # return 1
    # print(bracket_matcher("((hello (world))")) # return 0 (missing closing bracket)
    # print(bracket_matcher("hi()")) # return 1
    # print(bracket_matcher("(hi")) # return 0  (unmatched opening bracket)
"""


def bracket_matcher(a_string):

    counter = 0

    for char in a_string:
        print("Counter: ", counter)
        if char == "(":
            counter += 1

        if char == ")":
            counter -= 1

        if counter < 0:
            return 0

    # at the end
    if counter == 0:
        return 1
    else:
        return 0


# print(bracket_matcher("(hello (world))")) # return 1
# print(bracket_matcher("((hello (world))")) # return 0 (missing closing bracket)
# print(bracket_matcher("hi()")) # return 1
# print(bracket_matcher("(hi")) # return 0  (unmatched opening bracket)
# print(bracket_matcher(")))(((")) # return 0
