import os

# Read all data in the file
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "r")
print(file.read())
file.close()

# Read and return only file character in the file
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "r")
print(file.read(5))
file.close()

# Read only the first line of data in the file
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "r")
print(file.readline())
file.close()

# Read all the line in the file
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "r")
print(file.readlines())
file.close()

# Looping over the object
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "r")
for line in file:
    print(file.readlines())
file.close()

# Writing to a file

# the w method is write a new data
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "w")
file.write("hello world")
file.write("hello world again")
file.close()

# the w method write over an existing data
file = open("c:/Users/HP/Documents/python/FileHandling/handling.txt", "a")
file.write("hello world again")
file.close()

# the x method is used to create file
file = open("c:/Users/HP/Documents/python/FileHandling/newfile.txt", "x")
file.write("my new data")
file.close()

# if os.path.exists("c:/Users/HP/Documents/python/FileHandling/newfile.txt"):
#     os.remove("c:/Users/HP/Documents/python/FileHandling/newfile.txt")
# else:
#     print("The file does not exist")

# os.remove("c:/Users/HP/Documents/python/FileHandling/newfile.txt")