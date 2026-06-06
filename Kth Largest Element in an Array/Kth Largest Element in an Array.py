def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))