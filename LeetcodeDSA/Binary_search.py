def binary_search(nums,target):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
             return mid
        elif nums[mid] > target:
             right = mid -1
        elif nums[mid] < target:
            left = mid +1  
    return -1
nums = [1,2,3,4,5,6,7,8,9]
target = 8
print(binary_search(nums,target))

