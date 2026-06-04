def search(nums, target):
        
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [3,4,5,0,1,2]
target = 0
print(search(nums,target))