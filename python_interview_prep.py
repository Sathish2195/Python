# ### String ###
# course = "Python programmming"
# goal = "Completion certificate"

# print(len(course))
# print(course.replace("Python", "C++"))
# print("pro" not in course)
# print(f"This is a {course} course. After completion you will get a {goal}.")
# print(course[0:7])

# Numbers

# a = 10
# b = 20.12
# c = 1 + 2j

# x = 10
# print(x)
# x /= 3
# print(x)
# x -= 5.5
# print(x)
# print(type(x))
# print(round(x))
# print(abs(round(x)))

# Data structures

# Lists

# vowels = ["a", "e", "i", "o", "u"]
# words = ["b", "c", [vowels]]
# combine = [[words], "1", "*", [0]*10]
# print(combine)
# char = list("Hello")
# print(char)
# length = list(range(20))
# print(length)

# letters = ["H", "e", "l", "l", "o"]
# print(letters[0:2])
# print(letters[:3])

# nums = list(range(20))
# print(nums[::-3])

# List Unpacking

# numbers = [1, 2, 3, 4, 5]
# first, second, third, fourth, fifth = numbers
# print(first)

# one, two, *other = numbers
# print(two)
# print(other)

# Lambda function

# items = [("product1", 10), ("product2", 20), ("product3", 30)]

# x = list(map(lambda item: item[1], items))  # Lambda function
# print(x)


# List comprehension [expression for <> in <>]

# items = [("a", 1), ("b", 2), ("c", 3)]

# prices = [item[1] for item in items]
# print(prices)

# ZIP functions - Combining multiple lists #

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# x = list(zip(list1, list2))
# print(x)

# Stacks #
# Last in First out [Example, Browser backward and forward page option]

# web_session = []
# web_session.append(1)
# web_session.append(2)
# web_session.append(3)
# print(web_session)
# web_session.pop()
# print(web_session)
# print(web_session[-1])
# if not web_session:
#     print("disable back button")

# Queues #
# First in First Out
# dequeue from collections module

# from collections import deque
# queue = deque([])  # Define empty list in dequeu object to store values
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()  # Uses .popleft() method to remove first item from queue. This method is not available in lists, but only in deque
# print(queue)
# if not queue:
#     print("empty")


# Tuples #
# Immutable , cannot change the values

# convert list to tuple, we can call tuple function

# point = tuple([1, 2])

# print(type(point))
# print(point)

# Swap variables #

# x = 10
# y = 20

# x, y = y, x
# print("x", x)
# print("y", y)

# ls = [x, y]
# ls.reverse()
# print(ls)
# x, y = ls
# print(x)
# print(y)


# Arrays # Mutable
# useful when dealing with large amount of numbers/items, when compared to lists
# need to use typecodes for each datatype

# from array import array

# numbers = array("i", [1, 2, 3])

# Array vs Lists
# Arrays when defined can contain only one data type (ex. integer)
# Lists can contain combination of data types (integer, float, string etc)
# Use arrays only when dealing with large amount of numbers, for some performance improvement.

# Sets # Mutable #
# Unordered collection of unique items, removes duplicates
# Uses Curly braces, Doesn't support index access since its unordered
# Useful in math operationss - union, intersection

# numbers = [1, 1, 2, 2, 3, 4]
# first = set(numbers)
# second = {0, 4, 5}

# print(first | second)  # union
# print(first & second)  # intersection
# print(first - second)  # Diff
# print(second - first)  # Diff
# print(first ^ second)  # Symmetric [either first or second but not both]


# Dictionaries #
# key:value pair

# point = {"x": 1, "y": 2}

# point1 = dict(x=1, y=2)
# # print(point["x"])

# for key, value in point.items():
#     print(key, value)

# Unpacking operator # Take out individual values in any iterable

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)

# values = [*range(5)]
# print(values)


# Find most repeated chars in a text

# from pprint import pprint

# text = "This is an online test"

# chars_freq = {}

# for char in text:
#     if char in chars_freq:
#         chars_freq[char] += 1
#     else:
#         chars_freq[char] = 1

# # pprint(chars_freq)

# print(sorted(chars_freq.items()))

# def add_1(x, y):
#     z = x + y
#     return z


# result = add_1(10, 20)
# print(result)
