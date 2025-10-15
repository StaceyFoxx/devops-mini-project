"""
Problem: Counting Unique Connections in a Fully Connected Network

Formula:
Total connections = (n * (n - 1)) // 2

"""


def count_connections(n):
    return (n * (n - 1)) // 2


print(count_connections(5))