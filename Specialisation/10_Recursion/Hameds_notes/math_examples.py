def recursive_adder(n):
    # base case
    if n == 0:
        return 0

    return n + recursive_adder(n - 1)


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


# print(factorial(5))


def fib(n):
    # base case here
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


# print(fib(7)) # expect 13