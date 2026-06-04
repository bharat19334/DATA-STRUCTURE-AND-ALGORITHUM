# # 1st approach
def contains_duplicates(nums,):
    hash_dict = {}
    for i in range(0,len(nums)):
        if nums[i] in hash_dict:
            return True
        else:
            hash_dict[nums[i]] = 1
    return False
nums = [1,2,3]          
print(contains_duplicates(nums))

# 2nd approach
def contains_duplicates(nums,):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False
nums = [1,2,3,2]          
print(contains_duplicates(nums))

