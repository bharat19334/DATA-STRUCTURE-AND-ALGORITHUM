def count_devided(num):
    n = num
    count = 0
    while n>0:
        last = n%10
        if num%last == 0:
            count +=1
        n = n//10
    return count
num = 121
print(count_devided(num))