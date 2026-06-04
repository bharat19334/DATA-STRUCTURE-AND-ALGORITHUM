nums = [4,5,6,2,4,1,2,3,5,4,7,7,7,7,7]
hash_map = {}

for i in range(0,len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)