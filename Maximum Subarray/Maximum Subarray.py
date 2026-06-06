# 1) Brute force approach

# without using Max() function
def max_subarray(nums):
    max_sum = float("-inf")
    for i in range(0,len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if total > max_sum:
                max_sum = total
    return max_sum
    
nums = [1,2,-5,3,4,-3,6]
print(max_subarray(nums))

# With max() function
def max_subarray(nums):
    maxi_sum = float("-inf")
    for i in range(0,len(nums)):
        Total = 0
        for j in range(i,len(nums)):
            Total += nums[j]
            maxi_sum = max(Total,maxi_sum)
    return maxi_sum
nums = [1,2,-5,3,4,-3,6]
print(max_subarray(nums))

# 2) optimal approach

def max_subarray(nums):
    max_sum = float("-inf")
    Total = 0
    for i in range(0,len(nums)):
        Total += nums[i]
        if max_sum < Total:
            max_sum = Total
        if Total < 0:
            Total = 0
    return max_sum
nums = [1,2,-5,3,4,-3,6,2]
print(max_subarray(nums))

