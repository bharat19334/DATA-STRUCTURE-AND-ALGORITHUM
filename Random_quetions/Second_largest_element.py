def Second_largest(nums):
    largest = float("-inf")
    S_largest =float("-inf")  
    for i in range(0,len(nums)):
        if largest < nums[i]:
            largest = nums[i]
    for i in range(0,len(nums)):
        if S_largest < nums[i] and nums[i] != largest:
            S_largest = nums[i]
    return S_largest

nums = [44,22,-25,35]
print(Second_largest(nums))