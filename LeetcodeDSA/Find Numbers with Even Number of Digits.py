def number(nums):
    answer = 0
    for number in nums:
        temp = number
        count = 0

        if temp == 0:
            count = 1

        while temp > 0:
            temp = temp // 10
            count += 1
        
        if count % 2 == 0:
            answer += 1
    return answer
    
nums = [12,345,2,6,7896]
print(number(nums))