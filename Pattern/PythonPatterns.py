# Pyramid Pattern

def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i + 1):
            print("*", end = " ")
        print("\r")

# pattern(10)

# Inverse Pyramid pattern
def pattern2(n):
    k = n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end= " ")
        k = k + 1
        for j in range(0,i + 1):
            print("*", end=" ")
        print("\r")

# pattern2(10)

# Right start pattern

def pattern3(n):
    for i in range(0,n):
        for j in range(0,i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

# pattern3(5)

def pattern4(n):
    k = 2 * n - 2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

# pattern4(5)

# Hourglass pattern

def pattern5(n):
    k = n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end= " ")
        k = k + 1
        for j in range(0,i + 1):
            print("*", end=" ")
        print("\r")
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i + 1):
            print("*", end = " ")
        print("\r")

# pattern5(5)

# Half pyramid pattern

def pattern6(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

# pattern6(10)

# Half pyramid pattern left

def pattern7(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

# pattern7(10)

# downward half pyramid pattern

def pattern8(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

# pattern8(10)

#  diamond pattern

def pattern9(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i + 1):
            print("* ", end="")
        print("\r")
    k = n -2
    for i in range(n, -1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0, i +1):
            print("* ", end="")
        print("\r")

# pattern9(5)

#  diamond star pattern

def pattern01(n):
    for i in range(n):
        for j in range(n):
            if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
                print("* ", end="")
            else:
                print(end=" ")
        print()

# pattern01(5)

# Praxtice pattern code

def myPattern(n):
    k = 2 * n - 2
    for i  in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0,i + 1):
            print("* ", end="")
        print("\r")
myPattern(5)