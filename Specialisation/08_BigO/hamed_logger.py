"""
Note from Hamed - this file is meant for me to use. It really just a simple
logger decorator
"""
import time
import functools


def performance_logger(func):
    """
    A decorator that logs the execution time and number of function calls.
    """
    # Track number of function calls
    func.calls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Increment call counter
        wrapper.calls += 1

        # Time the function execution
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time

        # Log performance metrics
        print(f"Function: {func.__name__}")
        print(f"Input size: {len(args[0]) if args else 'N/A'} items")
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Function calls: {wrapper.calls}")
        print("-" * 40)

        return result

    wrapper.calls = 0
    return wrapper
