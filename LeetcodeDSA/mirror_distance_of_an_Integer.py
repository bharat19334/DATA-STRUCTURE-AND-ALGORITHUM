def mirrorDistance(n):
    num = n
    rev = 0
    while num > 0:
        last = num%10
        rev = rev*10 + last 
        num = num//10
    ans = abs(n-rev)
    return ans

n = 25
print(mirrorDistance(n))