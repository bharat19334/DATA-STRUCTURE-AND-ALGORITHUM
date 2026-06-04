num = 123
total_sum = 0
while num>0:
    last = num%10
    total_sum += last
    num = num//10
print(total_sum)

#using function
def digits_sum(num):
    total_sum = 0
    while num>0:
        total_sum += num%10
        num = num//10
    return total_sum
num = 123
print(digits_sum(num))
    