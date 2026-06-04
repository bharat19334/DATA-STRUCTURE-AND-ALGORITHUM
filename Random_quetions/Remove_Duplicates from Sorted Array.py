# optimal way

def find_unique_ele(nums):
    n = len(nums)
    if n == 1:
        return n
    i = 0
    j = i+1
    while j<n:
        if nums[j] != nums[i]:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
        j+=1
    return i+1
nums = [1,2,2,3,3,3,4]
print(find_unique_ele(nums))
        