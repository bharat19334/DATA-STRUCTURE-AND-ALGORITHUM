def dec_to_bin(n):
    ans = 0
    i = 0
    while n>0:
        rem = n%2
        ans += (10**i)*rem
        n = n//2
        i += 1
    
    return ans
n = 250
print(dec_to_bin(n))



# 1-10 binary numbers
n = 10
for i in range(1,n+1):
    print(dec_to_bin(i))