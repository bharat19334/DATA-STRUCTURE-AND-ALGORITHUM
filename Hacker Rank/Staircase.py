def staircase(n):
    for i in range(0,n+1):
        print(" "*(n-i) + "#"*(i))
n = 4
print(staircase(n))