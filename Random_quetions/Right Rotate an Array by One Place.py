def Right_rotate(nums):
    
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    return nums
nums = [5,-2,3,9,0,6,10,7]
print(Right_rotate(nums))