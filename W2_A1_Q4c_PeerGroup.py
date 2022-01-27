import timeit
from W2_A1_Q3_IreneBusah import *
import random
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


# ------------------------------------------ Question 3a -----------------------------------------
# Time Complexity of converting all letters to lowerCase

def concertLowerCase(string):
    lowerCase(string)


string1 = 'A'
string2 = 'BAHjidhfdifGGHGsjudsbKHKBsjkdksdbshfkhbsksbshdbssbsJKHVJIHYVAdbahbaHBJ'
string3 = 'NJHsdkjdslKLJNnLJnljsnlkdsndlskdLKLJnsldsdLjsdsndlsjJLJBBLJHsdnsldsdksl' \
          'hdsksjkdssfhfskfjsfsbfsfksfbhjskdbsnfKHBJKBKJKBJBKJdbsjkdfbkjfdfkfdbfdkbf '

timeResult = []
if __name__ == "__main__":
    timeResult.append(
        timeit.timeit("concertLowerCase(string1)", "from __main__ import concertLowerCase, string1", number=10))
    timeResult.append(
        timeit.timeit("concertLowerCase(string2)", "from __main__ import concertLowerCase, string2", number=10))
    timeResult.append(
        timeit.timeit("concertLowerCase(string3)", "from __main__ import concertLowerCase, string3", number=10))

# plotting the graph
# The graph that will be drawn is a linear(straight line) graph as
# the time complexity is O(n)

fig, ax = plt.subplots()
print(ax.plot(timeResult))
print(ax.set_title("Time Complexity of converting letters in lower Case"))
plt.show()


# ------------------------------------------ Question 3b -----------------------------------------
# Space Complexity for Converting letter to lowerCase

"""When you run memory_usage, it gives the output of the memory usage 3 times,
so we calculated the average of the output and store it"""

if __name__ == '__main__':
    memResults = []
    mem_usage1 = memory_usage((lowerCase, [string1]))
    mem_usage2 = memory_usage((lowerCase, [string2]))
    mem_usage3 = memory_usage((lowerCase, [string3]))
    memResults.append(sum(mem_usage1) // 3)
    memResults.append(sum(mem_usage2) // 3)
    memResults.append(sum(mem_usage3) // 3)

    print(memResults)
    fig, ax = plt.subplots()
    print(ax.plot(memResults))
    print(ax.set_title("Space Complexity of converting letters in lower Case"))
    plt.show()

