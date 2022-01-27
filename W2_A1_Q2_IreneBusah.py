# Implement a basic measure of tracking the space used by an algorithm.

from W2_A1_Q1_IreneBusah import fib
from memory_profiler import memory_usage

"""
To measure the space Complexity, we will use memory Profiler
we will use the same function from Question 1


When you run memory_usage, it gives the output of the memory usage 3 times,
so we calculated the average of the output and store it
"""

if __name__ == '__main__':
    n = 10
    mem_usage = memory_usage((fib, [n]))
    print(sum(mem_usage) // 3)
