def Bin_To_Deci(n):
    ans = 0
    i = 0
    while n>0:
        last = n%10
        ans += last*(2**i)
        n = n//10
        i += 1
    return ans

n = 101010
print(Bin_To_Deci(n))