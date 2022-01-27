import timeit
from W2_A1_Q3_IreneBusah import *
import random
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


# --------------------------------- Question 2a --------------------------------------
# Time Complexity for finding a max number in an array

def timeFindMax(array):
    findMax(array)


list1 = [2]
list2 = [random.randint(1, 50) for i in range(50)]
list3 = [random.randint(1, 100) for i in range(100)]

timeResult = []
if __name__ == "__main__":
    timeResult.append(timeit.timeit("timeFindMax(list1)", "from __main__ import timeFindMax, list1", number=10))
    timeResult.append(timeit.timeit("timeFindMax(list2)", "from __main__ import timeFindMax, list2", number=10))
    timeResult.append(timeit.timeit("timeFindMax(list3)", "from __main__ import timeFindMax, list3", number=10))

# plotting the graph

# The graph that will be drawn is a linear(straight line) graph as
# the time complexity is O(n)

# fig, ax = plt.subplots()
# ax.plot(timeResult)
# ax.set_title("Time Complexity of finding a max number in an array")
# plt.show()

# ----------------------------- Question 2b --------------------------
# Space complexity for finding a max number in an array

"""When you run memory_usage, it gives the output of the memory usage 3 times,
so we calculated the average of the output and store it"""

# print(memResults)
if __name__ == '__main__':
    memResults = []
    mem_usage1 = memory_usage((findMax, [list1]))
    mem_usage2 = memory_usage((findMax, [list2]))
    mem_usage3 = memory_usage((findMax, [list3]))
    memResults.append(sum(mem_usage1) // 3)
    memResults.append(sum(mem_usage2) // 3)
    memResults.append(sum(mem_usage3) // 3)
    fig, ax = plt.subplots()
    print(ax.plot(memResults))
    print(ax.set_title("Space Complexity of finding maximum number in array"))
    plt.show()
