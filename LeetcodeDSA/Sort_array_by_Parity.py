def  sortArrayByParity(nums):
    
    insert_position = 0
    for i in range(0,len(nums)):
        if nums[i]%2==0:
            nums[insert_position],nums[i] = nums[i],nums[insert_position]
            insert_position += 1
    return nums

nums = [2,3,4,5,6,1,8]
print(sortArrayByParity(nums))