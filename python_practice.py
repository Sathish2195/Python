# Strings ####
"""
String methods -

upper
lower
isUpper
isLower
isDecimal
split
join
strip

"""
# Split and Join Strings
foo = "Helllo.Monty.Python"
# print(foo.lower())
print(foo.split("."))
ps = " ".join(foo.split("."))
print(len(ps), ps)
print(foo[-6:][::-1])

# foo = "sampling"
# sl1 = foo[0:2]
# sl2 = foo[2:6].upper()
# sl3 = foo[-2:]
# print sampling as sa-MPLI-ng
# print(f"{foo[0:2]}-{foo[2:6].upper()}-{foo[-2:]}")

# # print sampling as S-nilpma-G
# print(f"{foo[0].upper()}-{foo[1:7][::-1]}-{foo[-1:].upper()}")

# a = "192.168.1.125"

# f1 = a.split(".")
# print(f1)
# f1[0] = "172"
# print(f1)

# import re
# # Sample string.
# text = "Ten 10, Twenty 20, Thirty 30"
# result = re.split("\D+", text)
# # Print results.
# for element in result:
#     print(element)

# Palindrome

# text = input("Enter your text:")
# if text[:] == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#
# Replace


# text = input("Enter your text:")

# text = text.lower().replace("a", "o")

# # text = text.replace("a", "o")
# print(text)
#
# # cCount vowels
# string = input("Enter string:")
# vowels = 0

# for i in string.lower():
#     if i in "aeiou":
#         vowels += 1
# print(f"No of vowels {vowels}")

##
# # No of chars and words
# string = input("Enter string:")
# char = 0
# word = 1
# for i in string:
#     char = char+1
#     if (i == ' '):
#         word = word+1
# print("Number of words in the string:")
# print(word)
# print("Number of characters in the string:")
# print(char)

# Count lowercase

# # No of chars and words
# string = input("Enter string:")

# count = 0

# for i in string:
#     if i.islower():
#         count += 1
# print(f"Total lower letter count is {count}")

##
# #
# print("-".join())
# l = ["Sat", "Sot", "Wot", "Rot", "Rat"]
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)

# num1 = 5
# num2 = 0

# while num2 != num1:
#     print("Not equal")
#     num2 += 1
# print("Now its equal")

# for i in range(10):
#     print(i)

# x = (1, 2, 3)
# z = x + (4, 5)
# print(z)

###########################################################################

# Lists
"""
List methods -

count
append
extend
remove
pop
insert
clear
sort
reverse

List functions -
cmp() - compare lists
len() - length

"""

# pow2 = [2**x for x in range(10) if x < 5]
# print(pow2)

# # even numbers in list
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# evenlist = []

# for i in a:
#     if i % 2 == 0:
#         evenlist.append(i)
# print(evenlist)


# # nums less than 10 in list
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# numlist = []

# for i in a:
#     if i < 10:
#         numlist.append(i)
# print(numlist)

# # Compare Lists and find common [union and intersection sets]

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [1, 15, 25, 36, 50, 65, 100]

# print((set(a) & set(b)))
# print((set(a).intersection(b)))

# Create new list from existing list
# lst = [1, 2, 3, 4, 5, 6]


# def create_new_list(old_list):
#     new_list = old_list[2:4]
#     return new_list


# nl = create_new_list(lst)
# print(nl)


# # Remove Duplicates from list

# lst = ["192.168.1.10", "192.168.1.10", "192.168.1.11",
#        "192.168.1.10", "192.168.1.12", "192.168.1.13", "192.168.1.11"]
# lst = sorted(set(lst))
# print(lst)


# Func to add numbers

# def add_nums(lst):
#     out = 0
#     for num in lst:
#         out += num
#     return out


# lst = [5, 5, 10, 20]
# print(add_nums(lst))


# Square root number as tuple using list comprehension


# def square_num(numlst):
#     return [(num, num**2) for num in numlst]


# elements = int(input("Enter the number of elements:"))
# num_list = [int(input(f"Enter element {i}: ")) for i in range(elements)]
# print(square_num(num_list))

# # generate random int from list
# import random
# entry = int((input("Enter elements:")))
# num_list = [random.randint(1, 20) for i in range(entry)]
# print(num_list)


# # Swap first and last
# entry = int(input("Enter elements:"))
# nums = []
# for i in range(entry):
#     num = int(input(f"Enter element {i}: "))
#     nums.append(num)
# print(nums)
# temp = nums[0]
# nums[0] = nums[-1]
# nums[-1] = temp
# print(nums)

########### TUPLES ##############

""" Tuple Methods
count()
index()
sorted()
In/Not In keyword

"""
############ Dictionaries #############
"""
len(dict)
str(dict)
dict.clear() - Remove all  elements
del <> - Delete dict
dict.copy()
dict.keys() - Get all keys
dict.values() - Get all values
dict.items()
update()
"""

# dict1 = {0: 10, 1: 20}
# dict1[2] = "30"
# print(dict1)

# d = {"blue": 1, "green": 2, "yellow": 3}
# for key, value in d.items():
#     print(key, value)

# my_dict = {'x': 500, 'y': 5874, 'z': 560}

# dt = my_dict.values()
# print(dt)
# print(sorted(dt)[-1])

############ Sets #############
"""
union
intersection
issubset
issuperset
difference(a-b)
isdisjoint
clear
"""

###################
"""
zip ()

combines multiple lists and convert to single list by taking each corresponding element from each list 
and putting in a tuple
"""

# list1 = ["a", "b", 3]
# list2 = [1, 2, 3, 4]
# list3 = list(zip(list1, list2))
# print(list3)

#### Enumerate ####
"""

Iterate through a seq and get the index position even if ther is no index 
"""

# for index, value in enumerate(["Python", "C", "Java"]):
#     print(index, value)
