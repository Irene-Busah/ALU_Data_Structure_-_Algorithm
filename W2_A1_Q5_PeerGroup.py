# Estimate how long each algorithm would take for inputs of size 1,000,000. Write your estimate clearly in the code.
from W2_A1_Q3_IreneBusah import *
import random
import timeit


# -------------------------------------------- Question 1 -------------------------------------------
# Find the maximum value in a list

def timeFindMax(array):
    findMax(array)


list2 = [random.randint(1, 50) for i in range(100)]

timeResult = []
if __name__ == "__main__":
    print(timeit.timeit("timeFindMax(list2)", "from __main__ import timeFindMax, list2", number=1000000))


# ------------------------------------------- Question 2 ------------------------------------------------
# Time Complexity of Sorting an array of Integers

def timeSortArray(array):
    sortList(array)


list3 = [random.randint(1, 100) for i in range(100)]

timeResult = []
if __name__ == "__main__":
    print(timeit.timeit("timeSortArray(list3)", "from __main__ import timeSortArray, list3", number=1000000))


# -------------------------------------- Question 3 ------------------------------------------------------
# Time Complexity of converting all letters to lowerCase

def concertLowerCase(string):
    lowerCase(string)


string2 = 'BAHjidhfdifGGHGsjudsbKHKBsjkdksdbshfkhbsksbshdbssbsJKHVJIHYVAdbahbaHBJ'

timeResult = []
if __name__ == "__main__":
    print(timeit.timeit("concertLowerCase(string2)", "from __main__ import concertLowerCase, string2", number=1000000))
