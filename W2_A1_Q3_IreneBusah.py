# Implement the following 3 algorithms:
# 1. Find the maximum value in a list
# 2. Make each letter in a string lowercase
# 3. Sort a list of integers (using the inbuilt python method)

# ------------------------------ Question 1 -------------------------------------
# 1. Find the maximum value in a list

"""
Time Complexity: Since we are looking for the input array only once then the time complexity is O(n).

Space Complexity: Since we are not using any extra space then the space complexity is O(1)
"""


def findMax(array):
    maxNum = array[0]
    for num in array:
        if num > maxNum:
            maxNum = num
    return maxNum


findMax([10, 4, 0, 22])

print(findMax([2, 5, 6, 9, 1, 0, 87]))

# ------------------------------- Question 2 --------------------------------
# 2. Make each letter in a string lowercase

"""Time Complexity: Since we are looping through the input only once. The time complexity is O(n). Checking an item 
in a dictionary is O(1). 

Space Complexity: Since the hashSet variable remains the same in every input, then the space complexity is O(1)
"""


def lowerCase(word):
    hashSet = {
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
        'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
        'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v',
        'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
    }
    word = list(word)
    newWord = ""
    for i in range(len(word)):
        if word[i] in hashSet:
            word[i] = hashSet[word[i]]
            newWord += word[i]
        else:
            newWord += word[i]
    return newWord


print(lowerCase('AbcDEfg'))

# ---------------------------------- Question 3 ------------------------------------
# 3. Sort a list of integers (using the inbuilt python method)

"""
Time complexity of sorting the list is O(n log n).
Space complexity is O(1)
"""


def sortList(array):
    array.sort()
    return array


print(sortList([100, -1, 3, 5, 2]))

# ------------------------------ TIME COMPLEXITY -----------------------------------

# import timeit
#
#
# def timeFindMax(array):
#     findMax(array)
#
#
# timeResult = []
# if __name__ == "__main__":
#     timeResult.append(timeit.timeit("timeFindMax(list1)", "from __main__ import timeFindMax, list1", number=10))
#     timeResult.append(timeit.timeit("timeFindMax(list2)", "from __main__ import timeFindMax, list2", number=10))
#     timeResult.append(timeit.timeit("timeFindMax(list3)", "from __main__ import timeFindMax, list3", number=10))
#
# # plotting the graph
# import matplotlib.pyplot as plt
#
# # %matplotlib inline
# fig, ax = plt.subplots()
# ax.plot(timeResult)
# ax.set_title("Time Complexity of finding a max number in an array")
# plt.show()
#
#
# # ------------------------------ Question 3 --------------------------------
#
# def sortList(array):
#     array.sort()
#     return array
#
#
# sortList([100, -1, 3, 5, 2])
#
# # ------------------------------- TIME COMPLEXITY --------------------------
# import timeit
# from random import randint
# import matplotlib
#
#
# def timeSortArray(array):
#     sortList(array)
#
#
# list1 = [2]
# list2 = [random.randint(1, 50) for i in range(50)]
# list3 = [random.randint(1, 100) for j in range(100)]
#
# timeResult = []
# if __name__ == "__main__":
#     timeResult.append(timeit.timeit("timeSortArray(list1)", "from __main__ import timeSortArray, list1", number=10))
#     timeResult.append(timeit.timeit("timeSortArray(list2)", "from __main__ import timeSortArray, list2", number=10))
#     timeResult.append(timeit.timeit("timeSortArray(list3)", "from __main__ import timeSortArray, list3", number=10))
#
# # plotting the graph
# import matplotlib.pyplot as plt
#
# # %matplotlib inline
# fig, ax = plt.subplots()
#
# print(ax.plot(timeResult))
# print(ax.set_title("Time Complexity of sorting integers"))
# plt.show()
#
#
# # ----------------------------- SPACE COMPLEXITY -----------------------
#
# # from memory_profiler import memory_usage
# #
# # """When you run memory_usage, it gives the output of the memory usage 3 times,
# # so we calculated the average of the output and store it"""
# # memResults = []
# # mem_usage1 = memory_usage((sortList, [list1]))
# # mem_usage2 = memory_usage((sortList, [list2]))
# # mem_usage3 = memory_usage((sortList, [list3]))
# # memResults.append(sum(mem_usage1) // 3)
# # memResults.append(sum(mem_usage2) // 3)
# # memResults.append(sum(mem_usage3) // 3)
# #
# # print(memResults)
# #
# #
# # fig, ax = plt.subplots()
# # print(ax.plot(memResults))
# # print(ax.set_title("Space Complexity of sorting integers"))
# # plt.show()
#
#
# # --------------------------------- QUESTION 2 -----------------------------------
# def lowerCase(word):
#     hashSet = {
#         'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
#         'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
#         'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v',
#         'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
#     }
#     word = list(word)
#     newWord = ""
#     for i in range(len(word)):
#         if word[i] in hashSet:
#             word[i] = hashSet[word[i]]
#             newWord += word[i]
#         else:
#             newWord += word[i]
#     return newWord
#
#
# print(lowerCase('AbcDEfg'))
