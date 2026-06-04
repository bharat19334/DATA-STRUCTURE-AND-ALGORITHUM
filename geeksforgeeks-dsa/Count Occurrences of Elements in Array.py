nums = [1,4,5,2,4,6,2,5,4,1,7,8,9,7,7,8,7,5,1]
freq_dict = {}
for i in range(0,len(nums)):
    if nums[i] in freq_dict:
        freq_dict[nums[i]] += 1
    else:
        freq_dict[nums[i]] = 1
print(freq_dict)