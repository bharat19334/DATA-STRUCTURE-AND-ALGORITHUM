# 1st approach
nums = [3,0,1,4,2,6]
n = len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)
        
# 2nd approach
def missing_number(nums):
    freq =  {}
    for i in range(0,len(nums)+1):
        freq[i] = 0
    for num in nums:
        freq[num] = 1
    for k,v in freq.items():
        if v == 0:
            return k
nums = [0,1,2,3,5]
print(missing_number(nums))

# 3rd approach
def missing_number(nums):
    n = len(nums)
    actual_sum = n*(n+1)/2
    current_sum = sum(nums)
    return int(actual_sum - current_sum)

nums = [1,2,0,4,5,6]
print(missing_number(nums))