def remove_duplicates(nums):
    nums.sort()
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[index - 1]:
            nums[index] = nums[i]
            index += 1
    
    return nums[:index]
nums = [1,2,2,2,3,3,3,4,4,4,5,6,6,7,8,9]
print(remove_duplicates(nums))