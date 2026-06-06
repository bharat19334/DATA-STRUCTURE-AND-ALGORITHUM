def mini_max(nums):
    sum = 0
    for i in range(0,len(nums)-1):
        sum += nums[i]
        max_sum = sum + nums[-1] - nums[0]
    return [sum,max_sum]
nums = [1,3,5,7,9]
print(mini_max(nums))