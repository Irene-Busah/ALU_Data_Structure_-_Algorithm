# Implement a basic measure of tracking the time taken to run an algorithm.

# creating a function to measure the time to run an algorithm using timeit module

"""We can measure the time taken to run an algorithm using timeit.
we will be looking for an algorithm which finds the nth fibonacci number"""


import timeit


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = 10

if __name__ == "__main__":
    print(timeit.timeit("fib(n)", "from __main__ import fib, n", number=10))

# ([duplicate] et al., 2022)

# REFERENCE:
# [duplicate], h., Rabbit, B., Byers, M., & Graham, M. (2022).
# how to measure running time of algorithms in python. Stack Overflow.
# Retrieved 24 January 2022, from https://stackoverflow.com/questions/
# 2662140/how-to-measure-running-time-of-algorithms-in-python.
