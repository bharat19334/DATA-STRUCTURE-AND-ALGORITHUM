# 1st approach
def kth_missing_number(nums):
    freq = {}
    n = nums[len(nums)-1] 
    m = 0
    for i in range(0,k*n):
        if i not in nums:
            freq[i] = m
            m += 1
    for key,value in freq.items():
        if value == k:
            return key
nums = [2,3,4,7,11]
k = 2
print(kth_missing_number(nums))



