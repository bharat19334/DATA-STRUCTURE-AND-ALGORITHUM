def addDigits(num):
    while num > 9:      
        Sum_count = 0
        while num > 0: 
            last_digit = num % 10
            Sum_count += last_digit
            num = num // 10
        num = Sum_count  
    return num
    
num = 39
print(addDigits(num))