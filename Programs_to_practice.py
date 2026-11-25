# # create new string from alternate chars from existing strings

# x = "abcz"
# y = "defy"

# final_text = ""
# i = 0
# j = 0

# while i < len(x) and j < len(y):
#     final_text += x[i]
#     final_text += y[j]
#     i += 1
#     j += 1
# print(final_text)


# # Remove repeated chars

# x = "sathishsatsathishsatshy"

# final = ""
# for i in x:
#     if i not in final:
#         final += i
# print(final)

# # Fibonacci


# def fib(num):
#     a = 0
#     b = 1
#     for i in range(1, num+1):
#         c = a + b
#         print(b, end="")
#         a = b
#         b = c
#     return c


# fib(10)

# # Convert mask to cidr

# mask = "255.255.255.0"


# def mask_cidr(mask):
#     mask.split()


# print(mask_cidr(mask))

# Number of occurrence in list

# from collections import Counter
# list1 = ["1", "1", "2", "1", "3", "6", "2", "2", "7", "7"]
# # count = {}
# # for i in list1:
# #     if i not in count:
# #         count[i] = 1
# #     else:
# #         count[i] += 1
# x = (Counter(list1))
# print(x)
# for key, value in x.items():
#     print(f" Number {key} occurred {value} times")

# def countDuplicate(numbers):
#     count = 0
#     result = dict((i, numbers.count(i)) for i in numbers)
#     # return result
#     final = {}
#     for i, j in result.items():
#         if j > 1:
#             final[i] = j
#     return final


# abc = 18, 1, 3, 1, 4, 5, 6, 3, 2, 18
# print(countDuplicate(abc))


# Find repeated word in string

# def word_count(str):
#     counts = {}
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts


# print(word_count('the quick brown fox jumps over the lazy brown dog.'))


# Palindrome (Number)

# num1 = int(input("Enter the number: "))

# temp = num1
# rev = 0

# while num1 > 0:
#     x = num1 % 10
#     rev = rev*10 + x
#     num1 = num1 // 10

# if rev == temp:
#     print("Given number is palindrome")
# else:
#     print("Given number is not a palindrome")

# Palindrome (String)

# str1 = str(input("Enter the name: "))

# str2 = str1[::-1]
# if str2 == str1:
#     print("Name is palindrome")
# else:
#     print("Name is not palindrome")


# def sum(nums, target):
#     ln = len(nums)
#     for i in range(ln):
#         x = nums[i]
#         y = target - x
#         if y in nums[i+1]:
#             return [nums[i].index(), nums[i+1].index()]


# nums = [1, 2, 3, 4]
# target = 5
# sum(nums, target)
