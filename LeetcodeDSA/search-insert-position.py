def searchInsert(nums, target,left,right):
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return left
nums = [1,3,6,8]
target = 7
left = 0
right = len(nums)-1
print(searchInsert(nums, target,left,right))
        