def majorityElement(nums):
    hash_dict = {}
    for n in nums:
        hash_dict[n] = hash_dict.get(n,0)+1
    for key,value in hash_dict.items():
        if value > len(nums)//2:
            return key
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))