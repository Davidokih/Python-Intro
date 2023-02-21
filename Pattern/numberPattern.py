
def numPattern(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0,i + 1):
            print(x, end="")
        print("\r")

# numPattern(5)

# Pascal principle

def numPattern2(n):
    for i in range(0,n):
        for j in range(0, i + 1):
            print(function(i,j)," ", end="")
        print("\r")

def function(n,k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0,k):
        res = res * (n-i)
        res = res//(i + 1)
    return res

numPattern2(10)