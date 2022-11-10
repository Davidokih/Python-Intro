# The first method to import an array
# import array

# a = array.array("i", [1,2,3,4,5,6,7,8,9])
# print(a)

#  Second method to simport array

import array as arr

# a = arr.array("i", [1,2,3,4,5,6,7,8,9])

# print(a[2])

# The third method to import array

# from array import *

# a = array("i", [1,2,3,4,5,6,7,8,9])
# print( a )

# Finding the lenght of an array

a = arr.array("i", [1,2,3,4,5,6,7,8,9])
# print(len(a))

#Adding element to an array 

# append is used when you want to add a single element at the end of an array
# a = arr.array("i", [1,2,3,9])
# a.append(8)
# print(a)

# extend is used when you want to add more than one element at the end of an array
# a = arr.array("i", [1,2,3,9])
# a.extend([5,4,6,7])
# print(a)

# insert is used when you want to add an element at a specific position in an array
# a = arr.array("i", [1,2,3,9])
# a.insert(2,6)
# print(a)

# pop is used when you want to remove an element and return it
# a = arr.array("i", [1,2,3,4,5,6,7,8,9])
# print(a.pop())
# print(a.pop(2))
# print(a.pop(-1))
# remove is used when you want to remove an element with a specific value without returning it
# a = arr.array("i", [1,2,3,4,5,6,7,8,9])
# a.remove(8)
# print(a)

# Array Concatenation
# a = arr.array("i", [1,2,3,4,5,6,7,8,9])
# b = arr.array("i", [4,5,6,8,8,3,65,7])
# c = arr.array("i")
# c = a + b
# print(c)

# SLicing an Array
# a = arr.array("i", [1,2,3,4,5,6,5,7,8,9])
# print(a[0:5])
# print(a[0:-2])

# ::-1 print a reverse copy of an array
# print(a[::-1])
# print(a)

# Looping Through an Array

# The for loops iterates over the items of an array in a specified number of times.
# a = arr.array("i", [1,2,3,4,5,6,7,8,9])

# for x in a:
#     print(x)
# for x in a[0: -3]:
#     print(x)
# The while loops iterates over the elements until a certain condition is met.

a = arr.array("i", [1,2,3,4,5,6,7,8,9])
temp = 0
# while temp < a[2]:
#     print(a[temp])
#     temp = temp + 1
while temp < len(a):
    print(a[temp])
    temp += 1