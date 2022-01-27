# For each of the above algorithms, plot graphs showing how the time and
# space taken as the input size changes from length 1 to length 100.
# (Lengths of lists and lengths of strings). You don’t need all values -
# just a few (e.g. 3) is enough.


# ----------------------------------- Question 1a ----------------------------------
# Time Complexity of Sorting an array of Integers

import timeit
from W2_A1_Q3_IreneBusah import *
import random
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


def timeSortArray(array):
    sortList(array)


list1 = [2]
list2 = [random.randint(1, 50) for i in range(50)]
list3 = [random.randint(1, 100) for j in range(100)]

timeResult = []
if __name__ == "__main__":
    timeResult.append(timeit.timeit("timeSortArray(list1)", "from __main__ import timeSortArray, list1", number=10))
    timeResult.append(timeit.timeit("timeSortArray(list2)", "from __main__ import timeSortArray, list2", number=10))
    timeResult.append(timeit.timeit("timeSortArray(list3)", "from __main__ import timeSortArray, list3", number=10))

# plotting the graph

# The graph that will drawn is a logarithmic graph as
# the time complexity is O(n log n)

fig, ax = plt.subplots()
print(ax.plot(timeResult))
print(ax.set_title("Time Complexity of sorting integers"))
plt.show()


# ----------------------------------------- Question 1b --------------------------------------
# ## Space Complexity for sorting an array of integers


"""When you run memory_usage, it gives the output of the memory usage 3 times,
so we calculated the average of the output and store it"""


if __name__ == '__main__':
    list1 = [2]
    list2 = [random.randint(1, 50) for i in range(50)]
    list3 = [random.randint(1, 100) for i in range(100)]
    memResults = []
    mem_usage1 = memory_usage((sortList, [list1]))
    mem_usage2 = memory_usage((sortList, [list2]))
    mem_usage3 = memory_usage((sortList, [list3]))
    memResults.append(sum(mem_usage1) // 3)
    memResults.append(sum(mem_usage2) // 3)
    memResults.append(sum(mem_usage3) // 3)

    # print(memResults)
    fig, ax = plt.subplots()
    print(ax.plot(memResults))
    print(ax.set_title("Space Complexity of sorting integers"))
    plt.show()
