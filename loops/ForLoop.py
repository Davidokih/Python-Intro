from math import sqrt


# For Loop

# fruits  = ["Mango", "Grapes", "Apple  "]

# for fruit in fruits:
#     print("current fruit:", fruit)

# print("Good Bye")

# using for loop for factorial

# num = int(input("Number:"))
# factorial = 1

# if num < 0:
#     print("must be positive")
# elif num == 0:
#     print("factorial = 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial * i
# print(factorial)




# making use of for loop to print pythagorean 

# n = int(input("Maximal Number? "))
# for a in range(1,n+1):
#     for b in range(a,n):
#         c_square = a**2 + b**2
#         c = int(sqrt(c_square))
#         if ((c_square - c**2) == 0):
#             print(a,b,c)

# while 


traveling = input("yes or no") 

while traveling == "yes":
    num = int(input("number of people traveling: "))
    for num in range(1,num + 1):
        name = input("Name: ")  
        age = input("Age: ")  
        sex = input("Male or Female: ")  
        print(name)
        print(age)
        print(sex)
    traveling = input("Oops! forget someone")