def substract_prod_sum(num):
    n = num
    product = 1
    sum = 0
    while n>0:
        last_digit = n%10
        product *= last_digit
        sum += last_digit
        n = n//10
        
    return product-sum

num = 1237
print(substract_prod_sum(num))