def minimizeArrayValue(nums):
    ans = 0
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
            
        current = (prefix_sum+i)//(i+1)            
        ans = max(ans,current)
    return ans
    
nums = [3,7,1,6]
print(minimizeArrayValue(nums))
