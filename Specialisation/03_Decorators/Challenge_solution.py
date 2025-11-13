############## CACHE EXERCISE ##############

"""
Creating a @memoize decorator.
It will cache results of a function with specific parameters and would instantaneously provide an answer instead
"""


class MemoizeDecorator:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("I did not run a function, just fetched a result for you! :)")
            return self.cache[key]

        value = self.function(*args, **kwargs)
        self.cache[key] = value
        return value


@MemoizeDecorator
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


## run worker function many times with different arguments

for i in range(10):
    print(worker_function_numbers(i))

print(worker_function_numbers.cache)

## run again to see check a value was cached
print(worker_function_numbers(3))
